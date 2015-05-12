# Note: this file will not run. It is only for recording answers.

# Part 2: Write queries

# Get the brand with the **id** of 8.
Brand.query.filter_by(id = 8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
Brand.query.filter(Brand.founded==1903, Brand.discontinued.is_(None)).all()

# Get all brands with that are either discontinued or founded before 1950.
Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued.isnot(None))).all()

# Get any model whose brand_name is not Chevrolet.
Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# Part 3: Discussion Questions

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
# This returns an object...

# 2. In your own words, what is an association table, and what *type* of relationship 
# does an association table manage?
# The assoc. table is used for many-to-many relationships and connects tables that have these relationships with each other.
