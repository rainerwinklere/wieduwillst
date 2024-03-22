# 0  = freier parkplatz 
# 1 = belegter parkplatz 

Parkplatz = [0,1,1,1,1,0,0,1,0,1,0,1]
schluss = 0

while schluss == 0: 
    eingabe = int(input("wählen sie einen parkplatz aus: "))
    eingabe = eingabe -1 

    if Parkplatz[eingabe] == 0:
        print("parkplatz gebucht")
        Parkplatz[eingabe] = 1        
        abfrage = input("wollen sie noch einen parkplatz buchen? [y/n]: ")
        if abfrage == "y":
            continue
        else:
            schluss = 1  

    else: 
        print("parkplatz ist besetzt bitte wähle einen anderen")



print(Parkplatz)
#belegt = True 


#while belegt == True:
 #   eingabe = input("Wählen sie den Parkplatz aus den sie nutzen wollen 1..." + str(len(Parkplatz)))

