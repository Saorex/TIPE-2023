import numpy as np
import csv
import random as rd

##Inialisation :
#Création des différents types de produit par catégorie :
viande=['poulet','boeuf','porc','veau','agneau','lapin']
poisson=['saumon','thon','moule','crevette','truite']
laitier=['lait','yaourt','creme_fraiche','beurre','emmental']
fruit=['pomme','banane','orange','clementine','peche','poire','raisin','pamplemousse']
legume=['tomate','pomme_de_terre','carotte','endive','salade','courgette','oignon','concombre','poireau','choux_fleur']
categorie=[viande,poisson,laitier,fruit,legume]
capacite=3400
jour = 0
stock_liste=[]
#Création du dictionnaire avec tout les aliments, leurs valeur est leurs index dans la liste categorie

def init_dict()-> (dict,dict,dict):
    '''
    Initialise les dictionnaires de base du programme
    Renvoie les dictionnaires: aliment_dict, stock_dict,reapprovisionnement_dict
    '''
    a=0
    reapprovisionnement_dict={}
    aliment_dict={}
    stock_dict={}
    demande_client_jour={}
    for i in range(0,len(categorie)):
        for k in categorie[i]:
            if k not in aliment_dict:
                aliment_dict[k]=a
                a+=1
                reapprovisionnement_dict[k]=0
                stock_dict[k]=0
                demande_client_jour[k]=0

    return aliment_dict,stock_dict,reapprovisionnement_dict,demande_client_jour

aliment_dict,stock_dict,reapprovisionnement_dict,demande_client_jour=init_dict()

def init_list()-> (list,list,list):
    '''
    Initialise les listes de base du programme à partir d'un ficher en .csv
    Renvoie les listes : prix, validite
    '''
    prix=[]
    validite=[]
    taille=[]
    f=open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\aliment_caracteristique.csv")
    reader = csv.reader(f)
    for i in categorie:
        for j in i:
            for row in reader:
                f=open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\aliment_caracteristique.csv")
                reader = csv.reader(f)
                if row[0]==j:
                    prix.append(float(row[1]))
                    validite.append(float(row[2]))
                    taille.append(int(row[3]))
    return prix,validite,taille

prix,validite,taille=init_list() #la liste prix, validite est dans l'ordre des indices des clefs dans la dictionnaire aliment ainsi prix[aliment_dict['poulet']] renvoie bien le prix au kg du poulet.

class Viande:

    def __init__(self,produit):
        self.type = produit
        self.age = validite[aliment_dict[self.type]]
        self.prix = prix[aliment_dict[self.type]]
        self.taille = taille[aliment_dict[self.type]]
        self.existance=True
        stock_dict[self.type]+=1

    def vendu(self):
        stock_dict[self.type]-=1
        self.existance=False

    def avance_jour(self):
        self.age-=1
        if self.age<0:
            print("{} a dépasser la date de consomation" .format(self))

class Poisson:

    def __init__(self,produit):
        self.type = produit
        self.age = validite[aliment_dict[self.type]]
        self.prix = prix[aliment_dict[self.type]]
        self.taille = taille[aliment_dict[self.type]]
        self.existance=True
        stock_dict[self.type]+=1

    def vendu(self):
        stock_dict[self.type]-=1
        self.existance=False

    def avance_jour(self):
        self.age-=1
        if self.age<0:
            print("{} a dépasser la date de consomation" .format(self))

class Laitier:

    def __init__(self,produit):
        self.type = produit
        self.age = validite[aliment_dict[self.type]]
        self.prix = prix[aliment_dict[self.type]]
        self.taille = taille[aliment_dict[self.type]]
        self.existance=True
        stock_dict[self.type]+=1

    def vendu(self):
        stock_dict[self.type]-=1
        self.existance=False

    def avance_jour(self):
        self.age-=1
        if self.age<0:
            print("{} a dépasser la date de consomation" .format(self))

class Fruit:

    def __init__(self,produit):
        self.type = produit
        self.age = validite[aliment_dict[self.type]]
        self.prix = prix[aliment_dict[self.type]]
        self.taille = taille[aliment_dict[self.type]]
        self.existance=True
        stock_dict[self.type]+=1

    def vendu(self):
        stock_dict[self.type]-=1
        self.existance=False

    def avance_jour(self):
        self.age-=1
        if self.age<0:
            print("{} a dépasser la date de consomation" .format(self))

class Legume:

    def __init__(self,produit):
        self.type = produit
        self.age = validite[aliment_dict[self.type]]
        self.prix = prix[aliment_dict[self.type]]
        self.taille = taille[aliment_dict[self.type]]
        self.existance=True
        stock_dict[self.type]+=1

    def vendu(self):
        stock_dict[self.type]-=1
        self.existance=False

    def avance_jour(self):
        self.age-=1
        if self.age<0:
            print("{} a dépasser la date de consomation" .format(self))

