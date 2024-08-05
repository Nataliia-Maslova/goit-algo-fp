import random
import matplotlib.pyplot as plt

def simulate_dice_rolls(num_rolls):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        roll_sum = random.randint(1, 6) + random.randint(1, 6)
        sum_counts[roll_sum] += 1

    probabilities = {s: count / num_rolls for s, count in sum_counts.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
    
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()

if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"Симуляція з {accuracy} кидків:")
        probabilities = simulate_dice_rolls(accuracy)
        for sum_val, prob in probabilities.items():
            print(f"Сума {sum_val}: {prob*100:.2f}%")
        
        plot_probabilities(probabilities)
