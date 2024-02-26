#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque
from collections import Counter
from collections import defaultdict

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
    if c_lib <= c_road:
        return n * c_lib
    else:
        graph = defaultdict(list)
        for (x, y) in cities:
            graph[x].append(y)
            graph[y].append(x)
            
        cc = [-1] * (n+1)
        cc_tag = 0
        for i in range(1, n+1):
            if cc[i] == -1:
                queue = deque()
                queue.append(i)
                cc[i] = cc_tag
                while queue:
                    node = queue.popleft()
                    for neighbour in graph[node]:
                        if cc[neighbour] == -1:
                            queue.append(neighbour)
                            cc[neighbour] = cc_tag
                cc_tag += 1
        
        cc.remove(-1)
        # print(cc)
        cc = Counter(cc).values()
        # print(cc)
        return sum([(count-1)*c_road + c_lib for count in cc])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()
