    
import threading

class Device():
    
    def __init__(self,name, device_id):
        self.name = name
        self.id = device_id
        self.active = False
        

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def Ucitaj(self,data):
        self.data=data
        result=divide_string(self.data,3)
        nek=[]
        for bruh in result:
            nek.append(custom_hash(bruh))
        self.datahash=nek
        

    def Napravi_torrent(self,ime_fajla):
        lokacija=self.id
        ime = self.name   
        result=divide_string(self.data,3)
        nek=[]
        for str1 in result:
            nek.append(custom_hash(str1)) 
        print(nek)
        print(lokacija)
        print(ime)
        self.torrentfile=",".join(str(element)for element in nek)
        self.torrentfile=self.torrentfile+","+str(lokacija)+","+str(ime)
        f = open(f"{ime_fajla}.txt", "w")
        f.write(self.torrentfile)
        print(self.torrentfile)
        



def divide_string(string, parts=3):
        part_length = len(string) // parts
        substrings = [string[i:i + part_length] for i in range(0, len(string), part_length)]

        if len(substrings) > parts:
            substrings[-2] += substrings[-1]
            substrings.pop()

        return substrings

def custom_hash(string,prime=31):
     hash_value=0
     for char in string:
          hash_value+=ord(char)
     return hash_value% prime
        

        

class Tracker:
    def __init__(self):
        self.available_devices = {}
        self.check_timer = None
        self.check_interval = 0.1

    def add_device(self, device):
        self.available_devices[device.id] = device
        print(f"Device {device.name} registered with tracker.")

    def get_available_devices(self):
        return self.available_devices.values()

    def check_device_activity(self):
        inactive_devices = [device for devices in self.available_devices.values() if not devices.active]
        for device in inactive_devices:
            del self.available_devices[device.id]
            print(f"Device {device.id} is inactive and has been removed from the list.")

        self.check_timer = threading.Timer(self.check_interval, self.check_device_activity)
        self.check_timer.start()

    def start_activity_check(self):
        self.check_timer = threading.Timer(self.check_interval, self.check_device_activity)
        self.check_timer.start()

    def stop_activity_check(self):
        if self.check_timer:
            self.check_timer.cancel()
    


pratilac=Tracker()
uredjaj=Device("bas radi",1)
uredjaj2=Device("najjaci uredjaj",2)
uredjaj.Ucitaj("torretnt")
uredjaj2.Ucitaj("amogus")
uredjaj.Napravi_torrent("amogus")
uredjaj2.Napravi_torrent("najjaci torrent")
pratilac.add_device(uredjaj)
print(pratilac.available_devices[1].name)
