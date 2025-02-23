faiz = 1.59
vade = 36
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)

#print(int(krediAdi))

faiz = str(faiz)

#vade = input("Lütfen istediğiniz vade sayısını giriniz: ")
print(type(vade)) 
print(int(vade) + 12)

vade = int(vade) + 12

#string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade: 


print("Seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("Seçtiğiniz vade sonucu ortaya çıkan vade: {vadeSayisi}".format(vadeSayisi = vade))
print(f"Seçtiğinia vade sonucu ortaya çıkan vade: {vade}")


isim = "Resul"
metin = "merhaba {name}".format(name=isim)
print(metin)


# f-string

metin = f"Hoşgeldiniz {1+1}"
print(metin)

#listeler
#döngüler
#fonksiyonlar

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut kredisi"]
print(type(krediler))

print(krediler)

print(krediler[0])

print(len(krediler))
# print(krediler[3]) => hata verir

krediler.append("Özel Kredi")
print(krediler)

krediler.append("X kredisi")
print(krediler)

krediler.pop(0)
print(krediler)

krediler.append("Taşıt Kredisi")
print(krediler)

krediler.remove("Taşıt Kredisi") #listede aynı değerden birden fazla varsa indeksi küçük olanı siler
print(krediler)

krediler.extend(["Y kredisi", "Z Kredisi"])
print(krediler)

# for 

for i in range(10):
    print(i)

print("*********")

for i in range(5,11):
    print(i)

print("*********")

for i in range(0,51,10):
    print(i)

print("*********")

#for i in range(0.1,0.5):
    #print(i)

krediler = ["İhtiyaç Kredisi", "Taşıt Kredisi", "Konut Kredisi"]

for kredi in krediler:
    print(kredi)
print("*********")   

for i in range(len(krediler)):
    print(krediler[i])

#sonsuz döngü
i = 0
while i<10:
    print("x")
    i += 1
print("y")

print("*********")  

while True:
    print("X")
    break

print("*********")  

i = 0
while i<len(krediler):
    i+=1
    print(i)
    print(krediler[i])
    if krediler[i] == "Konut Kredisi":
        break

# fonksiyonlar

fiyat = 100
indirim = 20
#definition define
def calculate():
    print(100-20)

calculate()

def calculateWithParams(fiyat,indirim):
    print(fiyat-indirim)

def sayHello(isim):
    print(f"Merhaba {isim}" )


calculateWithParams(50,10)
calculateWithParams(100,30)

sayHello("Resul")

def calculatePrice(price,discount):
    print(price-discount)

def calculateAndReturn(price,discount):
    return price-discount

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat)

print("*********")  

fonk1 = calculatePrice(100,50)
fonk2 = calculateAndReturn(100,50)
print(fonk1)
print(fonk2)

print("*********")  


#sınıflar => classlar
#moduller
#paket yonetimi

class Human:
    #built-in
    #constructor
    #initialize
     
    def __init__(self,name):
        self.name = name
        print("Bir Human instancesi üretildi")
    def __str__(self):
        return f"STR fonksiyonundan dönen değer: {self.name}"
         
    def talk(self,sentence):
        name = "Sinan"
        print(f"{self.name}: {sentence}")

    def walk(self):
        print(f"{self.name} is walking")
    
#instance => örnek  

human1 = Human("İcardi")

human1.talk("merhaba")
human1.walk()
print(human1)


human2 = Human("Ğ")
human2.talk("Hola")
human2.walk()
print(human2)















