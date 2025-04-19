

def knapsack(i, capacity, weight, value):
    """to steal the art in the gallary with maximum value and minimum weight"""
    
    if i == len(weight) or capacity == 0:
        return 0
    
    if weight[i] > capacity:
        return knapsack(i+1, capacity, weight, value)
    
    skip = knapsack(i+1, capacity, weight, value)
    take = value[i] + knapsack(i, capacity-weight[i], weight, value)
    return max(skip, take)

weight = [2, 3, 4, 5, 9]
value = [3, 4, 8, 8, 10]

print(knapsack(0, 20, weight, value))