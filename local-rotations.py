"""
Here we're going to code for the local rotations. We're doing an object oriented approach
"""

__version__ = 1.0
__author__ = 'Katie Kruzan'

import string  # just to get the alphabet easily itterable


# Getting the structure for the classes we're putting together
class Segment:
    """
    These are going to represent the outer segments and the mysteries they hold
    """
    def __init__(self, name):
        self.leftOuter = None
        self.rightOuter = None
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

    def setLeftOuter(self, left):
        self.leftOuter = left

    def setRightOuter(self, right):
        self.rightOuter = right

    def isValidObject(self):
        if (self.leftOuter is None) or (self.rightOuter is None):
            return False
        return True


class Outer:
    """
    Class to represent the outer vertices that are adjacent to an inner vertex and 2 outer segments
    """
    def __init__(self, name):
        self.adjInner = None
        self.leftSegment = None
        self.rightSegment = None
        self.name = name

    def getName(self):
        return self.name

    def getLeftSegment(self):
        return self.leftSegment

    def getRightSegment(self):
        return self.rightSegment

    def getAdjInner(self):
        return self.adjInner

    def setLeftSegment(self, left):
        self.leftSegment = left

    def setRightSegment(self, right):
        self.rightSegment = right

    def setAdjInner(self, inner):
        self.adjInner = inner

    def isValidObject(self):
        if (self.leftSegment is None) or (self.rightSegment is None) or (self.adjInner is None):
            return False
        return True


class Inner:
    """
    Class to represent the inner vertices that are adjacent to an outer vertex and 2 neighboring inner vertices
    """
    def __init__(self, name):
        self.adjOuter = None
        self.leftInner = None
        self.rightInner = None
        self.name = name

    def getName(self):
        return self.name

    def getLeftInner(self):
        return self.leftInner

    def getRightInner(self):
        return self.rightInner

    def getAdjOuter(self):
        return self.adjOuter

    def setLeftInner(self, left):
        self.leftInner = left

    def setRightInner(self, right):
        self.rightInner = right

    def setAdjOuter(self, outer):
        self.adjOuter = outer

    def isValidObject(self):
        if (self.leftInner is None) or (self.rightInner is None) or (self.adjOuter is None):
            return False
        return True


def standardCircle(num_verts):
    """
    This will go through and initialize our standard circle
    :param num_verts:
    :return:
    """
    segs = None
    outs = None
    ins = None
    for i in range(num_verts):
        continue
    string.ascii_letters
    return
