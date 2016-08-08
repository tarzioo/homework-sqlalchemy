"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
def get_brand_with_id(id=8):

    # I wasn't entirely sure what I needed to grab with this function.
    #The instructions said to not use filter() or filter_by()
    #So I was assuming with get(), we just return the whole object?
    return Model.query.get(id)


# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
def get_models_by_name_and_brand(name='Corvette', brand_name='Chevrolet'):
    model_by_name_and_brand = Model.query.filter_by(name=name, brand_name=brand_name).all()

    return model_by_name_and_brand


# Get all models that are older than 1960.

#I feel I may have gone the long way around in doing this and also made it more complicated and messy. I would normally do a filter_by and all() and that would have displayed the results a lot neater but with filtering just the years older than 1960, I was unsure how to do it with my results.
def get_models_by_year(year=1960):

    result = Model.query.filter(Model.year > year)

    model_list = []

    for r in result:
        model_info = (r.brand_name, r.name)
        model_list.append(model_info)

    return model_list


#I did this function very similar to the get_models_by_year which I'm sure is a very long way to get the answer.

def get_founded_by_year(year=1920):
    """Get all brands that were founded after 1920."""

    result = Brand.query.filter(Brand.founded > 1920)

    brand_list = []

    for r in result:
        brand_info = (r.name)
        brand_list.append(brand_info)

    return brand_list


def get_models_with_like_characters(text="Cor%"):
    """Get all models with names that begin with "Cor"."""

    result = Model.query.filter(Model.name.like(text))

    model_list = []

    for r in result:
        model_list.append(r.name)

    return model_list    

# Get all brands that were founded in 1903 and that are not yet discontinued.

# def get_brands_with_founded(founded=1903, discontinued=Null):

#     result = Brand.query.filter(Brand.founded=founded, Brand.discontinued!=discontinued)

#     pass


# Get all brands that are either 1) discontinued (at any time) or 2) founded 
# before 1950.

def get_brand_name(brand_name='Chevrolet'):
    """Get any model whose brand_name is not Chevrolet."""

    result = Model.query.filter(Model.brand_name!=brand_name)

    brand_name_list = []

    for r in result:
        brand_name_list.append(r.name)

    return brand_name_list   



# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    result = Model.query.filter_by(year=year).first()

    return result

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    pass

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#it is an object of brand with the attribute of id=1 and name=Ford

# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?

#it is a table that shows the realationship with other tables using a foreign key. For example, in our model.py, the class Brand shows an association table as it has the foreignKey defined and what it has a relationship with in the Model table

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass
