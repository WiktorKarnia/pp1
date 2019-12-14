class University():
    def __init__(self, name):
        self.name = name
    def set_name(self):
        new_name = input("Podaj nowa nazwe: ")
        self.name = new_name
p1 = University("UEK")
print('Nazwa uniwersytetu to: '+ p1.name)
p1.set_name()
print('Nazwa uniwersytetu to: '+ p1.name)