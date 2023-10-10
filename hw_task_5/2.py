import pandas as pd
import matplotlib.pyplot as plt

apple = pd.DataFrame({
    'id' : ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Column_1': [2015, 2017, 2018, 2019, 2027, 2035, 2040, 2050, 2525, 2121],
    'Column_2': [129, 128, 128, 118, 117, 116, 125, 125, 123, 147],
    'Column_3': [129, 128, 128, 118, 117, 116, 125, 125, 123, 147],
    'Column_4': [129, 128, 128, 118, 117, 116, 125, 125, 123, 147],
    'Column_5': [129, 128, 128, 118, 117, 116, 125, 125, 123, 147],
    'Column_6': [2015, 2017, 2018, 2019, 2027, 2035, 2040, 2050, 2525, 2121],
    'Column_7': [129, 128, 128, 118, 117, 116, 125, 125, 123, 147],
    'Column_8': [129, 128, 128, 118, 117, 116, 125, 125, 123, 147],
    'Column_9': [129, 128, 128, 118, 117, 116, 125, 125, 123, 147],
    'Column_10': [129, 128, 128, 118, 117, 116, 125, 125, 123, 147],

}).set_index('id')

print(apple[apple > 5])
