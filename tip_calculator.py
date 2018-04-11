# Create a program that lets the user input their total bill at a restaurant, and returns the total cost of the bill including a tip.

print('please input your bill')
bill = int(input())
print('was the service great, good or bad? Type "good" for good, "awesome" for great and "meh" for bad')
reply1 = input()
if reply1 == 'good':
    tip = (bill*0.15)+bill
    print('your bill inclusive of 15% tip is ' + str(tip))
elif reply1 == 'awesome':
    tip = (bill*0.20)+bill
    print('your bill inclusive of 20% tip is ' + str(tip))        
else:
    print('there is no tip for bad services. your bill remains ' + str(bill))