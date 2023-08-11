import pandas as pd
import random
import itertools


product_ids = range(1, 20001)


size_in_litres = [0.5, 0.25, 1, 0.75, 2, 3, 4, 5, 6, 7]
beverage_types = ['beer', 'gin', 'vodka', 'tequila', 'wine', 'whisky', 'rum', 'brandy', 'champagne']
sweetness = ['Dry', 'Sweet', 'Semi-Dry', 'Semi-Sweet']
colors = ['black', 'red', 'white', 'yellow', 'orange', 'green', 'blue', 'pink', 'brown']
flavours = ['orange', 'grape', 'raspberry', 'strawberry', 'lemon', 'lime', 'cherry', 'peach', 'apple', 'pineapple']
brands = ['Heineken', 'Corona', 'Budweiser', 'Absolut', 'JackDaniels', 'GreyGoose', 'Jameson', 'ChivasRegal', 'JohnnieWalker']
vintage = [random.randint(1900, 2023) for _ in product_ids]

# all possible combinations, total combinations will be mulitiplication fo len of each column 
# total number of unique combinations is: 36158400
all_combinations = list(itertools.product(size_in_litres, beverage_types, sweetness, vintage, colors, flavours, brands))
random.shuffle(all_combinations)

#taking only 20000 products
products_data = {
    'product_id': product_ids,
    'size_in_litres': [x[0] for x in all_combinations[:20000]],
    'beverage_type': [x[1] for x in all_combinations[:20000]],
    'sweetness': [x[2] for x in all_combinations[:20000]],
    'vintage': [x[3] for x in all_combinations[:20000]],
    'color': [x[4] for x in all_combinations[:20000]],
    'flavour': [x[5] for x in all_combinations[:20000]],
    'brand': [x[6] for x in all_combinations[:20000]]
}

#getting a dataframe from the above
products_df = pd.DataFrame(products_data)

#creating name to store the data
products_df['name'] = products_df['size_in_litres'].astype(str) + products_df['beverage_type'].str.capitalize() + products_df['vintage'].astype(str) + products_df['color'].str.capitalize() + products_df['flavour'].str.capitalize()

#Save to Parquet format
products_df.to_parquet('products.parquet')
