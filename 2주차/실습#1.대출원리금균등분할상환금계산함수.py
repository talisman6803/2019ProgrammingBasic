def monthlyPaymentPlan(principal, interest, year):
    d=((1+interest/1200)**(year*12)*principal*interest/1200)/((1+interest/1200)**(year*12)-1)
    return round(d)
print(monthlyPaymentPlan(10000000, 2.8, 4))
