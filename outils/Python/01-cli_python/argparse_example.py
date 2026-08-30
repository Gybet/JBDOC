import argparse

#initialisation du parser (obligatoire)
parser = argparse.ArgumentParser()


#definition d'un argument positionnel
parser.add_argument("argpos")

#definition d'un argument optionnel
parser.add_argument("--argopt")

#conversion et val par defaut 
parser.add_argument("--nbpote" , type = int , default = 0)

#definition d un flag
parser.add_argument("--surprise", action = "store_true", help="Flag surprise")


#lecture et affichage des arguments
args = parser.parse_args()
print(f"Bonjour, votre arg positionnel est  : {args.argpos}")
if args.argopt != None :
    print(f"Vous avez fourni l'argument optionnel : {args.argopt}")

print(f"Vous avez {args.nbpote} amis ... c est pas beaucoup")

if args.surprise == True :
    print("SURPRISE VOUS AVEZ DECLENCHE LA FONCTION SURPRISE")


