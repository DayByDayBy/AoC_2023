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
________________________________________________________________

05:

seedmap, a 'translation' of locations through various ranged shifts 
took me a minute as i was thinking too small (working with the examle data set without looking at the larger data set, where the ranges are giga-huge) - 'i code better at night', and other lies - had code that 'worked', but ran endlessly when it was running the puzzle input, as a result of firing on ahead and making code that created lists for everything 

________________________________________________________________

06:
racing game: charge-accelerate phase and travel phase, see how many ways you can beat the record with given times and distances
pt 1 was fairly straightforward, splitting the given time into pairs of non-zero, seeing which would travel the distance required, adding them to a list. numpy prod to get the answer, the number of ways to beat each race multiplied together 
pt 2 was just a bigger number crunch, as tyhe times and distances were a time and distance. left the return as it was even tho there was no need to return a product, because as a list of one number it made no difference - if i was code golfing i would change that, and if i was one-scripting for both parts i would just add a print for 0 or -1 index of the list. (in fact, i'll add that line to the pt2 code now, to remind myself if/when i come back)

________________________________________________________________

07:
camel cards - basically poker
made a dictionary for cards and hands, made a for loop with some if/elif to check hands (ie char count in 5 char strings) and arrange them into a win order.  assigned points (bid/bet multiplier) to the hands in reverse index order, ie [0] gives *1000, then printed sum of the multipled bids
pt 2 introduced a joker condition (and removed the J/jack) - edited the dictionary to place J as lowest card for settling ties (instructions said j can be any card, but remains j for comparison purposes), created specifc j count to be added to any char count 

________________________________________________________________

08:
desert maps 
str of L and R, page of three-char str names and their associated three-char str 2-tuples. task was to start at 'AAA', use LR sequence to choose left/right of each tuple str, using the resulting three-char str to find the next one until ZZZ
pt 1 easy enough, pt2 introduced ghosts (lol, merry christmas) who follow mulitiple paths that _end_ in A-Z until all are on node end in Z 

________________________________________________________________

09:
oasis instability, mirage maintennnce
difference bwetween the differnce between the dfifference between etc until the difference is 0, then predicting the next in each of those new sequences
pt1 - last number in seq, next gap (next list down in 2d list), next number (last number plus gap) - had it working then sorta bnroke the logic fiddling with it, tidying up

________________________________________________________________

10:
pipe maze - tunnel mapping, ie follow a path, step length of path to point farthest from start (assume that means farthest 'above ground'?)
________________________________________________________________

11:
galactic mapping
________________________________________________________________

12:
hot springs
________________________________________________________________

13:
point of incidence / mirror hunt
________________________________________________________________

14:
parabolic reflector dish / rock weight

________________________________________________________________

15:
leb library / hasher
________________________________________________________________

16:
floor will be lava / 

________________________________________________________________

17:
clumsy crucible

________________________________________________________________

18:
lavaductor - digging out a lava lagoon via 4 vectors, 4 directions and a distance (and a colour) that describe a path, inside of which is the lagoon area 

'create path', ie desacibe

either keep a record of sides, or distances travelled for for each 'move', or describe a rule for path -  seems like it would be either bulky/comlicated tho. seems like it might be simpler to go with a counter

________________________________________________________________

19: aplenty/accept-reject parts
________________________________________________________________

20:
pulse propagation / counting puleses through, based on module type/rules
maybe class? 
________________________________________________________________

21:

________________________________________________________________

22:

________________________________________________________________

23:

________________________________________________________________

24:

________________________________________________________________

25:

________________________________________________________________

