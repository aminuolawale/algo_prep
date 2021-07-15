def meeting_planner(slotsA, slotsB, dur):
    a = slotsA
    b = slotsB
    index_a = index_b = 0
    while index_a < len(a) or index_b < len(b):
        print(index_a, index_b)
        if a[index_a][1] < b[index_b][0]:
            index_a += 1
        elif b[index_b][1] < a[index_a][0]:
            index_b += 1
        else:
            alpha = b[index_b][1] - a[index_a][0]
            beta = a[index_a][1] - b[index_b][0]
            if alpha < beta and alpha >= dur:
                if b[index_b][1] - b[index_b][0] >= dur:
                    return [a[index_a][0], dur + a[index_a][0]]
            elif beta <= alpha and beta >= dur:
                if a[index_a][1] - a[index_a][0] >= dur:
                    return [b[index_b][0], dur + b[index_b][0]]
            if index_a < len(a) - 1:
                index_a += 1
            elif index_b < len(b) - 1:
                index_b += 1
    return []  # your code goes here


a = [[10, 50], [60, 120], [140, 210]]
b = [[0, 15], [60, 70]]
dur = 8
print(meeting_planner(a, b, dur))
