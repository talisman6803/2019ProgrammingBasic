def blackjack():
    print("Welcome to SMaSH Casino!")
    members = load_members()
    username, tries, wins, chips, members = login(members)
    deck = fresh_deck()
    temp = members[username]
    tmp = True
    while tmp == True:
        tries += 1
        print("-----")
        dealer = []
        player = []
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        card, deck = hit(deck)
        player.append(card)
        card, deck = hit(deck)
        dealer.append(card)
        print("My cards are:")
        print(" ", "****", "**")
        print(" ", dealer[1]["suit"], dealer[1]["rank"])
        show_cards(player, "Your cards are:")
        score_player = count_score(player)
        score_dealer = count_score(dealer)
        if score_player == 21:
            print("Blackjack! you won.")
            wins += 1
        else:
            while score_player <21 and more("Hit?") == True:
                card, deck = hit(deck)
                show_cards([card], "")
                player.append(card)
                score_player = count_score(player)
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
            else:
                while 16 > score_dealer:
                    card, deck = hit(deck)
                    dealer.append(card)
                    score_dealer = count_score(dealer)
                show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += 1
                    wins += 1
                elif score_dealer < score_player:
                    print("You won.")
                    chips += 1
                    wins += 1
                elif score_dealer == score_player:
                    print("We draw.")
                else:
                    print("I won.")
                    chips -= 1
        print("Chips = ",chips)
        tmp = more("Play more?")
    members[username] = list(members[username])
    members[username][1] = tries
    members[username][2] = wins
    members[username][3] = chips
    members[username] = tuple(members[username])
    store_members(members)
    print("You played", tries - temp[1], "games and won", wins - temp[2],"of them.")
    print("Your winning percentage today is", "{0:.1f}".format((tries - temp[2])/(tries - temp[1])*100), "%")
    print("Bye!")
    show_top5(members)

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

def load_members():
    file = open("members.txt","r")
    members = {}
    for line in file:
        name, passwd, tries, wins, chips = line.strip('\n').split(',')
        members[name] = (passwd,int(tries),float(wins),int(chips))
    file.close()
    return members

def store_members(members):
    file = open("members.txt","w")
    names = members.keys()
    for name in names:
        passwd, tries, wins, chips = members[name]
        line = name + ',' + passwd + ',' + \
               str(tries) + ',' + str(wins) + "," + str(chips) + '\n'              
        file.write(line)
    file.close()

def show_top5(members):
    print("-----")
    sorted_members = sorted(members.items(),key=lambda x: x[1][3],reverse=True)
    print("All-time Top 5 based on the number of chips earned")
    for i in range(5):
        if sorted_members [i][1][3] != 0:
            print(i+1, '.', sorted_members[i][0], ':', sorted_members[i][1][3])
        else:
            continue

def fresh_deck():
    import random
    suits = {"Spade", "Heart", "Diamond", "Club"}
    ranks = {"A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"}
    deck = []
    li_su = list(suits)
    li_ra = list(ranks)
    for i in range(len(suits)):
        for j in range(len(ranks)):
            deck.append({"suit": li_su[i], "rank": li_ra[j]})
    random.shuffle(deck)
    return deck

def hit(deck):
    if deck == []:
        deck = fresh_deck()
    return (deck[0], deck[1:])

def count_score(cards):
    score = 0
    number_of_ace = 0
    for card in cards:
        if card.get("rank") == "A":
            number_of_ace += 1
            score += 11
        elif card.get("rank") == "J":
            score += 10
        elif card.get("rank") == "Q":
            score += 10
        elif card.get("rank") == "K":
            score += 10
        else:
            score += card.get("rank")
    while score > 21 and number_of_ace > 0:
        number_of_ace -= 1
        score -= 10
    return score

def show_cards(cards,message):
    print(message)
    for card in cards:
        print(" ", card.get("suit"), card.get("rank"))

def more(message):
    answer = input(message)
    while not answer == 'y' and answer != 'n':
        answer = input(message)
    return answer == 'y'
