"""handles user account transactions"""

import random
import datetime
from data import prompts


class Transaction:
    """creates new transaction for user"""

    transactions = {}
    transaction_ids = []

    def __init__(
        self,
        trans_type,
        funding_account_title,
        funding_account_number,
        receiver_details,
        trans_amount,
        balance,
        trans_id=None,
        date=None,
        time=None,
    ):
        self.trans_id = (
            trans_id if trans_id is not None else self.generate_transaction_id()
        )
        self.date = (
            date if date is not None else datetime.datetime.now().strftime("%d-%m-%y")
        )
        self.time = (
            time if time is not None else datetime.datetime.now().strftime("%I:%M-%p")
        )
        self.trans_type = trans_type
        self.funding_account_title = funding_account_title
        self.funding_account_number = funding_account_number
        self.receiver_name = receiver_details[0]
        self.receiver_account_no = receiver_details[1]
        self.trans_amount = trans_amount
        self.balance = balance
        Transaction.transactions[self.trans_id] = self
        if not trans_id:
            self.save_transaction_to_file()
        if trans_id:
            Transaction.transaction_ids.append(trans_id)

    def generate_transaction_id(self):
        """generates the transaction receipt number"""
        transaction_id = ""
        count = 0
        while True:
            digits = random.randint(1, 9)
            alphabets = "abcdefghijklmnopqrstuvwxyz"
            char = random.choice(alphabets)
            transaction_id = transaction_id + char.title() + str(digits)
            count += 1
            if count == 11:
                if transaction_id in Transaction.transaction_ids:
                    count = 0
                    transaction_id = ""
                    continue
                Transaction.transaction_ids.append(transaction_id)
                break
        return transaction_id

    @staticmethod
    def display_transaction(given_trans_id):
        """displays the details of a give transaction ID"""
        transaction = Transaction.get_transaction_by_id(given_trans_id)
        if transaction:
            print(prompts.TRANSACTION_DETAILS)
            print(
                prompts.SHOW_TRANS_DETAIL.format(
                    transaction.trans_id,
                    transaction.date,
                    transaction.time,
                    transaction.trans_type,
                    transaction.funding_account_title,
                    transaction.funding_account_number,
                    transaction.receiver_name,
                    transaction.receiver_account_no,
                    transaction.trans_amount,
                    transaction.balance,
                )
            )
        else:
            print(prompts.UNKNOWN_TRANSACTION_ID)

    @staticmethod
    def get_transaction_by_id(trans_id):
        """returns the transaction object of the given id"""
        return Transaction.transactions[str(trans_id)]

    def save_transaction_to_file(self):
        """saves the transaction in a file"""
        with open("data/transactions.txt", "a", encoding="UTF-8") as file:
            data = f"{self.trans_id} {self.date} {self.time} \
{self.trans_type} {self.funding_account_title} {self.funding_account_number} {self.receiver_name} \
{self.receiver_account_no} {self.trans_amount} {self.balance}"
            file.write(data + "\n")
