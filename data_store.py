import pandas as pd
from models import Products,Orders,Customers
from db_session import get_db
from fastapi import APIRouter
import asyncio
router = APIRouter()

db=next(get_db())


@router.post("/products_data/")
async def products_data():
    db.query(Products).delete()
    db.commit()
    asyncio.create_task(async_insert_data("products"))
    return {"status": "accepted"}
    
    

@router.post("/orders_data/")
async def orders_data():
    db.query(Orders).delete()
    db.commit()
    asyncio.create_task(async_insert_data("orders"))
    return {"status": "accepted"}
    
 
@router.post("/customers_data/")
async def customers_data():
    db.query(Customers).delete()
    db.commit()
    asyncio.create_task(async_insert_data("customers"))
    return {"status": "accepted"}
    
       
    
async def async_insert_data(type):
    if type == "orders":
        print("inserting orders data...")
        df = pd.read_csv("data/orders.csv")
        for _, row in df.iterrows():
            orders_data_object = Orders(
                event_time=row['event_time'],
                event_type=str(row['event_type']),
                product_id=row['product_id'],
                category_code=row['category_code'],
                category_id=row['category_id'],
                price=row['price'],
                brand=str(row['brand']),
                user_id=row['user_id'],
                user_session=row['user_session']
            )
        db.add(orders_data_object)
        print("orders insert is in progress...")
    elif type == "customers":
        print("inserting customers data...")
        df = pd.read_csv("data/customers.csv")
        for _, row in df.iterrows():
            customers_data_object = Customers(
                ID=row['ID'],
                gender=row['Gender'],
                ever_Married=row['Ever_Married'],
                age=row['Age'],
                graduated=row['Graduated'],
                profession=row['Profession'],
                work_Experience=row['Work_Experience'],
                spending_Score=row['Spending_Score'],
                family_Size=row['Family_Size'],
                var_1=row['Var_1'],
                segmentation=row['Segmentation']
            )
            db.add(customers_data_object)
        db.commit()
        print("Customers insert is in progress...")
        await asyncio.sleep(1) 
    elif type == "products":
        print("inserting products data...")
        df = pd.read_csv("data/products.csv")
        for _, row in df.iterrows():
            products_data_object = Products(
                invoice=row['Invoice'],
                country=str(row['Country']),
                customer_id=row['Customer ID'],
                invoiceDate=row['InvoiceDate'],
                price=row['Price'],
                quantity=row['Quantity'],
                stockCode=row['StockCode'],
                description=row['Description']
            )
        db.add(products_data_object)
        print("products insert is in progress...")
    db.commit()
    await asyncio.sleep(1) 
    print("message:data inserted successfully.")


    


