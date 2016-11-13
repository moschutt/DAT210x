"""
assignment3.py
"""
import pandas as pd

# Ensuring you set the appropriate header column names
#
# .. your code here ..
DATA = pd.read_csv('Datasets/servo.data',
                   header=None,
                   names=['motor', 'screw', 'pgain', 'vgain', 'class'])


# having a vgain equal to 5. Then print the
# length of (# of samples in) that slice:
#
# .. your code here ..
DATA_VGAIN = DATA[DATA.vgain == 5]
print(len(DATA_VGAIN))


# having a motor equal to E and screw equal
# to E. Then print the length of (# of
# samples in) that slice:
#
# .. your code here ..
DATA_E = DATA[(DATA.motor == 'E') & (DATA.screw == 'E')]
print(len(DATA_E))


# having a pgain equal to 4. Use one of the
# various methods of finding the mean vgain
# value for the samples in that slice. Once
# you've found it, print it:
#
# .. your code here ..
DATA_V = DATA[DATA.pgain == 4]
print(DATA_V.vgain.mean())


# the .dtypes method on your dataframe!
print(DATA.dtypes)
