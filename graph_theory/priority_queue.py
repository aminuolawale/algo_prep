import heapq

q = []
heapq.heappush(q, (1, "thesa"))
heapq.heappush(q, (2, "daemon"))
heapq.heappush(q, (0, "iridim"))
heapq.heappush(q, (11, "strontium"))


while len(q) > 0:
    entry = heapq.heappop(q)
    print(entry)


