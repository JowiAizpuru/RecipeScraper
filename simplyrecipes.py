
import requests
from bs4 import BeautifulSoup
import re
# Format specifically for simplyrecipes.com

class SimplyRecipes():
    def __init__(self, url= None, name=None, prep_time=None, cook_time=None, total_time=None, servings=None, yields=None, ingredients=[], instructions=[] ):
        self.url = url
        self.name = name
        self.prep_time  =prep_time
        self.cook_time = cook_time
        self.total_time = total_time
        self.servings = servings
        self.yields = yields
        self.ingredients = ingredients
        self.instructions = instructions

        if self.url==None :
            self.page = None
            self.soup = None
        else: 
            self.page = requests.get(self.url)
            self.soup = BeautifulSoup(self.page.content, "html.parser")
   

    def get_url(self,url): 
        self.url = url
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
   
    def get_name(self):
        results = self.soup.find(id="recipe-block__header_1-0")
        self.name=  re.sub("\n","",  results.string)
    
    def get_prep_time(self):
        results = self.soup.find(id="meta-text_2-0")

        for i  in results.find_all("span","meta-text__data"):
            self.prep_time = re.sub("\n","",  i.string)   
            
    def get_cook_time(self):
        cook_time = self.soup.find(id="meta-text_3-0")
   
        for i  in cook_time.find_all("span","meta-text__data"):
            self.cook_time = re.sub("\n","",  i.string)
            
    def get_total_time(self):
        pass

    def get_yields(self): 
        pass
    
    def get_servings(self):
        pass

    def get_ingredients(self):
        pass

    def get_instructions(self):
        pass
        
    def return_data(self):
        self.get_name()
        self.get_prep_time()
        self.get_cook_time()
        self.get_total_time()
        self.get_yields()
        self.get_servings()
        self.get_ingredients()
        self.get_instructions()

        
        
        recipe_format = {"name": self.name, 
                 "prep_time": self.prep_time, 
                 "cook_time":self.cook_time, 
                 "total time":self.total_time,
                 "servings":self.servings,
                 "yield": self.yields,
                 "ingredients":self.ingredients,
                 "instructions":self.instructions                 
                 } 
        return recipe_format
    

if __name__ == "__main__":
    simplyTest = SimplyRecipes(url="https://www.simplyrecipes.com/easy-rice-and-beans-freezer-burritos-recipe-7106222")
    print(simplyTest.return_data())