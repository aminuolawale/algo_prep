from collections import OrderedDict

a = "abba"
d = OrderedDict()
for l in a:
    if not d.get(l):
        d[l] = 0
    d[l] += 1

print(d)