##Probabilité
def tirage_aliment(type_produit)-> str:
    """
    Tire un aliment d'une catégorie (viande,poisson...) donnée par l'utilisateur, selon la probabilité définie par la consommation moyenne des français.

    On tire un nombre aléatoirement entre 0 et 1, et on découpe l'interval [0,1] en fonction des pourcentages de consommation/vente d'un produit
    """

    n=rd.random()
    if type_produit == 'viande':
        if n<=0.3:
            return 'poulet'
        if 0.3<n<=0.5:
            return 'boeuf'
        if 0.5<n<=0.91:
            return 'porc'
        if 0.91<n<=0.94:
            return 'veau'
        if 0.94<n<=0.97 :
            return 'agneau'
        if 0.97<n<=1 :
            return 'lapin'

    if type_produit == 'poisson':
        if n<=0.39:
            return 'saumon'
        if 0.39<n<=0.42:
            return 'thon'
        if 0.42<n<= 0.88:
            return 'moule'
        if 0.88<n<=0.92 :
            return 'crevette'
        if 0.92<n<= 1:
            return 'truite'

    if type_produit == 'laitier':
        if n<=0.43:
            return 'lait'
        if 0.43<n<=0.62 :
            return 'yaourt'
        if 0.62 <n<=0.67:
            return 'creme_fraiche'
        if 0.67<n<=0.72:
            return 'beurre'
        if 0.72 < n<=1:
            return 'emmental'

    if type_produit == 'fruit' :
        if n<=0.13 :
            return 'pomme'
        if 0.13<n<=0.35 :
            return 'banane'
        if 0.35<n<=0.49 :
            return 'orange'
        if 0.49<n<=0.62 :
            return 'clementine'
        if 0.62<n<=0.75 :
            return 'peche'
        if 0.75<n<=0.90 :
            return 'poire'
        if 0.90<n<=0.95 :
            return 'raisin'
        if 0.95<n<=1 :
            return 'pamplemousse'

    if type_produit == 'legume' :
        if n<=0.18 :
            return 'tomate'
        if 0.18<n<=0.39 :
            return 'pomme_de_terre'
        if 0.39<n<=0.51 :
            return 'carotte'
        if 0.51<n<=0.58 :
            return 'endive'
        if 0.58<n<=0.65 :
            return 'salade'
        if 0.65<n<=0.79 :
            return 'courgette'
        if 0.79<n<=0.86 :
            return 'oignon'
        if 0.86<n<=0.9 :
            return 'concombre'
        if 0.9<n<=0.95 :
            return 'poireau'
        if 0.95<n<=1 :
            return 'choux_fleur'

def demande_client(nbr_client,demande_client_jour)-> dict:
    """
    Pour un nombre de client demandé, renvoie la demande en produit
    """
    for aliment in demande_client_jour:
        demande_client_jour[aliment]=0              #Remise à zéro du dictionnaire
    for client in range(nbr_client):
        nombre_produit_panier=rd.randint(1,20)      #Le client prendra entre 1 et 20 produits
        for k in range(nombre_produit_panier):
            type_produit=rd.choice(['viande','poisson','laitier','fruit','legume'])   #Chaque type de produit est pris de manière aléatoire pour le moment
            aliment=tirage_aliment(type_produit)    #On détermone le produit avec la fonction précédente
            demande_client_jour[aliment]+=1

    return demande_client_jour

def choix(aliment,stock_liste):
    """
    Détermine l'aliment qui à la date de péremption la plus courte dans le stock
    """
    if stock_dict[aliment]==0:                 #Si il n'y a pas de produit disponible en stock
        return None
    else :
        index=-1
        index_solution=0
        date_peremption_liste=[]
        for k in stock_liste:                           #On regarde pour tout les produits dans le stock
            index+=1
            if k.type==aliment:                         #Pour le type d'aliment qu'on cherche
                if date_peremption_liste==[]:           #Recherche du minimum
                    index_solution=index
                    date_peremption_liste.append(k.age)
                else:
                    if date_peremption_liste[-1]>k.age: #si la date de péremption de l'élement k est plus petit que celui du dernière élement solution temporaire alors la nouvelle solution est k si égalité on garde la première solution
                            index_solution=index
                            date_peremption_liste.append(k.age)

                return stock_liste[index_solution]

##Stock jour 1 simulation test
for aliment in reapprovisionnement_dict:
    reapprovisionnement_dict[aliment]=100

exec(open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\Réapprovisionnement.py").read())

##Simulation
jour+=1
nombre_aliment_vendu=0
nbr_client=rd.randint(10,500)
demande_client_jour=demande_client(nbr_client,demande_client_jour)
for aliment in demande_client_jour:
    for k in range(0,demande_client_jour[aliment]):
        if stock_dict[aliment]!=0:
            aliment_choisi=choix(aliment,stock_liste)  #On prend l'aliment avec la date la plus courte
            aliment_choisi.vendu()
            nombre_aliment_vendu+=1
        else:
            print('Rupture de stock pour {}'.format(aliment))
exec(open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\Suppression.py").read())  #Met à jour les stocks après vente
#reapprovisionnement_dict=... acheter les aliments pour remplir stock
#exec(open(r"D:\Julien\TIPE 2022-2023\Réapprovisionnement.py").read())