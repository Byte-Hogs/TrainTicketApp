from re import A
import user
import logging

logger = logging.getLogger("Logging system for e-wallet")
logger.propagate = False
logger.setLevel(logging.INFO)
if not logger.handlers:
    fh = logging.FileHandler(filename='history.log')
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

class wallet():

    def __init__(self) -> None:
        self.__balance = 0
        self.__thres = 100000

    def withdraw(self, amount : int) -> int:
        if amount > self.__balance:
            logger.info("Amount withdrawn from wallet:", amount)
            self.__balance -= amount
            logger.info('Existing wallet balance:', self.__balance)
            flag = 1
        else:
            logger.warning('Failed to deduct amount due to In-sufficient balance!')
            #print("In-sufficient balance")
            flag = -1

        return flag

    def deposit(self, amount : int) -> int:
        if (amount + self.__balance) > self.__thres:
            logger.warning('Wallet limit exceeded')
            #print("Exceeding wallet limit!")
            flag = -1
        else:
            logger.info('Amount added to wallet:', amount)
            self.__balance += amount
            logger.info('Existing wallet balance:', self.__balance)
            flag = 1
        
        return flag

    def operation(self, op : int):
        amount = int(input())

        if op == 1:
            f = self.withdraw(amount)
            if f != 1:
                print()
        
        elif op == 2:
            f = self.deposit(amount)

        else:
            print("Invalid operation!")
            exit(0)
