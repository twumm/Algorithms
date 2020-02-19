#!/usr/bin/python

import math

recipe = {'milk': 100, 'butter': 50, 'flour': 5}
ingredients = {'milk': 132, 'flour': 5, 'butter': 48}

recipe2 = {'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5}
ingredients2 = {'milk': 1288, 'flour': 9, 'sugar': 95}

recipe3 = {'milk': 100, 'butter': 50, 'cheese': 10}
ingredients3 = {'milk': 198, 'butter': 52, 'cheese': 10}

recipe4 = { 'milk': 2, 'sugar': 40, 'butter': 20 }
ingredients4 = { 'milk': 5, 'sugar': 120, 'butter': 500 }


def recipe_batches(recipe, ingredients):
    # check if length of recipe are less or same as ingredient length
    if (len(ingredients) < len(recipe)):
        # return 0 - not possible
        return 0
    # create a number_of_batches list variable
    number_of_batches = []
    for recipe_key, recipe_value in recipe.items():
        for ingredients_key, ingredients_value in ingredients.items():
            if recipe_key == ingredients_key and ingredients_value // recipe_value <= 0:
                return 0
            if recipe_key == ingredients_key and ingredients_value // recipe_value > 0:
                temp = ingredients_value // recipe_value
                number_of_batches.append(temp)
    minimum_batch = min(number_of_batches)
    return minimum_batch

    # for each same key in recipe and value

    # check number of times value in ingredients can be divided by value in recipe
    # if 0, return 0
    # if number of times value in ingredients can be divided by value in recipe is less than
    #   number_of_batches but more than 0 save to number_of_batches
    # return number_of_batches


# print(1288 // 100)
# print(9 // 4)
# print(48 // 50)
# print(recipe_batches(recipe, ingredients))
# print(recipe_batches(recipe2, ingredients2))
# print(recipe_batches(recipe3, ingredients3))
# print(recipe_batches(recipe4, ingredients4))

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
