# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

battery_level  = float (input("Pourcentage de batterie?"))
Distance= float (battery_level)
#round (float, Distance, 0.1)
#Distance ;05= float(battery_level *6)
#5:10= float(battery_level*2.5)
#10:25= float(battery_level)
#25:50= float(battery_level*0.5)   
#50:100= float(battery_level*2)


if int (0 < battery_level<= 5):
    Distance *=6 
    round (Distance, 1)
    print ("Distance remaining is ", Distance,"km")
   

if int  (5 <battery_level <=10):
    Distance*=2.5
    round (Distance, 1)
    print ("Distance remaining is ", Distance ,"km")

if int (10 <battery_level <=25):
    Distance *=1
    round (Distance, 2)
    print ("Distance remaining is ", Distance,"km")

if int  (25 <battery_level <=50):
    Distance *=0.5
    round (Distance, 1)
    print ("Distance remaining is ", Distance *0.5,"km")

if int  (50 <battery_level <=100):
    Distance *=2
    round (Distance, 1)
    print ("Distance remaining is ", Distance *2 ,"km")