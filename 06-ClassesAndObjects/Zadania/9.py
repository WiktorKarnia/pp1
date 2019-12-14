class University():
    def __init__(self, name, fullname):
        self.name = name
        self.fullname = fullname
    def set_name(self):
        new_name = input("Podaj nowa nazwe: ")
        self.name = new_name
    def set_fullname(self):
        new_fullname = input("Podaj nowa pełna nazwe: ")
        self.fullname = new_fullname
p1 = University("UEK","Uniwersytet Ekonomiczny w Krakowie")
print('Nazwa uniwersytetu to: '+ p1.name)
print('Pełna nazwa to: '+p1.fullname)
p1.set_name()
p1.set_fullname()
print('Nazwa uniwersytetu to: '+ p1.name)
print('Pełna nazwa to: '+p1.fullname)
