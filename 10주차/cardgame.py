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
