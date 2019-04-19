import numpy as np
import pandas as pd


def transform_columns(df, col_config):
    cols = col_config['columns']
    cols_name_map = {key: val[0] for key, val in cols.items()}
    cols_type_map = {key: val[1] for key, val in cols.items()}

    kwargs = {'errors': 'coerce'}

    for col_name, _type in cols_type_map.items():
        if _type in ('int'):
            df[col_name] = pd.to_numeric(df[col_name], **kwargs).fillna(0).astype(np.int64)
        elif _type in ('datetime', 'date', 'time'):   
            # df[col_name] = pd.to_datetime(df[col_name], infer_datetime_format=True, **kwargs)
            df[col_name] = df[col_name].astype(str)
        elif _type in ('str'):
            df[col_name] = df[col_name].astype(str)
        else:
            raise ValueError('There is no column type \'{}\''.format(_type))

    df = df.rename(index=str, columns=cols_name_map)

    return df
