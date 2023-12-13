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
            label = f'{max_count} of {len(hand)}'
        else:
            label = 'high_card'        
        labeled_hands.append((hand, bid, label))
    print( labeled_hands)

    

hand_checker(hand_grab())

    
    
    
    
    
    # if five_kind:
    # elif four_kind:
    # elif three_kind:
    # elif two_pair:
    # elif one_pair:
    # elif high_card:
    
        

