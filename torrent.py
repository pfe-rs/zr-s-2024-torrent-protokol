import threading
import hashlib

class Device():
    
    def __init__(self,name, device_id):
        self.name = name
        self.id = device_id
        self.active = False
        

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

    def Ucitaj(self,ime_fajla,parts=3):
       
        self.parts=parts
        f=open(ime_fajla,"r")
        self.ime_fajla=ime_fajla
        tekst=f.read()
        self.data=tekst
        result=divide_string(self.data,self.parts)
        self.datapieces=[]
        nek=[]
        for bruh in result:
            nek.append(custom_hash(bruh))
            self.datapieces.append(bruh)

        self.datahash=nek
        for u in range(14):
            self.datahash.append("0")
            self.datapieces.append("0")
        f.close()
        
        

    def Napravi_torrent(self,ime_fajla):
        lokacija=self.id
        ime = self.ime_fajla  
        delovi=self.parts
        result=divide_string(self.data,self.parts)
        nek=[]
        for str1 in result:
            nek.append(custom_hash(str1)) 
        self.torrentfile=str(delovi)+","
        self.torrentfile=self.torrentfile+",".join(str(element)for element in nek)
        self.torrentfile=self.torrentfile+","+str(lokacija)+","+str(ime)
        f = open(f"{ime_fajla}.txt", "w")
        f.write(self.torrentfile)
        f.close()
        print(self.torrentfile)
        print(result)


    def Uzmi_hash(self,ime_fajla):

        f=open(ime_fajla,"r")
        tekst=f.read()
        self.hash_za_trazenje=tekst.split(",")
        #print(self.hash_za_trazenje[0],self.hash_za_trazenje[1],self.hash_za_trazenje[2])
        return self.hash_za_trazenje

    def Skidaj_torrent(self,ime_fajla):
        self.podaci=[]
        poruka=""
        f=open(ime_fajla,"r")
        tek=f.read()
        delovi=tek.split(",")
        for i in range(int(tek[0])):
           for devices in pratilac.available_devices.values():
                bruh=[15]
                for k in range(14):
                    bruh.append("0")
                bruh=devices.Uzmi_hash(ime_fajla)
                #print(bruh[i+1],devices.datahash[i])
                #print(devices.datapieces[i])
                if bruh[i+1]==devices.datahash[i]:
                    self.podaci.append(devices.datapieces[i])
                    break
                
        print(self.podaci)
        for str2 in self.podaci:
            poruka=poruka+str2
        print(poruka)
        f.close()
        f=open(f"skinuti-{ime_fajla}","w")
        f.write(poruka)

            

                    




        
        



def divide_string(string, parts=3):
        part_length = len(string) // parts
        substrings = [string[i:i + part_length] for i in range(0, len(string), part_length)]

        if len(substrings) > parts:
            substrings[-2] += substrings[-1]
            substrings.pop()

        return substrings

#def custom_hash(string,prime=197):
     #hash_value=0
     #for char in string:
     #     hash_value+=ord(char)
     #return hash_value% prime
        

        

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
    
def OS_meni():
    
    char="0"

    print(f"Broj uredjaja:{len(pratilac.available_devices)}")
    print("Odaberite opciju\n")
    print("1. Dodajte novi uredjaj\n")
    print("2. Dodajte file u uredjaj\n")
    print("3. Napravite torrent file\n")
    print("4. Skinite file\n")
    print("5. Kraj")

    char=input()
    return char





def custom_hash(string):
    hashed_value=hashlib.sha256(string.encode()).hexdigest()
    return hashed_value

pratilac=Tracker()
char="0"

while(char!="5"):
    char=OS_meni()

    if char=="1":
        print("Unesite ime vaseg uredjaj\n")
        ime1=input()
        print("Unesite id vaseg uredjaja\n")
        id1=int(input())
        a=Device(ime1,id1)
        pratilac.add_device(a)
        print("Uredjaj napravljen")
        
    elif char=="2":
        if((len(pratilac.available_devices)==0)):
            print("Nema uredjaja")
        else:
            for devices in pratilac.available_devices.values():
                print(devices.name)
            print("Unesite ime uredjaja u koji ubacujete\n")
            ime1=input()
            print("Unesite ime faila koji unosite\n")
            fajl=input()
            print("Unesite broj piecova\n")
            br=int(input())
            for devices in pratilac.available_devices.values():
                if devices.name==ime1:
                    devices.Ucitaj(fajl,br)
            print("File ucitan\n")
    elif char=="3":
        if((len(pratilac.available_devices)==0)):
            print("Nema uredjaja")
        else:
            for devices in pratilac.available_devices.values():
                print(devices.name)
            print("Unesite ime ciji torren tfile pravite\n")
            ime1=input()
            print("Unesite kako ce se zvati fail\n")
            ime2=input()
            for devices in pratilac.available_devices.values():
                if devices.name==ime1:
                    devices.Napravi_torrent(ime2)
            print("fajl napravljen\n")

    elif char=="4":
        if((len(pratilac.available_devices)==0)):
            print("Nema uredjaja")
        else:
            for devices in pratilac.available_devices.values():
                print(devices.name)
            print("Unesite na koji uredjaj skidate\n")
            ime2=input()
            print("unesite ime torret file za skidanje\n")
            ime1=input()
            for devices in pratilac.available_devices.values():
                if devices.name==ime2:
                    devices.Skidaj_torrent(ime1)
            print("Skinuto\n")


        



        
        






'''uredjaj=Device("bas radi",0)
uredjaj2=Device("najjaci uredjaj",1)
uredjaj3=Device("BAS JAK UREDAJ",2)
uredjaj.Ucitaj("file.txt",3)
uredjaj2.Ucitaj("file2.txt",3)
uredjaj3.Ucitaj("file3.txt",9)
uredjaj.Napravi_torrent("amogus")
uredjaj2.Napravi_torrent("najjaci torrent")
uredjaj3.Napravi_torrent("idegas")
pratilac.add_device(uredjaj)
pratilac.add_device(uredjaj2)
pratilac.add_device(uredjaj3)
print(pratilac.available_devices[1].name)
uredjaj.Skidaj_torrent("idegas.txt")
uredjaj2.Skidaj_torrent("amogus.txt")
uredjaj3.Skidaj_torrent("najjaci torrent.txt")'''
