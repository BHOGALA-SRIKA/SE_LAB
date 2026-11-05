
"""
Food Delivery Order Queue Manager.

Manages food orders, delivery statuses, daily revenue,
menu configuration, and JSON-based order backups.
"""

import json
from datetime import datetime

# Default configuration
DEFAULT_MENU = {
    "pizza": 250,
    "burger": 150,
    "fries": 90,
    "coke": 40,
}

DEFAULT_MENU_FILE = "menu.json"
DEFAULT_BACKUP_FILE = "orders.json"

VALID_STATUSES = (
    "placed",
    "cooking",
    "out_for_delivery",
    "delivered",
)

# Global application state
orders = {}
menu = {}


def create_order(customer, items, order_history=None):
    """Create a food order and return its assigned order ID."""
    if order_history is None:
        order_history = []

    unknown_items = [item for item in items if item not in menu]

    if unknown_items:
        raise ValueError(
            f"Unknown menu items: {', '.join(unknown_items)}"
        )

    order_id = max(orders, default=0) + 1
    total = sum(menu[item] for item in items)

    orders[order_id] = {
        "customer": customer,
        "items": items,
        "total": total,
        "status": "placed",
    }

    order_history.append(order_id)
    return order_id


def update_order_status(order_id, status):
    """Update an order only when its ID and status are valid."""
    if order_id not in orders:
        return False

    if status not in VALID_STATUSES:
        return False

    orders[order_id]["status"] = status
    return True


def read_menu_config(file=DEFAULT_MENU_FILE):
    """Load the menu from JSON or use the default menu."""
    try:
        with open(file, "r", encoding="utf-8") as menu_file:
            loaded_menu = json.load(menu_file)

        if not isinstance(loaded_menu, dict):
            raise ValueError("Menu configuration must be a JSON object.")

        if not all(
            isinstance(price, (int, float)) and price >= 0
            for price in loaded_menu.values()
        ):
            raise ValueError("Menu prices must be non-negative numbers.")

        menu.clear()
        menu.update(loaded_menu)

    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        menu.clear()
        menu.update(DEFAULT_MENU)


def daily_revenue():
    """Calculate revenue from all delivered orders."""
    return sum(
        order["total"]
        for order in orders.values()
        if order["status"] == "delivered"
    )


def backup_orders(file=DEFAULT_BACKUP_FILE):
    """Save all orders to a JSON backup file."""
    with open(file, "w", encoding="utf-8") as backup_file:
        json.dump(orders, backup_file, indent=4)


def restore_orders(file=DEFAULT_BACKUP_FILE):
    """Restore orders from JSON and convert IDs back to integers."""
    with open(file, "r", encoding="utf-8") as backup_file:
        restored_orders = json.load(backup_file)

    orders.clear()
    orders.update({
        int(order_id): order
        for order_id, order in restored_orders.items()
    })


def print_queue():
    """Display the current order queue."""
    print(f"Order queue at {datetime.now()}")

    for order_id, order in orders.items():
        print(
            order_id,
            order["customer"],
            order["status"],
            order["total"],
        )


def main():
    """Run the food delivery order management demonstration."""
    read_menu_config()

    first_order = create_order("Asha", ["pizza", "coke"])

    try:
        create_order("Ravi", ["burger", "sushi"])
    except ValueError as error:
        print(f"Order rejected: {error}")

    second_order = create_order("Ravi", ["burger"])
    third_order = create_order("Guest", ["fries"])

    update_order_status(first_order, "delivered")

    if not update_order_status(second_order, "teleported"):
        print("Invalid delivery status rejected.")

    if not update_order_status(42, "delivered"):
        print("Unknown order ID rejected.")

    update_order_status(third_order, "delivered")

    print("Revenue today:", daily_revenue())

    backup_orders()
    restore_orders()
    print_queue()


if __name__ == "__main__":
    main()
