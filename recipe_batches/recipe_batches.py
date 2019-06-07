#!/usr/bin/python

import math

"""  
We need to check the amount needed of each recipe ingredient.
We need to see how many times the amount of ingredients we have can go into the amount needed in the recipe.
If the amount of each ingredient can go into the amount needed at least once, then return the lowest number of times a single ingredient
go into the amount needed.
else return 0
""" 

def recipe_batches(recipe, ingredients):
        list_of_enough_ingredients=[]
        for rec_name in recipe:
                try:
                        cur_rec_amount = recipe[rec_name]
                        cur_ing_amount = ingredients[rec_name]
                        number_of_times_we_meet_min_ingredient = int(cur_ing_amount/cur_rec_amount)
                        list_of_enough_ingredients.append(number_of_times_we_meet_min_ingredient)
                except KeyError:
                        list_of_enough_ingredients.append(0)
        for number in list_of_enough_ingredients:
                current_lowest = list_of_enough_ingredients[0]
                if current_lowest > number:
                        current_lowest = number
        return current_lowest


print(recipe_batches({ 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95 }))



# if __name__ == '__main__':
#         # Change the entries of these dictionaries to test 
#         # your implementation with different inputs
#         recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#         ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#         print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))