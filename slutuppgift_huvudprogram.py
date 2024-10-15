def meny():

   menyval = ["1. Starta övervakning", "2. Lista aktiv övervakning", "3. Skapa larm", "4. Visa larm", "5. Starta övervakningsläge"]
   for x in menyval:
        print(x)
        
        
def huvudprogram():
    val = input("Välj ett alternativ:")
    if val == "1":
            print("Startar övervakning")
            print()
            
    elif val == "2":
            print("Listar övervakning")
            print()
            import overvakning   #Importerar kod för procentuell användning för CPU, minne och diskanvändning.
            overvakning.usage()
            print()
            
    elif val == "3":
            print("Skapar larm")
            print()
            
    elif val == "4":
            print("Visar larm")
            print()
            
            
    elif val == "5":
            print("Startar övervakningsläge")
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
