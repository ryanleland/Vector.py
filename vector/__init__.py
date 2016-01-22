#!/usr/bin/env python

__version__ = '0.0.3'

from math import sqrt, acos, degrees


class Vector(object):

    def __init__(self, *coordinates):
        self.coordinates = coordinates
        self.index = 0

    @property
    def x(self):
        return self.coordinates[0]

    @property
    def y(self):
        return self.coordinates[1]

    @property
    def z(self):
        return self.coordinates[2]

    @property
    def magnitude(self):
        return abs(sqrt(sum(c ** 2 for c in self)))

    def normalize(self):
        return self / self.magnitude

    def dot(self, other):
        return sum(a * b for a, b in zip(self, other))

    def angle_in_radians(self, other):
        return acos(self.dot(other) / (self.magnitude * other.magnitude))

    def angle(self, other):
        return degrees(self.angle_in_radians(other))

    def __len__(self):
        return len(self.coordinates)

    def __iter__(self):
        return iter(self.coordinates)

    def __getitem__(self, index):
        return self.coordinates[index]

    def __add__(self, other):
        coordinates = (a + b for a, b in zip(self, other))
        return Vector(*coordinates)

    def __sub__(self, other):
        coordinates = (a - b for a, b in zip(self, other))
        return Vector(*coordinates)

    def __mul__(self, other):
        coordinates = (c * other for c in self)
        return Vector(*coordinates)

    def __div__(self, other):
        coordinates = (c / other for c in self)
        return Vector(*coordinates)

    def __str__(self):
        return str(self.coordinates)

    def __repr__(self):
        return str(self)
