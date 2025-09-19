import pandas as pd

orders_data = {
    'OrderID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'CustomerName': ['Alice Smith', 'Bob Johnson', 'Carol Davis', 'Dave Wilson', 'Eve Torres',
                     'Frank Brown', 'Grace Hall', 'Henry Young', 'Irene Scott', 'Jake Lewis'],
    'Product': ['Laptop', 'Office Chair', 'Monitor', 'Desk Lamp', 'Smartphone',
                'Bookcase', 'Headphones', 'Standing Desk', 'Tablet', 'Office Chair'],
    'Category': ['Electronics', 'Furniture', 'Electronics', 'Furniture', 'Electronics',
                 'Furniture', 'Electronics', 'Furniture', 'Electronics', 'Furniture'],
    'Quantity': [1, 2, 1, 3, 2, 1, 4, 1, 2, 1],
    'Price': [1200, 150, 300, 40, 800, 200, 75, 500, 350, 150],
    'OrderDate': ['2023-01-15', '2023-02-05', '2023-02-20', '2023-03-12', '2023-03-18',
                  '2023-04-02', '2023-04-10', '2023-05-05', '2023-05-22', '2023-06-01'],
    'Region': ['North', 'South', 'East', 'West', 'North',
              'South', 'East', 'West', 'North', 'South']
}
# orders_data =  pd.read_csv("orders_data.csv")

orders_df = pd.DataFrame(orders_data) #converts the dataset to Pandas Data Frame

print(orders_df)

# print(orders_df.head()) # prints the first 5 rows of the dataframe.

# print(orders_df.info()) # prints the info about all the columns

print(orders_df.describe())
