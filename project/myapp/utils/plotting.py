import io
import matplotlib
matplotlib.use('agg') # Should be called before pyplot import

import matplotlib.pyplot as plt
import numpy as np
from random import choice
from PIL import Image
from string import ascii_uppercase


def plot_barchart(dist, threshold=0, title=None, x_label=None, y_label=None):
    x = np.array([v[0] for v in dist]).astype(np.int32)
    y = np.array([v[1] for v in dist]).astype(np.int32)

    ixs = y > threshold
    x, y = x[ixs], y[ixs]

    idxs = np.arange(len(x))
    width = 0.8

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(idxs - width/2, y, width, color='SkyBlue')

    if title is not None:
        ax.set_title(title)

    ax.set_xticks(idxs)
    ax.set_xticklabels(tuple(x), rotation=45, ha='right')

    if x_label is not None:
        ax.set_xlabel(x_label)

    if y_label is not None:
        ax.set_ylabel(y_label)

    plt.tight_layout()

    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    return buf


def generate_random_name(length=16):
    return ''.join(choice(ascii_uppercase) for i in range(length))
