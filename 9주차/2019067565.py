import cardgame
def blackjack():
    print("Welcome to SMaSH Casino!")
    deck = cardgame.fresh_deck()
    chips = 0
    tmp = True
    while tmp == True:
        print("-----")
        dealer = []
        player = []
        card, deck = cardgame.hit(deck)
        player.append(card)
        card, deck = cardgame.hit(deck)
        dealer.append(card)
        card, deck = cardgame.hit(deck)
        player.append(card)
        card, deck = cardgame.hit(deck)
        dealer.append(card)
        print("My cards are:")
        print(" ", "****", "**")
        print(" ", dealer[1]["suit"], dealer[1]["rank"])
        cardgame.show_cards(player, "Your cards are:")
        score_player = cardgame.count_score(player)
        score_dealer = cardgame.count_score(dealer)
        if score_player == 21:
            chips += 2
            print("Blackjack! you won.")
        else:
            while score_player <21 and cardgame.more("Hit?") == True:
                card, deck = cardgame.hit(deck)
                cardgame.show_cards([card], "")
                player.append(card)
                score_player = cardgame.count_score(player)
            if score_player > 21:
                print("You bust! I won.")
                chips -= 1
            else:
                while 16 > score_dealer:
                    card, deck = cardgame.hit(deck)
                    dealer.append(card)
                    score_dealer = cardgame.count_score(dealer)
                cardgame.show_cards(dealer, "My cards are:")
                if score_dealer > 21:
                    print("I bust! You won.")
                    chips += 1
                elif score_dealer < score_player:
                    print("You won.")
                    chips += 1
                elif score_dealer == score_player:
                    print("We draw.")
                else:
                    print("I won.")
                    chips -= 1
        print("Chips = ",chips)
        tmp = cardgame.more("Play more?")
    print("Bye!")
