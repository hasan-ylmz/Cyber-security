final =int(input("Final notunuzu giriniz = "))
vize= int(input("Arasınav notunuzu giriniz = "))
ort=(vize+final)/2

if ort>0 and ort<45:
    print("Ortalamanız = ",ort, "Harf = ","F" )
elif ort>45 and ort<60:
    print("Ortalamanız = ",ort, "Harf = ", "D" )
elif ort>60 and ort<70:
    print("Ortalamanız = ",ort, "Harf = ", "C")
elif ort>70 and ort<85:
    print("Ortalamanız = ",ort, "Harf = ", "B" )
elif ort>85 and ort<100:
    print("Ortalamanız = ",ort, "Harf = ", "A" )        
