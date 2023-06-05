class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    total_value = 0.0
    remaining_capacity = capacity

    for item in items:
        if remaining_capacity >= item.weight:
            total_value += item.value
            remaining_capacity -= item.weight
        else:
            fraction = remaining_capacity / item.weight
            total_value += fraction * item.value
            remaining_capacity = 0
            break

    return total_value

# Example usage
items = [
    Item(10, 60),
    Item(20, 100),
    Item(30, 120),
]
knapsack_capacity = 50

max_value = fractional_knapsack(items, knapsack_capacity)
print("Maximum value achievable:", max_value)
