"""handles user accounts notifications"""

import datetime
import random


class Notification:
    """handle notifications"""

    notifications = {}
    notification_ids = []

    def __init__(
        self,
        notification_type,
        acc_num,
        acc_name,
        card_num=None,
        bill_id=None,
        card_new_status=None,
        amount=None,
        notification_id=None,
        date=None,
        time=None,
        transaction_id=None,
        status="Unread",
    ):
        self.notification_id = (
            notification_id
            if notification_id is not None
            else self.generate_notification_id()
        )
        self.date = (
            date if date is not None else datetime.datetime.now().strftime("%d-%m-%y")
        )
        self.time = (
            time if time is not None else datetime.datetime.now().strftime("%I:%M-%p")
        )
        self.notification_type = notification_type
        self.acc_num = acc_num
        self.acc_name = acc_name
        self.card_num = card_num
        self.bill_id = bill_id
        self.card_new_status = card_new_status
        self.amount = amount
        self.transaction_id = transaction_id
        self.status = status

        Notification.notifications[self.notification_id] = self
        if not notification_id:
            self.save_notification_to_file()
        if notification_id:
            Notification.notification_ids.append(notification_id)

    def generate_notification_id(self):
        """generates the Notification id"""
        notification_id = ""
        count = 0
        while True:
            digits = random.randint(1, 9)
            alphabets = "abcdefghijklmnopqrstuvwxyz"
            char = random.choice(alphabets)
            notification_id = notification_id + char.title() + str(digits)
            count += 1
            if count == 5:
                if notification_id in Notification.notification_ids:
                    count = 0
                    notification_id = ""
                    continue
                Notification.notification_ids.append(notification_id)
                break
        return notification_id

    def save_notification_to_file(self):
        """saves the transaction in a file"""
        with open("data/notifications.txt", "a", encoding="UTF-8") as file:
            data = f"{self.acc_name} {self.acc_num} {self.date} {self.notification_id} {self.time} {self.notification_type} {self.card_num} {self.bill_id} {self.card_new_status} {self.amount} {self.transaction_id} {self.status}"
            file.write(data + "\n")

    @staticmethod
    def get_notification_by_id(notification_id):
        """returns the notification object of the given id"""
        return Notification.notifications[str(notification_id)]

    def display_notification(self):
        """displays the details of a give transaction ID"""
        acc_num = self.acc_num
        acc_name = self.acc_name
        date = self.date
        time = self.time
        notification_mapping = {
            "Logged_In": f"Your account {acc_num}, titled '{acc_name}', was Logged In at {time} on {date}.",
            "Registered": f"Your account {acc_num}, titled '{acc_name}', registered with CUAP at {time} on {date}.",
            "Bill_Paid": f"Your account {acc_num}, titled '{acc_name}', was used to pay a bill with Bill ID as {self.bill_id}. Transaction ID is {self.transaction_id}.",
            "Card_Used": f"Your account {acc_num}, titled '{acc_name}', was used for a card payment with your card ending with {self.card_num}. Transaction ID is {self.transaction_id}.",
            "Details_Edited": f"You edited some of your Account Details for your account {acc_num}, titled '{acc_name}'.",
            "PIN_Changed": f"You changed your PIN Code for your account {acc_num}, titled '{acc_name}'.",
            "Card_Status_Changed": f"Your card status was changed to {self.card_new_status} for your account {acc_num}, titled '{acc_name}'.",
            "Logged_Out": f"Your account {acc_num}, titled '{acc_name}', was Logged Out at {time} on {date}.",
            "Amount_Debited": f"Your account {acc_num}, titled '{acc_name}', was Debited with an amount of {self.amount}. Transaction ID is {self.transaction_id}.",
            "Amount_Credited": f"Your account {acc_num}, titled '{acc_name}', was Credited with an amount of {self.amount}. Transaction ID is {self.transaction_id}.",
            "Amount_Withdrawn": f"Your account {acc_num}, titled '{acc_name}', was Withdrawn with an amount of {self.amount}. Transaction ID is {self.transaction_id}.",
            "Amount_Deposited": f"Your account {acc_num}, titled '{acc_name}', was Deposited with an amount of {self.amount}.Transaction ID is {self.transaction_id}.",
        }
        return notification_mapping.get(self.notification_type, "Invalid Notification")

    def mark_as_read(self):
        """changes status from unread to read"""
        self.status = "Read"
        Notification.update_notification_on_file()

    @staticmethod
    def update_notification_on_file(updated_lines=None):
        """updates the notifications in the file"""
        with open("data/notifications.txt", "w", encoding="UTF-8") as file:
            if updated_lines:
                for line in updated_lines:
                    file.write(line if line.endswith("\n") else line + "\n")
            else:
                for n_id in Notification.notifications:
                    self = Notification.get_notification_by_id(n_id)
                    data = f"{self.acc_name} {self.acc_num} {self.date} {self.notification_id} {self.time} {self.notification_type} {self.card_num} {self.bill_id} {self.card_new_status} {self.amount} {self.transaction_id} {self.status}"
                    file.write(data + "\n")
