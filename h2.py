# Homework 2 Yutong Liu

# 1 . (1 points) Write a python reads creates a dataframe from a URL
# that points to a CSV file such as the pronto data or CSVs in data.gov.

import pandas as pd


def read(url):
    #  create data frame
    df = pd.read_csv(url)
    return df

def test_create_dateframe(df, columnsName):
    df_col = list(df.columns)


    if df_col == columnsName:
        condition_1 = 1
    else:
        condition_1 = 0

    for i in df_col:
        df_col = list(df.columns)
        for i in df_col:
            l = []
            for j in df[i]:
                l.append(type(j))
            for i in l:
                if i != l[0]:
                    condition_2 = 0
                else:
                    condition_2 = 1


    numOfRows = df.count(axis='rows')
    for i in numOfRows:
        if int(i) > 10:
            condition_3 = 1
        else:
            condition_3 = 0

    if condition_1 and condition_2 and condition_3:
        print('True')
        return True
    else:
        print('False')
        return False

