print("Kodlamaio")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
#int, integer => tam sayı
vade = 36
vade2 = "36"
ekVade = 6

# float, decimal, double 
aylıkOdeme = 200.50 

# bool, boolean => True ya da False 
yukselisteMi= False

# Matematiksel operatörler

# +
print(5 + 5)
print(vade + 12)
print(vade + ekVade)

# -
print(5-5)
print(vade-12)
print(vade-ekVade)

# * 
print(5*5)
print(vade*12)
print(vade*ekVade)

# / 

print(5/5)
print(vade/12)
print(vade/ekVade)


yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)

# mod operatörü %
print(10%2)
print(vade % 5)
print(vade % ekVade)

# mantıksal operatörler
print(1 == 1) 
print(1 == 2) 

print(1 > 2)
print(3 > 1)
print(1 > 1)
print(1 >= 1)

print(1 < 2)
print(1 < 3)
print(1 < 1)
print(1 <= 1)

print(1 != 1)
print(1 != 2)

# or, and


# or => veya
print(1 > 2 or 5 > 2)
print(1 > 2 and 5 > 2)
print(1 > 2 or 5 > 2 and 3 > 2)

print(1 > 2 and 5 > 2 and 3 > 2)

print(2 > 1 or 1 > 2 and 3 > 2)

#karar yapıları
#if else  
sayi1 = 15
sayi2 = 15

#sayi1 sayi2'den büyükse ekrana sayi1 daha büyüktür yazdır
#condition

#indent
if sayi1 < sayi2:
    print("Sayi1 Sayi2'den büyüktür")
#eğer if bloğuna girmezse
elif sayi1 == sayi2:
    print("Sayi1 Sayi2'ye eşittir")
#eğer if ve else if blokolarından hiçbirine girmezse 
else:
    print("Sayi1 Sayi2den küçüktür")

print("***************")

if sayi1 <= sayi2:
    print("Sayi1 Sayi2'den küçüktür")
if sayi1 == sayi2:
    print("İki sayi eşittir")
else:
    print("Sayi1 Sayi2'den büyüktür")

print("Burası if bloğunun dışındadır")





