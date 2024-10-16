menu_option = ''

while menu_option != 'q':
    print(f'''
    Shop information FAQS:
    a: glue and tape newspapers
    b: deliver newspapers
    q: discard
    ''')
    menu_option = input("Enter a letter for more info around the shop: ")
    
    if menu_option == 'a':
        print('Gluing and taping is safe, no training necessary!')
    elif menu_option == 'b':
        van_driver = input('Are you comfortable driving a bike to deliver? enter (y or n): ')
        if van_driver == 'y':
            print("Awesome! It would be great to have you help deliver by bike!")
        else:
            print("We won't ask you to bike!")
