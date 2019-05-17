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
