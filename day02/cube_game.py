def bag_count():
    possible_games = []
    
    with open("game_data.txt", "r") as data:
        for game in data:
            game_info = game.strip().split(": ")
            game_ID = int(game_info[0].split()[-1])
            rounds = game_info[1].split("; ")
            possible = True
            
            for round in rounds:
                red = 12
                green = 13
                blue = 14
                cubes = round.split(", ")                
                for pair in cubes:
                    number, colour = pair.split()
                    number = int(number)
                    
                    if colour == 'red':
                        red -= number
                    elif colour == 'green':
                        green -= number
                    elif colour == 'blue':
                        blue -= number                    
                    if red < 0 or green < 0 or blue < 0:
                        possible = False
                        break                
                if not possible:
                        break                    
            if possible:
                possible_games.append(game_ID)
        return possible_games

    
real_games = bag_count()
print(real_games)
print(sum(real_games))        
        
        
    
