age = int(input("quel est votre age ?"))
if age < 18 :
    print(f"Vous ne pouvez pas entrer vous n’êtes pas majeur vous avez {age}")
elif 18 <= age < 42 :
    print(f"Vous pouvez entrer vous êtes majeur vous avez {age}")
elif age >= 42 :
    print(f"vous etes patron de la boite")

#Créer un algorithme qui retourne : “Cool” quand la valeur est comprise entre 0 et 10. “Tepid” quand la valeur est comprise entre 11 et 20. “Warm” quand la valeur est comprise entre 21 et 30. Cette condition devra utiliser une variable “rand” avec un nombre aléatoire compris entre 0 et 30.
import random
rand = random.randint(0,30)
if rand <= 10:
    print("Cool")
elif rand >= 11 and rand <= 20 :
    print("Tepid")
else :
    print("Warm")

#Utilisez le “match” pour déterminer le jour de la semaine avec “datetime”. Si nous sommes lundi vous devrez reconnaître que nous sommes lundi et afficher “nous sommes {jour}”. Faites cela pour tous les autres jours de la semaine.
from datetime import datetime
today = datetime.now()
jour = today.strftime('%A')

match jour:
    case 'Monday':
        print(f"Nous sommes {jour}")
    case 'Tuesday':
        print(f"Nous sommes {jour}")
    case 'Wednesday':
        print(f"Nous sommes {jour}")
    case 'Thursday':
        print(f"Nous sommes {jour}")
    case 'Friday':
        print(f"Nous sommes {jour}")
    case 'Saturday':
        print(f"Nous sommes {jour}")
    case 'Sunday':
        print(f"Nous sommes {jour}")



#Afin d’utiliser les conditions imbriquées, créer une histoire avec 3 niveaux minimum avec au minimum 3 fins différentes vous devez faire des “if” imbriqués. Vous devez utiliser la fonction “input()”. Aucune autre fonction n’est autorisée. Bien entendu une des fins doit obligatoirement finir par “La grande réponse sur la vie, l’univers et le reste !”.  Utilisez “print()”. 


#Faites une condition ternaire qui teste si une variable existe ou non. Si elle n’existe pas écrivez “cette variable n’existe pas” autrement écrivez “42”.
a = 12
match a :
    case True :
        print("42")
    case False :
        print("cette variable n’existe pas")


#Calculer le prix d'un article après l'application d'une remise. L'utilisateur est invité à entrer le prix initial de l'article et le pourcentage de remise. Ensuite, le programme calcule le montant de la remise et le prix final après remise. Si le prix final est supérieur à la moitié du prix initial, les résultats sont affichés. Sinon, un message d'erreur est affiché indiquant que la remise est trop élevée.
prix_initial = float(input("Entrez le prix initial de l'article : "))
pourcentage_remise = float(input("Entrez le pourcentage de remise (par exemple, pour 20%, entrez 20) : "))
montant_remise = (pourcentage_remise / 100) * prix_initial
prix_final = prix_initial - montant_remise

if prix_final > prix_initial / 2:
    print(f"Le montant de la remise est de {montant_remise} euros.")
    print(f"Le prix final après remise est de {prix_final} euros.")
else:
    print("Erreur : la remise est trop élevée.")

#Vérifier si un nombre saisi par l'utilisateur est pair ou non. Le programme demande à l'utilisateur d'entrer un nombre, puis il vérifie si le nombre est pair ou impair. Si c'est le cas, le programme affiche que le nombre est pair. Sinon, il affiche que le nombre n'est pas pair.
nombre = int(input("Veuillez entrer un nombre : "))
if nombre%2 == 0 :
    print("le nombre est pair")
else :
    print("le nombre n'est pas pair")



