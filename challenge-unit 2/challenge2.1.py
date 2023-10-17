class BankAccount:
  def __init__(self, account_number, account_holder_name, initial_balance=0):
      self.__account_number = account_number
      self.__account_holder_name = account_holder_name
      self.__account_balance = initial_balance

  def deposit(self, amount):
      if amount > 0:
          self.__account_balance += amount
          print(f"Deposited ${amount}. New balance: ${self.__account_balance:.2f}")
      else:
          print("Invalid deposit amount. Amount must be greater than 0.")

  def withdraw(self, amount):
      if 0 < amount <= self.__account_balance:
          self.__account_balance -= amount
          print(f"Withdrew ${amount}. New balance: ${self.__account_balance:.2f}")
      elif amount > self.__account_balance:
          print("Insufficient funds.")
      else:
          print("Invalid withdrawal amount. Amount must be greater than 0.")

  def display_balance(self):
      print(f"Account Holder: {self.__account_holder_name}")
      print(f"Account Number: {self.__account_number}")
      print(f"Account Balance: ${self.__account_balance:.2f}")

# Testing the BankAccount class
if __name__ == "__main__":
  # Creating a new account
  my_account = BankAccount("123456789", "santhosh", 1000)

  # Displaying initial balance
  my_account.display_balance()

  # Making a deposit
  my_account.deposit(500)

  # Making a withdrawal
  my_account.withdraw(200)

  # Trying to withdraw more than the balance
  my_account.withdraw(2000)

  # Displaying the updated balance
  my_account.display_balance()
