from itertools import combinations

def brute_force(W, wt, val, n):
    # Base Case
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    bitlst = []
    if (wt[n-1] > W):
        bitlst.append(0)
        return brute_force(W, wt, val, n-1)
 
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        bitlst.append(1)
        new = []
        return max( val[n-1] + brute_force(W-wt[n-1], wt, val, n-1, bitlst),brute_force(W, wt, val, n-1))

def brute_force(number, capacity, weight_cost):
    """Brute force method for solving knapsack problem

    :param number: number of existing items
    :param capacity: the capacity of knapsack
    :param weight_cost: list of tuples like: [(weight, cost), (weight, cost), ...]
    :return: tuple like: (best cost, best combination list(contains 1 and 0))
    """
    best_cost = None
    best_combination = []
    # generating combinations by all ways: C by 1 from n, C by 2 from n, ...
    for way in range(number):
        for comb in combinations(weight_cost, way + 1):
            weight = sum([wc[0] for wc in comb])
            cost = sum([wc[1] for wc in comb])
            if (best_cost is None or best_cost < cost) and weight <= capacity:
                best_cost = cost
                best_combination = [0] * number
                for wc in comb:
                    best_combination[weight_cost.index(wc)] = 1
    return best_cost, best_combination