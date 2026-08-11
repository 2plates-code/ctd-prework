# this code is based off of arbitrary personal finance goals
# I have in regards to saving for and planning a car purchase

# The program asks for several factors including the trade-in value of
# the current car, the purchase price of the desired car,
# the savings amount per month, and how many months that amount will be saved.

# The ideal goal is to have enough to pay off the car entirely

# assumptions and limitations: starting off with zero savings
# and NOT accounting for any inflation, interest rates, etc

trade_in = input("Do you have a car to trade-in? (Y/N): ")

if trade_in == "Y" or trade_in == "Yes" or trade_in == "yes" or trade_in == "y":
    trade_in = input("How much is the trade-in worth? ")
elif trade_in == "N" or trade_in == "No" or trade_in == "no" or trade_in == "n":
    trade_in = int(0)
    print ("Proceed to the next question.")
else:
    print ("invalid answer")
    trade_in = input("Do you have a car to trade-in? (Y/N): ")


car_price = int(input("What is the price of your next desired car (in USD)? "))
savings = int(input("How much can you save per month (in USD)? "))
time = int(input("How many months can you save for (within 60 months)? "))

ratio = float((savings * time + int(trade_in))/ car_price)

if ratio >= 1.0:
    print ("Great news! You will have saved enough "
    + "to buy your car outright without an auto loan!")
elif float((savings * time + int(trade_in))/ car_price) >= 0.5 < 1.0:
    print ("Good job! You are saving enough to cover at least half of your "
    + "car purchase as a down payment, "
    + "thus minimizing the amount you will have to finance.")
else:
    print ("You have only saved up " + str(100 * ratio)
    + " percent of your planned car purchase. "
    + "I recommend saving at least half the amount "
    + "of the car price as a down payment.")
