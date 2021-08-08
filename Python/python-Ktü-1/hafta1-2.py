price=int(input("Ürün fiyatını  giriniz = "))
borc=0
if price>100:
    borc=price
    print("borcunuz ", borc)
else:
    borc=price+10
    print("borcunuz ",borc)
