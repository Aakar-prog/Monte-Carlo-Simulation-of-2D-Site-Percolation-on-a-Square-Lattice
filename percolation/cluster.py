from collections import deque


def neighbors(i, j, size):
    """
    Yield valid neighboring coordinates.
    """

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for di, dj in directions:
        ni = i + di
        nj = j + dj

        if 0 <= ni < size and 0 <= nj < size:
            yield ni, nj


def percolates(lattice):
    """
    Check if the lattice percolates from top to bottom.
    """

    size = lattice.shape[0]

    visited = set()
    queue = deque()

    # Start BFS (Breadth First Search) from open sites in the top row
    for j in range(size):
        if lattice[0, j] == 1:
            queue.append((0, j))
            visited.add((0, j))

    while queue:
        i, j = queue.popleft()

        # reached bottom row → percolation
        if i == size - 1:
            return True

        for ni, nj in neighbors(i, j, size):

            if lattice[ni, nj] == 1 and (ni, nj) not in visited:
                visited.add((ni, nj))
                queue.append((ni, nj))

    return False