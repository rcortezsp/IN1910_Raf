def less_than(original, n):
    n_list = [ i for i in original if i < n]
    return n_list

def test_less_than():
    list = [1,2,3,4,5,6,7,8,9]
    computed = less_than(list, 6)
    expected = [1,2,3,4,5]
    success = computed == expected
    assert success

test_less_than()
