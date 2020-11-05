#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to tht tip calculator")

bill = float(input("What was the total bill? $"))

tip = int(input("What percentage would you like to give? 10, 12 or 15: "))

people = int(input("how many people to split the bill? "))

tip_as_percent = tip/100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill/people

final_amount = round(bill_per_person, 2)

message = f"Each person is to pay: ${final_amount}, thank you."

print(message)
