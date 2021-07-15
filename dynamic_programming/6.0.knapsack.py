# # problem:
# Given items, their individual weights and their corresponding values, and a bag of capacity w, choose items such that they yield the maximum total value while fitting in the bag.

# # Solution
# done eventually following jenny's lectures




def knapsack(profits, weights, capacity):
    profits = [0] + profits
    weights = [0] + weights
    store = [[0 for _ in range(capacity+1)] for _ in range(len(profits))]
    cri = 1
    while cri < len(store):
        current_row = store[cri]
        for i, c in enumerate(current_row):
            if i >= weights[cri]:
                store[cri][i] = max(profits[cri] + store[cri-1][i-weights[cri]], store[cri-1][i])
            else:
                store[cri][i] = store[cri-1][i]
        cri += 1
    max_sum = store[-1][-1]
    i = len(store) -1
    j = len(store[0]) -1
    indexes = []
    while i >0 and j > 0:
        if store[i][j] != store[i-1][j]:
            indexes.append(i)
            j -= weights[i]
        i-=1
    chosen_profits = []
    chosen_weights = []
    for i in indexes:
        chosen_profits.append(profits[i])
        chosen_weights.append(weights[i])
    return chosen_profits, sum(chosen_profits), chosen_weights,  sum(chosen_weights)



if __name__ == "__main__":
    profits = [5, 2, 2, 4, 3]
    weights = [4, 3, 1, 3, 2]
    c = 7
    print(knapsack(profits, weights, c))