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

number = float(input(" Sláðu inn tölu: "))
choice = input(str(" Ef þú vilt umbreyta frá sentimetra í tommu stimplaðu 'A' \n Ef þú vilt umbreyta frá tommum í sentimetra stimplaðu 'B': "))
if choice in ("A" , "a"):
    print(" Svarið þitt er" , number/2.54, "tommur")
else:
    print(" Svarið þitt er" , number*2.54, "sentimetrar")


print()

#Lidur 3, Forritið spyr um númer mánaðar. Forritið skrifar síðan hvort nú sé vetur, sumar, vor eða haust.

month = input("Sláðu inn númer mánuð.: ")

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
name = input("hvað er nafnið þitt?: ")
gender = input("hvort ertu kk eða kvk?: ")

if gender.lower() == 'kk':
    print("Blessaður "+name)
elif gender.lower() == 'kvk':
    print("Blessuð "+name)
else:
    print('Blessaður eða Blessuð ég veit ekki hvors kyns þú ert')
print()

print("gefðu mig tvær tölur og ég mun reikna út hvort mismunur talnanna sé meiri eða minni en 100 og hvor er stærri. ") 
print()
x = int(input("Sláðu inn tölu: "))
y = int(input("Sláðu inn tölu: "))
if x < y:
    print (x, "er minni en", y)
    x = y-x
    print ("og mismunur er" , x)
elif x > y:
    print (x, "er stærri en", y)
    Y = x-y
    print ("og mismunur er:", y)
else:
    print (x, "og", y, "eru jafnstór")
print()
#Lidur 5, Forritið biður notanda um tölu sem er lægri en 0 eða hærri en 10. 
num = (input("Sláðu inn tölu sem er lægri en 0 eða hærri en 10: "))
if num in ('0', '1', '2', '3', '4,', '5', '6', '7', '8', '9', '10'):
    num2 = 'Þessi tala er ekki lægri en núll eða hærri en 10'
    
else:
       num2 = 'Vel gert snillingur!'

if (num == '10') :
    num2 = 'Þessi tala er ekki lægri en núll eða hærri en 10, fíflið þitt!'

print (num2)

print()

choice = input(str(" Stimplaðu Enter ef þú vilt hætta 'ENTER': "))
if choice in ("ENTER"):
    exit()


