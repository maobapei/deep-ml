import pandas as pd

def solution(df):
    # 1. Lọc status == 'completed'
    # df_filtered = ...
    df_filtered = df[df['status'] == 'completed']

    # 2. Gom nhóm theo region và tính tổng amount
    # df_grouped = ...
    df_grouped = df_filtered.groupby('region', as_index=False)['amount'].sum()

    # 3. Lấy top 10 amount lớn nhất và sắp xếp giảm dần
    # df_top10 = ...
    df_top10 = df_grouped.sort_values(by='amount', ascending=False).head(10)

    # 4. Reset index về dạng 0-based
    # result = ...
    result = df_top10.reset_index(drop=True)

    return result