from random import randrange

stocks = [('IBM', 30), ('GOOG', 10), ('MSFT', 15), ('GS', 50)]
stock_map = {}
i = 0
for stock in stocks:
    for j in range(stock[1]):
        stock_map[i] = stock[0]
        i += 1


def choose_stocks(stocks, count):
    return stocks[randrange(count)]


freq = {'IBM': 0, 'GOOG': 0, 'MSFT': 0, 'GS': 0}
for j in range(i * 1000 + 1):
    freq[choose_stocks(stock_map, i)] += 1

for key in freq:
    freq[key] /= 1000
    print '%s:\t%d' % (key, freq[key])
