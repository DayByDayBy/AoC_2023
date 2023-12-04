import re 

class Card():
    def __init__ (self, id, win_nums, play_nums):
        self.id = id
        self.win_nums = win_nums
        self.play_nums = play_nums
    
def scratchy():
    cards = []
    with open('cards.txt', 'r') as data:
        for line in data:
            card = re.split(r'[:|]', line)
            id = card[0].strip()
            win_nums = tuple(map(int, card[1].split()))
            play_nums = tuple(map(int, card[2].split()))
            card = Card(id, win_nums, play_nums)
            cards.append(card)

    return cards             
card_list = scratchy()
for card in card_list:
    print(f"{card.id} - W: {card.win_nums} P: {card.play_nums}")
            
            
            
