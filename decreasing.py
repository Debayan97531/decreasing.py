string = input("Enter the string : ")


def most_frequent(string):
    dic = {i: string.count(i) for i in string}
    li = list(map(lambda i: (i[1], i[0]), list(dic.items())))
    li.sort(reverse=True)
    for i in li:
        print(i[1])


most_frequent(string)
