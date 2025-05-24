from fastapi import FastAPI
from datasets import gathering_datasets

import data_store
app = FastAPI()

gathering_datasets()
app.include_router(data_store.router)  