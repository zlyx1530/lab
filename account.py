class Account:
    def __init__(self, name: str) -> None:
        """
        initilize function. Sets 2 private
         params: name to str and sets account_balance to 0
        :param name: passed name of account
        """
        self.__account_name: str = name
        self.__account_balance: float = 0

    def deposit(self, amount: float) -> bool:
        """
        This function increments the account balance by the specified amount.
        :param amount: The amount the total balance should be incremented by. Non-negative value that isn't 0
        :return: boolean value of true or false based on success of the addition to account
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        This function decrements the account balance by the specified amount.
        :param amount: The amount the total balance should be decremented by. Non-negative value that isn't 0
        :return: boolean value of true or false based on success of the subtraction to account
        """
        if amount > self.__account_balance or amount <= 0:
            return False
        else:
            self.__account_balance += amount
            return True

    def get_balance(self) -> float:
        return self.__account_balance

    def get_name(self) -> str:
        return self.__account_name