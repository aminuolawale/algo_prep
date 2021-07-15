count = 0
cache = {}
call1 = 0
def tiling(board_size,  a, b, enc=0):
    global call1
    call1 +=1
    global count
    if enc == board_size:
        count += 1
        return
    if a + enc <= board_size:
        tiling(board_size, a, b, a+enc)
    if b + enc<= board_size:
        tiling(board_size, a,b, b+enc)


def tiling1(board_size,  a, b):
    global call2
    call2 += 1
    global count
    if board_size==0:
        count += 1
        return count
    if board_size >a:
        if board_size -a in cache:
            res = cache[board_size-a]
        else:
            res = tiling(board_size-a, a, b)
            cache[board_size-a] = res
    if board_size > b:
        if board_size -b in cache:
            res1 = cache[board_size-b]
        else:
            res1 = tiling(board_size-b, a,b)
            cache[board_size-b] = res1
    print(cache)


r = (11,2,1)

tiling(*r)
print(count, call1)
count = 0
call2 = 0
tiling1(*r)
print(count, call2)