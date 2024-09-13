#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input ("Pays concerné?")
code_medals = input ("Chaîne représentant les médailles?")
B= 0, "Médaille de Bronze"
G= 0, "Médaille d'Or"
S= 0, "Médaille d'Argent"

print ( country, ":")

if (B):
    B+=1 
print (B,  + "Médaille de Bronze")

if (G): G+=1
print (G,+ "Médaille d'Or")
    
if (S):S+=1
print ( S, + "Médaille d'Argent")

