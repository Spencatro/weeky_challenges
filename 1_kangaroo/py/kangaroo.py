import sys


def _parse_in_as_ints(strings):
    return [int(x) for x in strings]


def kangaroo(k1_pos, k1_speed, k2_pos, k2_speed):
    if k2_speed == k1_speed:
        return k1_pos == k2_pos
    x_intersect = (k1_pos - k2_pos) / float(k2_speed - k1_speed)
    y_intersect = k1_speed * x_intersect + k1_pos
    return 0 <= x_intersect and 0 <= y_intersect == int(y_intersect)


def kangaroo_BIGO_N(k1_pos, k1_speed, k2_pos, k2_speed):
    if k1_pos == k2_pos:
        return True
    if k1_speed == k2_speed:  # only works if also starting on same spot; we've already ruled it out
        return False
    if k1_pos > k2_pos and k1_speed >= k2_speed:
        return False
    if k1_pos < k2_pos and k1_speed <= k2_speed:
        return False
    # now we iterate for a while
    behind_pos = min(k1_pos, k2_pos)
    if behind_pos == k1_pos:
        behind_speed = k1_speed
        ahead_speed = k2_speed
    else:
        behind_speed = k2_speed
        ahead_speed = k1_speed
    ahead_pos = max(k1_pos, k2_pos)

    while behind_pos <= ahead_pos:
        # print("iteration: k1@{} hops {}, k2@{} hops {}".format(behind_pos, behind_speed, ahead_pos, ahead_speed))
        behind_pos += behind_speed
        ahead_pos += ahead_speed
        # print("end iteration: k1@{}, k2@{}".format(behind_pos, ahead_pos))
        if behind_pos == ahead_pos:
            return True
    return False


def _main():
    kangaroo(*_parse_in_as_ints(sys.argv[1:]))


if __name__ == '__main__':
    _main()