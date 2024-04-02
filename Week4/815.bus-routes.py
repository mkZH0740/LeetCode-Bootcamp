from typing import List
from math import inf


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0

        maxBusStop = max(max(route) for route in routes)
        if maxBusStop < target or maxBusStop < source:
            return -1

        minNumBusesToBusStop = [inf] * (maxBusStop + 1)
        minNumBusesToBusStop[source] = 0

        notFound = True
        while notFound:
            notFound = False
            for route in routes:
                currMin = inf

                for stop in route:
                    currMin = min(currMin, minNumBusesToBusStop[stop])
                currMin += 1

                for stop in route:
                    if minNumBusesToBusStop[stop] > currMin:
                        minNumBusesToBusStop[stop] = currMin
                        notFound = True

        if minNumBusesToBusStop[target] < inf:
            return minNumBusesToBusStop[target]
        else:
            return -1
