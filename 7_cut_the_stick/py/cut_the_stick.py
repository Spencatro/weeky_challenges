from six.moves import input


def cut_the_stick(sticks):
    stickt_dict = {}
    start_count = len(sticks)
    for stick in sticks:
        if stick not in stickt_dict:
            stickt_dict[stick] = 0
        stickt_dict[stick] += 1
    results = [start_count] if start_count else []
    keys = list(stickt_dict.keys())
    keys.sort()
    for key in keys:
        start_count -= stickt_dict[key]
        if start_count:
            results.append(start_count)
    return results


def slow_cut_the_stick(sticks):
    sticks.sort()
    results = []
    while sticks:
        results.append(len(sticks))
        stick_cut_length = sticks[0]
        new_sticks = []
        for stick in sticks:
            if stick == stick_cut_length:
                continue
            else:
                new_sticks.append(stick - stick_cut_length)
        sticks = new_sticks
    return results

