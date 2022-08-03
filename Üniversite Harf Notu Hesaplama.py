vize1 = int(input("Vize Notunuz:"))

vize2 = int(input("İkinci Vize Notunuz"))

final = int(input("Final Notunuz:"))

toplam_not = (vize1*30)/100 + (vize2*30) /100 + (final*40)/100

if(toplam_not >= 90):
    print("Harf notunuz AA' dır.")
elif(toplam_not >= 85):
    print("Harf notunuz BA' dır.")
elif(toplam_not >= 80):
    print("Harf notunuz BB' dir.")
elif(toplam_not >= 75):
    print("Harf notunuz BC' dir.")
elif(toplam_not >= 70):
    print("Harf notunuz CC' dir.")
elif(toplam_not >= 65):
    print("Harf notunuz DC' dir.")
elif(toplam_not >= 60):
    print("Harf notunuz DD' dir.")
elif(toplam_not >= 55):
    print("Harf notunuz FD' dir.")
elif(toplam_not < 55):
    print("Harf notunuz FF' dir.")
