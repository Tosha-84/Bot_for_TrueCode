import pandas as pd

# data = [['Гамаюнова Аделина', '89842740104'], ['Вилачёв Антон', '89148891191']]
# excel_file = "numbers.xlsx"


def create_excel(data, filename):
    df = pd.DataFrame(data, columns=['ФИО', 'Номер'])
    df.to_excel(filename, index=False)


async def parse_excel(filename):
    users_dict = {}
    parsed_df = pd.read_excel(filename)
    for index, row in parsed_df.iterrows():
        # users_dict[row['ФИО']] = row['Номер']
        users_dict[row['Номер']] = row['ФИО']
    return users_dict


# users = parse_excel(excel_file)
# print(users)
