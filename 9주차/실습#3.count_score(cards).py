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
