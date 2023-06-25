# If user enters a number, and it equals the lucky number, user wins 3 million dollars,
# else he keeps trying for 2 more times. For each trial, the lucky number updates
# But if the user hits jackpot on any trial, the programs ends.

print("This is a guess game with a winning price of $3,000,000 should you guess the right winning number.\n"
      "You only have 3 chances before the game is terminated. \n"
      "Good luck to you.")
print("-------------------------------------------------------------")
max_trial = 3 #number of trial in the game
user_name = input("What is your first name?\n") # user enters their first name
lucky_num = len(user_name)*9+3  # calculation of lucky number with character length of username

while max_trial > 0: # this repeat the trial for 3 times as long as trial time is greater than 0 (3 times completed)
    lucky_num += 21  # lucky number is incremented at the next trial
    user_num = input("Enter a number for jackpot\n")  # user enters guess number
    try:
        guess_num = int(user_num)  # converting user guess input number (string) to integer
    except Exception as ex:
        if ex:
            print("Invalid entry!")
            print(ex)
            quit()
    if guess_num == lucky_num: # logic for jackpot
        print("Bingo! " + user_name + ", You just won a jackpot of $3,000,000\n"
                                      "We shall wire transfer your money to you right away.")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++") # user bank details collected
        user_bank = input("Enter your Bank name\n")
        user_account_num = input("Enter account number\n")
        user_account_name = input("Enter Full bank name\n")
        user_country = input("Enter bank country\n")
        print("processing.....")
        print("*****************************************************************")
        print('Payment successfully processed with the following details:\n'
        'Amount: $3,000,000.00\n'
        "Bank: " + user_bank + '\n'
        "Account Name: "+ user_account_name + '\n'
        "Country: " + user_country)
        print("*****************************************************************")
        print("Money should arrive in your account in 48hrs. Consult with your bank.\n"
              "Once again,congratulations to you, " + user_account_name)
        break
    else:
        print("Thank you, " + user_name + ", but you missed. Your lucky number on the previous attempt was "
              + str(lucky_num) + ". Please, try agian.")
        max_trial -= 1
        if max_trial == 1:
            print("your have " + str(max_trial) + " attempt(s) remaining (your very last attempt)")
        else:
            print("your have " + str(max_trial) + " attempt(s) remaining")
if max_trial == 0:
    print("*****************************************************************")
    print("Dear " + user_name + ", your chances are over, and we regret that you lost. Try again.")
