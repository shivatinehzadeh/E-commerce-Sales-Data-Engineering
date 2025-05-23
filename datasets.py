import os 
import kagglehub
import shutil
from dotenv import load_dotenv
load_dotenv()


def gathering_datasets():
    if not os.path.exists("data/orders.csv"):
        path_orders = kagglehub.dataset_download(os.getenv("path_orders"))
        shutil.copy(path_orders+(os.getenv("orders_name")), "data/orders.csv")
    else:
        print("Orders dataset already exists.")
    if not os.path.exists("data/products.csv"):
        path_products = kagglehub.dataset_download(os.getenv("path_products"))
        shutil.copy(path_products+(os.getenv("products_name")), "data/products.csv")
    else:
        print("Products dataset already exists.")
    if not os.path.exists("data/customers.csv"):
        path_customers = kagglehub.dataset_download(os.getenv("path_customers"))
        shutil.copy(path_customers+(os.getenv("customers_name")), "data/customers.csv")
    else:
        print("Customers dataset already exists.")