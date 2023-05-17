import numpy as np
##Algorithme du simplexe

G = np.array([[1,1,1], [0,1,0],[0,0,-1]])
D = np.array([34,4,-5])
C1 = np.array([1,2,3])

def simplexe(C1,G,D):
    """
    Permet de calculer le maximum de C1 sous les contraintes G*X <= D
    X étant les inconnues (dans notre modèle le nombre de chaque aliments)
    D étant les contraintes de places (Ex : on demande moins de 25 poulet)
    C1 étant la fonction à maximiser ( ici c'est le bénéfice total)

    """
    m =len(G)
    p = len(G[0])
    n = m + p

    # Transformation en contrainte égalité
    A = np.concatenate((G, np.eye(m)), axis=1)
    B = D
    C = np.concatenate((C1, np.zeros(m)))

    # Recherche du premier sommet
    Jin = np.arange(p, n) #indice de la base
    Jout = np.arange(p) #indice hors base
    X = np.zeros(n)
    X[Jin] = np.linalg.inv(A[:, Jin][0:m, :]) @ B
    val = C @ X

    # Calcul de H, Bprime, Cprime
    H = np.linalg.inv(A[:, Jin][0:m, :]) @ A[:, Jout]
    Bprime = np.linalg.inv(A[:, Jin][0:m, :]) @ B
    Cprime = C[Jout] - H.T @ C[Jin]
    valmax = np.max(Cprime)

    # Boucle simplexe
    while valmax > 0:
        # Qui entre dans la base ?
        b = np.argmax(Cprime)
        iin = Jout[b]

        # Qui sort de la base ?
        K = Bprime / np.abs(H[:, iin]) #pivot
        ind = np.where(K > 0)[0]
        e = np.argmin(K[ind])
        iout = Jin[ind[e]]

        # Nouveau sommet
        Jin[ind[e]] = iin
        Jout[b] = iout
        X = np.zeros(n)
        X[Jin] = np.linalg.inv(A[:, Jin][0:m, :]) @ B
        val = C @ X

        # Actualisation de H, Bprime, Cprime
        H = np.linalg.inv(A[:, Jin][0:m, :]) @ A[:, Jout]
        Bprime = np.linalg.inv(A[:, Jin][0:m, :]) @ B
        Cprime = C[Jout] - H.T @ C[Jin]
        valmax = np.max(Cprime)

    return val, list(X[0:p])
