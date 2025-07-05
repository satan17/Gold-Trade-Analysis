import pandas as pd
import csv
import os
import glob

folders = [
    'burkino_monthly'
]

df_list = []

for folder in folders:
    csv_files = glob.glob(os.path.join(folder , "*"))
    for file in csv_files:
        df = pd.read_excel(file)
        
        df_list.append(df)



merged_df = pd.concat(df_list , ignore_index=False)
merged_df.to_excel('merged_burkina_faso_monthly.xlsx' , index=False)