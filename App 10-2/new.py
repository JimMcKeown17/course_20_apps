class User:
    def __init__(self, name, birthyear):
        self.name = name.upper()
        self.birthyear = birthyear
    def get_name(self):
        return self.name
    def age(self):
        current_year = 2023
        self.age = current_year - self.birthyear
        return self.age

user1 = User('John', 1982)
print(user1.get_name())
print(user1.age())


