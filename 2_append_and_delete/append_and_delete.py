import sys


def get_idx_last_same_char(s, t):
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
    return idx_last_same_char


def append_and_delete(k, s, t):
    if s == t:
        return k % 2 == 0 or k - 2 * len(s) >= 0
    if len(s) < len(t):  # assume the problem is identical regardless of order of s, t
        s, t = t, s
    if len(s) >= len(t):  # asdasd asd. need to trim s down to last idx_same
        idx_last_same = get_idx_last_same_char(s, t)  # find the last char where they match
        diff_spent_trimming = len(s) - idx_last_same  # calculate how much we have to trim
        diff_spent_adding = len(t) - idx_last_same    # calculate how much we would have to add
        diff_spent_getting_to_0 = idx_last_same * 2   # calculate how much we would have to spend to reduce the string to empty string
        total_diff_no_zero = diff_spent_adding + diff_spent_trimming  # calculate how much we trim total if we don't go to zero
        # first condition: easy way to stop early
        # however, if total_diff fits in k, we still either need:
        #     - the total difference left over to be even (add one, remove one, until we have used exactly k)
        #  OR - the total difference PLUS the amount spent getting to empty string fits
        #       (if we can get to empty string, we can beat the even rule by deleting a char from the empty string)
        return total_diff_no_zero <= k and ((total_diff_no_zero - k) % 2 == 0 or (total_diff_no_zero + diff_spent_getting_to_0) <= k)


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