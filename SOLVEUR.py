from pulp import *
import numpy as np
import random as rd


objectif=np.eye(34)
contraintes = np.array([rd.randint(0,50) for i in range(0,34)])
fonction_benefices = np.array(prix)

# Problème
prob = LpProblem("chiffre_affaires_supermarché", LpMaximize)

# Paramètres
L=[]
for i in aliment_dict:
    L+=[LpVariable( i,lowBound=0, cat=LpInteger)]

# Contraintes
for i in range(len(objectif)):
    e=[]

    for j in range(len(objectif[i])):
        e+=[objectif[i][j]*L[j]]
    prob += (lpSum(e)>=int(contraintes[i])) #contraintes de minimum pour chacune des variables


#Fonction objectif
    a=[]
    b=[]
    for i in range(len(objectif[0])):
        b+=[L[i]]
        a += [L[i]*fonction_benefices[i]]
    prob += (lpSum(b)<=capacite_jour)
    prob += (lpSum(a))

# Résolution
solver = PULP_CBC_CMD(timeLimit=20, msg=False)
prob.solve(solver=solver)

# Résultat
for i in range(len(objectif[0])):
    print(L[i],'=',L[i].value())





