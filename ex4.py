# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level  = float (input("Pourcentage de batterie ? "))
Distance = float (0)

if int  (50 <battery_level <=100):
    Distance += 2 * (battery_level - 50)
    battery_level = 50
   
    
if int  (25 <battery_level <=50):
    Distance += 0.5* (battery_level-25) 
    battery_level = 25
    
if int (10 <battery_level <=25):
    Distance += 1*(battery_level - 10)
    battery_level = 10
    

if int  (5 <battery_level <=10):
    Distance += 2.5* (battery_level - 5)
    battery_level = 5
   

if int (0 < battery_level<= 5):
    Distance +=6*(battery_level) 
    print (round (Distance, 1),"km")

if int (0 == battery_level):
    print ("La batterie est vide")




   






