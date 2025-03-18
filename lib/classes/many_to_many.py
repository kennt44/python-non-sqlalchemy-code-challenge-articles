class Article:
    # Class variable to store all instances of Article
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception("Title must be a string between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        """Title is immutable."""
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        """The name is immutable."""
        return self._name

    def articles(self):
        """Returns a list of all articles written by the author."""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Returns a unique list of magazines the author has written for."""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """Creates and returns a new Article for the given magazine."""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns a unique list of categories of magazines the author has written for."""
        return list(set(magazine.category for magazine in self.magazines()))


class Magazine:
    all_magazines = []  # Class variable to store all instances of Magazine

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (2 <= len(new_name) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        self._name = new_name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        if not isinstance(new_category, str) or len(new_category) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = new_category

    def articles(self):
        """Returns a list of all articles in this magazine."""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Returns a unique list of authors who have written for this magazine."""
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        """Returns a list of titles of all articles in this magazine."""
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        """Returns authors with more than 2 articles in this magazine."""
        return [
            author for author in self.contributors()
            if len([article for article in self.articles() if article.author == author]) > 2
        ] or None

    @classmethod
    def top_publisher(cls):
        """Returns the magazine with the most articles."""
        if not Article.all:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()), default=None)
