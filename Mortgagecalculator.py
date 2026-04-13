principal = int(input("Enter the loan amount: "))
annual_rate = int(input("Enter the annual interst rate in (%): "))
years = int(input("Enter the number of years: "))


monthly_rate = (annual_rate / 100)/12

months = years * 12

if monthly_rate ==0:
    monthly_payment = principal / months

else:
  
 numerator = monthly_rate *(1 + monthly_rate) ** months
 denominator = (1 + monthly_rate) ** months -1

monthly_payment = principal * (numerator / denominator)

print("Your monthly payment is: $", monthly_payment)
