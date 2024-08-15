# Consider a deck of normal playing cards. A playing card is represented as a string, where the first part represents the rank (one of Ace A, 2, 3, 10, Jack J, Queen Q, King K) and the second part represents the suit (one of Clubs C. Diamonds D, Hearts H. Spades S)
from fileinput import input

# Criterion 1: the set has 3 or more cards and all cards in the set have the same rank and any suit. Examples:

# AC, AD, AS (Ace of Clubs, Diamonds and Spades) 5C, "5D", "SH", "5S" (Five of Clubs, Diamonds, Spades and Hearts)

# Criterion 2: the set has 3 or more cards and all cards in the set have the same suit and consecutive ranks.

# 1C, 2C, 3C, 4C (1, 2, 3 and 4 of Clubs)

# 8H, 9H, 10H, JH, QH, KH (8, 9, 10, Jack, Queen and King of Hearts)

# Examples of invalid sets:

# 2C, 3C only two cards are present but a minimum of 3 are required "2C", "3C", "5C": not consecutive ranks as it's missing the 4 of Clubs.

# 2C, 3C", "4H" not all cards have the same suit (mix of Clubs and Hearts)

# Write a function that takes as input a list of cards, and determines if the input is a valid playing card set.

# Examples:

# Input: [2C, 2S, 2H], Function returns: true

# Input: [2C, 3C, 4C], Function returns: true

# Input: [2C, 3C, 4H] Function returns: false

# google
# strings
# maps

input = ['2C', '3C', '4H'] 
mp = {
    'J' : 11,
    'Q' : 12,
    'K' : 13,
    'A' : 1
}

def check_criteria_1(input):
    if len(input) < 3:
        return False
    for i in range(0,len(input)-1):
        if input[i][0]!=input[i+1][0]:
            return False
        
    return True

def check_criteria_2(input):
    #assuming the set is not sorted eg [1Q , 32 ,2A] is still valid
    if len(input) < 3:
        return False
    s = 0
    for i in range(0,len(input)-1):
        if input[i][1] != input[i+1][1] or not (int(mp[input[i][0]]) if input[i][0] in mp else int(input[i][0]) \
                                                != int(mp[input[i+1][0]]) -1 if input[i+1][0] in mp else int(input[i+1][0])-1):
            return False
        
    return True
        

print(check_criteria_1(input) or check_criteria_2(input))
