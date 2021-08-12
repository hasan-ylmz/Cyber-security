#klavyeden iki ürünün fiyatı girildiğinde toplam fiyat 200tl-300tl arasndaysa
#%15 indirim, 300-400 tl arasında ise %22 indirim ,400-750 tl arasında ise %27 indirim
# 750 -1000 arasında ise %34 indirim ,1000tlden fazla ise %40 indirim
#
 #   price1=int(input("Birinci ürünün fiyatını giriniz = "))
 #   price2=int(input("İkinci ürünün fiyatını giriniz = "))
 #   toplam=price1+price2
 #   if toplam>200:
 #       price=price1+ (price2-(price2/4))
 #       print(price)
 #   else :
 #      print(toplam)

price1 = int(input("birinci fiyatı giriniz = "))
price2 = int(input("ikinci fiyatı giriniz = "))
total=price1+price2
if total>200 and total<300:
    price_t=total-((total/100)*15)
    print("Ödenecek tutar",price_t)
elif total>300 and total<400:
    price_t=total-((total/100)*22)
    print("Ödenecek tutar",price_t)
elif total>400 and total<750:
    price_t=total-((total/100)*27)
    print("Ödenecek tutar",price_t)
elif total>750 and total<1000:
    price_t=total-((total/100)*34)
    print("Ödenecek tutar = ",price_t)
elif  total>1000:
    price_t=total-((total/100)*40)
    print("Ödenecek tutar = ",price_t)
else:
    print("ödenecek tutar = ", price_t)
