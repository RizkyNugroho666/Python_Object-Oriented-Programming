
class User:
    total = 0
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role
        User.total += 1
        
    #method
    def info(self):
        return f"{self.name} - {self.email} - {self.role}"

    def update_role(self, new_role):
        if self.role != "user": # Jika role nya User, maka akan tetap user, tidak bisa di update
            self.role = new_role

rizky = User("Rizky", "rizkynugroho2901@gmail.com", "user")
print(rizky.info())
rizky.update_role("Moderator")
print(rizky.info())

zelda = User("Zelda", "zelda@gmail.com", "admin")
print(zelda.info())
zelda.update_role("Super Admin")
print(zelda.info())
