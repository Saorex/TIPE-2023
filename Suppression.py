##Suppression des objets vendus

for aliment in stock_dict:        #permet de déterminer le nombre potentiel de variables à supprimer
    nombre_aliment+= stock_dict[aliment] + nombre_aliment_vendu  #Les aliments qui ont été vendu ne seront pas compté dans le dictionnaire nombre aliment (car actualisé en amont) donc on ajoute au moins le nombre total d'aliment vendu le jour même
    for i in range(0,nombre_aliment):
        if aliment+str(i) in globals():   #permet de vérifier si cette variable est bien défini dans l'environnement
            if not globals()[aliment+str(i)].existance:   #cet atribut est un booléen
               stock_liste.remove(globals()[aliment+str(i)])
               del globals()[aliment+str(i)]