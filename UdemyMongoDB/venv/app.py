# MONGO DB
# COMANDO DO MONGO DB
# use fullstack (Cria database fulstack)
# show dbs (Mostra bases de dados)
# show collections (mostra collections)
# db.students.insert({"Name": "Wagner", "idade": 32}) (Cria coleção na tabela)
# db.students.find() (lista todos os registros)
# db.students.remove({"Name": "Wagner"}) (Remove registro)


import pymongo


# ----------- AULA 36 --------------------
from Models.Database import Database
from Models.Post import Post

uri = "mongodb://127.0.0.1/27017"
client = pymongo.MongoClient(uri)
database = client["fullstack"]
collection = database["students"]

students = collection.find()

for student in students:
    print(student)

# ----------- AULA 37 --------------------

students2 = collection.find()
students2List = []

# Adicionando a uma lista
for student in students2:
    students2List.append(student)

for list in students2List:
    print(list['name'])

# Criando direto uma lista
students3 = [student for student in collection.find()]
print(students3)

# Adicionando somente campo NAME
students4 = [student['name'] for student in collection.find()]
print(students4)

# Adicionando a lista com condição
students5 = [student for student in collection.find() if student['idade'] == 32]
print(students5)


# ----------- AULA 38 - Orientação a objetos --------------------
class MyClass:
    def __init__(self, arg):
        self.arg1 = arg

mc = MyClass("test")

print(mc.arg1)

# O import tem que ser "from Models.Post import Post"
post = Post(1, 1, "2020-02-20", "Title 1", "content 1", "Author 1")
print(post.author)

# ----------- AULA 40 - Orientação a objetos --------------------

Database.initialize()
