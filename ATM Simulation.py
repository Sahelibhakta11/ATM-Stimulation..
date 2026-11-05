import math

class ATM:
    MENU_OPTIONS = ("1", "2", "3", "4")
    MENU_LABELS = ("Check balance", "Deposit money", "Withdraw money", "Exit")

    def __init__(self, balance: float, pin: str = "1234") -> None:
        if not math.isfinite(balance) or balance < 0:
            raise ValueError("The starting balance must be a non-negative number.")
        if not pin or not all(character.isdigit() for character in pin):
            raise ValueError("The PIN must contain only digits.")

        self.__balance = balance
        self.__pin = pin

    def authenticate(self) -> bool:
        attempts = (0)
        while attempts < 3:
            entered_pin = input("Enter your ATM PIN: ")
            if all(character.isdigit() for character in entered_pin) and entered_pin == self.__pin:
                print("Access granted.")
                return True

            attempts += 1
            print("Incorrect PIN.")

        print("Access denied. Too many incorrect attempts.")
        return False

    def display_balance(self):
        print(f"Current balance: {self.__balance:.2f}")

    def deposit(self, amount: float):
        if not math.isfinite(amount) or amount <= 0:
            raise ValueError("The deposit amount must be a positive number.")

        self.__balance += amount
        print(f"Deposited: {amount:.2f}")
        self.display_balance()

    def withdraw(self, amount: float):
        if not math.isfinite(amount) or amount <= 0:
            raise ValueError("The withdrawal amount must be a positive number.")
        if amount > self.__balance:
            print(f"Insufficient funds. Current balance: {self.__balance:.2f}")
            return

        self.__balance -= amount
        print(f"Withdrawn: {amount:.2f}")
        self.display_balance()

    @staticmethod
    def _read_amount(prompt: str):
        try:
            amount = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            return None

        if not math.isfinite(amount) or amount <= 0:
            print("Please enter an amount greater than zero.")
            return None
        return amount

    def run(self):
        if not self.authenticate():
            return

        while True:
            print("\nATM Menu:")
            for option, label in zip(self.MENU_OPTIONS, self.MENU_LABELS):
                print(f"{option}. {label}")

            choice = input("Enter your choice (1-4): ").strip()
            if choice not in self.MENU_OPTIONS:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
            elif choice == "1":
                self.display_balance()
            elif choice == "2":
                amount = self._read_amount("Enter amount to deposit: ")
                if amount is not None:
                    self.deposit(amount)
            elif choice == "3":
                amount = self._read_amount("Enter amount to withdraw: ")
                if amount is not None:
                    self.withdraw(amount)
            else:
                print("Thank you for using the ATM.")
                return


if __name__ == "__main__":
    ATM(balance=1000000, pin="1234").run()