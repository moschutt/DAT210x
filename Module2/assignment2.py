"""
assignment2 module
"""
import pandas as pd
#
# .. your code here ..
TDATA = pd.read_csv('Datasets/tutorial.csv')

#
# .. your code here ..
print(TDATA.describe())

# use in order to index your dataframe with: [2:4,'col3']
# And print the results
#
# .. your code here ..
print(TDATA.loc[2:4, 'col3'])
