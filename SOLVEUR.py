from pulp import *

objectif = np.array([[1,2,3,1,2],
[4,5,6,1,2],
[7,8,9,1,2]])
contraintes = np.array([7,8,40])
fonction_benefices = np.array([2,7,4,2,4])

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
    prob += (lpSum(e)<=int(contraintes[i]))

#Fonction objectif
    a=[]
    for i in range(len(objectif[0])):
        a += [L[i]*fonction_benefices[i]]
    prob += (lpSum(a))

# Résolution
solver = PULP_CBC_CMD(timeLimit=20, msg=False)
prob.solve(solver=solver)

# Résultat
for i in range(len(objectif[0])):
    print(L[i],'=',L[i].value())





