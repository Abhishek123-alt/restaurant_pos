# Python Restaurant Point of Sale (POS) System

## Overview

The Python Restaurant POS System is designed to streamline restaurant operations by managing customer orders and
facilitating interactions with third-party POS systems. This implementation emphasizes object-oriented programming
principles such as abstraction, inheritance, and polymorphism while incorporating an efficient logging mechanism for
tracking system events.

## Key Features

- **Object-Oriented Design**: Utilizes core OOP principles to structure the system effectively.
- **Third-Party API Simulation**: Simulates interactions with POS systems like Toast and Square for processing orders and payments.
- **Logging Mechanism**: Includes automatic log management, daily log rotation, and cleanup of logs older than 5 days.
- **Core Components**: Manages orders, products, and ingredients with a clear hierarchy of classes.

## System Components

### 1. Log Management

- **Log Directory**: All log files are stored in a dedicated `logs` directory.
- **Log Retention**: Logs are retained for a maximum of 5 days; older logs are automatically deleted.
- **Log Rotation**: The system rotates logs daily, renaming `app.log` to include the date and creating a new log file for the current day.

### 2. Core Classes

- **Order Class**: Represents different types of customer orders (e.g., dine-in, takeout, delivery).
- **Product Class**: Represents items available on the menu (e.g., pizzas, drinks).
- **Ingredient Class**: Represents ingredients used in products (e.g., cheese, tomato).

### 3. Third-Party POS API Simulation

- **ToastPOS Class**: Simulates the Toast POS system API.
- **SquarePOS Class**: Simulates the Square POS system API.
- Each class provides methods for sending orders and processing payments, with randomized outcomes to simulate success or failure.

### 4. Polymorphism

- The `process_order_through_pos()` function allows interaction with different POS systems using a common interface, demonstrating polymorphism. This flexibility enables easy addition of new POS systems in the future.

## Usage Instructions
s
1. **Clone the Repository**:
   ```bash
       git clone https://github.com/Abhishek123-alt/restaurant_pos
