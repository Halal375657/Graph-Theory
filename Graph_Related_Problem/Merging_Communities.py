

#
# https://www.hackerrank.com/challenges/merging-communities/problem
# Merging Communities
# 1.Initialization persons and results.
# 2Path Compression
# 3.I Connect with J
# 4.Finally, query.
#


class Network:
    def __init__(self, n):
        self.n = n
        self.persons = [None] * n
        self.results = [1] * n

        for i in range(self.n):
            self.make_set(i)
            
    def make_set(self, n):
        self.persons[n] = n

    def findRip(self, r):
        root = r
        while self.persons[root] != root:
            root = self.persons[root]

        while self.persons[root] != r:
            temp = self.persons[r]
            self.persons[r] = root
            r = self.persons[temp]

        return root

    def union(self, a, b):
        u, v = self.findRip(a), self.findRip(b)

        if v != u:
            self.persons[v] = u
            self.results[u] += self.results[v]

    def query(self, p):
        print(self.results[self.findRip(p)])



if __name__ == "__main__":
    
    n, q = map(int, input().split())
    sol = Network(n)
    
    for _ in range(q):
        query = input().split()
        if query[0] == "M":
            sol.union(int(query[1])-1, int(query[2])-1)
        else:
            sol.query(int(query[1])-1)
