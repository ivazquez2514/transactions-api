from pathlib import Path
from datetime import datetime
from .dates import months 
import csv

class MonthlyTransactions:
    january: int = 0
    february: int = 0
    march: int = 0
    april: int = 0
    may: int = 0
    june: int = 0
    july: int = 0
    august: int = 0
    september: int = 0
    october: int = 0
    november: int = 0
    december: int = 0

class AverageTotal:
    count = 0
    average = 0

class Transactions:
    total = 0
    credit = AverageTotal()
    debit = AverageTotal()
    monthly_transactions = MonthlyTransactions()

    def readFromCSV(self, csv_path: Path):
        self.total = 0
        with open(csv_path, "r") as file:
            csv_reader = csv.reader(file)
            for count, row in enumerate(csv_reader, start = 0):
                if count != 0:
                    month = months[int(row[1].split("/")[0])];
                    currentMonthValue = getattr(self.monthly_transactions, month, 10)
                    setattr(self.monthly_transactions, month, currentMonthValue + 1)
                    
                    transaction_quantity = float(row[2])
                    self.total += transaction_quantity

                    if transaction_quantity > 0:
                        self.credit.average += transaction_quantity
                        self.credit.count += 1
                    else:
                        self.debit.average += transaction_quantity
                        self.debit.count += 1
            
            self.credit.average /= 2
            self.debit.average /= 2