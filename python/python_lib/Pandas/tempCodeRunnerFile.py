import pandas as pd

df = pd.read_csv(r"C:\Users\jayde\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv", 
 encoding="unicode_escape")
df.drop(["Status","unnamed1"],axis=1,inplace=True)
