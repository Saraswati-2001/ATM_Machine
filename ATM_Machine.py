# ATM Machine Simulation

# User data storage
user_data = {
    'pin': '1234',
    'balance': 1000.0,
    'transactions': []
}

# Function to display the main menu
def display_menu():
    print("\n--- ATM Machine ---")
    print("1. Account Balance Inquiry")
    print("2. Cash Withdrawal")
    print("3. Cash Deposit")
    print("4. PIN Change")
    print("5. Transaction History")
    print("6. Exit")

# Function to check the account balance
def check_balance():
    print(f"\nYour current balance is: ${user_data['balance']:.2f}")

# Function to withdraw cash
def cash_withdrawal():
    amount = float(input("Enter amount to withdraw: $"))
    if amount > 0 and amount <= user_data['balance']:
        user_data['balance'] -= amount
        user_data['transactions'].append(f"Withdrawn: ${amount:.2f}")
        print(f"\nWithdrawal successful. Your new balance is: ${user_data['balance']:.2f}")
    else:
        print("\nInsufficient balance or invalid amount.")

# Function to deposit cash
def cash_deposit():
    amount = float(input("Enter amount to deposit: $"))
    if amount > 0:
        user_data['balance'] += amount
        user_data['transactions'].append(f"Deposited: ${amount:.2f}")
        print(f"\nDeposit successful. Your new balance is: ${user_data['balance']:.2f}")
    else:
        print("\nInvalid deposit amount.")

# Function to change PIN
def change_pin():
    current_pin = input("Enter current PIN: ")
    if current_pin == user_data['pin']:
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin:
            user_data['pin'] = new_pin
            print("\nPIN changed successfully.")
        else:
            print("\nNew PINs do not match.")
    else:
        print("\nIncorrect current PIN.")

# Function to display transaction history
def transaction_history():
    print("\n--- Transaction History ---")
    if user_data['transactions']:
        for transaction in user_data['transactions']:
            print(transaction)
    else:
        print("No transactions yet.")

# Function to validate user PIN before granting access
def pin_validation():
    attempts = 3
    while attempts > 0:
        pin = input("Enter your PIN: ")
        if pin == user_data['pin']:
            print("\nAccess Granted.")
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. {attempts} attempts left.")
    print("\nAccount Locked. Too many incorrect attempts.")
    return False

# Main program loop
def atm_simulation():
    if pin_validation():
        while True:
            display_menu()
            choice = input("\nSelect an option (1-6): ")
            if choice == '1':
                check_balance()
            elif choice == '2':
                cash_withdrawal()
            elif choice == '3':
                cash_deposit()
            elif choice == '4':
                change_pin()
            elif choice == '5':
                transaction_history()
            elif choice == '6':
                print("\nThank you for using the ATM. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")

# Run the ATM simulation
atm_simulation()
