import pandas as pd

def solution(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Bỏ các cột có tỷ lệ giá trị thiếu > 0.5
    col_missing = df.isnull().mean()
    df = df.drop(columns=col_missing[col_missing > 0.5].index)
    
    # 2. Sau khi đã bỏ cột, bỏ các dòng có tỷ lệ giá trị thiếu (trên các cột còn lại) > 0.5
    row_missing = df.isnull().mean(axis=1)
    df = df.drop(index=row_missing[row_missing > 0.5].index)
    
    # 3. Điền giá trị thiếu:
    # - Cột số: dùng mean
    numeric_cols = df.select_dtypes(include='number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    
    # - Cột không phải số: dùng mode đầu tiên
    non_numeric_cols = df.select_dtypes(exclude='number').columns
    for col in non_numeric_cols:
        mode_val = df[col].mode()[0]
        df[col] = df[col].fillna(mode_val)
        
    # 4. Reset index về (0, 1, 2, ...)
    df = df.reset_index(drop=True)
    
    return df