import random
numbers = list(range(1, 51))

def get_numbers_ticket():
    ticket_numbers = random.sample(numbers, 5)
    return sorted(ticket_numbers)

print(get_numbers_ticket())
