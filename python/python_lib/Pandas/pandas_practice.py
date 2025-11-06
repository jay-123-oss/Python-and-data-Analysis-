import pandas as pd

df = pd.read_csv(r"C:\Users\jayde\Downloads\Python_Diwali_Sales_Analysis-main\Python_Diwali_Sales_Analysis-main\Diwali Sales Data.csv", 
 encoding="unicode_escape")
df.drop(["Status","unnamed1"],axis=1,inplace=True)

df.dropna(inplace=True)

df['Amount']=df["Amount"].astype("int")
df['Orders']=df['Orders'].astype("int")


# print(df[['Orders', 'Amount']].describe())
male = df[df["Gender"] == "M"]
male_amount = male["Amount"].sum()

# ✅ Female Amount Sum
female = df[df["Gender"] == "F"]
female_amount = female["Amount"].sum()

print(f"Total sales amount by Males: {male_amount}")
print(f"Total sales amount by Females: {female_amount}")



