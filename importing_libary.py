# import math
# result = math.sqrt(16)
# print(result)

# import math

# def result(number):
#     resultt = math.sqrt(number)
#     return resultt

# print(result(8))

# def result(number):
#     if number < 0:
#      return "just"
#     result = math.log2(number)
#     return result
# print(result(10))

from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
 return "<p>hello, world!</p>"
print(app)
 # Creating arrays
# import numpy as np
# arr = np.array([1, 2, 3, 4, 5])
# matrix = np.array([[1, 2, 3], [4, 5, 6], [6, 5,1]])

# mean = np.mean(arr)
# std = np.std(arr)
# reshaped = arr.reshape(5, 1)
# print(matrix)

# import pandas as pd
# series = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['NYC', 'LA', 'Chicago']
#  })

# df = pd.read_csv('Nigeria_Retail_Sales_2023_2024.csv')
# df_start = df.describe()
# # print(df_start)

# missing_value = df.isnull().sum()
# print(missing_value)

#  df['numeric_column'].fillna(df['numeric_column'].median(), inplace=True)