def show_cards(cards,message):
    print(message)
    for card in cards:
        print(card.get("suit"), card.get("rank"))
