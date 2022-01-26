##################################################################
# Hello there! This gameis a simple stock trading                #
# desktop game. Its run entirely from the terminal to make       #
# things easier on me, allowing me to focus more on the math     #
# and order of operations since this is my first proper project  #
# in python.                                                     #
#                                                                #
# by James A. Metz, @distasteful-bear                            #
# Feel free to poke around in this program and shoot me an email #
# if you have an suggestions, but please respect that my time    #
# went into this project and all the original copyright is still #
# under my possesion. Cheers!                                    #
##################################################################




# All the currencies, stocks and their relevant information is stored in the following lists
# according to this ruberic: [Risk Level, Daily Prediction, User's Balance, Resulting Change of Day]
#  - Risk Level int(1,10) = this is an integer from 1 to 10 indicating how much a given currency is 
#       likely to change in a day.
#  - Daily Prediction float(-1,1) = This is a sort of tradjectory for the day that the user will see 
#       and help them make decisions.
#  - User's Balance float(0,~) = The current balance the user has, the user primarily interacts with 
#       it in integers but it runs better if under the hood its still a float
#  - Resulting Change of the Day Float(-1,1) = This is the percent change the currency has incurred 
#       in the previous day. 

from asyncore import loop
import random
import os
import time

os.system('clear')


# general purpose variables 
day_counter = 0
loop_counter = 0
net_worth = 1000
net_worth_yesterday = 0
pound_line = "###############################################"
change_in_nw = 0
start_day = True


# currencies, user should start with some dollars and everything is measured in dollars.
dollars = [3, 0.0, 1000.0, 0.0]
bitcoin = [7, 0.0, 0.0, 0.0]
gold    = [1, 0.0, 0.0, 0.0]
tmc = [6, 0.0, 0.0, 0.0]
bwc = [2, 0.0, 0.0, 0.0]
qbl = [5, 0.0, 0.0, 0.0]
ppb = [9, 0.0, 0.0, 0.0]
ubv = [4, 0.0, 0.0, 0.0]


# these lists are to aid in display and maniputating the currencies in bulk
# adding and removing from these lists will not break any mechanics (hopefully haha)
# but will just adjust the number of currencies.
all_currencies = [gold,bitcoin,tmc,bwc,qbl,ppb,ubv]
all_curr_display = ['Gold','Bitcoin','TMC','BWC','QBL','PPB','UBV']


# this function prints the standard balances screen. Used at the start of every day
# and after a transaction. 
def standard_print(day_counter,net_worth,dollars,all_currencies,all_curr_display,start_day):
    pound_line = "###############################################"
    print(pound_line, "\nWelcome to Day:",day_counter, "\n\n")
    print("Here is your portfolio: ")
    if (day_counter > 1):
        print("Change in Net Worth from Yesterday: %", change_in_nw)
    print("Net worth: $", net_worth)
    print("Dollars  = $",dollars[2])
    loop_counter = 0
    for i in all_currencies:   
        print(all_curr_display[loop_counter], " = $", i[2])
        loop_counter += 1
    loop_counter = 0

    # the first use of this def a day must actually calc these values, this just prints them
    if (start_day == False) :
        print("\nHere are the predictions for today:")
        for i in all_currencies:
            print(all_curr_display[loop_counter], " : ", int(i[1]*100), "%")
            loop_counter += 1
        loop_counter = 0
        



