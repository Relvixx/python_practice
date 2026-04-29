class My_Account:
	def __init__(self, account_holder, account_balence):
		self.account_holder = account_holder
		self.account_balence = account_balence

	def deposit(self,amount):
		self.account_balence += amount
		print(f"hello, {self.account_holder} your updated account balance is {self.account_balence}")

	def withdraw(self,amount):
		if(amount > self.account_balence):
			print("you not have enough money")
		else:
			self.account_balence -= amount
			print(f"hello, {self.account_holder} your remaining account balance is {self.account_balence}")

pr1 = My_Account("John", 10000)

pr1.deposit(500000)
pr1.withdraw(20000)
