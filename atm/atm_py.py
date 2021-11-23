print("Welcome to python.hub Bank ATM")
restart = ('Y')
chances = 3
balance = 999.12
while chances >= 0:
    pin = int(input('Please enter your 4 Digit Pin: '))
    if pin == ('1234'):
        print('You entered your pin Correctly')
        print('Please press 1 For your Balance')
        print('Please press 2 to make a withdrawl')
        print('Please press 3 to pay in')
        print('Please press 4 To return card')
        while restart not in ('n','NO', 'no', 'N'):
            print('Please press 1 For your Balance')
            print('Please press 2 to make a withdrawl')
            print('Please press 3 to pay in')
            print('Please press 4 To return card')
            option = int(input('What would youlike to choose?: '))
            if option == 1:
                print('Your balance is,',balance)
                restart = input('Would you like go back? ')
                if restart in ('n','NO', 'no', 'N'):
                    print('Thank you')
                    break
            
            elif option == 2:
                option2 = ('y')
                withdrawl = float(input('How much would you like to withdrawl?: 10, 20 40, 60, 80, 100 for other enter 1:'))


if withdrawl in [10, 20, 40 , 60, 80, 100]:
    balance = balance - withdrawl
    print('\nYour Balance is now  $', balance)
    restart = input('Would you like to go back? ')
    if restart in ('n','NO', 'no', 'N'):
        print('thank you')
        break

    elif withdrawl != [10, 20, 40 , 60, 80, 100]:
        print('\nInvalid amount, Please ret-ry')
        restart = ('y')
    elif withdrawl == 1:
        withdrawl = float(input('Please enter desired amount:'))

    elif option == 3:
        Pay_in = float(input('How much would you like to pay in? '))
        balance = balance + Pay_in
        print('\nToyr balance is now $', balance)
        restart = input('Would you like to go back? ')
    if restart in ('n', 'NO', 'no', 'N'):
        print('Thank you')
        break
    elif option == 4:
        print('Please wait whilst your card is returned...\n')
        print('Thank you for your service')
        break
    else:
        print('Please enter a correct number. \n')
        restart = ('y')
    elif pin != ('1234'):
        print('Incorrect Password')
        chances = chances - 1
        print(chances)
    if chances == 0:
        print('\nNo more tries')
        break