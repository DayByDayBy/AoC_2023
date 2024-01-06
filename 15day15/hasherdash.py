# The HASH algorithm is a way to turn any string of characters into a single number in the range 0 to 255. To run the HASH algorithm on a string, start with a current value of 0. Then, for each character in the string starting from the beginning:

# Determine the ASCII code for the current character of the string.
# Increase the current value by the ASCII code you just determined.
# Set the current value to itself multiplied by 17.
# Set the current value to the remainder of dividing itself by 256.
# After following these steps for each character in the string in order, the current value is the output of the HASH algorithm.

# So, to find the result of running the HASH algorithm on the string HASH:

# The current value starts at 0.
# The first character is H; its ASCII code is 72.
# The current value increases to 72.
# The current value is multiplied by 17 to become 1224.
# The current value becomes 200 (the remainder of 1224 divided by 256).
# The next character is A; its ASCII code is 65.
# The current value increases to 265.
# The current value is multiplied by 17 to become 4505.
# The current value becomes 153 (the remainder of 4505 divided by 256).
# The next character is S; its ASCII code is 83.
# The current value increases to 236.
# The current value is multiplied by 17 to become 4012.
# The current value becomes 172 (the remainder of 4012 divided by 256).
# The next character is H; its ASCII code is 72.
# The current value increases to 244.
# The current value is multiplied by 17 to become 4148.
# The current value becomes 52 (the remainder of 4148 divided by 256).
# So, the result of running the HASH algorithm on the string HASH is 52.


with open ('smallnitialisation.txt') as initialisation:
    strings = initialisation.read().split(',')
    for string in strings:
        print(string)