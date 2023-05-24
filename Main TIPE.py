import numpy as np
import csv
import random as rd
import matplotlib.pyplot as plt

MOY={'poulet':63, 'boeuf':45, 'porc':83, 'veau':6, 'agneau':11, 'lapin':8, 'saumon':30,'thon':20,'moule':8,'crevette':6,'truite':15,'lait':69,'yaourt':35,'creme_fraiche':11,'beurre':10,'emmental':49,'pomme':16,'banane':28,'orange':24,'clementine':19,'peche':16,'poire':21,'raisin':10,'pamplemousse':11,'tomate':26,'pomme_de_terre':28,'carotte':17,'endive':9,'salade':12,'courgette':21,'oignon':11,'concombre':6,'poireau':10,'choux_fleur':10}

##Inialisation :
#Création des différents types de produit par catégorie :
viande=['poulet','boeuf','porc','veau','agneau','lapin']
poisson=['saumon','thon','moule','crevette','truite']
laitier=['lait','yaourt','creme_fraiche','beurre','emmental']
fruit=['pomme','banane','orange','clementine','peche','poire','raisin','pamplemousse']
legume=['tomate','pomme_de_terre','carotte','endive','salade','courgette','oignon','concombre','poireau','choux_fleur']
categorie=[viande,poisson,laitier,fruit,legume]
capacite_max=4000*4
capacite_jour=capacite_max
capacite=0
jour=0
perte_gachis=[0]
nombre_aliment_manquant_liste=[0]
stock_liste=[]
promo_liste=[]
profit=[]
temps=[]
nombre_aliment_perime_liste=[0]
perte_viande=[0]
perte_poisson=[0]
perte_laitier=[0]
perte_fruit=[0]
perte_legume=[0]
#Création du dictionnaire avec tous les aliments, leur valeur est leurs index dans la liste categorie

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

prix,validite,taille=init_list() #la liste prix, validite est dans l'ordre des indices des clefs dans le dictionnaire aliment ainsi prix[aliment_dict['poulet']] renvoie bien le prix au kg du poulet.

class Viande:

    def __init__(self,produit):
        self.type = produit
        self.age = validite[aliment_dict[self.type]]
        self.prix_achat = prix[aliment_dict[self.type]]
        self.prix_vente = prix[aliment_dict[self.type]] + prix[aliment_dict[self.type]]*(30/100)
        self.taille = taille[aliment_dict[self.type]]
        self.existence=True
        self.promo=0
        stock_dict[self.type]+=1

        if jour==0:
            self.age =rd.randint(1,validite[aliment_dict[self.type]])
        if jour>0:
            self.age =validite[aliment_dict[self.type]]

    def vendu(self):
        if self.existence :
            stock_dict[self.type]-=1
            self.existence=False

    def avance_jour(self):
        self.age-=1
        if self.age<0 and self.existence :
            perte_viande[0]+=1
            perte_gachis[0]+=self.prix_achat
            stock_dict[self.type]-=1
            self.existence=False

class Poisson:

    def __init__(self,produit):
        self.type = produit
        self.prix_achat = prix[aliment_dict[self.type]]
        self.prix_vente = prix[aliment_dict[self.type]] + prix[aliment_dict[self.type]]*(30/100)
        self.taille = taille[aliment_dict[self.type]]
        self.existence=True
        self.promo=0
        stock_dict[self.type]+=1
        if jour==0:
            self.age =rd.randint(1,validite[aliment_dict[self.type]])
        if jour>0:
            self.age =validite[aliment_dict[self.type]]

    def vendu(self):
        if self.existence :
            stock_dict[self.type]-=1
            self.existence=False

    def avance_jour(self):
        self.age-=1
        if self.age<0 and self.existence :
            perte_poisson[0]+=1
            perte_gachis[0]+=self.prix_achat
            stock_dict[self.type]-=1
            self.existence=False

class Laitier:

    def __init__(self,produit):
        self.type = produit
        self.prix_achat = prix[aliment_dict[self.type]]
        self.prix_vente = prix[aliment_dict[self.type]] + prix[aliment_dict[self.type]]*(30/100)
        self.taille = taille[aliment_dict[self.type]]
        self.existence=True
        self.promo=0
        stock_dict[self.type]+=1
        if jour==0:
            self.age =rd.randint(1,validite[aliment_dict[self.type]])
        if jour>0:
            self.age =validite[aliment_dict[self.type]]

    def vendu(self):
        if self.existence:
            stock_dict[self.type]-=1
            self.existence=False

    def avance_jour(self):
        self.age-=1
        if self.age<0 and self.existence:
            perte_laitier[0]+=1
            perte_gachis[0]+=self.prix_achat
            stock_dict[self.type]-=1
            self.existence=False

