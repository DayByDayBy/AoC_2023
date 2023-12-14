card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
hand_values = {"high_card":1, "one_pair":2, "two_pair":3, "three_kind":4, "full_house":5, "four_kind":6, "five_kind":7}

def hand_grab():
    with open('hands.txt') as data:               
        hands_and_bids = [tuple(i.split()) for i in data.readlines()]   
    return hands_and_bids
    
def hand_sort(hand):
    return hand_values[hand[2]]

def card_sort(hand):
    # print([card_values[char] for char in hand[0]])
    return [card_values[char] for char in hand[0]]

def hand_checker(hands_and_bids):
    labeled_hands = []    
    for hand, bid in hands_and_bids:
        char_counts = {}
        for char in hand:
            char_counts[char] = char_counts.get(char, 0)+1
        max_count = max(char_counts.values(), default = 0)
        if max_count == 5:
            label = 'five_kind'
        elif max_count == 4:
            label = 'four_kind'    
        elif max_count == 3 and len(char_counts) == 2:
            label = 'full_house'
        elif max_count == 3:
            label = 'three_kind'
        elif max_count == 2 and len([count for count in char_counts.values() if count == 2]) == 2:
                label = 'two_pair'
        elif max_count == 2:
                label = 'one_pair'
        elif max_count == 1:
            label = 'high_card'                 
        labeled_hands.append((hand, int(bid), label))
        # print(labeled_hands)
        
    sorted_hands = sorted(labeled_hands, key=lambda hand: (hand_sort(hand), card_sort(hand)), reverse=True)
    print(sorted_hands)
    scores = [len(sorted_hands) - i for i, _ in enumerate(sorted_hands)]  
    all_winnings = []
    
    for hand, score in zip(sorted_hands, scores):
        # print(hand, score)
        winnings = hand[1] * score
        # print(winnings)
        all_winnings.append(winnings)
        # print(f"{hand[0]}:{winnings}")
    # print(all_winnings)
    print(sum(all_winnings))        
hand_checker(hand_grab())
    
        

