class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise Exception("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters.")
        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name.strip()) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("Invalid magazine.")
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = list({magazine.category for magazine in self.magazines()})
        return categories if categories else None


class Magazine:
    def __init__(self, name, category):
        if len(name) < 2 or len(name) > 16:
            raise Exception("Name must be between 2 and 16 characters.")
        if len(category) == 0:
            raise Exception("Category cannot be empty.")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 16:
            raise Exception("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) == 0:
            raise Exception("Category cannot be empty.")
        self._category = value

    @property
    def articles(self):
        """Returns a list of all articles for this magazine."""
        return [article for article in Article.all if article.magazine == self]

    @property
    def contributors(self):
        """Returns a list of all unique authors who contributed to this magazine."""
        return list(set(article.author for article in self.articles))

    def article_titles(self):
        """Returns the titles of all articles in the magazine."""
        return [article.title for article in self.articles]

    def contributing_authors(self):
        """Returns authors who have written more than 2 articles for this magazine."""
        author_article_count = {}
        for article in self.articles:
            author_article_count[article.author] = author_article_count.get(article.author, 0) + 1
        authors = [author for author, count in author_article_count.items() if count > 2]
        return authors if authors else None  # Return None only when no contributing authors

    @classmethod
    def top_publisher(cls):
        """Returns the magazine with the most articles across all magazines."""
        magazines = {article.magazine for article in Article.all}
        if not magazines:
            return None
        return max(magazines, key=lambda mag: len(mag.articles))