class Fruit:

    def __init__(self,produit):
        self.type = produit
        self.prix_achat = prix[aliment_dict[self.type]]
        self.prix_vente = prix[aliment_dict[self.type]] + prix[aliment_dict[self.type]]*(30/100)
        self.taille = taille[aliment_dict[self.type]]
        self.existence=True
        self.promo=0
        stock_dict[self.type]+=1
        if jour==0:
            self.age =rd.randint(1,validite[aliment_dict[self.type]])
        if jour>0:
            self.age =validite[aliment_dict[self.type]]

    def vendu(self):
        if self.existence:
            stock_dict[self.type]-=1
            self.existence=False

    def avance_jour(self):
        self.age-=1
        if self.age<0 and self.existence :
            perte_fruit[0]+=1
            perte_gachis[0]+=self.prix_achat
            stock_dict[self.type]-=1
            self.existence=False


class Legume:

    def __init__(self,produit):
        self.type = produit
        self.prix_achat = prix[aliment_dict[self.type]]
        self.prix_vente = prix[aliment_dict[self.type]] + prix[aliment_dict[self.type]]*(30/100)
        self.taille = taille[aliment_dict[self.type]]
        self.existence=True
        self.promo=0
        stock_dict[self.type]+=1
        if jour==0:
            self.age =rd.randint(1,validite[aliment_dict[self.type]])
        if jour>0:
            self.age =validite[aliment_dict[self.type]]

    def vendu(self):
        if self.existence :
            stock_dict[self.type]-=1
            self.existence=False

    def avance_jour(self):
        self.age-=1
        if self.age<0 and self.existence :
            perte_legume[0]+=1
            perte_gachis[0]+=self.prix_achat
            stock_dict[self.type]-=1
            self.existence=False

