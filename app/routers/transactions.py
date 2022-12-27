import os
from fastapi import APIRouter, Depends
from pathlib import Path
from ..utils.transactions import Transactions
from pydantic import EmailStr
from ..core.config import get_settings

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/balance/{email}")
async def getBalance(email: EmailStr):
    csv_path = Path("app/data/transactions.csv")
    transactionTotals = Transactions()
    transactionTotals.readFromCSV(csv_path = csv_path)
                
    return {
        "settings": get_settings(),
        "total": transactionTotals,
        "credit": transactionTotals.credit,
        "debit": transactionTotals.debit
    }



