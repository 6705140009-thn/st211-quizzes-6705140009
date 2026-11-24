# Student: Thet Htoo Naing
# Student ID: 6705140009

def check_access(user_role, is_active):
    access = "denied"
    if user_role == "admin" and is_active:
        access = "granted"
    return access
