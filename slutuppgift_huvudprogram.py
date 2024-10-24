import overvakning   #Importerar overvakning.py för procentuell användning för CPU, minne och diskanvändning.
import larmFil
import json

larmLista = [] #Tom lista för att lagra larm. Larm läggs till här.

def meny():
   menyval = ["1. Starta övervakning", "2. Lista aktiv övervakning", "3. Skapa larm", "4. Visa larm", "5. Starta övervakningsläge", "6. Ta bort larm"]
   for x in menyval:
        print(x)
        
        
def visaLarm():
   larmLista.sort(key=lambda larm: larm.typ)
   for index, larm in enumerate(larmLista, start=1):
        print(f"{index}. {larm}")  
        
        
def huvudprogram():
    val = input("Välj ett alternativ: ")
    if val == "1": #Startar övervakningen och tillåter att övervakningen kan listas med meny val 2.
            print("Startar övervakning")
            overvakning.usage()
            print("Övervakning slutförd")
            print()
            
    elif val == "2": #Listar övervakningen som startats med meny val 1. Om övervakningen inte startats fungerar ej meny valet.
            print("Listar övervakning")
            print()
            try:                                                                                      #Avrundar till 7 istället för 8
                print(f"RAM användning är: {overvakning.ramPer}% ({int(overvakning.ramUse)}GB av {int(overvakning.ramTot)}GB) \nCPU användning är {overvakning.cpu}% \nDisk användning är {overvakning.diskPer}% ({int(overvakning.diskUse)}GB av {int(overvakning.diskTot)}GB)")
            except:
                print("Övervakning har inte startats")
                
            
    elif val == "3":
            print()
            global skapaLarmTyp, skapaLarmGrad, addLarm
            skapaLarmTyp = input("Vad vill du skapa larm för? \n1. CPU användning \n2. RAM-minne användning \n3. Disk användning\nVälj ett alternativ: ")
            
            if skapaLarmTyp == "1":
                        skapaLarmGrad = int(input("Ange gränsvärde för larm (i procent): "))
                        addLarm = larmFil.Larm("CPU", skapaLarmGrad)
                        larmLista.append(addLarm)
                        with open("larmLager.json", "w") as openLager:
                           json.dump(addLarm.__dict__, openLager) #Kolla upp varför det inte fungerar.
                           
                        
            elif skapaLarmTyp == "2":
                        skapaLarmGrad = int(input("Ange gränsvärde för larm (i procent): "))
                        addLarm = larmFil.Larm("RAM", skapaLarmGrad)
                        larmLista.append(addLarm)
                        
            elif skapaLarmTyp == "3":
                        skapaLarmGrad = int(input("Ange gränsvärde för larm (i procent): "))
                        addLarm = larmFil.Larm("Disk", skapaLarmGrad)
                        larmLista.append(addLarm)
                
            else:
                        print("Du valde inte en av alternativen.")
            print()
            
            
            
    elif val == "4":
            print("Visar larm")
            if larmLista == []:
              print("Inga larm har skapats.")
            else: 
                visaLarm()
            print()
            
            
    elif val == "5":
            print("Startar övervakningsläge")
            while True:
                    try:
                        overvakning.usage()
                        print(f"\nRAM användning är: {overvakning.ramPer}%\nCPU användning är {overvakning.cpu}% \nDisk användning är {overvakning.diskPer}%\n(Avsluta övervakningläge med Ctrl+C)")
                        for larm in larmLista:
                          larm.alarm()
                          
                    except KeyboardInterrupt:
                        print("Övervakningsläge avslutad")
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
                else:
                    print("Inte giltigt val. Ange index för existerande larm.")
           except ValueError:
                   print("Inte giltigt val. Ange index för existerande larm.")
            
            
        
        
    else:
            print("Du valde inte en av alternativen. Programmet startas om.")
            print()
            meny()
            huvudprogram()
              

while True:
    meny()
    huvudprogram()
    input("Tryck på valfri tangent för att återgå till start meny.")
