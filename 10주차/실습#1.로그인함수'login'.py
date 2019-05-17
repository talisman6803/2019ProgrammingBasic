def login(members):
    username = input("Enter your name: (4 letters max) ")
    while len(username) > 4:
        username = input("Enter your name: (4 letters max) ")
    trypasswd = input("Enter your password: ")
    if username in members:
        if members[username][0] == trypasswd:
            tries = members[username][1]
            wins = members[username][2]
            chips = members[username][3]
            print('You played', tries, 'games and won', wins, 'of them.')
            if tries != 0:
                print('Your all-time winning percentage is', "{0:.1f}".format(wins/tries*100) , '%')
            if chips > 0:
                print("You have", chips, "chips.")
            if chips < 0:
                print("You owe",chips, "chips.")
            return username, tries, wins, chips, members
        else:
            return login(members)
    else:
        members[username] = (trypasswd,0,0,0)
        return username, 0, 0, 0, members
