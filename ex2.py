# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math
water_quantity = float (input("Quelle quantité d'eau faut-il assainir ? " ))
nombre_de_filtres =  math.ceil((water_quantity)/5)
nombre_lampesUV= math.ceil((water_quantity/5 *3))
nombre_kgChlore= round (water_quantity/10, 2)
if (water_quantity%1 ==0):
    water_quantity= round(water_quantity)
print(f"Voici les éléments requis pour assainir {water_quantity}L d'eau:\n")
print (f"        \t- Filtre(s) : {nombre_de_filtres}\n")
print (f"        \t- Lampe(s) UV : {nombre_lampesUV}\n")
print (f"        \t- Chlore : {nombre_kgChlore}kg")