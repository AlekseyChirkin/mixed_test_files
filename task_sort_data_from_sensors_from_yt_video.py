sensor1_data = [
    "2024-03-191 datafromsensor2221 veryimportentintdata1",
    "2024-43-211 datafromsensor2221 veryimportentintdata56465487981631684964",
    "2024-23-11 datafromsensor2221 veryimportentintdata564654879816316845964",
    "2024-03-191 datafromsensor2221 veryimportentintdata5646548798163163454964",
    "2024-03-41 datafromsensor2221 veryimportentintdata56465487981631686434564",
    "2024-03-101 datafromsensor2221 veryimportentintdata56465487981631684964",
    "2024-03-31 datafromsensor2221 veryimportentintdata56465487981631684964",
    "2024-03-10 datafromsensor2221 veryimportentintdata56465487981631684964",
    "2024-03-191 datafromsensor2221 veryimportentintdata2",
    "2024-03-13 datafromsensor2221 veryimportentintdata5646548798163164584964",
    "2024-03-41 datafromsensor2221 veryimportentintdata56465487981631684964",
    "2024-03-81 datafromsensor2221 veryimportentintdata56465487981631684964",
]
sensor2_data = [
    "2024-053-191 datafromsensor555 veryimportentintdata56465487981631683454964",
    "2024-423-211 datafromsensor555 veryimportentintdata56465487981631684964",
    "2024-243-11 datafromsensor555 veryimportentintdata56465487981631684345964",
    "2024-503-121 datafromsensor555 veryimportentintdata56465487981631684964",
    "2024-03-191 datafromsensor555 veryimportentintdata64",
    "2024-03-01 datafromsensor555 veryimportentintdata56465487981631684964",
    "2024-03-31 datafromsensor555 veryimportentintdata56465487981631683454964",
    "2024-01-123 datafromsensor555 veryimportentintdata56465487981631684964",
    "2024-14-11 datafromsensor555 veryimportentintdata56465487981631684964",
    "2024-03-191 datafromsensor555 veryimportentintdata56465487981631684964",
    "2024-63-41 datafromsensor555 veryimportentintdata5646548798163163454964",
    "2024-43-81 datafromsensor555 veryimportentintdata56465487981631684964",
]


def combine_sensors_data(list1: list, list2: list) -> list:
    # total_data = list1 + list2
    # total_data_list = []

    # for rec in total_data:
    #     data = rec.split(' ')
    #     data_rec = {
    #         'time': data[0],
    #         'data1': data[1],
    #         'data2': data[2]
    #     }
    #     total_data_list.append(data_rec)

    # return sorted(total_data_list, key=lambda x: x['time'])

    return sorted(list1 + list2, key=lambda x: (x.split(' ')[0], x.split(' ')[2]))


res = combine_sensors_data(sensor2_data, sensor1_data)
# print(res)
for x in res:
    print(x)
