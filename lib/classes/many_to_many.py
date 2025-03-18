class Article:
 # class variable to store all instances of Article
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance(new_title, str) and len(new_title) > 0 and not hasattr(self, '_title'):
            self._title = new_title
        else:
            return 'invalid title'
        

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            return f'invalid author'




class Author:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        # Setter to set the name only if it's a non-empty string and `_name` doesn't already exist
        if isinstance(new_name, str) and len(new_name) > 0 and not hasattr(self, '_name'):
            self._name = new_name
        else:
            return 'invalid author'


    def articles(self):
        # return a list of all articles written by the author
        article_list= []
        for article in Article.all:
            if article.author is self:
                article_list.append(article)
        return article_list


    def magazines(self):
        # return a unique list of magazines for which the author has written articles
        magazine_list= []
        for magazine_obj in self.articles():
            if magazine_obj.author is self:
                magazine_list.append(magazine_obj.magazine)
        return list(set(magazine_list))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics= []
        for topic in self.articles():
                topics.append(topic.magazine.category)
        return list(set(topics))if topics else None
        
        
    

class Magazine:

# initilalize the magazine with a name and category
    def __init__(self, name, category):
        self.name = name
        self.category = category
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            return f'invalid magazine'
        
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            return f'bad category'


    def articles(self):
        article_list= []
        for article in Article.all:
            if article.magazine is self:
                article_list.append(article)
        return article_list

    def contributors(self):
        author_list= []
        for article in Article.all:
            if article.magazine is self:
                author_list.append(article.author)
        return list(set(author_list))

    def article_titles(self):
        articles = self.articles()
        if articles:
            titles = []
            for article in articles:
                titles.append(article.title)
            return titles
        else:
            return None
        


    def contributing_authors(self):
        cont_list = [] 
        for author in self.contributors():
            if isinstance(author, Author):
                article_count = sum(1 for article in self.articles() if article.author == author)
                if article_count > 2:
                    cont_list.append(author)
        if cont_list:    
            return cont_list
        else:
            return None