def has_negatives(a):

    cache ={}
    result = []
    for i in a:
        if abs(i) not in cache:
            if i > 0:
                cache[abs(i)] = 'POS'
            else:
                cache[abs(i)] = 'NEG'
        else:
            if i > 0:
                cache[abs(i)] == 'NEG'
                result.append(abs(i))
            elif i < 0:
                cache[abs(i)] == 'POS'
                result.append(abs(i))
    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
