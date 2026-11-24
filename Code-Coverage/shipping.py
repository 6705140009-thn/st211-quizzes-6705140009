# Student: Thet Htoo Naing
# Student ID: 6705140009

def calculate_shipping(weight, express=False):
    if weight <= 0:
        raise ValueError("Weight must be positive")
    base = weight * 2
    if express:
        base = base * 1.5
    if weight > 100:
        base = base + 50  # heavy surcharge
    return base

def free_shipping_eligible(order_total):
    return order_total >= 1000
