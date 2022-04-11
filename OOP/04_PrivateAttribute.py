
# Private Attribute

class User:
    total = 0
    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.__role = role # INI ADALAH PRIVATE VARIABLE/ATTRIBUTE
        User.total += 1
    #method
    def info(self): # Function untuk memanggil info user
        return f"{self.name} - {self.email} - {self.__role}"

    def update_role(self, new_role): # Function untuk mengubah role
        if self.__role != "user": # Jika role nya User, maka akan tetap user, tidak bisa di update
            self.__role = new_role

    def getRole(self): # Function hanya untuk memanggil role
        return self.__role

rizky = User("Rizky", "rizkynugroho2901@gmail.com", "user")
rizky.update_role("Moderator") # untuk meng-update/mengubah role
print(rizky.info()) # untuk memanggil info user
print(rizky.__dict__) # untuk mengetahui variable
print("role:", rizky.getRole()) # untuk memanggil role saja