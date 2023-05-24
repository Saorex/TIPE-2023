##Reapprovisionnement
for aliment in reapprovisionnement_dict:
    nombre_aliment=reapprovisionnement_dict[aliment]
    for k in range(0,nombre_aliment):
        if aliment in viande:
            stock_liste.append(Viande(aliment))
            perte+=stock_liste[-1].prix_achat
        if aliment in poisson:
            stock_liste.append(Poisson(aliment))
            perte+=stock_liste[-1].prix_achat
        if aliment in laitier:
            stock_liste.append(Laitier(aliment))
            perte+=stock_liste[-1].prix_achat
        if aliment in fruit:
            stock_liste.append(Fruit(aliment))
            perte+=stock_liste[-1].prix_achat
        if aliment in legume:
            stock_liste.append(Legume(aliment))
            perte+=stock_liste[-1].prix_achat

revenue_estime=0
for aliment in stock_liste:
    revenue_estime+= aliment.prix_vente