print("""**********************
Kullanıcı Girişi
************""")

sys_kullanıcı_adı = "Murat"
sys_parola = "7447"

kullanıcı_adı = input("Kullanıcı Adınız:")
parola= input("Parolanız:")

if (kullanıcı_adı== sys_kullanıcı_adı and parola!=sys_parola):
    print("Şifreniz hatalıdır,giriş yapılamadı!!")
elif(kullanıcı_adı!= sys_kullanıcı_adı and parola==sys_parola):
    print("Kullanıcı adınız hatalıdır,giriş yapılamadı!!")
elif(kullanıcı_adı!= sys_kullanıcı_adı and parola!=sys_parola):
    print("Kullanıcı adı ve şifreniz hatalıdır, giriş yapılamadı!!")
elif(kullanıcı_adı== sys_kullanıcı_adı and parola==sys_parola):
    print("Giriş başarı ile yapılmıştır.")

