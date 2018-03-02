from check_bst import check_bst, build_tree


def test_bad_tree_1():
    """
                887
            886
                885
        884
                883
            882
                881
    880
                879
            878
                875  # wrong
        876
                875
            874
                873
    """
    tree = build_tree("873 874 875 876 875 878 879 880 881 882 883 884 885 886 887")
    assert not check_bst(tree)


def test_bad_small_tree():
    """
       1
    2
       1
    """
    teeny_tree = build_tree("1 2 1")
    assert not check_bst(teeny_tree)


def test_monotonic_increasing_trees():
    """ trees that look like
            7
        6
            5
    4
            3
        2
            1
    """
    small_tree = build_tree("1 2 3")
    assert check_bst(small_tree)
    powers_of_2 = [(2**x) - 1 for x in range(3, 15)]
    for max_obj in powers_of_2:
        tree_str = " ".join(str(i) for i in range(max_obj))
        tree = build_tree(tree_str)
        assert check_bst(tree), "failed for tree [0..{}]".format(max_obj)
