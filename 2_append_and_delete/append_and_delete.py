import sys


def append_and_delete(k, s, t):
    if s == t:
        return k % 2 == 0 or k - 2 * len(s) >= 0
    idx_last_same_char = 0
    max_len = max(len(s), len(t))
    for i in range(max_len):
        try:
            if s[i] == t[i]:
                idx_last_same_char += 1
            else:
                break
        except IndexError:
            break
    distance_s = max(0, len(s) - idx_last_same_char)
    distance_t = max(0, len(t) - idx_last_same_char)
    remains = k - (distance_s + distance_t)
    print(remains)
    return remains >= 0 and (remains % 2 == 0 or remains - (2 * len(s) - 1) > 0)


def _autocast(strings):
    new_list = []
    for x in strings:
        try:
            x = float(x)
            x_as_int = int(x)
            if int(x) == x_as_int:
                new_list.append(x_as_int)
            else:
                new_list.append(x)
        except ValueError:
            new_list.append(x)
    return new_list


def _main():
    append_and_delete(_autocast(sys.argv[1:]))


if __name__ == '__main__':
    _main()