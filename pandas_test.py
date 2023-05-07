import pandas as pd


width = [5, 10, 10, 25]
headings = ['id','first_name','last_name','occupation']

file1 = pd.read_fwf("/Users/dereksmart/Documents/fixed_width_test.txt",
                   widths=width, header=None, names=headings)
print(file1.head())

width = [5, 10, 10, 25]
headings = ['id','extra_1','extra_2','extra_3']

file2 = pd.read_fwf("/Users/dereksmart/Documents/fixed_width_test2.txt",
                   widths=width, header=None, names=headings)
print(file2.head())

file3 = pd.merge(file1[['id','occupation']], file2[['id','extra_1']], on='id', how='inner')
print("Final merged file")
print(file3.head())