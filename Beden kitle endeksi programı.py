print("""******************
Beden kitle İndeksi Hesaplama Programı (BKİ)
*****************""")

kilo = int(input("Kaç kilosunuz?"))
boy = float(input("Boyunuz kaç?"))

bki= kilo / (boy**2)
if(bki<=18.5):
    print("Zayıfsınız")
elif(18.5 <= bki <= 25):
    print("Normal kilodasınız")
elif(25 <= bki <= 30):
    print("Kilolusunuz")
elif(30 <= bki):
    print("Obezsiniz")
