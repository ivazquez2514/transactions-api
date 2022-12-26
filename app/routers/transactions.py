from fastapi import APIRouter
from pathlib import Path
from ..utils.transactions import Transactions

router = APIRouter(
    prefix="/transactions",
    tags=["transactions"]
)

@router.get("/balance")
def getBalance():
    csv_path = Path("app/data/transactions.csv")
    transactionTotals = Transactions()
    transactionTotals.readFromCSV(csv_path = csv_path)
                
    return { "total": transactionTotals, "credit": transactionTotals.credit, "debit": transactionTotals.debit }



