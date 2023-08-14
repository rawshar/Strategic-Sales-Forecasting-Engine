import pandas as pd
import random
from datetime import datetime, timedelta


num_transactions = 200000


quantities = [0.5, 0.25, 1, 0.75, 2, 3, 4] 


transaction_data = {
    'transaction_id': range(1, num_transactions + 1),
    'customer_id': [random.randint(1, 20001) for _ in range(num_transactions)], 
    'product_id': [random.randint(1, 20001) for _ in range(num_transactions)], 
    'quantity': [random.choice(quantities) for _ in range(num_transactions)],
    'transaction_date': [datetime.now() - timedelta(days=random.randint(0, 365)) for _ in range(num_transactions)]
}


transactions_df = pd.DataFrame(transaction_data)


transactions_df.to_parquet('transactions.parquet', index=False)
