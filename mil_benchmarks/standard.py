import tensorflow as tf
from mil_benchmarks.utils import load_dataset

class DatasetLoader:
    @classmethod
    def load_all(cls, pad=True, onehot=True):
        return {
            f'{cls.name:}-0': cls.load_0(pad=pad, onehot=onehot),
            f'{cls.name:}-1': cls.load_1(pad=pad, onehot=onehot),
            f'{cls.name:}-2': cls.load_2(pad=pad, onehot=onehot),
            f'{cls.name:}-3': cls.load_3(pad=pad, onehot=onehot),
            f'{cls.name:}-4': cls.load_4(pad=pad, onehot=onehot),
            f'{cls.name:}-5': cls.load_5(pad=pad, onehot=onehot),
            f'{cls.name:}-6': cls.load_6(pad=pad, onehot=onehot),
            f'{cls.name:}-7': cls.load_7(pad=pad, onehot=onehot),
            f'{cls.name:}-8': cls.load_8(pad=pad, onehot=onehot),
            f'{cls.name:}-9': cls.load_9(pad=pad, onehot=onehot),
        }

    @classmethod
    def load_data(cls, class_id, pad=True, onehot=True):
        return load_dataset(cls.source, pad, onehot, f'standard.{cls.name}', f'{class_id}')

    @classmethod
    def load_0(cls, pad=True, onehot=True):
        return cls.load_data(0, pad=pad, onehot=onehot)

    @classmethod
    def load_1(cls, pad=True, onehot=True):
        return cls.load_data(1, pad=pad, onehot=onehot)

    @classmethod
    def load_2(cls, pad=True, onehot=True):
        return cls.load_data(2, pad=pad, onehot=onehot)

    @classmethod
    def load_3(cls, pad=True, onehot=True):
        return cls.load_data(3, pad=pad, onehot=onehot)

    @classmethod
    def load_4(cls, pad=True, onehot=True):
        return cls.load_data(4, pad=pad, onehot=onehot)

    @classmethod
    def load_5(cls, pad=True, onehot=True):
        return cls.load_data(5, pad=pad, onehot=onehot)

    @classmethod
    def load_6(cls, pad=True, onehot=True):
        return cls.load_data(6, pad=pad, onehot=onehot)

    @classmethod
    def load_7(cls, pad=True, onehot=True):
        return cls.load_data(7, pad=pad, onehot=onehot)

    @classmethod
    def load_8(cls, pad=True, onehot=True):
        return cls.load_data(8, pad=pad, onehot=onehot)

    @classmethod
    def load_9(cls, pad=True, onehot=True):
        return cls.load_data(9, pad=pad, onehot=onehot)

class mnist(DatasetLoader):
    source = tf.keras.datasets.mnist
    name = 'mnist'

class fashion(DatasetLoader):
    source = tf.keras.datasets.fashion_mnist
    name = 'fashion'

class cifar10(DatasetLoader):
    source = tf.keras.datasets.cifar10
    name = 'cifar10'