#Liður 1, Spyr um þrjár tölur og finnur út miðgildið
print("Gefðu mig þrjár Heiltölur og ég skal finna miðgildið")
print()
num1=int(input("Sláðu inn fyrsta tölu: "))
num2=int(input("Sláðu inn annar tölu: "))
num3=int(input("Sláðu inn þriðja tölu: "))
if num1>num2:
    if num1<num3:
        miðjan= num1
    elif num2>num3:
        miðjan= num2
    else:
        miðjan= num3
else:
    if num1>num3:
        miðjan= num1
    elif num2<num3:
        miðjan= num2
    else:
        miðjan= num3
print()
print("Talan í miðjunni er",miðjan)
print()

#Liður 2, Umbreytir tölu í sentimetrar eða tommur
print("Gefðu mig tölu og ég skal breyta það í tommur eða sentimetra")
print()
number = float(input(" Sláðu inn tölu: "))
choice = input(str(" Ef þú vilt umbreyta frá sentimetra í tommu stimplaðu 'A' \n Ef þú vilt umbreyta frá tommum í sentimetra stimplaðu 'B': "))
if choice in ("A" or "a"):
    print(" Svarið þitt er" , number*2.54, "tommur")
    
else:
    print(" Svarið þitt er" , number/2.54, "sentimetrar")

print()

#Lidur 3, Forritið spyr um númer mánaðar. Forritið skrifar síðan hvort nú sé vetur, sumar, vor eða haust.

month = input("Sláðu inn númer mánuð.): ")

if month in ('1', '2', '3'):
	season = 'Nú er daginn tekið að lengja.'
elif month in ('4', '5'):
	season = 'Vorið er komið og grundirnar gróa.'
elif month in ('6','7', '8'):
	season = 'Núna er sumarið komið með blóm í haga.'
elif month in ('9','10'):
        season =  'Núna er haustið gengið í garð.'
elif month in ('11','12'):
        season = 'Núna styttist í jólin'

else:
	season = 'Rangur innsláttur'

if (month == '3') :
	season = 'Nú er daginn tekið að lengja.'
elif (month == '5') :
	season = 'Vorið er komið og grundirnar gróa.'
elif (month == '8') :
	season = 'Núna er sumarið komið með blóm í haga.'
elif (month == '10') :
	season = 'Núna er haustið gengið í garð.'
elif (month == '12'):
        season = 'Núna styttist í jólin'


print (season)

print()
#Lidur 4, Spurt er um kyn og tvær tölur
name = input("hvað er nafnið þitt?")
gender = input("hvort ertu kk eða kvk?")

if gender.lower() == 'kk':
    print("Blessaður "+name)
elif gender.lower() == 'kvk':
    print("Blessuð "+name)
else:
    print('Blessaður eða Blessuð ég veit ekki hvors kyns þú ert')


