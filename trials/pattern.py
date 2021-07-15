a = "jquery"
s = "jquery"


def build_map(st, pattern=False):
    if not pattern:
        st = st.split(" ")
    d = {}
    for i, l in enumerate(st):
        if not l in d:
            d[l] = []
        d[l].append(i)
    return d


def compare(a, b):
    for x, y in zip(a.values(), b.values()):
        if x != y:
            return False
    return True


x = build_map(a, True)
y = build_map(s)
print(x)
print(y)
print(compare(x, y))
