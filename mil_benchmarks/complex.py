import tensorflow as tf
from mil_benchmarks.utils import load_dataset

class fashion:
    source = tf.keras.datasets.fashion_mnist

    @classmethod
    def load_data(cls, name, pad=True, onehot=True):
        return load_dataset(cls.source, pad, onehot, f'complex/fashion/{name}')
    
    @classmethod
    def load_basic_outfit(cls, pad=True, onehot=True):
        return cls.load_data('basic-outfit', pad=pad, onehot=onehot)

    @classmethod
    def load_multi_outfit(cls, pad=True, onehot=True):
        return cls.load_data('multi-outfit', pad=pad, onehot=onehot)