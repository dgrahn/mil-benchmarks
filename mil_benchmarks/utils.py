import numpy as np
import pandas as pd
import pkg_resources
import tensorflow as tf

from pathlib import Path

def load_dataset(source, pad, onehot, prefix):
    (xi_train, _), (xi_test, _) = source.load_data()
    return (
        load_mil(xi_train, pad, onehot, prefix + '_train.csv'),
        load_mil(xi_test, pad, onehot, prefix + '_test.csv')
    )

def load_mil(x_orig, pad, onehot, csv):
    base = Path(pkg_resources.resource_string(__file__, 'csvs'))
    df = pd.read_csv(base.joinpath('csvs').joinpath(csv))

    if pad:
        x = np.zeros((df.shape[0], df.shape[1] - 1) + x_orig[0].shape)

        for i, r in df.iterrows():
            idx = r[1:][r[1:] != -1]
            x[i, :idx.shape[0]] = x_orig[idx]

    else:
        x = list([
            list(x_orig[i] for i in r[1:])
            for _, r in df.iterrows()
        ])
    
    if onehot:
        y = tf.one_hot(df.y, df.y.max() + 1).numpy()
    else:
        y = df.y.values

    return x, y