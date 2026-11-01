import pandas as pd

def solution(df1, df2, df3):
    first_merged = pd.merge(df1, df2, on = 'emp_id', how = 'inner')
    second_merged = pd.merge(first_merged, df3, on = 'emp_id', how = 'left')
    return second_merged