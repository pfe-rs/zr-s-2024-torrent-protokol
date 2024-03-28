class Tracker():
    def __init__(self):
        self.devices=[]

    
class Device():
    
    def __init__(self,name,value=0):
        self.name=name
        pratilac.devices.append(self.name)
    
    def Ucitaj(self,data):
        self.data=data
        result=divide_string(self.data,3)
        nek=[]
        for bruh in result:
            nek.append(custom_hash(bruh))
        self.datahash=nek
        

    def Napravi_torrent(self,ime_fajla):
        lokacija=pratilac.devices.index(self.name)
        ime=self.name
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
        

        
    




pratilac=Tracker()
uredjaj=Device("bas radi")
uredjaj2=Device("najaci uredjaj")
uredjaj.Ucitaj("torretnt")
uredjaj2.Ucitaj("amogus")
uredjaj.Napravi_torrent("amogus")
uredjaj2.Napravi_torrent("najaci torrent")
