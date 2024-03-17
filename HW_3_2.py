import random
def get_numbers_ticket(min:int, max:int ,quantity:int) -> list:
    lot_number = list()
    for i in range(min,max):
        lot_number.append(i)
    lot_choices = random.sample(lot_number,k=quantity)
    return lot_choices

incur_input = True
while incur_input:
    try:
        min_str, max_str, quantity_str = input("Input min, max and qty: ").split()
        min_value = int(min_str)
        max_value = int(max_str)
        quantity = int(quantity_str)  
        if 1<=min_value<max_value and max_value <=1000 and quantity> 0 and quantity<=(max_value-min_value):
            incur_input = False
        else: 
            raise ValueError
    except ValueError:
        print("Incorect data input. Use positive integer numbers, min should be less than max, quantity more than 0")
        incur_input = True

lottery_numbers = get_numbers_ticket(min_value,max_value,quantity)

print(f"Your numbers is: {lottery_numbers}")