age= int(input(" Yaşınızı giriniz = "))
weight = int(input("Kilonuzu giriniz = "))
price = int(input("ürün fiyatını giriniz = "))

if age>21 or weight<80:
    lastprice=price - ((price/100)*20)
    print(lastprice)
else:
    print("Ödenecek tutar = " ,price)