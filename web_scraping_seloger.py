
#import module
import requests
import numpy


#function
def nb_page_recherche(nb_annonce, nb_annonce_page) :
    """
    définit le nombre de pages en fonction du nombre d'annonces.
    """
    nb_page = nb_annonce/nb_annonce_page
    if type(nb_page) == float :
        nb_page = int(nb_page) + 1
    return nb_page


def list_adresses(adresse_0, nb_page) :
    """
    Crée la liste des adresses de chacune des pages de notre recherche.
    """
    adresses = []
    for i in range(1, nb_page + 1) :
        ad_page = adresse_0 + str(i)
        adresses.append(ad_page)
    return adresses


def test_conn(liste_add) :
    """
    Test de connexion à chacune des adresses listées et liste les codes sources.
    """
    list_test_ad = []
    for a in liste_add :
        response = ''
        response = requests.get(a)
        list_test_ad.append(response.text)
    return list_test_ad


#main code
nb_annonce = 2301
nb_annonce_page = 25
nb_page = nb_page_recherche(nb_annonce, nb_annonce_page)
adresse_0 = 'https://www.seloger.com/list.htm?projects=2%2C5&types=1%2C2&natures= \
            1%2C2%2C4&places=%5B%7Bcp%3A75%7D%5D&price=500000%2F750000&surface=42%2 \
            F100&enterprise=0&qsVersion=1.0&LISTING-LISTpg='
liste_add = list_adresses(adresse_0, nb_page )
test_add = test_conn(liste_add)
print(test_add)

