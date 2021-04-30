import tensorflow as tf
from . import load_dataset

class DatasetLoader:
    @classmethod
    def load_data(cls, class_id, pad=True, onehot=True):
        return load_dataset(cls.source, pad, onehot, f'{cls.prefix}/{class_id}')

    @staticmethod
    def load_0(pad=True, onehot=True):
        return _parent.load_data(0, pad=pad, onehot=onehot)

class mnist(DatasetLoader):
    source = tf.keras.datasets.mnist
    prefix = 'standard/mnist'

