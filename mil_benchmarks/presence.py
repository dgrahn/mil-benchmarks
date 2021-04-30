import tensorflow as tf
from mil_benchmarks.utils import load_dataset

class DatasetLoader:
    @classmethod
    def load_all(cls, pad=True, onehot=True):
        return [
            cls.load_01(pad=pad, onehot=onehot),
            cls.load_12(pad=pad, onehot=onehot),
            cls.load_23(pad=pad, onehot=onehot),
            cls.load_34(pad=pad, onehot=onehot),
            cls.load_45(pad=pad, onehot=onehot),
            cls.load_56(pad=pad, onehot=onehot),
            cls.load_67(pad=pad, onehot=onehot),
            cls.load_78(pad=pad, onehot=onehot),
            cls.load_89(pad=pad, onehot=onehot),
        ]

    @classmethod
    def load_data(cls, class_id, pad=True, onehot=True):
        return load_dataset(cls.source, pad, onehot, f'presence/{cls.name}/{class_id}')

    @classmethod
    def load_01(cls, pad=True, onehot=True):
        return cls.load_data('01', pad=pad, onehot=onehot)

    @classmethod
    def load_12(cls, pad=True, onehot=True):
        return cls.load_data('12', pad=pad, onehot=onehot)

    @classmethod
    def load_23(cls, pad=True, onehot=True):
        return cls.load_data('23', pad=pad, onehot=onehot)

    @classmethod
    def load_34(cls, pad=True, onehot=True):
        return cls.load_data('34', pad=pad, onehot=onehot)

    @classmethod
    def load_45(cls, pad=True, onehot=True):
        return cls.load_data('45', pad=pad, onehot=onehot)

    @classmethod
    def load_56(cls, pad=True, onehot=True):
        return cls.load_data('56', pad=pad, onehot=onehot)

    @classmethod
    def load_67(cls, pad=True, onehot=True):
        return cls.load_data('67', pad=pad, onehot=onehot)

    @classmethod
    def load_78(cls, pad=True, onehot=True):
        return cls.load_data('78', pad=pad, onehot=onehot)

    @classmethod
    def load_89(cls, pad=True, onehot=True):
        return cls.load_data('89', pad=pad, onehot=onehot)

class mnist(DatasetLoader):
    source = tf.keras.datasets.mnist
    name = 'mnist'

class fashion(DatasetLoader):
    source = tf.keras.datasets.fashion_mnist
    name = 'fashion'

class cifar10(DatasetLoader):
    source = tf.keras.datasets.cifar10
    name = 'cifar10'