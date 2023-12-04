import re 


class Card():
    def __init__ (self, id, win_nums, play_nums):
        self.id = id
        self.win_nums = win_nums
        self.play_nums = play_nums
    
def scratchy():
    all_points = []
    cards = []    
    with open('cards.txt', 'r') as data:
        for line in data:
            card = re.split(r'[:|]', line)
            id = card[0].strip()
            win_nums = tuple(map(int, card[1].split()))
            play_nums = tuple(map(int, card[2].split()))
            card = Card(id, win_nums, play_nums)
            cards.append(card)
    for card in cards:
            matches = set(card.win_nums) & set(card.play_nums)
            score  = len(matches)
            points = 0
            if score > 0: 
                points += 2 ** (score - 1)
            print(f"{card.id} matched {score} for {points} points")
            all_points.append(points)
    return all_points

all_points = scratchy()
print(sum(all_points))
