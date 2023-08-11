import pandas as pd
import itertools

locations = ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Edmonton', 'Ottawa', 'Quebec_City', 'Winnipeg', 'Hamilton', 'Halifax']
store_types = ['Supermarket', 'Hypermarket', 'Mini_Store', 'Department_Store', 'Convenience_Store', 'Specialty_Store']
store_sizes = ['Extra_Small', 'Small', 'Medium', 'Large', 'Extra_Large']
number_of_employees = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 250, 300]
flower_names = ['Rose', 'Tulip', 'Lily', 'Daisy', 'Sunflower', 'Orchid', 'Daffodil', 'Carnation', 'Violet', 'Chrysanthemum']

#total number of combinations are 42000
combinations = list(itertools.product(locations, store_types, store_sizes, number_of_employees, flower_names))
combinations = combinations[:20000]
# taking only 20000 combinations
customer_data = {
    'customer_id': range(1, 20001),
    'location': [x[0] for x in combinations],
    'store_type': [x[1] for x in combinations],
    'store_size': [x[2] for x in combinations],
    'flower_name': [x[4] for x in combinations],
    'name': ['{}_{}_{}_{}Emp_{}'.format(x[0], x[1], x[2], x[3], x[4]) for x in combinations],
    'number_of_employees': [x[3] for x in combinations]
}

# Creating a DataFrame
customers_df = pd.DataFrame(customer_data)

# Saving to parquet format
customers_df.to_parquet('customers.parquet', index=False)
