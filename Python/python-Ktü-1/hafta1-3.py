elma_kilo= int(input("Elma kg yazınız = "))
armut_kilo=int(input("armut kg yazınız = "))
elma=10
armut=8
toplam_borc=((elma_kilo*elma)+(armut_kilo*armut))
borc=0
if toplam_borc>100:
    borc=toplam_borc-((toplam_borc/100)*10)
    print("borcunuz = ",borc)
else:
    borc=toplam_borc
    print("borcunuz = ",borc)   




