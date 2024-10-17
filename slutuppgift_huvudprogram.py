import overvakning   #Importerar kod för procentuell användning för CPU, minne och diskanvändning.

larmLista = []

def meny():
   menyval = ["1. Starta övervakning", "2. Lista aktiv övervakning", "3. Skapa larm", "4. Visa larm", "5. Starta övervakningsläge"]
   for x in menyval:
        print(x)
        
        
        
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
            try:
                print(f"RAM användning är: {overvakning.ramPer}% ({overvakning.ramUse}GB av {overvakning.ramTot}GB) \nCPU användning är {overvakning.cpu}% \nDisk användning är {overvakning.diskPer}% ({overvakning.diskUse}GB av {overvakning.diskTot}GB)")
            except:
                print("Övervakning har inte startats")
            
    elif val == "3":
            print()
            global skapaLarmTyp
            skapaLarmTyp = input("Vad vill du skapa larm för? \n1. CPU användning \n2. RAM-minne användning \n3. Disk användning\nVälj ett alternativ: ")
            print()
            
    elif val == "4":
            print("Visar larm")
            print()
            
            
    elif val == "5":
            print("Startar övervakningsläge")
            while True:
                    try:
                        overvakning.usage()
                        print(f"\nRAM användning är: {overvakning.ramPer}%\nCPU användning är {overvakning.cpu}% \nDisk användning är {overvakning.diskPer}%\n(Avsluta övervakningläge med Ctrl+C)")
                    except KeyboardInterrupt:
                        print("Övervakningsläge avslutad")
                        break
            print()
            
    else:
            print("Du valde inte en av alternativen. Programmet startas om.")
            print()
            meny()
            huvudprogram()
              

while True:
    meny()
    huvudprogram()
    input("Tryck på valfri tangent för att återgå till start meny.")
