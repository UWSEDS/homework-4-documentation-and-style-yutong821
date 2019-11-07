'''

1.Create a python module called test_dataframe.py that has a test
 that replicates what was done in item (2) for HW2.

'''
import unittest
import pandas as pd
import h2


class Testdataframe(unittest.TestCase):
    '''
        Testcase of dataframe
    '''
    def test_dataframe(self):
        '''
        recall hw2
        '''
        self.assertTrue(h2.test_create_dateframe(DATA_FRAME, COLUMNS_NAMES))


    def test_column_type(self):
        '''
        Check that all columns have values of the corect type.
        '''
        df_col = list(DATA_FRAME.columns)
        for i in df_col:
            new_df = []
            for j in DATA_FRAME[i]:
                new_df.append(type(j))
            for n_th_element in new_df:
                self.assertTrue(n_th_element == new_df[0])



    def test_nan_value(self):
        '''
        Check for nan values.
        '''
        for i in list(DATA_FRAME.columns):
            self.assertTrue(not pd.isna(DATA_FRAME[i]).any())


    def test_one_row(self):
        '''
        Verify that the dataframe has at least one row.
        '''
        num_of_rows = DATA_FRAME.count(axis='rows')
        for i in num_of_rows:
            self.assertTrue(int(i) > 1)


URL = 'https://inventory.data.gov/dataset/9b8df339-a659-4f7a-b6f0-de8e17964f68/\
resource/583cf78f-2508-4d21-a55d-3e3cb1dfff16/download/userssharedsdfteachingamericanhistory\
2010applicants.csv'

DATA_FRAME = h2.read(URL)
COLUMNS_NAMES = ['Project Title', 'City', 'State', 'ZIP', 'Award', 'Location']

if __name__ == '__main__':
    unittest.main(verbosity=2)
