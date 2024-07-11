"""
https://www.hackerrank.com/challenges/nimble-game-1/problem?isFullScreen=false
"""
import random


def select_random_index_excluding_zeros(arr):
    # Create a list of indices that are not at the 0th position and have non-zero values
    valid_indices = [i for i in range(1, len(arr)) if arr[i] != 0]

    if not valid_indices:
        raise ValueError("No valid elements to select from")

    return random.choice(valid_indices)


def move_coins(coins_square, selected_index):
    coins_square[selected_index] = coins_square[selected_index] - 1
    coins_square[0] = coins_square[0] + 1
    return coins_square

s="133161 69274 462545 18681 396705 285084 226326 270806 437186 227508 512146 119870 505792 342737 459406 712327 954917 415178 467194 978336 503793 791934 577929 455175 622282 883955 430658 77224 524252 149189 827785 657413 734815 290330 676094 131521 91766 418773 918679 45305 162633 430825 681527 184778 289914 140933 897105 244832 556112 880652 739520 576257 188938 317449 31432 811221 717757 978442 404797 242009 127631 232582"
coins_square = list(map(lambda x: int(x),s.split(" ")))
total_coins = sum(coins_square)
all_zero = all(x == 0 for x in coins_square)  # set(coins_square) == {0}
if all_zero:
    print('Second')
elif total_coins == coins_square[0]:
    print('Second')
count = 0
while True:
    try:
        selected_index = select_random_index_excluding_zeros(coins_square)
        coins_square = move_coins(coins_square, selected_index)
    except ValueError:
        if count % 2 == 0:
            print('First')
        else:
            print('Second')
        break
# Setting coins at the selected index subtracting 1


"""
x = 0
for i in range(1, len(s)):
    if s[i] % 2:
        x ^= i
return "First" if x else "Second"
"""