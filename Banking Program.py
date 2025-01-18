def show_balance(balance): 
  print(f"Your Balance is : {balance:.2f}") 

def deposit(): 
  amount = float(input("Enter an amount to be deposited : ")) 
  if amount < 0: 
         print("Amount can't be less than zero") 
            return 0 
   else : 
          return amount 

def withdrawal(balance): 
  amount = float(input("Enter an amount to be withdrawn : ")) 
  if amount < 0: 
    print("Amount can't be less than zero")) 
       return 0 
  elif amount > balance: 
     print("Amount can't be greater than balance ")
       return 0 
  else : 
       return amount 

def main(): 
  balance = 1000 
  is_running = True 

  while is_running:
        print("_______BANKING PROGRAM________") 
        print("1.Show Balance ") 
        print("2.Deposit ") 
        print("3.Withdrawal ")
        print("4.Exit") 

        choice = int(input("Enter a choice : ")) 

        if choice == 1: 
            show_balance(balance)
        elif choice == 2:
            balance += deposit() 
        elif choice == 3: 
            balance -= withdrawal(balance)
        elif choice == 4: 
            is_running = False 
        else : 
            print("Please enter a valid choice ") 

print("Have a Great Day! ") 

if __name__ == "__main__": 
    main()

  

      
