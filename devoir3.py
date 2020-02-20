# coding: utf-8
# importer les modules dont j'ai besoin
import csv
import requests
from bs4 import BeautifulSoup

fichier = "goodfood.csv"

# je m'intéresse au site web de la compagnie Goodfood, je veux afficher toutes les recettes/ingrédients disponibles

url = "https://www.makegoodfood.ca/fr/recipes/"

# annoncer ma présence sur le serveur

entetes = {
    "User-Agent": "Mayssa Ferah, journalism student UQAM",
    "from":"mayssa.ferah@gmail.com"
}

# placer le contenu de ma page web dans une variable + analyse (parse) 

pages = list(range(1,200))


for url1 in pages:
    url1= url + str(pages)

    contenu = requests.get(url1, headers=entetes)

    page = BeautifulSoup(contenu.text,"html.parser")

    recettes = page.find_all("div",class_="recipeofweek-title")
    # print(recettes)

    for recette in recettes:
        # print(recette.find("a"))

        urlrecette = recette.find("a")["href"]

        contenu = requests.get(urlrecette, headers=entetes)

        page = BeautifulSoup(contenu.text,"html.parser")

        
        ingredients = page.find_all("li", class_="ingred")

        titres = page.find("h1", class_="name-of-dish-size")

        for titre in titres:
            # print(titre)


            for ingredient in ingredients:
                i = ingredient.text.strip().split("\n") #\n = séparer en fonction du return
            # print(ingredient.text.strip())
            # print(i)
                ing = i[1].strip()
                qute = i[0].strip()
                

            infos = [
                ing, 
                qute, 
                titre 
            ]

            harry = open(fichier,"a")
            potter = csv.writer(harry)
            potter.writerow(infos)
                
            # print(qute)
            # <h1 class="name-of-dish-size">Côtelettes de porc poêlées</h1>



