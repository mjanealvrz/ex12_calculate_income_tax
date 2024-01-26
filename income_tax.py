#  Calculate income tax for the given income by adhering to the rules below
# Expected Output:
# For example, suppose the taxable income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.


# Pseudocode

# Set taxable income to variable
taxable_income = 45000

# Print the the given taxable income
print("Given taxable income is ", taxable_income)

# Create calculate income tax function with conditional statements
def calculate_income_tax(income):

    # Set the first  income tax payable
    first_income_tax = 10000

    # Set the second income tax payable
    second_income_tax = 20000
    
    # if income <= first income_tax then
    if income <= first_income_tax:
        # set income_amount  to income * 0
        income_amount = income * 0

        
    # else if taxable_income <=  second income_tax_payable then
        # set second_tax to income -10000
        # set tax_payable to second_tax * 10/100
    # else
        # first 10, 000, set tax_payable to 0
        # next 10,000 10% tax, set tax_payable to tax_payable + 10000 * 10/100
        # remaining 20% tax, SET tax_payable TO tax_payable + (income - 20000) * 20 / 100
# Print result



