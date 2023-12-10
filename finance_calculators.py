#Capstone Project:
#Below is a program that allows the user to access two different financial calculators: 
#an investment calculator and a home loan repayment calculator.

import math

invest_options = '''investment - to calculate the amount of interest you'll earn on your investment
bond       - to calculate the amount you'll have to pay on a home loan'''
print(invest_options)

invest_choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower() 

if invest_choice == 'investment': #If 'investment' is chosen then below inputs requested.
    p = float(input('\nEnter the amount of your deposit: '))
    r = float(input('Enter your specific interest rate (exclude the symbol %): '))
    t = int(input('Enter your investment period in years: '))

    interest = input('''\nDo you want “simple” or “compound” interest? ''').lower()

    if interest == 'simple': #Calculates Simple interest if 'simple' chosen as input for 'interest'. 
        simple_i = p * (1 + ((r/100) * t)) #Simple interest Formula
        print(f'\nYour investment on {p:,.2f} deposit after {t} years at {r:.2f}% Simple interest rate would be {simple_i:,.2f}.')
    
    elif interest == 'compound': #Calculates Compound interest if 'compound' chosen as input for 'interest'. 
        compound_i = p * math.pow((1 + (r/100)), t) #Compound interest Formula
        print(f'\nYour investment on {p:,.2f} deposit after {t} years at {r:.2f}% Compound interest rate would be {compound_i:,.2f}.')
            
    else: 
        print('\nValid option not chosen. Please re-try.')
        #Shows above message when neither 'interest' options are chosen.

elif invest_choice == 'bond': #If 'bond' is chosen then below inputs requested.
    p = float(input('\nEnter the present value of your house: '))
    i = float(input('Enter your specific interest rate (exclude the symbol %): '))
    n = int(input('Enter your bond repayment period in months: '))

    r = (((i / 100)/12) * p) / (1 - (1 + ((i / 100)/12)) ** (-n)) #Bond repayment Formula
    print(f'\nYour monthly bond repayment on {p:,.2f} value of your house after {n} months at {i:.2f}% interest rate would be {r:,.2f}.')

else:
    print('\nValid option not chosen. Please re-try.') 
    #Shows above message when neither 'invest_choice' options are chosen.