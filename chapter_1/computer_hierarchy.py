class Computer:
    """basic requirements for computer"""
    
    def __init__(self):
        self.ram = None
        self.rom = None
        self.Os = None

class Portable(Computer):
    """Portable devices"""
    
    def __init__(self):
        super().__init__()
    
    def set_ram(self, ram):
        if ram <= 32:
            self.ram = ram
        else:
            print("not possible ram size ", ram)
    
    
    def set_rom(self, rom):
        if rom <= 512:
            self.rom = rom
        else:
            print("not possible rom size ", rom)
    
    
    def set_os(self, os):
        if os in ['windows', 'android', 'mac']:
            self.Os = os
        else:
            print("not possible this os ", os)


class Non_Portable(Computer):
    """replicate the non-portable devices"""
    
    def __init__(self):
        super().__init__()

l1= Portable()
l1.set_ram(32)
l1.set_rom(500)
l1.set_os("windows")

d1 = Non_Portable()
d1.ram = 1000
d1.rom = 10000
d1.Os = 'linux'

print(f"device name l1, specfs-> ram: {l1.ram}, rom: {l1.rom}, os: {l1.Os}")
print(f"device name d1, specfs-> ram: {d1.ram}, rom: {d1.rom}, os: {d1.Os}")