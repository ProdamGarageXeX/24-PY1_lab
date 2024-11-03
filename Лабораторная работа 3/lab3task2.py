# TODO Напишите функцию find_common_participants
def find_common_participants(gr1, gr2, separator=','):
    participants1 = gr1.split(separator)
    participants2 = gr2.split(separator)

    common_participants = []
    for participant in participants1:
        if participant in participants2 and participant not in common_participants:
            common_participants.append(participant)

    common_participants.sort()

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common = find_common_participants(participants_first_group, participants_second_group, separator="|")
print(common)