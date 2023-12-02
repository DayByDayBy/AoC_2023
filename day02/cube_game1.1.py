def bad_solution(ohnobro):
    are_you_doing = 'wat'
    abortive = True
    thinking = False 
print(sadface)






# import math, logging

# def bag_count(token_limits=None, all_possible=False):
    
#     possible_games =[]
    
#     with open("game_data.txt", "r") as data:
#         for game in data:
#             game_data, rounds = game.strip().split(": ")
#             game_ID = int(game_data.split()[-1])
        
#             red_limit, green_limit, blue_limit = token_limits if token_limits else (math.inf, math.inf, math.inf)
#             game_possible = all(
#                     sum(int(number) for number, _ in pair_split) <= limit
#                     if len(pair_split) == 2
#                     else (print(f"Problematic pair: {pair_split}"), False)
#                     for round in rounds
#                     for pair in round.split(", ")
#                     for limit, pair_split in zip((red_limit, green_limit, blue_limit), (pair.split() for pair in round.split(", ")))
#                     )

#             if (all_possible and game_possible) or (not all_possible and game_possible):
#                 possible_games.append(game_ID)
#     if token_limits:
#         logging.debug(f"Sum of IDs for Possible Games with Token Limits {token_limits}: {sum(possible_games)}")
#     else:
#         total_product = sum(power_sum(round) for round in possible_games)
#         logging.debug(f"Sum of Possible Games: {total_product}")


# def power_sum(round):
#     return sum(min(int(number) for number in pair.split(", ")) for pair in round.split("; "))

# bag_count(token_limits=(12, 13, 14))
# bag_count(all_possible=True)

        