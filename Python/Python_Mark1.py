#Liður 1. nafnið þitt og uppáhaldsfagið þitt.
name= input ("Hvað er nafnið þitt? ")
print ("halló " + name +"!")
subject= str(input("Hvað er uppáldsfagið þitt í skólanum " + name + "?"))
print ("Velkominn í áfangann" , uppáldsfagið , " Þetta verður skemmtileg önn hjá okkur " + name + ".")

#Liður 2. Deilun
print ("Gefðu mig tvær tölur og ég skal deila þá með 5.5")
tala = int(input("sláðu in tölu hærra en 100:"))
tala = tala/5.5
print (round(tala,2))



#Liður 3. Margföldun, tvær heiltölur.
print ("Gefðu mig tvær Heiltölur og ég skal margfalda þá ")
heiltala1 = int(input("sláðu inn Heiltölu: "))
heiltala2 = int(input("sláðu inn aðra Heiltölu: "))
mul = heiltala1 * heiltala2
print ("svarið er: ", mul)

#Liður 4. Reikna út rúmmál.
def cube(length,width,heigth):
  volume = length * width * heigth
  return volume
  

  
print("Gefðu mig þrjár hliðarlengdir og ég skal reikna út rúmmálið")
length = int(input("Sláðu inn lengd > "))
width = int(input("sláðu inn breidd > "))
heigth = int(input("sláðu inn hæð > "))
volume = cube(length,width,heigth)
print("Rúmmálið er:", volume)

#Liður 5. Reikna út aldur.
print ("sláðu inn aldur þinn og aldur pabba þíns og ég mun reikna hvað pabbi þinn var gamall þegur þú fæddist")
aldur1 = int(input("sláðu inn aldur pabba þíns: "))
aldur2 = int(input("sláðu inn aldur þinn: "))
mul = aldur1-aldur2
print ("Pabbi þinn var:", mul)

#Liður 6. Reikna út meðalaldur
print ("Gefið mig aldur af þremur einstaklingum og ég skal reikna meðalaldur.")
einstaklingur1 = int(input("sláðu inn aldur þinn > "))
einstaklingur2 = int(input("Sláðu inn aldur þinn > "))
einstaklingur3 = int(input("sláðu inn aldur þinn > "))

meðalaldur =(einstaklingur1+einstaklingur2+einstaklingur3)/3
print ("Meðalaldurinn er:", meðalaldur)

print ("Gaman að geta aðstoðað þig við þessa útreikninga " + name + ".")














