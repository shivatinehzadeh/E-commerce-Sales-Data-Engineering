from fastapi import FastAPI
from datasets import gathering_datasets


app = FastAPI()
gathering_datasets()