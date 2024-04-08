class ATM:
    def __init__(self):
        self.__pin = ""
        self.__balance = 0

        self.__menu()

    def __menu(self):
        user_input = input('''
                1. CREATE PIN, ENTER 1
                2. DEPOSIT CASE, ENTER 2
                3. WITHDRAW CASE, ENTER 3
                4. CHECK BELANCE, ENTER 4
                5. EXIT, ENTER 5                                 
                        ''')
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("THANKS FOR USING OUR SERVICE.")
        else:
            print("INVELID OPTION, PLEASE CHOOSE FROM MENU")

    def create_pin(self):
        self.__pin = input("ENTER YOUR PIN: ")
        print("PIN SAVE SUCCESSFULLY.")
        
        self.__menu()

    
    def deposit(self):
        temp = input("ENTER YOUR PIN: ")
        if temp == self.__pin:
            amount = int(input("ENTER THE AMOUNT: "))
            self.__balance = self.__balance + amount
            print("DEPOSIT SUCCESSFULLY.")
        else:
            print("INVELID PIN.")
        
        self.__menu()


    def withdraw(self):
        temp = input("ENTER YOUR PIN: ")
        if temp == self.__pin:
            amount = int(input("ENTER THE AMOUNT: "))
            if amount <= self.__balance:
                self.__balance = self.__balance - amount
                print("WITHDRAW SUCCESSFULLY.")
            else:
                print("NOT SUFFICENT BALANCE.")
        else:
            print("INVELID PIN.")
            
        self.__menu()

    def check_balance(self):
        temp = input("ENTER YOUR PIN: ")
        if temp == self.__pin:
            print("YOUR BALANCE IS: ", self.__balance)
        else:
            print("INVELID PIN.")
            
        self.__menu()