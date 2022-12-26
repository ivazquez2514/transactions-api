from pathlib import Path
from datetime import datetime
import csv

class AverageTotal:
    count = 0
    average = 0

class Transactions:
    total = 0
    credit = AverageTotal()
    debit = AverageTotal()

    def readFromCSV(self, csv_path: Path):
        self.total = 0
        with open(csv_path, "r") as file:
            csv_reader = csv.reader(file)
            for count, row in enumerate(csv_reader, start = 0):
                if count != 0:
                    # print(datetime.strptime(row[1], "%m/%d"))
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