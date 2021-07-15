# pretty simple algorithm
# min(r, w*h)//2 + 1 represent the number of plains. We are subtracting it because we don't want to count plains.


count = 0
cache = {}


def execute(r, w, h):
    return mountain_scenes(r,w, h) - (min(r, w*h)//w+ 1)

def mountain_scenes(ribbon_length, width, height, history="") -> int:
    global count
    if width == 0:
        return 1
    res = 0
    for i in range(height + 1):
        if ribbon_length - i >= 0:
            if cache.get((ribbon_length-i, width-1)):
                res += cache[(ribbon_length-i, width-1)]
            else:
                res += mountain_scenes(
                    ribbon_length - i, width - 1, height, history + str(i)
                )
    cache[(ribbon_length, width)] = res
    return res


if __name__ == "__main__":
    print(execute(60, 11, 10))
