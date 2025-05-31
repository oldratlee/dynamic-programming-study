from dynamic_programming_study.knapsack import knapsack


def test_knapsack():
    assert knapsack([], [], 5) == 0
    assert knapsack([2, 1, 3, 2], [12, 10, 20, 15], 5) == 37
