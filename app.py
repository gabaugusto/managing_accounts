import pickle 
import os
import pathlib

class Account:
    accNo = 0 
    name = ''
    balance = 0
    type = ''

    def createAccount(self):
        self.accNo = int(input('Enter the new account Number:'))
        self.name = input('Enter Holder Name:')  
        self.type = input('C/S?:') 
        self.balance = input('Enter the initial balance:')
    
    def showAccount(self):
        print('Account Number: ', self.accNo)
        print('Account Holder Name: ', self.name)
        print('Account Type: ', self.type)
        print('Balance: ', self.balance)

    def modifyAccount(self):
        print('Account Number: ', self.accNo)
        self.name = input('Update Account Holder Name :')
        self.type = input('Update Account Type :')
        self.balance = input('Modify balance :')

    def depositAmout(self, amount):
        self.balance += amount

    def withdrawAmout(self, amount):
        self.balance -= amount

    def report(self):
        print(self.accNo, ' \t| ', self.name, ' \t| ', self.type, ' \t| ', self.balance )

    def getAccountNo(self):
        return self.accNo

    def getAccountHolderName(self):
        return self.name

    def getAccountGetType(self):
        return self.type

    def getBalance(self):
        return self.balance

def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)

def displayAll():
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", 'rb')
        mylist = pickle.load(infile)
        for item in mylist:
            print(item.accNo, " \t| ", item.name, " \t| ", item.type, " \t| ", item.balance) 
        infile.close()
    else:
        print('No records to display.')
        
def displaySp(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", 'rb')
        mylist = pickle.load(infile)
        infile.close()
        global found 
        found = False
        for item in mylist:
            if item.accNo == num:
                print('Your account Balance is:', item.balance)
                found = True

    else:
        print('No records to search!')
    
    if not found:
        print('No existing record with this number')

def depositAndWithdraw(num1, num2):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", 'rb')
        mylist = pickle.load(infile)
        infile.close()   
        os.remove('accounts.data')
        for item in mylist:
            if item.accNo == num1:
                balance = int(item.balance)
                if num2 == 1:
                    amount = int(input('Enter the amout to deposit:'))
                    balance += amount
                    item.balance = balance
                    print('Deposit was a sucess!')
                elif num2 == 2:
                    amount = int(input('Enter the amount to withdraw: '))
                    if amount <= int(item.balance):
                        balance -= amount
                        item.balance = balance
                        print('Withdraw was a sucess!')
                    else: 
                        print('You cannot withdraw. ')
    else: 
        print('No records to search')

    outfile = open('newaccount.data', 'wb') 
    pickle.dump(mylist, outfile)
    outfile.close()       
    os.rename('newaccount.data','accounts.data')

def deleteAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", 'rb')
        oldlist = pickle.load(infile)
        infile.close()  
        newlist = []
        for item in oldlist:
            if item.accNo != num:
                newlist.append(item)
        os.remove('accounts.data')
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')

def modifyAccount(num):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", 'rb')
        oldlist = pickle.load(infile)
        infile.close()  
        os.remove('accounts.data')
        for item in oldlist:
            if item.accNo == num:
                item.name = input('Enter the account holder name: ')
                item.type = input('Enter the account type: ')
                item.balance = int(input('Enter the amount: '))
     
        outfile = open('newaccounts.data', 'wb')
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename('newaccounts.data', 'accounts.data')                

def writeAccountsFile(account):
    file = pathlib.Path("accounts.data")
    if file.exists():
        infile = open("accounts.data", 'rb')
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()  
        os.remove('accounts.data')
    else:
        oldlist = [account]
    outfile = open('newaccounts.data', 'wb')
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename('newaccounts.data', 'accounts.data')         

def opening():
    print('\t\t\t\t\t***********************') 
    print('\t\t\t\t\t Python Bank') 
    print('\t\t\t\t\t***********************') 

    while key != 8:
        print('\tMain Menu')
        print('\t1. New Account')
        print('\t2. Deposit Amount')
        print('\t3. Withdraw Amount')
        print('\t4. Balance')
        print('\t5. All Accounts List')
        print('\t6. Close an Account')
        print('\t7. Modify an Account')
        print('\t8. Exit')
        print('\tSelect your option (1-8)')
        key = input()

        if key == '1':
            writeAccount()
        elif key == '2':
            num = int(input('Enter the account number:' ))
            depositAndWithdraw(num, 1)
        elif key == '3':
            num = int(input('Enter the account number:' ))
            depositAndWithdraw(num, 2)   
        elif key == '4':
            num = int(input('Enter the account number:' ))
            displaySp(num)     
        elif key == '5':
            displayAll()  
        elif key == '6':
            num = int(input('Enter the account number:' ))
            deleteAccount(num)       
        elif key == '7':
            num = int(input('Enter the account number:' ))
            modifyAccount(num)  
        elif key == '8':
            print('\tThanks for using the system.')
            break
        else:
            print('Invalid choice')

# Definitions #
key = ''
num = 0
found = False

# Opening #
opening()        