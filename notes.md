01:
find coordinates/first last number embedded in string
isdigit, finditer,  used a dictionary of days to find non-dogit numbers for part 2, 
and scanned reverse string to find last number to avoid the 'TWONE' etc problem. 
later realised it would be better to replace numbers in string with eg one1one; solves the 'twone' problem without scanning two strings and having two dictionaries
________________________________________________________________

02:
cubes in a bag: figure out whether games are possible given set number of cubes/colours; figure out minimum cubes required for each game to be possoible
created a 'Game' class, but tbh that was more for the sake of doing so than it being a _particularly_ good solution - ends up being quite verbose, and overkill for the task at hand

________________________________________________________________

03:
finding part numbers 

verbosity of the last one made me want a more neat solution this time, so regex and list comp approach was on ythe list. task was a bit more involved, so it still wasnt that neat. 
adjacency checking is new to me, and on refelction the code could def be golfed a bit, but i dont really use list comp all that often, was more intrested in playing with that and tbh solving the puzzle, as it was getting late
had an early confound as my initial approach was adding numbers once per adjacent digit, rather than once if they had an adjacent digit - bit of a rethink, but used start and end points to solve that

part two was after some chat with a pal, and took a different, leaner approach, 'baking in' the start/end stuff and treating the numbers a bit differently

________________________________________________________________

04:

scratchcard problem, matching winning numbers to player numbers 
playing with the Class approach again, to represnet cards - split the data into lines as per, then split those into the three attribites of the class, id, winning numbers, 'played' numbers. then loop through the cards to gather points
for part two i oplayed with list comp again, more practice for a thing i feel like i should/could use more often - simpler approach seemed a good idea, considering the nnumbers involved (winning cards win cards, many of which also win cards, etc, etc)

05:

seedmap, a 'translation' of locations through various ranged shifts 
took me a minute as i was thinking too small (working with the examle data set without looking at the larger data set, where the ranges are giga-huge) - 'i code better at night', and other lies - had code that 'worked', but ran endlessly when it was running the puzzle input


06
07
08
09
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25

