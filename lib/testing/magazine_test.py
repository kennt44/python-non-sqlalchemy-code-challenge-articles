import pytest
from classes.many_to_many import Article
from classes.many_to_many import Magazine
from classes.many_to_many import Author


class TestMagazine:
    """Tests for the Magazine class in many_to_many.py"""

    def test_has_name(self):
        """Magazine is initialized with a name"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        # Verify magazine names are correctly assigned
        assert magazine_1.name == "Vogue"
        assert magazine_2.name == "AD"

    def test_name_is_mutable_string(self):
        """Magazine name is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")

        # Verify initial name
        assert isinstance(magazine_1.name, str)
        assert magazine_1.name == "Vogue"

        # Change the name and verify
        magazine_1.name = "New Yorker"
        assert magazine_1.name == "New Yorker"

        # Test invalid name with exceptions
        with pytest.raises(Exception):
            magazine_1.name = 2

    def test_name_len(self):
        """Magazine name must be between 2 and 16 characters, inclusive"""
        magazine_1 = Magazine("Vogue", "Fashion")

        # Verify valid length
        assert 2 <= len(magazine_1.name) <= 16

        # Test invalid lengths with exceptions
        with pytest.raises(Exception):
            magazine_1.name = "A"
        with pytest.raises(Exception):
            magazine_1.name = "New Yorker Plus Extra Long Title"

    def test_has_category(self):
        """Magazine is initialized with a category"""
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")

        # Verify categories are correctly assigned
        assert magazine_1.category == "Fashion"
        assert magazine_2.category == "Architecture"

    def test_category_is_mutable_string(self):
        """Magazine category is of type str and can change"""
        magazine_1 = Magazine("Vogue", "Fashion")

        # Verify initial category
        assert isinstance(magazine_1.category, str)
        assert magazine_1.category == "Fashion"

        # Change the category and verify
        magazine_1.category = "Life Style"
        assert magazine_1.category == "Life Style"

        # Test invalid category with exceptions
        with pytest.raises(Exception):
            magazine_1.category = 2

    def test_category_len(self):
        """Magazine category must have length greater than 0"""
        magazine_1 = Magazine("Vogue", "Fashion")

        # Verify non-empty category
        assert magazine_1.category != ""

        # Test empty category with exceptions
        with pytest.raises(Exception):
            magazine_1.category = ""

    def test_has_many_articles(self):
        """Magazine has many articles"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        article_1 = Article(author, magazine, "How to wear a tutu with style")
        article_2 = Article(author, magazine, "Dating life in NYC")

        # Verify articles are correctly associated
        assert len(magazine.articles()) == 2
        assert article_1 in magazine.articles()
        assert article_2 in magazine.articles()

    def test_articles_of_type_articles(self):
        """Magazine articles are of type Article"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "Dating life in NYC")

        # Verify articles are of type Article
        assert isinstance(magazine.articles()[0], Article)
        assert isinstance(magazine.articles()[1], Article)

    def test_has_many_contributors(self):
        """Magazine has many contributors"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        # Verify contributors are correctly associated
        assert len(magazine.contributors()) == 2
        assert author_1 in magazine.contributors()
        assert author_2 in magazine.contributors()

    def test_contributors_of_type_author(self):
        """Magazine contributors are of type Author"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_2, magazine, "Dating life in NYC")

        # Verify contributors are of type Author
        assert isinstance(magazine.contributors()[0], Author)
        assert isinstance(magazine.contributors()[1], Author)

    def test_contributors_are_unique(self):
        """Magazine contributors are unique"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_1, magazine, "How to be single and happy")
        Article(author_2, magazine, "Dating life in NYC")

        # Verify unique contributors
        assert len(set(magazine.contributors())) == len(magazine.contributors())
        assert len(magazine.contributors()) == 2

    def test_article_titles(self):
        """Returns list of titles of all articles written for that magazine"""
        author = Author("Carry Bradshaw")
        magazine = Magazine("Vogue", "Fashion")
        Article(author, magazine, "How to wear a tutu with style")
        Article(author, magazine, "Dating life in NYC")

        # Verify article titles
        assert magazine.article_titles() == ["How to wear a tutu with style", "Dating life in NYC"]

    def test_contributing_authors(self):
        """Returns authors who have written more than 2 articles for the magazine"""
        author_1 = Author("Carry Bradshaw")
        author_2 = Author("Nathaniel Hawthorne")
        magazine = Magazine("Vogue", "Fashion")
        Article(author_1, magazine, "How to wear a tutu with style")
        Article(author_1, magazine, "How to be single and happy")
        Article(author_1, magazine, "Dating life in NYC")
        Article(author_2, magazine, "Fashion Trends")

        # Verify contributing authors
        assert author_1 in magazine.contributing_authors()
        assert author_2 not in magazine.contributing_authors()
        assert all(isinstance(author, Author) for author in magazine.contributing_authors())

    def test_top_publisher(self):
        """Returns the magazine with the most articles"""
        # Clear all for testing
        Magazine.all_magazines = []
        Article.all_articles = []

        # No articles exist
        assert Magazine.top_publisher() is None

        # Create magazines and articles
        author = Author("Carry Bradshaw")
        magazine_1 = Magazine("Vogue", "Fashion")
        magazine_2 = Magazine("AD", "Architecture")
        Article(author, magazine_1, "How to wear a tutu with style")
        Article(author, magazine_1, "Dating life in NYC")
        Article(author, magazine_2, "2023 Eccentric Design Trends")

        # Verify top publisher
        assert Magazine.top_publisher() == magazine_1
        assert isinstance(Magazine.top_publisher(), Magazine)
