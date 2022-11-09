import pandas as pd
import re

# data = [['Гамаюнова Аделина', '89842740104'], ['Вилачёв Антон', '89148891191']]
# excel_file = "numbers.xlsx"


def create_excel(data, filename):
    df = pd.DataFrame(data, columns=['ФИО', 'Номер'])
    df.to_excel(filename, index=False)


async def parse_number(df):
    num_re = re.compile(r".*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*(\d).*")
    df['Номер'] = df['Номер'].apply(lambda x: "+7" + ''.join(num_re.match(str(x)).groups()))
    return df


async def parse_excel(filename):
    users_dict = {}
    parsed_df = await parse_number(pd.read_excel(filename))
    for index, row in parsed_df.iterrows():
        users_dict[row['Номер']] = row['ФИО']
    return users_dict


# users = parse_excel(excel_file)
# print(users)
