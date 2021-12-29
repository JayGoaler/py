import sys
import pandas as pd
import warnings


def transportExcel(src, dst):
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('ignore', ResourceWarning)
        df = pd.read_excel(src, header=None, engine="openpyxl")
    df = df.T
    df.to_excel(dst, header=None, index=False)


if __name__ == '__main__':
    transportExcel(sys.argv[1], sys.argv[2])
