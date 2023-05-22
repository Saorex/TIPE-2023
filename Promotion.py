promo_liste=[]
for aliment in stock_liste:
    if 0<aliment.age<=1:
        promo_liste.append(aliment)
        aliment.prix= aliment.prix - aliment.prix*(30/100)