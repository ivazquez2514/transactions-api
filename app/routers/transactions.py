import os
from fastapi import APIRouter
from pathlib import Path
from ..utils.transactions import Transactions
from ..utils.email import send_email

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/balance/{email}")
async def getBalance(email):
    csv_path = Path("app/data/transactions.csv")
    transaction_totals = Transactions()
    transaction_totals.readFromCSV(csv_path = csv_path)

    return await send_email(email = email, data = transaction_totals)