# this is the primary loop, be sure to change the game_over = true as needed
game_over = False
while game_over == False:


    # Game Ends at net worth of 100k
    if net_worth >= 10000:
        game_over = True


    # asks user if they want to run the tutorial, output is held in 'tutorial' boolean
    if day_counter == 0:
        os.system("clear")
        user_entry_valid = False
        while user_entry_valid == False:
            try:
                user_entry = str(input("\nWelcome! Would you like to run through the tutorial? \n(y -> begin tutorial, n -> start game)\n"))
                if user_entry == 'y':
                    os.system('clear')
                    tutorial = True
                    break    
                elif user_entry == 'n':
                    os.system('clear')
                    tutorial = False
                    break
                else :
                    print("Invlalid entry :/")
            except ValueError:
                print("Invalid entry :/")

    if tutorial == True:
        ## enter tutorial here lol 
        print("Placeholder for tutorial, best of luck chap this will take a bit :/")


    # intro to today text, day # and balances of usr portfolio etc.
    day_counter += 1
    start_day = True
    standard_print(day_counter,net_worth,dollars,all_currencies,all_curr_display,start_day)
    

    # predicitons for each day's varience - expected proformance 
    # the variance caluclation edits the [1] in all currency's lists 
    print("\nHere are the predictions for today:")
    for curr in all_currencies:
        generic = random.random()/10
        if random.random() < 0.5:
            generic = generic*-1
        curr[1] = generic
        display_curr = curr[1]*100
        display_curr = int(display_curr)
        print(all_curr_display[loop_counter], " : ", display_curr, "%")
        loop_counter += 1
    loop_counter = 0
    start_day = False


    # this is the transaction logic loop. Essentially for each of the currencies the user needs to either 
    # deposit or withdrawal. This is a general loop which will run for each of the currencies
    # the curr_counter keeps track of the number of times the loop has run to allow editing the list of the currency
    # while the curr variable is the string title of the current selected currency.
    user_trans_complete = False
    if user_trans_complete == False:

        curr_counter = 0
        for curr in all_curr_display:
            

            #reset display after last transaction
            if curr_counter >= 1:
                os.system('clear')
                standard_print(day_counter,net_worth,dollars,all_currencies,all_curr_display,start_day)


            valid_change = False
            while valid_change == False:
                try:
                    print("\n\nWould you like to make any changes to your", curr ,"balance? ")
                    user_change = int(input("(integers only)\n"))
                    if dollars[2] >= user_change:
                        if all_currencies[curr_counter][2] >= -user_change:
                            valid_charge = True
                            break
                        else:
                            print("\nNot enough", curr ,"to withdrawal :/ \nCurrent value of your", curr ,"is: $", all_currencies[curr_counter][2], )
                    else:
                        print("\nNot enough dollars to deposit :/ \nCurrent Balance is: ", dollars[2], "Dollars")
                except ValueError:
                    print("\nNot a valid entry, integers only.")

            all_currencies[curr_counter][2] = all_currencies[curr_counter][2] + user_change 
            dollars[2] = dollars[2] - user_change
            print("\n\n## Transaction was successful! ##   \n\nYour current balance in Dollars: $", dollars[2])
            print("Your current",curr, "Balance is $", all_currencies[curr_counter][2])
            
            # this allows the user to see 'transaction successful, for a second
            time.sleep(1)
            curr_counter += 1 


        user_entry_valid = False
        while user_entry_valid == False:
            try:
                user_entry = str(input("Are you finished making transactions for today? \n(y/n) \n"))
                if user_entry == 'y':
                    user_trans_complete = True
                    break    
                elif user_entry == 'n':
                    user_trans_complete = False
                    break
                else :
                    print("Invlalid entry :/")
            except ValueError:
                print("Invalid entry :/")

        



    # main logic for the change in value of all currencies
    # it follows this main action sequence:
    # variance number is input along with prediction, then the system runs random functions in magnitude approximating
    # the variance number and a small handful of times, starting with the prediction number. 
    curr_counter = 0
    os.system('clear')
    for curr in all_curr_display:
        # these are somewhat redundant but they help with readability in the algorithm.
        curr_variance = all_currencies[curr_counter][0]
        curr_prediction = all_currencies[curr_counter][1]
        curr_balance = all_currencies[curr_counter][2]
        curr_change = all_currencies[curr_counter][3]


        # it will run more cycles direcly in proportion to the variance score, then adjust the output 
        # to be more or less in magnitude by multiplying the (variance/5) with the random 
        print("Market Movements of ", curr)
        for cycles in range(0,curr_variance):
            cycle_change = (random.random()/100)*(curr_variance/5)
            if random.random() < 0.5:
                cycle_change = cycle_change*-1
            curr_prediction = curr_prediction + cycle_change
            
            # @testing
            
            print("%", int(curr_prediction*100))

        # each cycle updates the 'predicion' then the last cycle is the result of our random algorithm
        # this then is used ot find the change from the day, then adjusts the user's balance accordingly.
        curr_change = curr_prediction
        curr_balance = int(curr_balance + (curr_balance*curr_change))

        # this has to be included to remedy the variables we made for clarity.
        all_currencies[curr_counter][0] = curr_variance
        all_currencies[curr_counter][1] = curr_prediction
        all_currencies[curr_counter][2] = curr_balance
        all_currencies[curr_counter][3] = curr_change
    

        curr_counter += 1


    # collects net worth data from the day
    net_worth_yesterday = net_worth    
    curr_counter = 0
    for all in all_curr_display:
        if (curr_counter ==0):
            net_worth = 0
        net_worth = net_worth + all_currencies[curr_counter][2]
        curr_counter += 1
    change_in_nw = int((net_worth - net_worth_yesterday)/(net_worth_yesterday)*100)


    # dialog asking user to start the next day or quit the game
    user_entry_valid = False
    while user_entry_valid == False:
        try:
            user_entry = str(input("\nWould you like to continue to the next day? \n(y -> continue, n -> quit game)\n"))
            if user_entry == 'y':
                os.system('clear')
                break    
            elif user_entry == 'n':
                os.system('clear')
                game_over = True
                break
            else :
                print("Invlalid entry :/")
        except ValueError:
            print("Invalid entry :/")
        
    


