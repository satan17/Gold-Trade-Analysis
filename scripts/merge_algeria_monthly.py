import pandas as pd
import csv
import os
import glob

folders = [
    'algeria_monthly'
]

df_list = []

for folder in folders:
    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)

    relative_path_to_outside_folder = os.path.join("..", "datasets", folder)
    outside_folder_path = os.path.join(script_dir, relative_path_to_outside_folder)
    csv_files = glob.glob(os.path.join(outside_folder_path , "*"))
    print(csv_files)
    for file in csv_files:
        df = pd.read_excel(file)    
        df_list.append(df)



merged_df = pd.concat(df_list , ignore_index=False)
merged_df.to_excel('merged_algeria_monthly.xlsx' , index=False)