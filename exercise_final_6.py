import heapq

# Define the items with their cost and calorie value.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Greedy approach
def greedy_algorithm(items, budget):
    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    # Сортуємо предмети за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)

    for item, details in sorted_items:
        if remaining_budget >= details['cost']:
            chosen_items.append(item)
            total_calories += details['calories']
            remaining_budget -= details['cost']

    return total_calories, budget - remaining_budget, chosen_items

# Dynamic Programming approach
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(items)

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(budget + 1):
            item_name = item_names[i - 1]
            item_cost = items[item_name]['cost']
            item_calories = items[item_name]['calories']

            if item_cost <= w:
                dp_table[i][w] = max(dp_table[i - 1][w], dp_table[i - 1][w - item_cost] + item_calories)
            else:
                dp_table[i][w] = dp_table[i - 1][w]

    # Finding the chosen items
    chosen_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp_table[i][w] != dp_table[i - 1][w]:
            item_name = item_names[i - 1]
            chosen_items.append(item_name)
            w -= items[item_name]['cost']

    total_calories = dp_table[n][budget]
    remaining_budget = w

    return total_calories, budget - remaining_budget, chosen_items

if __name__ == '__main__':
    # Execute both algorithms
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Greedy Result:", greedy_result)
    print("Dynamic Programming Result:", dp_result)

