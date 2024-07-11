arr = [1, 2, 3, 4, 5]


def first_way():
    sum_list = []
    for index in range(len(arr)):
        sum_list.append(sum(arr[index + 1:] + arr[:index]))

    print(min(sum_list), max(sum_list))


def filter_way():
    sum_list = list(map(lambda idx: sum(arr[idx + 1:] + arr[:idx]), range(len(arr))))
    print(min(sum_list), max(sum_list))


first_way()
filter_way()
