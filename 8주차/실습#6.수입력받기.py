def get_integer(message,i,j):
    number = input(message)
    while not (i<=int(number)<=j):
        number = input(message)
    return int(number)
