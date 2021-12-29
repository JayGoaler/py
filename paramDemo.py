import pandas as pd
import warnings


def transportExcel(src, dst):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('ignore', ResourceWarning)
        df = pd.read_excel(src, header=None, engine="openpyxl")
    # print(df)
    df = df.T
    # print(df)
    # print(df.iloc[0, 0])
    # print(df.loc[0].values)
    df.to_excel(dst, header=None, index=False)


if __name__ == '__main__':
    transportExcel(r'D:\Downloads\2021-01至2021-11跨行转置测试.xlsx', r'D:\Downloads\2021-01至2021-11跨行转置测试(转).xlsx')
