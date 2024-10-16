menu_option = ''

while menu_option != 'q':
    print('MENU:', 'a: glue and tape newspapers', 'b: deliver newspapers', 'q: discard', sep='\n')
    menu_option = input("Enter a letter for more info around the shop: ")
    
    if menu_option == 'a':
        print('You chose to glue and tape newspapers')
    elif menu_option == 'deliver newspapers':
        print('You chose to deliver newspapers.')