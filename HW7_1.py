burger_prices = [int(input()) for _ in range(3)]
drink_prices = [int(input()) for _ in range(2)]

set_prices = [burger_price + drink_price - 50 for burger_price in burger_prices for drink_price in drink_prices]

print(min(set_prices))
