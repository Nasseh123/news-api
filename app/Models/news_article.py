class Newsarticle:
    """
    Newssource class to define newssource objects
    """
    def __init__(self,id,name,author,title,urlToImage,description,url,publishedAt,content):
        self.id=id
        self.name=name
        self.author=author
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.publishedAt=publishedAt
        self.content=content
