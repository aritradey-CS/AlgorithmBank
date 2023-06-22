#Currency_Convert

def inr_to_usd(amount):
    exchange_rate = 0.014  # 1 INR = 0.014 USD
    return amount * exchange_rate

def usd_to_inr(amount):
    exchange_rate = 71.43  # 1 USD = 71.43 INR
    return amount * exchange_rate

# Get conversion direction from the user
conversion_direction = input("Enter '1' to convert INR to USD, or '2' to convert USD to INR: ")

if conversion_direction == '1':
    # Convert INR to USD
    inr_amount = float(input("Enter the amount in Indian Rupees (INR): "))
    usd_amount = inr_to_usd(inr_amount)
    print(f"{inr_amount} INR is equal to {usd_amount} USD.")
elif conversion_direction == '2':
    # Convert USD to INR
    usd_amount = float(input("Enter the amount in US Dollars (USD): "))
    inr_amount = usd_to_inr(usd_amount)
    print(f"{usd_amount} USD is equal to {inr_amount} INR.")
else:
    print("Invalid input. Please enter '1' or '2' for conversion direction.")
