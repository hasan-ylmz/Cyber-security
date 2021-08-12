no = int(input("Birinci sayıyı giriniz ="))
nt = int(input("İkinci sayıyı giriniz = "))
islem = int(input("Toplama için 1 , çıkarma için 2 , bölme için 3, çarpma 4 için 4 e basınız ="))
sonuc=0
if islem==1:
    sonuc=no+nt
    print(sonuc)    
elif islem==2:
    sonuc=no-nt
    print(sonuc)  
elif islem==3:
    sonuc=no/nt
    print(sonuc)    
elif islem==4:
    sonuc=no*nt
    print(sonuc) 