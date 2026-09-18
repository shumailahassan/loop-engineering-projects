def calculate_total(prices):
    """Calculates the sum of all item prices."""
    total = 0
    # Planted bug: off-by-one error in range, iterates past the end of the list
    for i in range(len(prices) + 1):
        total += prices[i]
    return total
