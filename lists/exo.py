#Vous devez réaliser les tables de multiplications de “1, 2, 3, 5” et “8”.
#Création d’une liste par table avec l’ensemble des résultats des multiplications
numbers = [1, 2, 3, 5, 8]
multiplication_tables = []

for number in numbers:
    table = []
    for i in range(1, 11):
        table.append(number * i)
    multiplication_tables.append(table)

print(multiplication_tables)

#Vous devez créer une liste de 1 à 10 et multiplier les résultats de la table de “5” (vous n'avez le droit d’utiliser que les String). Utilisez une boucle For.
table_5_strings = []
for i in range(1, 11):
    table_5_strings.append(f"5 x {i} = {5 * i}")
print('\n'.join(table_5_strings))

#Même exercice que le 2 avec une boucle “while” avec “true” comme valeur de condition. Faites une incrémentation dans un print() avec la table de multiplication par “5”.
i = 1
table_5_strings = []
while True:
    table_5_strings.append(f"5 x {i} = {5 * i}")
    i += 1
    if i > 10:
        break
print('\n'.join(table_5_strings))

#Vous devez créer une variable avec l’objet suivant {“a”: 42, “b”: 42, “c”: 42, “d”: 42}. Vous devrez parcourir chaque key et faire la multiplication de la valeur précédente par la nouvelle (accumulateur) sauf pour la lettre ‘d’ ou vous devrez faire une soustraction de 42. Le calcul retournera “74046”
dict1 = {"a": 42, "b": 42, "c": 42, "d": 42}
accumulation = 1
for key, value in dict1.items():
    if key == "d":
        accumulation  -= value
    else:
        accumulation  *= value
print(accumulation)

#Écrivez un programme qui génère et affiche le motif suivant en utilisant des boucles imbriquées : * **  *** **** *****
for i in range(1, 6):
    print("*" * i)

#Faire une liste partant de 1980 à nos jours en prenant en compte l’année actuelle actualisé.
import datetime

current_year = datetime.datetime.now().year
years = list(range(1980, current_year + 1))
print(years) 

#Faite en sorte d’afficher la structure visuelle suivante (cf ex5) en un script avec une boucle for :
for i in range(1, 11):
    print("1" * i)

#Si vous avez réussi le précédent exercice, vous devez essayer d’afficher cette structure :
for i in range(1, 11):
    spaces = " " * (10 - i)
    ones = "1" * (2 * i - 1)
    print(spaces + ones)  





