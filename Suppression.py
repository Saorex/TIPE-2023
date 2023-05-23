##Suppression des objets vendus
stock_temp=[]
promo_temp=[]

for indice in range(len(stock_liste)):
    if stock_liste[indice].existence:
        stock_temp.append(stock_liste[indice])

stock_liste=stock_temp

for indice in range(len(promo_liste)):
    if promo_liste[indice].existence:
        promo_temp.append(promo_liste[indice])

promo_liste=promo_temp




