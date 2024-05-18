import heapq


def min_cost_to_connect_cables(cables_stock):
    heapq.heapify(cables_stock)
    total_cost = 0

    while len(cables_stock) > 1:
        first_cable = heapq.heappop(cables_stock)
        second_cable = heapq.heappop(cables_stock)

        cost = first_cable + second_cable
        total_cost += cost

        heapq.heappush(cables_stock, cost)

    return total_cost


if __name__ == "__main__":
    cables = [55, 49, 63, 73, 83, 43, 53]
    min_cost = min_cost_to_connect_cables(cables)
    print("Min cost to connect cables:", min_cost)