##Probabilité
def tirage_aliment(type_produit=str)-> str:
    """
    Tire un aliment d'une catégorie (viande,poisson...) donnée par l'utilisateur, selon la probabilité définie par la consommation moyenne des Français.

    On tire un nombre aléatoirement entre 0 et 1, et on découpe l'intervalle [0,1] en fonction des pourcentages de consommation/vente d'un produit
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
        if n<=0.41:
            return 'saumon'
        if 0.41<n<=0.71:
            return 'thon'
        if 0.71<n<= 0.77:
            return 'moule'
        if 0.77<n<=0.8 :
            return 'crevette'
        if 0.8<n<= 1:
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

def demande_client(nbr_client=int,demande_client_jour=dict)-> dict:
    """
    Pour un nombre de clients donné, renvoie la demande en produit
    """
    for aliment in demande_client_jour:
        demande_client_jour[aliment]=0              #Remise à zéro du dictionnaire
    for client in range(nbr_client):
        nombre_produit_panier=rd.randint(1,20)      #Le client prendra entre 1 et 20 produits
        for k in range(nombre_produit_panier):
            n=rd.random()
            if n<=0.30:
                type_produit='viande'
            if 0.30<n<=0.39:
                type_produit='poisson'
            if 0.39<n<=0.61:
                type_produit='laitier'
            if 0.61<n<=0.80:
                type_produit='fruit'
            if 0.80<n<=1:
                type_produit='legume'
            aliment=tirage_aliment(type_produit)    #On détermine le produit avec la fonction tirage_aliement
            demande_client_jour[aliment]+=1

    return demande_client_jour

def choix(aliment=str,stock_liste=list,stock_dict=dict):
    """
    Détermine l'aliment qui a la date de péremption la plus courte dans le stock
    """
    if stock_dict[aliment]<=0 :                 #S'il n'y a pas de produit disponible en stock
        return 'Rupture'

    if stock_dict[aliment]>0 :
        index_solution=0
        for i in range(len(stock_liste)):
            if stock_liste[i].type==aliment and stock_liste[i].existence :
                index_solution=i
                break

        for i in range(len(stock_liste)):
            if stock_liste[i].type==aliment and stock_liste[i].age < stock_liste[index_solution].age and stock_liste[i].existence :
                index_solution=i

    return stock_liste[index_solution]

def choix_promo(stock_liste=list,stock_dict=dict):

    promo_liste=[]
    for aliment in stock_liste:
        if aliment.promo!=0 :
            promo_liste.append(aliment)

    return rd.choice(promo_liste)


##Stock jour 0
jour=0
for aliment in reapprovisionnement_dict:
    reapprovisionnement_dict[aliment]=5*MOY[aliment]
perte=0
exec(open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\Réapprovisionnement.py").read())
profit_jour = - perte
profit.append(profit_jour)
temps.append(jour)

##Simulation
for k in range(30):

    jour+=1
    capacite=0
    nombre_aliment_vendu=0
    profit_jour=0
    profit_vente=0
    perte=0
    perte_gachis=[0]   #Aliments périmés qui sont jetés : Variable mise à jour avec la méthode avance_jour
    perte_viande=[0]
    perte_poisson=[0]
    perte_laitier=[0]
    perte_fruit=[0]
    perte_legume=[0]
    nombre_aliment_vendu_promo=0
    nombre_aliment_manquant=0

    print("")
    print("------Jour {}------" .format(jour))
    print("")

    if jour%5==0:  #Approvisionnement tout les 4 jours
        exec(open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\SOLVEUR.py").read())
        exec(open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\Réapprovisionnement.py").read())
        capacite_jour=capacite_max
        print("Réapprovisionnement effectué")


    #On effectue la vente du jour
    nbr_client=rd.randint(50,100)
    demande_client_jour=demande_client(nbr_client,demande_client_jour)
    for aliment in demande_client_jour:
        for k in range(demande_client_jour[aliment]):
            aliment_choisi=choix(aliment,stock_liste,stock_dict)   #On prend l'aliment avec la date la plus courte dans le stock (pas en promo)
            if aliment_choisi!=None and aliment_choisi!='Rupture' and aliment_choisi.existence==True and aliment_choisi.promo==0 :
                aliment_choisi.vendu()
                stock_liste.remove(aliment_choisi)
                nombre_aliment_vendu+=1
                profit_vente+=aliment_choisi.prix_vente
                capacite+= aliment_choisi.taille

            if aliment_choisi=='Rupture':
                nombre_aliment_manquant+= abs(stock_dict[aliment] - demande_client_jour[aliment])
                print('Rupture de stock pour {}'.format(aliment))
                break


    exec(open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\Suppression.py").read())  #Mets à jour les stocks après vente

    capacite_jour-= capacite

    print("Nombre de produit vendu : {}" .format(nombre_aliment_vendu))

    #On met à jour l'âge des aliments
    for aliment in stock_liste:
        aliment.avance_jour()

    exec(open(r"C:\Users\julie\Documents\GitHub\TIPE-2022-2023\Suppression.py").read())
    #Mise en place de promotion pour les produits avec une date de péremption arrivante a échéance dans 2 jour

    nombre_aliment_perime=perte_viande[0]+perte_poisson[0]+perte_laitier[0]+perte_fruit[0]+perte_legume[0]
    perte+= perte_gachis[0]

    print("{} viandes ont dépassé la date de consommation" .format(perte_viande[0]))
    print("{} poissons ont dépassé la date de consommation" .format(perte_poisson[0]))
    print("{} produits laitiers ont dépassé la date de consommation" .format(perte_laitier[0]))
    print("{} fruits ont dépassé la date de consommation" .format(perte_fruit[0]))
    print("{} legumes ont dépassé la date de consommation" .format(perte_legume[0]))
    print("Perte total : {} aliments" .format(nombre_aliment_perime))
    print("")
    print("-------------------")

    profit_jour = profit_vente - perte
    nombre_aliment_perime_liste.append(nombre_aliment_perime)
    nombre_aliment_manquant_liste.append(nombre_aliment_manquant)
    profit.append(profit_jour)
    temps.append(jour)

##Affichage Profit
plt.close()
plt.subplot(221)
plt.plot(temps[1:],profit[1:], "x-", color='red')
plt.xticks(temps[1:])
plt.ylabel('Profit (en euro)',size = 16,)
plt.xlabel('Jour',size = 16,)
plt.title("Profit effectué",fontdict={'family': 'serif','color' : 'darkblue','weight': 'bold','size': 18})
plt.grid(True)

profit_tt=0
for k in range(len(profit)):
    profit_tt=profit[k]

print("Le profit depuis l'ouverture est de : {}" .format(profit_tt))

plt.subplot(222)
plt.plot(temps[1:],nombre_aliment_perime_liste[1:], "x-", color='green')
plt.xticks(temps[1:])
plt.ylabel('Perte (par aliment)',size = 16,)
plt.xlabel('Jour',size = 16,)
plt.title("Perte d'aliment",fontdict={'family': 'serif','color' : 'darkblue','weight': 'bold','size': 18})
plt.grid(True)

plt.subplot(223)
plt.plot(temps[1:],nombre_aliment_manquant_liste[1:], "x-", color='orange')
plt.xticks(temps[1:])
plt.ylabel('Aliment manquant',size = 16,)
plt.xlabel('Jour',size = 16,)
plt.title("Nombre d'aliment manquant par jour",fontdict={'family': 'serif','color' : 'darkblue','weight': 'bold','size': 18})
plt.grid(True)

plt.subplots_adjust(hspace=0.3)
plt.show()