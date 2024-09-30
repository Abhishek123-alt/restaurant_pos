import logging
import os
from datetime import datetime

# Log directory and retention settings
LOG_DIR = 'logs'
LOG_RETENTION_DAYS = 5
CURRENT_LOG = os.path.join(LOG_DIR, 'app.log')

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Function to rotate log files based on the current date
def rotate_logs():

    if os.path.exists(CURRENT_LOG):
        file_mod_time = datetime.fromtimestamp(os.path.getmtime(CURRENT_LOG))
        current_date = datetime.now().date()

        if file_mod_time.date() < current_date:
            previous_day = file_mod_time.strftime('%Y-%m-%d')
            previous_log = os.path.join(LOG_DIR, f"{previous_day}.log")
            os.rename(CURRENT_LOG, previous_log)
            logging.info(f"Rotated log: {CURRENT_LOG} -> {previous_log}")

    clean_old_logs()

# Function to delete logs older than the retention period
def clean_old_logs():
    now = datetime.now()
    for filename in os.listdir(LOG_DIR):
        file_path = os.path.join(LOG_DIR, filename)
        if os.path.isfile(file_path) and filename != 'app.log':
            try:
                file_date = datetime.strptime(filename.split('.')[0], '%Y-%m-%d')
            except ValueError:
                continue

            if (now - file_date).days > LOG_RETENTION_DAYS:
                os.remove(file_path)
                logging.info(f"Deleted old log file: {filename}")

rotate_logs()

# Configure logging to always write to 'app.log'
logging.basicConfig(filename=CURRENT_LOG,
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# Example code to simulate POS system
from abc import ABC, abstractmethod
import random


# 1. Abstract classes
class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass


class Product(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Ingredient(ABC):
    @abstractmethod
    def get_quantity(self):
        pass


class DineInOrder(Order):
    def process_order(self):
        result = "Processing dine-in order."
        logging.info(result)
        return result


class TakeoutOrder(Order):
    def process_order(self):
        result = "Processing takeout order."
        logging.info(result)
        return result


class Pizza(Product):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self):
        result = self.price
        logging.info(f"Price of {self.name}: ${result}")
        return result


class Cheese(Ingredient):
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_quantity(self):
        result = self.quantity
        logging.info(f"Quantity of {self.name}: {result}")
        return result


class ThirdPartyPOS(ABC):
    @abstractmethod
    def send_order(self, order):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass


# Helper function to simulate API responses
def simulate_api_response(success=True):
    if success:
        return {"status": 200, "message": "Success"}
    else:
        return {"status": 500, "message": "API error"}


class ToastPOS(ThirdPartyPOS):
    def send_order(self, order):
        logging.info("Sending order to Toast POS...")
        response = simulate_api_response(success=random.choice([True, False]))
        if response["status"] == 200:
            logging.info(f"Toast POS: {order.process_order()}")
            return response
        else:
            logging.error("Error while sending order to Toast POS: " + response["message"])
            raise Exception("Toast POS API Error: Failed to send order.")

    def process_payment(self, amount):
        logging.info(f"Processing payment of ${amount} via Toast POS...")
        response = simulate_api_response(success=random.choice([True, False]))
        if response["status"] == 200:
            logging.info(f"Toast POS: Payment of ${amount} processed successfully.")
            return response
        else:
            logging.error("Error while processing the payment in Toast POS: " + response["message"])
            raise Exception("Toast POS API Error: Failed to process payment.")


class SquarePOS(ThirdPartyPOS):
    def send_order(self, order):
        logging.info("Sending order to Square POS...")
        response = simulate_api_response(success=random.choice([True, False]))
        if response["status"] == 200:
            logging.info(f"Square POS: {order.process_order()}")
            return response
        else:
            logging.error("Error while sending order to Square POS: " + response["message"])
            raise Exception("Square POS API Error: Failed to send order.")

    def process_payment(self, amount):
        logging.info(f"Processing payment of ${amount} via Square POS...")
        response = simulate_api_response(success=random.choice([True, False]))
        if response["status"] == 200:
            logging.info(f"Square POS: Payment of ${amount} processed successfully.")
            return response
        else:
            logging.error("Error while processing the payment in Square POS:" + response["message"])
            raise Exception("Square POS API Error: Failed to process payment.")


# Interact with different POS systems uniformly
def process_order_through_pos(pos_system, order, product):
    try:
        send_order_response = pos_system.send_order(order)
        logging.info(f"Order Response: {send_order_response}")

        payment_response = pos_system.process_payment(product.get_price())
        logging.info(f"Payment Response: {payment_response}")

        return {"order_response": send_order_response, "payment_response": payment_response}
    except Exception as e:
        logging.error(f"Error during POS operation: {e}")
        return {"error": str(e)}


# Example Usage
if __name__ == "__main__":
    # Create orders, products, and ingredients
    order1 = DineInOrder()
    product1 = Pizza("Margherita Pizza", 15.99)

    toast_pos = ToastPOS()
    toast_result = process_order_through_pos(toast_pos, order1, product1)
    print(toast_result)

    square_pos = SquarePOS()
    square_result = process_order_through_pos(square_pos, order1, product1)
    print(square_result)
