valid_users = [
    {"ip_address": "194.24.31.56", "password": "Mike@123"}
]

def authenticate_user(ip_address, password):
    for user in valid_users:
        if user["ip_address"] == ip_address and user["password"] == password:
            return True
    return False

def main():
    ip_address = input("Enter IP address: ")
    password = input("Enter password: ")

    if authenticate_user(ip_address, password):
        print("Valid user")
    else:
        print("Invalid user")

if __name__ == "__main__":
    main()