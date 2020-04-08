import pandas as pd
from openpyxl.workbook import Workbook

df_excel = pd.read_excel("test.xlsx")

# df_csv = pd.read_csv("test.csv")
# df_text = pd.read_csv("test.txt")
# print(df_excel)
# print("------------------------")
# print(df_csv)
# print("------------------------")
# print(df_text)

print(df_excel[['Name'][0]])


