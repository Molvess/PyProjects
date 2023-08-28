#PAYMENT

produ = float(input('What is the price of the product you want to buy? R$'))
print('Your product is {:.2f} R$, with the purchase of this product in cash you can get a discount of up to 15% off'.format(produ))
print('If you pay in installments the value will be increased by 10%, (note: you can pay in up to 6 installments')
parc = produ + (produ * 10 / 100)
form = input('do you want (pay in installments) or pay (in cash)?')
if form == 'in cash':
    print('Your price is R$'.format(produ - (produ * 15 / 100)))
    
if form == 'pay in installments':
    question = input('How many times do you want to pay in the amount of {:.2f} R$?'.format(produ))
if question == '2x':
    print('{:.2f} R$ in 2 installments'.format(parc/2))  
if question == '3x':
    print('{:.2f} R$ in 3 installments'.format(parc/3))
if question == '4x':
    print('{:.2f} R$ in 4 installments'.format(parc/4))
if question == '5x':
    print('{:.2f} R$ in 5 installments'.format(parc/5))
if question == '6x':
    print('{:.2f} R$ in 6 installments '.format(parc/6))
