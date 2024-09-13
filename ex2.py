# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.

water_quantity = float(input("Quelle est la quantité d'eau à assainir :"))
nombre_de_filtres = ((water_quantity)/5)
nombre_lampesUV= (water_quantity/5 *3)
nombre_kgChlore= water_quantity/10
print("Voici les éléments requis pour assainir ", water_quantity, "L d'eau")
print("")
print (" - Lampes UV:" , nombre_lampesUV, )
print (" - Chlore:",nombre_kgChlore, "Kg" )
print (" - Filtres : ",nombre_de_filtres)