# MIL Benchmarks

This repository contains a set of multiple-instance learning benchmarks
available through a python module. More details are available on arXiv: https://arxiv.org/abs/2105.01443

## Benchmarks
| Assumption | Source  | Function                            | Positive If         |
| ---------- | ------- | ----------------------------------- | ------------------- |
| Absence    | mnist   | `absence.mnist.load_01`             | 0 and 1 are absent  |
| Absence    | mnist   | `absence.mnist.load_12`             | 1 and 2 are absent  |
| Absence    | mnist   | `absence.mnist.load_23`             | 2 and 3 are absent  |
| Absence    | mnist   | `absence.mnist.load_34`             | 3 and 4 are absent  |
| Absence    | mnist   | `absence.mnist.load_45`             | 4 and 5 are absent  |
| Absence    | mnist   | `absence.mnist.load_56`             | 5 and 6 are absent  |
| Absence    | mnist   | `absence.mnist.load_67`             | 6 and 7 are absent  |
| Absence    | mnist   | `absence.mnist.load_78`             | 7 and 8 are absent  |
| Absence    | mnist   | `absence.mnist.load_89`             | 8 and 9 are absent  |
| Absence    | fashion | `absence.fashion.load_01`           | 0 and 1 are absent  |
| Absence    | fashion | `absence.fashion.load_12`           | 1 and 2 are absent  |
| Absence    | fashion | `absence.fashion.load_23`           | 2 and 3 are absent  |
| Absence    | fashion | `absence.fashion.load_34`           | 3 and 4 are absent  |
| Absence    | fashion | `absence.fashion.load_45`           | 4 and 5 are absent  |
| Absence    | fashion | `absence.fashion.load_56`           | 5 and 6 are absent  |
| Absence    | fashion | `absence.fashion.load_67`           | 6 and 7 are absent  |
| Absence    | fashion | `absence.fashion.load_78`           | 7 and 8 are absent  |
| Absence    | fashion | `absence.fashion.load_89`           | 8 and 9 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_01`           | 0 and 1 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_12`           | 1 and 2 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_23`           | 2 and 3 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_34`           | 3 and 4 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_45`           | 4 and 5 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_56`           | 5 and 6 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_67`           | 6 and 7 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_78`           | 7 and 8 are absent  |
| Absence    | cifar10 | `absence.cifar10.load_89`           | 8 and 9 are absent  |
| Complex    | fashion | `complex.fashion.load_basic_outfit` | See details below   |
| Complex    | fashion | `complex.fashion.load_multi_outfit` | See details below   |
| Presence   | mnist   | `presence.mnist.load_01`            | 0 or 1 are present  |
| Presence   | mnist   | `presence.mnist.load_12`            | 1 or 2 are present  |
| Presence   | mnist   | `presence.mnist.load_23`            | 2 or 3 are present  |
| Presence   | mnist   | `presence.mnist.load_34`            | 3 or 4 are present  |
| Presence   | mnist   | `presence.mnist.load_45`            | 4 or 5 are present  |
| Presence   | mnist   | `presence.mnist.load_56`            | 5 or 6 are present  |
| Presence   | mnist   | `presence.mnist.load_67`            | 6 or 7 are present  |
| Presence   | mnist   | `presence.mnist.load_78`            | 7 or 8 are present  |
| Presence   | mnist   | `presence.mnist.load_89`            | 8 or 9 are present  |
| Presence   | fashion | `presence.fashion.load_01`          | 0 or 1 are present  |
| Presence   | fashion | `presence.fashion.load_12`          | 1 or 2 are present  |
| Presence   | fashion | `presence.fashion.load_23`          | 2 or 3 are present  |
| Presence   | fashion | `presence.fashion.load_34`          | 3 or 4 are present  |
| Presence   | fashion | `presence.fashion.load_45`          | 4 or 5 are present  |
| Presence   | fashion | `presence.fashion.load_56`          | 5 or 6 are present  |
| Presence   | fashion | `presence.fashion.load_67`          | 6 or 7 are present  |
| Presence   | fashion | `presence.fashion.load_78`          | 7 or 8 are present  |
| Presence   | fashion | `presence.fashion.load_89`          | 8 or 9 are present  |
| Presence   | cifar10 | `presence.cifar10.load_01`          | 0 or 1 are present  |
| Presence   | cifar10 | `presence.cifar10.load_12`          | 1 or 2 are present  |
| Presence   | cifar10 | `presence.cifar10.load_23`          | 2 or 3 are present  |
| Presence   | cifar10 | `presence.cifar10.load_34`          | 3 or 4 are present  |
| Presence   | cifar10 | `presence.cifar10.load_45`          | 4 or 5 are present  |
| Presence   | cifar10 | `presence.cifar10.load_56`          | 5 or 6 are present  |
| Presence   | cifar10 | `presence.cifar10.load_67`          | 6 or 7 are present  |
| Presence   | cifar10 | `presence.cifar10.load_78`          | 7 or 8 are present  |
| Presence   | cifar10 | `presence.cifar10.load_89`          | 8 or 9 are present  |
| Standard   | mnist   | `standard.mnist.load_0`             | 0 is present        |
| Standard   | mnist   | `standard.mnist.load_1`             | 1 is present        |
| Standard   | mnist   | `standard.mnist.load_2`             | 2 is present        |
| Standard   | mnist   | `standard.mnist.load_3`             | 3 is present        |
| Standard   | mnist   | `standard.mnist.load_4`             | 4 is present        |
| Standard   | mnist   | `standard.mnist.load_5`             | 5 is present        |
| Standard   | mnist   | `standard.mnist.load_6`             | 6 is present        |
| Standard   | mnist   | `standard.mnist.load_7`             | 7 is present        |
| Standard   | mnist   | `standard.mnist.load_8`             | 8 is present        |
| Standard   | mnist   | `standard.mnist.load_9`             | 9 is present        |
| Standard   | fashion | `standard.fashion.load_0`           | 0 is present        |
| Standard   | fashion | `standard.fashion.load_1`           | 1 is present        |
| Standard   | fashion | `standard.fashion.load_2`           | 2 is present        |
| Standard   | fashion | `standard.fashion.load_3`           | 3 is present        |
| Standard   | fashion | `standard.fashion.load_4`           | 4 is present        |
| Standard   | fashion | `standard.fashion.load_5`           | 5 is present        |
| Standard   | fashion | `standard.fashion.load_6`           | 6 is present        |
| Standard   | fashion | `standard.fashion.load_7`           | 7 is present        |
| Standard   | fashion | `standard.fashion.load_8`           | 8 is present        |
| Standard   | fashion | `standard.fashion.load_9`           | 9 is present        |
| Standard   | cifar10 | `standard.cifar10.load_0`           | 0 is present        |
| Standard   | cifar10 | `standard.cifar10.load_1`           | 1 is present        |
| Standard   | cifar10 | `standard.cifar10.load_2`           | 2 is present        |
| Standard   | cifar10 | `standard.cifar10.load_3`           | 3 is present        |
| Standard   | cifar10 | `standard.cifar10.load_4`           | 4 is present        |
| Standard   | cifar10 | `standard.cifar10.load_5`           | 5 is present        |
| Standard   | cifar10 | `standard.cifar10.load_6`           | 6 is present        |
| Standard   | cifar10 | `standard.cifar10.load_7`           | 7 is present        |
| Standard   | cifar10 | `standard.cifar10.load_8`           | 8 is present        |
| Standard   | cifar10 | `standard.cifar10.load_9`           | 9 is present        |
