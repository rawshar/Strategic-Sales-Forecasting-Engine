The Schema for the two tables is:

Customers:
1. locations = ['Toronto', 'Vancouver', 'Montreal', 'Calgary', 'Edmonton', 'Ottawa', 'Quebec_City', 'Winnipeg', 'Hamilton', 'Halifax'] (Varchar)
2. store_types = ['Supermarket', 'Hypermarket', 'Mini_Store', 'Department_Store', 'Convenience_Store', 'Specialty_Store'] (Varchar)
3. store_sizes = ['Extra_Small', 'Small', 'Medium', 'Large', 'Extra_Large'] (Varchar)
4. number_of_employees = [5, 10, 15, 20, 25, 30, 40, 50, 75, 100, 150, 200, 250, 300] (Varchar)
5. flower_names = ['Rose', 'Tulip', 'Lily', 'Daisy', 'Sunflower', 'Orchid', 'Daffodil', 'Carnation', 'Violet', 'Chrysanthemum'] (Varchar)
6. CustomerId = range(1, 20001) (int)
7. Name= Created from the combination of the first 5 attributes

Products

1. size_in_litres = [0.5, 0.25, 1, 0.75, 2, 3, 4, 5, 6, 7]
2. beverage_types = ['beer', 'gin', 'vodka', 'tequila', 'wine', 'whisky', 'rum', 'brandy', 'champagne'] (Varchar)
3. sweetness = ['Dry', 'Sweet', 'Semi-Dry', 'Semi-Sweet'] (Varchar)
4. colors = ['black', 'red', 'white', 'yellow', 'orange', 'green', 'blue', 'pink', 'brown'] (Varchar)
5. flavours = ['orange', 'grape', 'raspberry', 'strawberry', 'lemon', 'lime', 'cherry', 'peach', 'apple', 'pineapple'] (Varchar)
6. brands = ['Heineken', 'Corona', 'Budweiser', 'Absolut', 'JackDaniels', 'GreyGoose', 'Jameson', 'ChivasRegal', 'JohnnieWalker'] (Varchar)
7. vintage = range(1900, 2033)
8. name: combination of the above 7 (Varchar)
9. PrdouctId: range(1, 20001) (int)

Transactions:


'transaction_id': range(1,200001)
'customer_id': range(1,20001)
'product_id': range(1,20001) 
'quantity': [0.5, 0.25, 1, 0.75, 2, 3, 4]# 7
'transaction_date': 1 year before


