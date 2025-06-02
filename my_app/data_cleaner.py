import pandas as pd
import numpy as np
import sys
import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Adjust this path to the folder containing your `my_app` folder
base_dir = os.getenv("BASE_PATH")

if base_dir and base_dir not in sys.path:
    sys.path.insert(0, base_dir)
print(f"Base directory added to sys.path: {base_dir}")    


def data_cleaner():
    # Load datasets
    chunksize=10000
    chunk_orders = pd.read_csv("data/orders.csv", chunksize=chunksize,dtype=str)
    chunk_products = pd.read_csv("data/products.csv", chunksize=chunksize)
    chunk_customers = pd.read_csv("data/customers.csv", chunksize=chunksize)
    
    for orders in chunk_orders:
    # Clean orders dataset
        orders.dropna(subset=['user_id', 'category_id', 'product_id','category_code'], inplace=True)
        orders['event_time'] = pd.to_datetime(orders['event_time'], errors='coerce')
        orders.to_csv("data/orders.csv", index=False)
        print("Orders dataset cleaned and saved.")
        
        
    for products in chunk_products:
    # Clean products dataset
        products.dropna(subset=['Price', 'Customer ID'], inplace=True)
        products['InvoiceDate'] = pd.to_datetime(products['InvoiceDate'], errors='coerce') 
        products['Quantity'] = pd.to_numeric( products['Quantity'], errors='coerce').fillna(0).astype(int)
        products['Customer ID'] = pd.to_numeric( products['Customer ID'], errors='coerce').fillna(0).astype(int)
        products['Invoice'] = pd.to_numeric( products['Invoice'], errors='coerce').fillna(0).astype(int)
        products['StockCode'] = pd.to_numeric( products['StockCode'], errors='coerce').fillna(0).astype(int)
        products['Price'] = pd.to_numeric(products['Price'], errors='coerce')
        products.to_csv("data/products.csv", index=False)
        print("Products dataset cleaned and saved.")
        
    for customers in chunk_customers:
        # Clean customers dataset
        customers.dropna(subset=['ID'], inplace=True)
        customers.drop_duplicates(subset='ID', keep='first', inplace=True)
        customers['Ever_Married'] = customers['Ever_Married'].astype(bool)
        customers['Graduated'] = customers['Graduated'].astype(bool)
        customers['Work_Experience'] = pd.to_numeric( customers['Work_Experience'], errors='coerce').fillna(0).astype(int)
        customers['Family_Size'] = pd.to_numeric( customers['Family_Size'], errors='coerce').fillna(0).astype(int)

        customers.to_csv("data/customers.csv", index=False)
        print("Customers dataset cleaned and saved.")
    print("Data cleaning completed and cleaned datasets saved.")
    
