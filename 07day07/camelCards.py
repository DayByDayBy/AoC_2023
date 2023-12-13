card_values = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13, "A":14}
hand_values = {"high_card":1, "one_pair":2, "two_pair":3, "three_kind":4, "full_house":5, "four_kind":6, "five_kind":7}
    # if five_kind:
    # elif four_kind:
    # elif three_kind:
    # elif two_pair:
    # elif one_pair:
    # elif high_card:

def hand_grab():
    with open('hands.txt') as data:               
        hands_and_bids = [tuple(i.split()) for i in data.readlines()]       
    return hands_and_bids 
    
def hand_checker(hands_and_bids):
    labeled_hands = []
    
    for hand, bid in hands_and_bids:
        char_counts = {}
        for char in hand:
            char_counts[char] = char_counts.get(char, 0)+1
        max_count = max(char_counts.values(), default = 0)
        if max_count > 1:
            label = tuple((max_count, char))
        else:
            label = 'high_card'        
        labeled_hands.append((hand, bid, label))
        
    for h in labeled_hands:
        if labeled_hands[h][2][0] == 5:
            
        

        
    print(labeled_hands)

    

hand_checker(hand_grab())
    
        

