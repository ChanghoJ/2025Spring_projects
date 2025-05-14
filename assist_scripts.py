'''
IS 597 PY - Final Project:
Name: Changho Jung, Prisha Singhania

The following code is handwork by Changho.
The purpose of the code is:
1. Merge two dataframes.
2. Merge two series.
'''

import pandas as pd

def merge(merge_on_df:pd.DataFrame, merge_from_df:pd.DataFrame, merge_from_keep:list[str],
          foreign_key_left:str, foreign_key_right:str=None, merge_direction:str='left') -> pd.DataFrame:
    '''
    This is a function to merge two dataframes.

    :param merge_on_df: pandas dataframe. Dataframe to merge on.
    :param merge_from_df: pandas dataframe. Dataframe to merge from.
    :param merge_from_keep: list of strings. Columns to keep from merge_from_df.
    :param foreign_key_left: string. Foreign key to merge on.
    :param foreign_key_right: string. Foreign key to merge from. Not strictly required if merging dataframe have same foreign key name, foreign_key_right=None.
    :param merge_direction: string. Direction of merge, merge_on_df or merge_from_df.
    :return: pandas dataframe. Merged dataframe.

    >>> test_df1 = pd.DataFrame({'key':[1,2,3], 'value_x':[1,2,3]})
    >>> test_df2 = pd.DataFrame({'key':[1,2,3], 'value_y':[4,5,6]})
    >>> merge(merge_on_df=test_df1, merge_from_df=test_df2, merge_from_keep=['key', 'value_y'], foreign_key_left='key')
       key  value_x  value_y
    0    1        1        4
    1    2        2        5
    2    3        3        6
    '''
    return merge_on_df.merge(merge_from_df[merge_from_keep], on=foreign_key_left, how=merge_direction) \
        if foreign_key_right is None \
        else merge_on_df.merge(merge_from_df[merge_from_keep], left_on=foreign_key_left, right_on=foreign_key_right, how=merge_direction)

def fips_merger(state_fips:pd.Series, country_fips:pd.Series) -> pd.Series:
    '''
    This is a function to merge two series of FIPS codes, intended for pandas series of state and country FIPS codes. specifically

    :param state_fips: pandas series. State FIPS code.
    :param country_fips: pandas series. Country FIPS code.
    :return: pandas series. FIPS code that combines state_fips and country_fips

    >>> test_series1 = pd.Series(['01','02','03'])
    >>> test_series2 = pd.Series(['400','050','006'])
    >>> fips_merger(test_series1, test_series2)
    0    01400
    1    02050
    2    03006
    dtype: object
    '''
    return (state_fips.astype(int).astype(str).str.zfill(2) +
            country_fips.astype(int).astype(str).str.zfill(3))