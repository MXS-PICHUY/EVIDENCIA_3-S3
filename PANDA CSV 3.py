import pandas as pd

df2=pd.read_csv("e2pandas.csv",header=None,
                names=["lenguaje","usuarios","hombres","mujeres"])

print(df2)