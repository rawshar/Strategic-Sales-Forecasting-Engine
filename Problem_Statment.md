Problem Statement:
Manage the data for a retail company that deals with beverages. There are three main entities:

1. Customers: Details of 20,000 shops.
2. Products: Information about 20,000 different beverage products.
3. Transactions: Historical sales data from the past year.

Need to synthesize this data and load it into a DuckDB in-memory database. From this data, I need to predict the sales for the upcoming month (September 2023) and find the sales prediction of a product that is similar to existing ones but not in the current tables.


Synthetic Data Generation:
To create the synthetic data for these tables in the Parquet format. An Action Plan is:

1. Generate Customers and Products:
Customers: Generate details for 20,000 shops.
Products: Generate details for 20,000 beverage products.

2. Generate Transactions: Create a reasonable number of transactions for each customer and product from the past year.

3. Save the Tables in Parquet Format

4. Load into DuckDB

5. Predict Sales for September 2023:

6. Find Sales for Similar Products: Identify a product that is similar to existing products using clustering or similarity measures. Use the predictions for similar products to infer the sales of the new product.





