import math


def solve(n, cities, start=None, end=None):
    best_route = []
    best_len = 0
    visited = [0] * (n + 1)
    visited[0] = 1

    if start == None:
        current_node = 1
    else:
        current_node = start

    while len(best_route) < n:
        best_route.append(current_node)
        visited[current_node] = 1
        if len(best_route) == n:
            break

        if current_node == end and end != None:
            break
        best_dist = float("inf")

        node = 1
        while(node <= n):
            if visited[node] == 0:
                if cities[current_node - 1][node - 1] - best_dist < pow(10, -3):
                    closest = node
                    best_dist = cities[current_node - 1][node - 1]
            node = node + 1

        current_node = closest
        best_len += best_dist

    if end == None:
        best_len += cities[current_node - 1][0]

    return best_len, best_route


def getdata():
    try:
        f = open("data.txt", "r")
    except IOError:
        print("Fisierul nu exista")

    dim = int(f.readline())
    m = []
    line = f.readline().strip()
    while line != "":
        el = line.split(",")
        l = []
        i = 0
        while i < dim:
            l.append(int(el[i]))
            i = i + 1
        m.append(l)
        line = f.readline().strip()

    f.close()

    return dim, m


def main():
    n, matrix = getdata()
    length, result = solve(n, matrix)
    print(length)
    print(result)


main()