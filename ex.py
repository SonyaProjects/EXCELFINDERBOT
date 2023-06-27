import pandas as pd
xlsx = pd.ExcelFile('./База данных пользователей.xlsx')
df = pd.read_excel(xlsx, 'Sheet1')


def search_pass_name(name: str):
    row_num = 0
    for idx in df.index:
        row_num += 1
        if df['ФИО'].loc[idx] == name:
            break
    return df['Номер телефона'].loc[row_num-1]


def search_pass_id(id: int):
    row_num = 0
    for idx in df.index:
        row_num += 1
        if int(df['ИНН'].loc[idx] )== int(id):
            break
    return df['Номер телефона'].loc[row_num-1]


# print(search_pass_name('Иванов Иван Иванович'))
# print(search_pass_id(424346346))
