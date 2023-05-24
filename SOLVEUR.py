from pulp import *
import numpy as np
import random as rd

"""
Utilisation du solveur :

1) Définir un problème avec probleme = LpProblem(nom du probleme, LpMaximize pour maximiser une fonction (resp LpMinimize))

2) Définir les variables : x =LpVariable(nom de la variable, borne minimale,cat=LpInteger pour des résultats entiers (resp Continous))

3) Ajouter des contraintes avec probleme += ( x +2*y <= 3) (resp >=)

4) Ajouter la fonction objectif avec probleme += 5*x + y (ici maximiser 5x + y)

5) Résoudre le problème avec probleme.solve(solver = votre solveur (par défaut c'est PULP_CBC_CMD)

6) Récupérer les valeur avec x.value()
"""

objectif=np.eye(34)
contraintes = np.array([MOY[i]*5 for i in MOY])
fonction_benefices = np.array(prix)

# Problème
prob = LpProblem("chiffre_affaires_supermarché", LpMaximize)

# Paramètres
L=[]
for i in aliment_dict:
    L+=[LpVariable( i,lowBound=0, cat=LpInteger)] #création variables du problème qui doivent etre entiere

# Contraintes
for i in range(len(objectif)):
    e=[]

    for j in range(len(objectif[i])):
        e += [objectif[i][j]*L[j]]


    prob += (lpSum(e)>=int(contraintes[i]-(contraintes[i]*15)/100)) #contraintes de minimum pour chacune des variables a -10% de la moyenne sur 4 jours
    prob += (lpSum(e)<=int(contraintes[i]+(contraintes[i]*15)/100)) #contraintes de maximum pour chacune des variables a +10% de la moyenne sur 4 jours


#Fonction objectif
    a=[]
    b=[]
    for i in range(len(objectif[0])):
        b +=[L[i]]
        a += [L[i]*fonction_benefices[i]]
prob += (lpSum(b)<=capacite_max-capacite_jour) #contrainte de stockage des aliments
prob += (lpSum(a)) # fonction a maximiser : ici le benefice

# Résolution
solver = PULP_CBC_CMD(timeLimit=20, msg=False) #limite le temps de calcul a 20sec
prob.solve(solver=solver)

# Résultat
compteur=-1
for i in reapprovisionnement_dict:
    compteur +=1
    reapprovisionnement_dict[i]=int(L[compteur].value())





