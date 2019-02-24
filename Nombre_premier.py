def est_premier(num):

	'''
    Méthode simple de vérification de nombre premiers
    '''
    
    for n in range(2,num):
        if num % n == 0 :
            print("n'est pas premier")
            break
        else:
            print("est premier")
            break


# Autre méthode plus élaborée

import math

def est_premier(num):
    '''
    Fonction plus elaborée pour déterminer si un nombre est premier
    parametre : num, le nb a tester
    Renvoie un booléen
    False nest pas premier
    True le nb est premier
    '''
    if num % 2 ==0 and num > 2:
        return False
    for n in range(3, int(math.sqrt(num))+1, 2):
        if num % n ==0:
            return False
    return True