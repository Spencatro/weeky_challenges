#!/bin/python3

import math


def max_distance_between_stations(s1, s2):
    """ given two station locations, determine the max distance any city between them would have

    :param s1: location of first city, or -1 if there isn't one
    :param s2: location of second city (or first city, if s1 is -1)
    :return:
    """
    diff = abs(s2 - s1)
    if s1 < 0:
        # in this case, no s1, so the map looks like:
        # C--C--C--S1
        # Where S is s2. Therefore, max distance is s2 - 0 = s2
        return s2
    # else, looks like this:
    # S0--C0--C1--C2--S1
    # Floor because odd maps (above) don't have to travel through themselves (i.e. C1 -> C0 -> S0 or C1 -> C2 -> S2)
    # Even maps divide evenly
    return math.floor(diff / 2)


def flatland_space_stations(map_size, city_indexes):
    max_distance = 0
    city_indexes.sort()
    for i in range(len(city_indexes)):
        if i == 0:
            distance_i = max_distance_between_stations(-1, city_indexes[i])
        else:
            distance_i = max_distance_between_stations(city_indexes[i], city_indexes[i - 1])
        if distance_i > max_distance:
            max_distance = distance_i
    # still must check the last city, it may not be a station
    distace_last_city = max_distance_between_stations(-1, map_size - city_indexes[-1] - 1)
    if distace_last_city > max_distance:
        max_distance = distace_last_city
    return max_distance


if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = flatland_space_stations(n, c)
    print(result)
