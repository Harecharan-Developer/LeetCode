def cheapest_flights_bellman_ford(n, flights, src, dst, k):
  """
  Finds the cheapest flight from src to dst with at most k stops using Bellman-Ford.

  Args:
    n: Number of cities.
    flights: List of flights as [[from, to, price]].
    src: Source city.
    dst: Destination city.
    k: Maximum number of stops.

  Returns:
    The cheapest price, or -1 if no path exists.
  """
  dist = [float('inf')] * n
  dist[src] = 0

  for _ in range(k + 1):
    for flight in flights:
      from_, to_, price = flight
      dist[to_] = min(dist[to_], dist[from_] + price)

  return dist[dst] if dist[dst] != float('inf') else -1

# Example usage
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
cheapest_price = cheapest_flights_bellman_ford(n, flights, src, dst, k)
print(f"Cheapest price: {cheapest_price}")
def cheapest_flights_dp(n, flights, src, dst, k):
  """
  Finds the cheapest flight from src to dst with at most k stops using dynamic programming.

  Args:
    n: Number of cities.
    flights: List of flights as [[from, to, price]].
    src: Source city.
    dst: Destination city.
    k: Maximum number of stops.

  Returns:
    The cheapest price, or -1 if no path exists.
  """
  dp = [[float('inf')] * n for _ in range(k + 2)]
  dp[0][src] = 0

  for i in range(1, k + 2):
    for flight in flights:
      from_, to_, price = flight
      dp[i][to_] = min(dp[i][to_], dp[i - 1][from_] + price)

  return dp[k + 1][dst] if dp[k + 1][dst] != float('inf') else -1

# Example usage
n = 4
flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
src = 0
dst = 3
k = 1
cheapest_price = cheapest_flights_dp(n, flights, src, dst, k)
print(f"Cheapest price: {cheapest_price}")
