# Author :  Harrison Toppen-Ryan
# Description :  Tip Calculator (HW 4), CSCI 141
# Date :  November 11th, 2020

# importing math for sqrt function later on 
import math 

# Asking for number of adults 
numAdults = int(input("How many adults? "))
# Asking for number of cildren 
numChildren = int(input("How many children? "))
# Asking for total coast 
totalCost = float(input("Total cost without tip? "))
# Asking for cheapest meal 
cheapMeal = float(input("Cheatpest meal? "))
# Asking for most expensive meal 
exMeal = float(input("Most expensive meal? "))
# Asking for number of sodas 
numSodas = int(input("How many sodas were consumed? "))

# Function for A 
def funcA():
    #variable A is the sum of number of adults to the power of 1.4 and the number of children to the power of 0.8
    A = (numAdults ** 1.4) + (numChildren ** 0.8)
    return A
   
# Function for B
def funcB():
    if cheapMeal < (exMeal / 2):
        # B is the most expenisve meal if half of the most expensive meal is still greater than the cheepest meal
        B = exMeal
        return B
    else:
        # if not, then B is the square root of the most expensive meal minus the cheapest meal 
        B = (math.sqrt(exMeal - cheapMeal))
        return B
    
# Function for C 
def funcC():
    # C is %10 of the toal cost if the number of sodas consumed is greater than the total number of people at the resturant 
    if numSodas > int(numAdults + numChildren):
        C = float(totalCost * 0.10)
        return C
    else: 
        #if not, C is %15 of the total cost
        C = float(totalCost * 0.15)
        return C
# CalcTip adding all functons together 
def calcTip():
    # all three functions combined 
    return funcA() + funcB() + funcC()
    
# main function    
def main():
    retTotal = calcTip()
    # round the answer to the nearest decimal places ( "%.2f" % is for trailing zeros)
    retTotal2 = "%.2f" % round(retTotal, 2)
    #dollar sign next to answer with no spaces 
    print("Required tip amount is $" + retTotal2)


# calling the main function
main()

