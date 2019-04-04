def cheese_and_crackers(cheese_count, boxes_of_crackers): # defines and executes the variables
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for the party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:") # assigns numbers directly to variables
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:") # assigns values to each independent variable
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We even do math inside too:") # assigns number value through addition
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:") # combines the use of variables and math together
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)