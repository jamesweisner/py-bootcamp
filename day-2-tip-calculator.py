print('Welcome to the evil tip calculator!')

while True:
    try:
        bill_amount = float(input('What was the bill total, before tip? $'))
        assert bill_amount > 0
        break
    except:
        print('Invalid amount! Must be a positive number.')

while True:
    try:
        tip_percent = input('What percent tip would you like to give? (20%) ')
        tip_percent = int(tip_percent.strip() or 20)
        assert tip_percent > 0
        assert tip_percent <= 50
        break
    except:
        print('Invalid tip percent! Must be integer between 1 and 50')

while True:
    try:
        party_size = int(input('How many people to split the bill? '))
        assert party_size > 1
        break
    except:
        print('Invalid party size! Must be a positive integer.')

while True:
    try:
        sucker_tax = input('How big of suckers are these chumps? (10%) ')
        sucker_tax = int(sucker_tax.strip() or 10)
        assert tip_percent > 0
        assert tip_percent <= 50
        break
    except:
        print('Invalid sucker tax! Must be integer between 1 and 50')

total = bill_amount * (1.0 + tip_percent / 100.0)

sucker_price = round((1.0 + sucker_tax / 100.0) * total / party_size, 2)
my_price = round(sucker_price - (sucker_tax / 100.0) * total, 2)

print(f'I will only pay: ${my_price}')
print(f'But everyone else pays: ${sucker_price}')
