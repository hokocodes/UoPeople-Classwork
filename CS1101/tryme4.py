# to make reading blank lines easier
def new_line():
    print('.')

# Prints three lines.
def three_lines():
    new_line()
    new_line()
    new_line()

# Prints nine lines.
def nine_lines():
    three_lines()
    three_lines()
    three_lines()

#Prints 25 lines.
def clear_screen():
    nine_lines()
    nine_lines()
    three_lines()
    three_lines()
    new_line()

#Calls the function to print nine lines.
nine_lines()

#Makes it helpful to know when we're done printing 9 lines to see the next 25 lines.
print('Calling clear_screen()')

#Prints 25 lines.
clear_screen()
