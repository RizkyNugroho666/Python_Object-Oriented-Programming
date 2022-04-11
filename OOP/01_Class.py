

class User:
    total = 0
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        User.total += 1

rizky = User("Name: Rizky", "Email: rizkynugroho2901@gmail.com", "Role: Admin")
print(User.total)

zelda = User("Name: Zelda", "Email: Zelda@gmail.com", "Role: User")
print(User.total)

print(rizky.name)
print(rizky.email)
print(rizky.role)
print(zelda.name)
print(zelda.email)
print(zelda.role)
