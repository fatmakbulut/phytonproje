class Library:
    file = open("books.txt","a+",encoding="utf-8")

    adList=[]
    kitapList=[]

    def kitapList (self):
        self.file.seek(0)
        kitaplar= self.file.read().splitlines()
        if not kitaplar:
            print("Kitap mevcut değildir.")
        else:
            print("Kitap Listesi")
            for kitap in kitaplar:
                baslik,yazar,yayinlanmaTarihi,sayfaSayisi=kitap.split(',')
                print(f"Başlık:{baslik},Yazar: {yazar},Yayınlanma Tarihi:{yayinlanmaTarihi},Sayfa Sayısı:{sayfaSayisi}")

    def kitapEkle (self):
         baslik= input("Kitap başlığını giriniz:")
         yazar= input("Yazar adını giriniz:")
         yayinlanmaTarihi=input("Yayınlanma tarihini giriniz:")
         sayfaSayisi=input("Sayfa sayısını giriniz:")
         kitapBilgi=f"{baslik},{yazar},{yayinlanmaTarihi},{sayfaSayisi}\n"
         self.file.write(kitapBilgi)
         print(f"Kitap'{baslik}'başarılı bir şekilde eklendi.")


    def kitapSil (self):
        baslik=input("Silmek istediğiniz kitabın başlığını yazınız:")
        self.file.seek(0)
        kitaplar=self.file.readlines()
        kitaplariGuncelle=[]
        silindi=False
        for kitap in kitaplar:
            if baslik not in kitap:
                kitaplariGuncelle.append(kitap)
            else :
                silindi=True
        if silindi:
            self.file.seek(0)
            self.file.truncate()
            self.file.writelines(kitaplariGuncelle)
            print(f"Kitap '{baslik}' başarılı bir şekilde silindi.")
        else:
            print(f"Kitap '{baslik}' bulunamadı.")


kütüp= Library()

while True:
    print("\n*** MENÜ ***")
    print("1) Kitaplarin Listesi")
    print("2) Kitap Ekle")
    print("3) Kitabı Sil")
    print("4) Çık")

    secenek= input ("Seçiminizi giriniz: ")

    if secenek =='1':
        kütüp.kitapList()
    elif secenek == '2':
        kütüp.kitapEkle()
    elif secenek == '3':
        kütüp.kitapSil()
    elif secenek == '4':
        break
    else:
        print("Böyle bir seçenek yoktur. Lütfen tekrar deneyiniz.")









