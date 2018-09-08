# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

lst = [1, 2, 4, 5, 6, 2, 5, 2, 16, 16 ,72, 85, 90]

# неповторяющиеся элементы исходного списка
lst2 = list(set(lst))
print(lst2)

# элементы исходного списка, которые не имеют повторений
lst3 = []
for i in lst:
   if lst.count(i) == 1:
       lst3.append(i)
print(lst3)