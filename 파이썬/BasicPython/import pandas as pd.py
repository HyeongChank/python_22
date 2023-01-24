import pandas as pd


df = pd.read_excel('(본 최신)비즈니스서비스기업 참여 현황(2.7.).xlsx')

df_list = df.values.tolist()

print(df)

