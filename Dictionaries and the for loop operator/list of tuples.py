 # list_of_tuples = []
 # for i in range(1, 10):
 #     j = i ** 2
 #     list_of_tuples.append((i, j))
 # print(list_of_tuples)

list_of_tuples = [(i, j) for i in range(1, 10) for j in (i * i, )]
print(list_of_tuples)
