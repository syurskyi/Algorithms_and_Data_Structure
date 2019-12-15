from itertools import count

import pandas as pd
import numpy as np

movie_excel_file = "https://bit.ly/2BVUyrO"


def explode(df, lst_cols, fill_value='', preserve_index=False):
    """Helper found on SO to split pipe (|) separted genres into
       multiple rows so it becomes easier to group the data -
       https://stackoverflow.com/a/40449726
    """
    if (lst_cols is not None and len(lst_cols) > 0 and not
    isinstance(lst_cols, (list, tuple, np.ndarray, pd.Series))):
        lst_cols = [lst_cols]
    idx_cols = df.columns.difference(lst_cols)
    lens = df[lst_cols[0]].str.len()
    idx = np.repeat(df.index.values, lens)
    res = (pd.DataFrame({
        col: np.repeat(df[col].values, lens)
        for col in idx_cols},
        index=idx)
           .assign(**{col: np.concatenate(df.loc[lens > 0, col].values)
                      for col in lst_cols}))
    if (lens == 0).any():
        res = (res.append(df.loc[lens == 0, idx_cols], sort=False)
               .fillna(fill_value))
    res = res.sort_index()
    if not preserve_index:
        res = res.reset_index(drop=True)
    return res


def group_by_genre(data=movie_excel_file):
    """Takes movies data excel file (https://bit.ly/2BXra4w) and loads it
       into a DataFrame (df).

       Explode genre1|genre2|genre3 into separte rows using the provided
       "explode" function we found here: https://bit.ly/2Udfkdt

       Filters out '(no genres listed)' and groups the df by genre
       counting the movies in each genre.

       Return the new df of shape (rows, cols) = (19, 1) sorted by movie count
       descending (example output: https://bit.ly/2ILODva)
    """
    df = pd.read_excel(data, skiprows=7, usecols='C:D')
    df = df.assign(genres=df.genres.str.split('|'))
    df = explode(df, 'genres')
    df = df[df.genres != '(no genres listed)']
    df = df.groupby('genres').agg(movie=('movie','count'))
    df = df.sort_values(by=['movie'], ascending=False)
    return df

