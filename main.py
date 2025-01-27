#This is a program that potrays a coffee shop but beneath that is a secret service company that uses the shop for cover
def secret_service():# This is a function of a secret service, it is called when the user types the correct security key
    assignment= input(('Enter the code you are having: '))
    tasks = {# A list of tasks for the secret service agents
    "Champagne" :"The rescue",
    "Whisky" : "Killing the Janitor",
    "Tequila" : "president's lead escort",
    "Hennessy"  :"The sniper"
    }

    print('Putting out your skill to the fullest Honours us Agent')

    if assignment == 'Champagne':
        print(tasks.get("Champagne"))
    elif assignment == 'Whisky':
        print(tasks.get('Whisky'))
    elif assignment == 'Tequila':
        print(tasks.get('Tequila'))
    elif assignment == 'Hennessy':
        print(tasks.get('Hennessy'))


security_key = 1123
i = 0
#The coffee shop together with the list of products in it please type the product you want the same way it is in here
print("""Welcome to But Jonny's coffee shop here is the list of our menu
         Cupachino - R50
         Tea - R35
         Coffee - R60
         Coffee(black) - R35""")
Cupachino = 50
Tea = 35
Coffee = 60
Coffee_black = 35

output = input("Please select what you would like to have in our store today :")
how_many = int(input(f'\nHow many {output} would you like: '))
if output == 'Cupachino':
    print(f"\nYour total will be: R{(Cupachino) * (how_many)}")
elif output == 'Tea':
    print(f"\nYour total will be: R{(Tea) * (how_many)}")
elif output == 'Coffee':
    print(f"\nYour total will be: R{(Coffee) * (how_many)}")
elif output == 'Coffee(black)':
    print(f"\nYour total will be: R{(Coffee_black) * (how_many)}")

code1 = 1001 #These are codes which becomes different each and everyday and they offer rewards
code2 = 2011
code3 = 3018
code4 = 5612

while i < 3: #This is a while loop that provides a customer 3 tries incase they make a mistake on their code
    recieve = int(input('''Everyday we reward 4 customers with free coffe based on the code they have on their slip 
    \nEnter you code to see your reward:  
    '''))
    i = i + 1
    if recieve == security_key:
        print('\nAttempt successfull launching the secret service...')
        print(secret_service())
        break
    elif recieve == code1:
        print("Wow you're the lucky winner, go claim your coffee at the counter")
        break
    elif recieve == code2:
        print("Wow you're the lucky winner, go claim your coffee at the counter")
        break
    elif recieve == code3:
        print("Wow you're the lucky winner, go claim your coffee at the counter")
        break
    elif recieve == code4:
        print("Wow you're the lucky winner, go claim your coffee at the counter")
        break
    else:
        print("Invalid code try again")
















