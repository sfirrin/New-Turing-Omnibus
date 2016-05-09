
class lincongmethod:
    def __init__(self, k, c, m, x0):
        self.k = k
        self.c = c
        self.m = m
        self.x = x0
    def get_random(self):
        previous = self.x
        self.x = (self.k*previous + self.c) % self.m
        return previous
    def get_random_list(self, n):
        randoms = []
        for i in range(n):
            randoms.append(self.get_random())
        return randoms

# Problem 1 - Find a combination of k and c that, with m = 100, produces
# a random looking sequence with a period of 50

best_k_c = [1, 1, 0]

# When I started k and c at 1 and they just gave me the ints from 1 to 100

for k in range(19, 100):
    for c in range(51, 100):
        l = lincongmethod(k, c, 100, 25)
        rlist = l.get_random_list(200)
        duplicates = [x for x in rlist if rlist.count(x) > 1]
        first_dupe = rlist.index(duplicates[0])
        second_dupe = rlist[first_dupe+1:].index(duplicates[0])
        if second_dupe > best_k_c[2]:
            best_k_c = [k, c, second_dupe]

print(best_k_c)
print(lincongmethod(best_k_c[0], best_k_c[1], 100, 25).get_random_list(200))