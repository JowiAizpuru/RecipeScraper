import requests
from bs4 import BeautifulSoup
import re
from simplyrecipes import SimplyRecipes

URL = "https://www.simplyrecipes.com/easy-rice-and-beans-freezer-burritos-recipe-7106222"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

recipe_format = {"name":"none", 
                 "prep_time":"none", 
                 "cook_time":"none", 
                 "total time":"none",
                 "servings":"none",
                 "yield": "none",
                 "ingredients":"none",
                 "instructions":"none"                 
                 }
cook_time = soup.find(id="meta-text_3-0")
   
for i  in cook_time.find_all("span","meta-text__data"):
    recipe_format["cook_time"] = re.sub("\n","",  i.string)


total_time = soup.find(id ="meta-text_1-0")

for i  in  total_time.find_all("span","meta-text__data"):
    recipe_format["total_time"] = re.sub("\n","",  i.string)



servings = soup.find(id ="meta-text_6-0")

for i  in  servings.find_all("span","meta-text__data"):
    recipe_format["servings"] = re.sub("\n"," ",  i.string)


yields = soup.find(id ="meta-text_5-0")

for i  in  yields.find_all("span","meta-text__data"):
    recipe_format["yield"] = re.sub("\n","",  i.string)

ingredients = soup.find(id= "section--ingredients_1-0")
ingred_list = []

text_combine = []
for i in ingredients.find_all("li",class_="structured-ingredients__list-item"):
   
    text_combine = [] 
    for j in i.find_all("span"):
        text_combine.append(j.string)
    
    # print(text_combine)
    # ingred_list.append(re.sub("\n","",  i.string))


# print(recipe_format)

if __name__ == "__main__":
    simplyTest = SimplyRecipes(url="https://www.simplyrecipes.com/easy-rice-and-beans-freezer-burritos-recipe-7106222")
    simplyTest.get_name()
    print(simplyTest.return_data())