from unicodedata import name
from winreg import KEY_ALL_ACCESS


class User:
    def __init__(self, name, kelas): # __init__ adalah Constructor
        self.name = name
        self.kelas = kelas 

rizky = User("Rizky", "SE 05 B")

print(rizky.name)
print(rizky.kelas)
