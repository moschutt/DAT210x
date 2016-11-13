import pandas as pd


# TODO: Load up the table, and extract the dataset
# out of it. If you're having issues with this, look
# carefully at the sample code provided in the reading
#
# .. your code here ..
DATA = pd.read_html('http://www.espn.com/nhl/statistics/player/_/stat/points/sort/points/year/2015/seasontype/2')
DATA = DATA[0]
DATA = DATA.loc[2:, :]


# column definitions provided to you on the website
#
# .. your code here ..
DATA.columns = ['RK', 'PLAYER', 'TEAM', 'GP', 'G', 'A', 'PTS', '+/-', 'PIM',
                'PTS/G', 'SOG', 'PCT', 'GWG', 'PP-G', 'PP-A', 'SH-G', 'SH-A']

# TODO: Get rid of any row that has at least 4 NANs in it
#
# .. your code here ..
DATA = DATA.dropna(axis=0, thresh=4)


# TODO: At this point, look through your dataset by printing
# it. There probably still are some erroneous rows in there.
# What indexing command(s) can you use to select all rows
# EXCEPT those rows?
#
# .. your code here ..
DATA = DATA[DATA.RK != 'RK']


# TODO: Get rid of the 'RK' column
#
# .. your code here ..
DATA = DATA.iloc[:, 1:]


# TODO: Ensure there are no holes in your index by resetting
# it. By the way, don't store the original index
#
# .. your code here ..
DATA.reset_index(inplace=True)


# TODO: Check the data type of all columns, and ensure those
# that should be numeric are numeric
DATA.GP = pd.to_numeric(DATA.GP)
DATA.G = pd.to_numeric(DATA.G)
DATA.A = pd.to_numeric(DATA.A)
DATA.PTS = pd.to_numeric(DATA.PTS)
DATA.loc[:, '+/-'] = pd.to_numeric(DATA.loc[:, '+/-'])
DATA.PIM = pd.to_numeric(DATA.PIM)
DATA.loc[:, 'PTS/G'] = pd.to_numeric(DATA.loc[:, 'PTS/G'])
DATA.SOG = pd.to_numeric(DATA.SOG)
DATA.GWG = pd.to_numeric(DATA.GWG)
DATA.PCT = pd.to_numeric(DATA.PCT)
DATA.loc[:, 'PP-G'] = pd.to_numeric(DATA.loc[:, 'PP-G'])
DATA.loc[:, 'PP-A'] = pd.to_numeric(DATA.loc[:, 'PP-A'])
DATA.loc[:, 'SH-G'] = pd.to_numeric(DATA.loc[:, 'SH-G'])
DATA.loc[:, 'SH-A'] = pd.to_numeric(DATA.loc[:, 'SH-A'])


# TODO: Your dataframe is now ready! Use the appropriate 
# commands to answer the questions on the course lab page.

