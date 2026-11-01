import pandas as pd

def solution(df):
    # làm sạch cột name
    df['name'] = df['name'].str.strip().str.title()
    # làm sạch cột date
    df['date'] = df['date'].str.strip()
    df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    # xóa trùng lặp
    df = df.drop_duplicates(keep = 'first').reset_index(drop=True)
    # điền khuyết thiếu = mean
    mean_val = df['value'].mean()
    df['value'] = df['value'].fillna(mean_val)
    return df
