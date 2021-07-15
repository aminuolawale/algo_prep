def matching_pair_sum(array):
    """ """
    fronti = 0
    backi = len(array) - 1
    while fronti != backi:
        sum = array[fronti] + array[backi]
        if sum < 8:
            fronti += 1
        elif sum == 8:
            return "YES"
        else:
            backi -= 1
    return "NO"


if __name__ == "__main__":
    array = [1, 3, 4, 4]
    answer = matching_pair_sum(array)
    print("the answer", answer)
