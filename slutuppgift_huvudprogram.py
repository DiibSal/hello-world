import overvakning
import larmFil
import json, datetime

try: #Try försöker läsa larm skapade från innan i en larmLager.json fil. Hittades den inte startas listan som tom.
    with open ("larmLager.json", "r") as f:
        file = json.load(f)
        larmLista = [larmFil.Larm(**larm) for larm in file] #Packar upp datan i larmLager.json som delar av dict och läggs in i listan.
except: #läs om list comprehension
    larmLista = []

def meny():
   menyval = ["1. Starta övervakning", "2. Lista aktiv övervakning", "3. Skapa larm", "4. Visa larm", "5. Starta övervakningsläge", "6. Ta bort larm", "7. Avsluta programmet"]
   for x in menyval:
        print(x)
        
        
def visaLarm(): #Funktion för att visa larmen (val 4 i huvudmeny). Sorterar larmLista på typ, sedan lägger värde (index) för larmen efter sorteringen. Funktionen och värdet används även för att ta bort larm (val 6 i huvdumeny)
   larmLista.sort(key=lambda larm: larm.typ)
   for index, larm in enumerate(larmLista, start=1):
        print(f"{index}. {larm}")  
        
        
def logFunc(logMed): #Funktion som tillkallas när man använder programmet. Använder datetime modulen för att skriva tid i en separat loggfil.
        dagochtid = datetime.datetime.now()
        with open("logs.txt", "a", encoding="utf-8") as logFil:
            logFil.write(f"{dagochtid},{logMed}" + "\n")
        
        
def huvudprogram():
    val = input("Välj ett alternativ: ")
    if val == "1": #Startar övervakningen och tillåter att övervakningen kan listas med meny val 2.
            print("Startar övervakning")
            overvakning.usage()
            print("Övervakning slutförd\n")
            logFunc("Övervakning startad")
            
    elif val == "2": #Listar övervakningen som startats med meny val 1. Om övervakningen inte startats fungerar ej meny valet.
            print("Listar övervakning \n")
            logFunc("Övervakning listad")
            try:
                print(f"RAM användning är: {overvakning.ramPer}% ({int(overvakning.ramUse)}GB av {int(overvakning.ramTot)}GB) \nCPU användning är {overvakning.cpu}% \nDisk användning är {overvakning.diskPer}% ({int(overvakning.diskUse)}GB av {int(overvakning.diskTot)}GB)")
            except:
                print("Övervakning har inte startats")
                
            
    elif val == "3":
            print()
            global skapaLarmTyp, skapaLarmGrad, addLarm
            skapaLarmTyp = input("Vad vill du skapa larm för? \n1. CPU användning \n2. RAM-minne användning \n3. Disk användning\nVälj ett alternativ: ")
            
            if skapaLarmTyp in ["1", "2", "3"]: 
                    while True: #Loop som endast bryts när man angett ett heltal mellan 0-100
                      try:
                        skapaLarmGrad = int(input("Ange gränsvärde för larm (i procent): "))
                        if 0 <= skapaLarmGrad <= 100:
                                break
                        else:
                                print("Gränsvärdet måste ligga mellan 0-100%. Försök igen")
                      except ValueError:
                              print("Ogiltigt värde. Ange heltal mellan 0-100%")
                        
                        
            if skapaLarmTyp == "1":
                addLarm = larmFil.Larm("CPU", skapaLarmGrad)
                larmLista.append(addLarm)
                logFunc(f"CPU Larm skapat med gränsvärd: {skapaLarmGrad}%")
            elif skapaLarmTyp == "2":
                addLarm = larmFil.Larm("RAM", skapaLarmGrad)
                larmLista.append(addLarm)
                logFunc(f"RAM Larm skapat med gränsvärd: {skapaLarmGrad}%")
            elif skapaLarmTyp == "3":
                addLarm = larmFil.Larm("Disk", skapaLarmGrad)
                larmLista.append(addLarm)
                logFunc(f"Disk Larm skapat med gränsvärd: {skapaLarmGrad}%")
            else:
                print("Ogiltigt alternativ.")   
        
            with open("larmLager.json", "w") as openLager: #Efter larm lagts till i listan, så skrivs listan över i json filen med den nya larmen.
                    json.dump([larm.__dict__ for larm in larmLista], openLager)
            
            
    elif val == "4":
            print("Visar larm")
            logFunc("Visar larm")
            if larmLista == []:
              print("Inga larm har skapats.")
            else: 
                visaLarm()
            print()
            
            
    elif val == "5":
            print("Startar övervakningsläge")
            logFunc("Startar övervakningsläge")
            while True:
                    try:
                        overvakning.usage()
                        print(f"\nRAM användning är: {overvakning.ramPer}%\nCPU användning är {overvakning.cpu}% \nDisk användning är {overvakning.diskPer}%\n(Avsluta övervakningläge med Ctrl+C)")
                        for larm in larmLista:
                          larm.alarm()
                          
                    except KeyboardInterrupt:
                        print("Övervakningsläge avslutad")
                        logFunc("Övervakningsläge avslutad")
                        break
            print()
            
            
    elif val == "6":
        if larmLista == []:
           print("Inga larm har skapats ännu")
        else:
           visaLarm()
           try:
                taBortLarm = int(input("Välj ett larm du vill ta bort: ")) - 1
                if 0 <= taBortLarm < len(larmLista):
                        borttagenLarm = larmLista.pop(taBortLarm)
                        print(f"Tagit bort: {borttagenLarm}")
                        
                        with open("larmLager.json", "w") as taBortLager: #Gör liknande som när man lägger till larm. Skriver över ny lista.
                            json.dump([larm.__dict__ for larm in larmLista], taBortLager)
                            
                        logFunc(f"Tagit bort larm: {borttagenLarm}")
                else:
                    print("Inte giltigt val. Ange index för existerande larm.")
           except ValueError:
                   print("Inte giltigt val. Ange index för existerande larm.")
        
    elif val == "7":
        print("Avslutar programmet.")
        logFunc("Avslutar programmet från huvudmeny")
        exit()
        
           
    else:
            print("Du valde inte en av alternativen. Programmet startas om.")
            print()
            meny()
            huvudprogram()
              
              
              

while True: #While loop för att köra hela programmet och gå tillbaka till huvudmenyn.
    meny()
    huvudprogram()
    input("Tryck på valfri tangent för att återgå till start meny.")
