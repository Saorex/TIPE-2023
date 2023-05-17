##Réapprovisionnement
#On se sert du dictionnaire reapprovisionnement_dict pour connaitre le nombre d'objet à crée
perte=0

for aliment in reapprovisionnement_dict:
    nombre_aliment=reapprovisionnement_dict[aliment]
    for k in range (1,nombre_aliment+1):
        test=False
        i=0
        if aliment in viande:
            while not test:                                 #Boucle permetant de vérifier l'existance d'une variable et donc éviter de l'écrasser
                if aliment+str(i) not in globals():         #Si elle n'est pas définie
                    test=True
                else:
                    i+=1
            globals()[aliment+str(i)]=Viande(aliment)
            stock_liste.append(globals()[aliment+str(i)])
            perte+=stock_liste[-1].prix


        if aliment in poisson:
            while not test:                                 #permet de vérifier l'existance d'une variable
                if aliment+str(i) not in globals():         #Si elle n'est pas définie
                    test=True
                else :
                    i+=1
            globals()[aliment+str(i)]=Poisson(aliment)
            stock_liste.append(globals()[aliment+str(i)])
            perte+=stock_liste[-1].prix

        if aliment in laitier:
            while not test:                                 #permet de vérifier l'existance d'une variable
                if aliment+str(i) not in globals():         #Si elle n'est pas définie
                    test=True
                else :
                    i+=1
            globals()[aliment+str(i)]=Laitier(aliment)
            stock_liste.append(globals()[aliment+str(i)])
            perte+=stock_liste[-1].prix

        if aliment in fruit:
            while not test:                                 #permet de vérifier l'existance d'une variable
                if aliment+str(i) not in globals():         #Si elle n'est pas définie
                    test=True
                else :
                    i+=1
            globals()[aliment+str(i)]=Fruit(aliment)
            stock_liste.append(globals()[aliment+str(i)])
            perte+=stock_liste[-1].prix

        if aliment in legume:
            while not test:                                 #permet de vérifier l'existance d'une variable
                if aliment+str(i) not in globals():         #Si elle n'est pas définie
                    test=True
                else :
                    i+=1
            globals()[aliment+str(i)]=Legume(aliment)
            stock_liste.append(globals()[aliment+str(i)])
            perte+=stock_liste[-1].prix