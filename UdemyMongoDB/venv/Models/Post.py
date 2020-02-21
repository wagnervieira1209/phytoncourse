from Models.Database import Database

class Post:

    def __init__(self, id, blog_id, date, tittle, content, author):
        self.id = id
        self.blog_id = blog_id
        self.create_date = date
        self.tittle = tittle
        self.content = content
        self.author = author

    def save_to_mongo(self):
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        return {
            'id': self.id,
            'blog_id': self.blog_id,
            'create_date': self.create_date,
            'author': self.author,
            'tittle': self.tittle,
            'content': self.content
        }

    @staticmethod
    def from_mongo(id):
        return Database.find_one(collection='posts',
                                 query={'id': id})

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts', query={'blog_id': id})]

