
scratchies = [[1]+[numbers.split() for numbers in line[9:].split(" | ")] for line in open(r"cards.txt")]
# print(scratchies[0])
scratchy_count = 0 

for card in range(len(scratchies)):
    wins = 0 
    scratchy_count += scratchies[card][0]

    for win in scratchies[card][1]:
        if win in scratchies[card][2]:
            wins += 1

    for new in range(card+1, card+wins+1):
            scratchies[new][0] += scratchies[card][0]
           
print(scratchy_count)