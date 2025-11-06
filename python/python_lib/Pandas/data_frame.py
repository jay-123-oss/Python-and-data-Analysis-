import pandas as pd

dict1 = {"name":["jaydeep","raja","ram","mohan"],"mark":[25,38,85,95,],"add":["sagar","bhopal","riwa","gowa"],"highest":[54,65,85,25,]}
df = pd.DataFrame(dict1)
print(df)

# coloum selection 
print(df[["name","mark"]])