# Student: Thet Htoo Naing
# Student ID: 6705140009

def apply_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("Percent must be 0-100")
    return price * (1 - discount / 100)
