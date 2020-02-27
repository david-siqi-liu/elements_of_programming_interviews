from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_buy = float('inf')
    max_profit = float('-inf')

    # At any price, we
    # 1. Update the minimum price thus-far
    # 2. Update the maximum possible profit
    for i in range(len(prices)):
        min_buy = min(min_buy, prices[i])
        max_profit = max(max_profit, prices[i] - min_buy)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
