def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    valeurs = []
    while not n == 1 :
        if n % 2 == 0 :
            n = n/2
            valeurs.append(n)
        else :
            n = n*3 + 1
            valeurs.append(n)
    return valeurs

def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 1 à n_max """
    for i in range (1,n_max+1): syracuse(i) 
    return True

def tempsVol(n):
    """ Retourne le temps de vol de n """
    return len(syracuse(n))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    return [tempsVol(i) for i in range (1, n_max+1)]
