class Game:
    def __init__(self, game_data, rounds_data):
        self.id = int(game_data.split()[-1])
        self.rounds = self.parse_rounds(rounds_data)

    def parse_rounds(self, rounds_data):
        rounds = []
        for round_data in rounds_data.split("; "):
            round_dict = {}
            for pair in round_data.split(", "):
                count, color = pair.split()
                count = int(count)
                round_dict[color] = count
            rounds.append(round_dict)
        return rounds
    
def poss_games(self): 
    red = 12
    green = 13       
    blue = 14
    poss = True

    for round_data in self.rounds:
        if (
            sum(value for color, value in round_data.items() if color == 'red') < red or
            sum(value for color, value in round_data.items() if color == 'green') < green or 
            sum(value for color, value in round_data.items() if color == 'blue') < blue
        ):
            poss = False
            break      
    if poss == True:
        possible_games.append(self.id)

def powers(self):
    global game_powers
    max_counts = {'red': 0, 'green': 0, 'blue': 0}    
    for round_data in self.rounds:
        for colour, count in round_data.items():
            max_counts[colour] = max(max_counts[colour], count)
    result = 1
    for count in max_counts.values():
        result *= count
    game_powers.append(result)    

games = []
possible_games = []
game_powers = []

with open("game_data.txt", "r") as data:
    for i in data:
        game_data, rounds_data = i.strip().split(": ")
        game = Game(game_data, rounds_data)
        games.append(game)
        
        
for game in games:
    poss_games(game)
    powers(game)
    
print(sum(possible_games))
print(sum(game_powers))


    
    



