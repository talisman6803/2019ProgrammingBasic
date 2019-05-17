def more(message):
    answer = input(message)
    while not answer == 'y' and answer != 'n':
        answer = input(message)
    return answer == 'y'
