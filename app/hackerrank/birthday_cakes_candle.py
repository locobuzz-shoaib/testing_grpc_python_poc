def birthday_cake_candles(candles):
    # Write your code here
    return candles.count(max(candles))


candles = [4, 4, 1, 3]
print(birthday_cake_candles(candles))
