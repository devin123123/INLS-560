import sys
# Make program repeat
while True:

    # Get user input for file
    file_variable = input('''
                          What file would you like to search for?:
                          a) 60s-music file
                          b) athletes file
                          x) to exit
                          ''')

    # Process user input
    if file_variable == 'x':
        sys.exit()
    elif file_variable == 'a':
         file_variable = '60s-music.csv'
    elif file_variable == 'b':
         file_variable = 'athletes.csv'
    else:
         print('Invalid option. Please select a, b, or x.')
         continue
    
    # Enter a search term
    search_variable = input(f'Enter the search term for {file_variable} file:')
    search_variable = search_variable.lower()  # Convert user input to lowercase

    # Define the function to search the file
    def find(file_variable, search_variable):
        with open(file_variable, 'r') as file:
            content = file.read().lower()  # Read file and convert to lowercase for case-insensitivity
        
        # Now the file is in the memory buffer as content
        if search_variable in content:
            print(f'Your search term "{search_variable}" exists in the {file_variable} file!')
            see_entries = input('Would you like to see the entries? (y or n)?')

            # If 'y', output all entries
            if see_entries.lower() == 'y':
                print(f'Here are all of the entries with the term "{search_variable}":')
                with open(file_variable, 'r') as file:
                    for line in file:
                        # Lowercase both the line and search term to ensure case-insensitive search
                        if search_variable in line.lower():
                            print(line.strip())

            # If 'n', exit
            elif see_entries.lower() == 'n':
                print('Goodbye')
                sys.exit()
            else:
                print("Invalid option. Please enter y or n.")
        else:
            print(f'{search_variable} does not exist in {file_variable}')

    # Call the function
    find(file_variable, search_variable)
