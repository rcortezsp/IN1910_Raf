def factorize(number):
    list = []
    while number >1:
        for n in range(2,number+1):
            if number % n ==0:
                list.append(n)
                number /= n
                number = int(number)
                break
    return list

def test_factorize():
    assert factorize(412415) == [5, 82483]
    assert factorize(27) == [3,3,3]
    assert factorize(31) == [31]
    
test_factorize()
