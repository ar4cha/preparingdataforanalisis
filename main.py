import pandas as pd
import numpy  as np
import yfinance as yf
print("---------------------------------------------------------------------------------")
print("enter ticker")
a = input()
msft = yf.Ticker(a)
print(msft.recommendations)
print(msft.dividends)

print("---------------------------------------------------------------------------------")
# Importing data from CSV file:
df = pd.read_csv('cereal.csv')

# Getting the dimensions of the dataframe:
#print(df.shape)

print(df.info())
# Getting the structure of the dataframe:
#print(df.info())

# Setting column names: 

print(df.head())

# Changing column names:
df.columns = ["name","mfr","type","calories","protein","fat","sodium","fiber","carbo","sugars","potass","vitamins","shelf","weight","cups","rating"]
print("List of column names: ", df.columns)

# Counting number of missing vals:
missing = df.isnull().sum().reset_index(name='Missing Values Counted')
print("Table with missing values counted: \n", missing)

# Dropping Missing:
df_complete = df.dropna() 
cereal = np.array(df_complete)
print(cereal.shape)

print("---------------------------------------------------------------------------------")
first_cereal_data= cereal[1,6]
print(first_cereal_data)
print("---------------------------------------------------------------------------------")
cereal_name= cereal[:,4]
print(cereal_name)
("---------------------------------------------------------------------------------")
print("minimum:",np.amin(cereal[:,3]))
print("maximum:",np.amax(cereal[:,3]))
print("---------------------------------------------------------------------------------")
print("Top 5")
sorted_by_name =  cereal[cereal[:,0].argsort()]
print(sorted_by_name[0:5])
print("---------------------------------------------------------------------------------")

print(np.mean(cereal[:,3]))