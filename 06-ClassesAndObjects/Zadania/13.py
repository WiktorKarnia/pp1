class TV():
    def __init__(self, is_on, channel_no):
        self.is_on = is_on
        self.channel_no = channel_no
    channels = []
    def on(self):
        self.is_on = True
    def off(self):
        self.is_on = False
    def set_channel_no(self):
        new_channel_no = input("Na jaki kanał chcesz zminic? ")
        self.channel_no = new_channel_no
    def set_channels(self):
        self.channels.append('TVP1')
        self.channels.append('TVP2')
        self.channels.append('Polsat')
        self.channels.append('TVN')
        self.channels.append('Filmbox')
    def show_channels(self):
        if len(self.channels) == 0:
            print("Telewizor niezaprogramowany, brak dostępnych kanałów")
        else:
            print(self.channels)
    def show_status(self):
        if self.is_on == True:
            print("Telewizor włączony, kanał:",self.channel_no)
        else:
            print("Telewizor wyłaczony.")
p1 = TV(False,4)
p1.show_status()
p1.on()
p1.show_status()
p1.show_channels()
p1.set_channels()
p1.show_channels()
p1.show_status()
p1.off()
p1.show_status()


