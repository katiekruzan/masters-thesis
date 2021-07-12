"""
Here we're going to code for the local rotations. We're doing an object oriented approach
"""

__version__ = 1.0
__author__ = 'Katie Kruzan'

import string # just to get the alphabet easily itterable


# Getting the structure for the classes we're putting together
class Segment:
    """
    These are going to represent the outer segments and the mysteries they hold
    """
    def __init__(self, name, left, right):
        self.leftOuter = left
        self.rightOuter = right
        self.name = name

    # TODO: Force object types in the init
    # def __setattr__(self, name, value):
    #     if name in ['leftOuter', 'rightOuter'] and not isinstance(value, Outer):
    #         raise TypeError('Segment.leftOuter must be an Outer object')
    #     super().__setattr__(name, value)

    def getName(self):
        return self.name

    def getLeftVertex(self):
        return self.leftVertex

    def getRightVertex(self):
        return self.rightVertex


class Outer:
    """
    Class to represent the outer vertices that are adjacent to an inner vertex and 2 outer segments
    """
    def __init__(self, name, inner, left, right):
        self.adjInner = inner
        self.leftSegment = left
        self.rightSegment = right
        self.name = name

    def getName(self):
        return self.name

    def getLeftSegment(self):
        return self.leftSegment

    def getRightSegment(self):
        return self.rightSegment

    def getAdjInner(self):
        return self.adjInner


class Inner:
    """
    Class to represent the inner vertices that are adjacent to an outer vertex and 2 neighboring inner vertices
    """
    def __init__(self, name, outer, left, right):
        self.adjOuter = outer
        self.leftInner = left
        self.rightInner = right
        self.name = name

    def getName(self):
        return self.name

    def getLeftInner(self):
        return self.leftInner

    def getRightInner(self):
        return self.rightInner

    def getAdjOuter(self):
        return self.adjOuter


def standardCircle(num_verts):
    """
    This will go through and initialize our standard circle
    :param num_verts:
    :return:
    """
    segs = None
    outs = None
    ins = None
    i = 0
    while i < num_verts-1:

        continue
    string.ascii_letters
    return
