class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username

user_1 = User(username="Satheesh", user_id = "001")
print(user_1.username)

# user_2 = User("005", "Pandian")
# print(user_2.username)