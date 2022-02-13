task_list = list(range(1, 100))
cut_list = []
index_num = 0

while index_num < len(task_list) - 1:
    index_num += 1
    if (task_list[index_num] % 7 == 0) and (task_list[index_num] % 5 != 0):
        cut_list.append(task_list[index_num])

print(cut_list)