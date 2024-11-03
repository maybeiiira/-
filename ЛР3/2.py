# TODO Напишите функцию find_common_participants
def find_common_participants(str1_, str2_, n=','):
    set_first = set(str1_.split(n))
    list_second = str2_.split(n)
    common_set = set_first.intersection(list_second)
    common_list = []
    for i in common_set:
        common_list.append(i)
    common_list.sort()
    return(common_list)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, )
# TODO Провеьте работу функции с разделителем отличным от запятой
