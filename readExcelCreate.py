import pandas as pd


file1 = pd.read_csv("file1.csv")
condition_data = (file1['delegate_descriptor_condition_settings'][0])

descriptor, page1 = list(condition_data.split(","))

