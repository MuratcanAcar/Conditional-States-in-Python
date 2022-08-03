şekil = input("Dörtgenin mi yoksa Üçgenin mi tipini öğrenmek istiyorsunuz?")

if(şekil == "Dörtgen"):
    print("Lütfen kenarlarını giriniz:")

    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    d = int(input("Kenar-3:"))
    if(a==b and c==d):
        print("Şekil Karedir.")
    elif(a==c and b==d):
        print("Şekil Dikdörtgendir.")
    else:
        print("Dörtgen")

elif(şekil == "Üçgen"):
    print("Lütfen kenarları giriniz:")
    a = int(input("Kenar-1:"))
    b = int(input("Kenar-2:"))
    c = int(input("Kenar-3:"))
    if(abs(a+b)>c and abs(a+c) >b and abs(b+c) > a ):
       if(a==b and a==c):
        print("Eşkenar Üçgen")
       elif((a==b and a!=c) or (a==c and a!=b) or (b==c and b!=a)):
         print("İkizkenar Üçgen")
       else:
         print("Çeşitkenar Üçgen")
    else:
       print("Üçgen Belirtmiyor")
else:
    print("Geçersiz şekil!")
