a = int (input("ilk sayıyı giriniz:"))

b = int (input("ikinci sayıyı giriniz:"))

c = int (input("Üçüncü sayıyı giriniz:"))

if(a>b and a>c):
    print("En büyük sayı:", a )
elif(b>a and b>c):
    print("En büyük sayı:", b )
elif(c>a and c>b):
    print("En büyük sayı:", c )
elif(a==b and a==c):
    print("Tüm sayılar Eşittir.")
    