class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        from article import Article
        return [article for article in Article.all_articles if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        from article import Article
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise Exception("Title must be a string between 5 and 50 characters.")
        return Article(self, magazine, title)

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines()))
