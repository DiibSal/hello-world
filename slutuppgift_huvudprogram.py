def meny():
#Q: Önödigt att göra for loop? Går att bara göra val2 till array och printa.
   val2 = ["1. Starta övervakning", "2. Lista aktiv övervakning", "3. Skapa larm", "4. Visa larm", "5. Starta övervakningsläge"]
   for x in val2:
        print(x)


def back():
#Q: Hur tillåter man flera inputs i en rad?
    YN = input("Vill du återgå till startmenyn? (Y/N)")
    if YN == "y":
        meny()
        huvudprogram()
        back()
    elif YN == "n":
        print()
    else:
        print("Inget giltigt svar")
        back()
        
        
def huvudprogram():
    val = input("Välj ett alternativ:")
    if val == "1":
            print("Startar övervakning")
            print()
            
    elif val == "2":
            print("Listar övervakning")
            print()
#Q: Repeterar första gången man kör koden
#Importerar kod från overvakning.py för procentuell användning för CPU, minne och diskanvändning.
            import overvakning    
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
    back()
    break