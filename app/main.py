from fastapi import FastAPI
from .routers.transactions import router as TransactionsRouter

app = FastAPI()

app.include_router(TransactionsRouter)

@app.get("/")
def root():
    return { "message": "Welcome to transactions balance API" }