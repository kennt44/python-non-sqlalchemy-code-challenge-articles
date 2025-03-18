class Magazine:
    all_magazines = []

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
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise Exception("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        from article import Article
        return [article for article in Article.all_articles if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        return [article.title for article in self.articles()] or None

    def contributing_authors(self):
        return [author for author in self.contributors() if len([a for a in self.articles() if a.author == author]) > 2] or None

    @classmethod
    def top_publisher(cls):
        from article import Article
        articles_count = {magazine: len(magazine.articles()) for magazine in cls.all_magazines}
        return max(articles_count, key=articles_count.get, default=None)
