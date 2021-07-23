"""
Here we're going to code for the local rotations. We're doing an object oriented approach
Left and right are in referene to the center
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

    def getName(self):
        return self.name

    def getLeftOuter(self):
        return self.leftOuter

    def getRightOuter(self):
        return self.rightOuter

    def setLeftOuter(self, left):
        self.leftOuter = left
        if left.getRightSegment() is None:
            left.setRightSegment(self)

    def setRightOuter(self, right):
        self.rightOuter = right
        if right.getLeftSegment() is None:
            right.setLeftSegment(self)

    def isValidObject(self):
        if (self.leftOuter is None) or (self.rightOuter is None):
            return False
        return True

    def toString(self):
        return 'left Outer: ' + self.leftOuter.getName() + '\nright Outer: ' + self.rightOuter.getName()


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
        # this is a segment
        self.leftSegment = left
        if left.getRightOuter() is None:
            left.setRightOuter(self)

    def setRightSegment(self, right):
        self.rightSegment = right
        if right.getLeftOuter() is None:
            right.setLeftOuter(self)

    def setAdjInner(self, inner):
        self.adjInner = inner
        if inner.getAdjOuter() is None:
            inner.setAdjOuter(self)

    def isValidObject(self):
        if (self.leftSegment is None) or (self.rightSegment is None) or (self.adjInner is None):
            return False
        return True

    def toString(self):
        return 'left Segment: ' + self.leftSegment.getName() + '\nright Segment: ' + self.rightSegment.getName() \
               + '\nadj Inner: ' + self.adjInner.getName()


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
        if left.getRightInner() is None:
            left.setRightInner(self)

    def setRightInner(self, right):
        self.rightInner = right
        if right.getLeftInner() is None:
            right.setLeftInner(self)

    def setAdjOuter(self, outer):
        self.adjOuter = outer
        if outer.getAdjInner() is None:
            outer.setAdjInner(self)

    def isValidObject(self):
        if (self.leftInner is None) or (self.rightInner is None) or (self.adjOuter is None):
            return False
        return True

    def toString(self):
        return 'left Inner: ' + self.leftInner.getName() + '\nright Inner: ' + self.rightInner.getName() \
               + '\nadj Outer: ' + self.adjOuter.getName()


# def findABuddy(collection, name):
#     for l in collection:
#         if l.getName == name:
#             return l
#     print('Buddy not found: ' + name)
#     return None


def standardCircle(num_verts):
    """
    This will go through and initialize our standard circle
    :param num_verts:
    :return:
    """
    segs = dict()
    outs = dict()
    inns = dict()

    for i in range(num_verts):
        # For labeling, we will use the standard labeling for inner and outer, and then negative numbers, etc for
        # the segments

        # start inner
        inn = Inner(string.ascii_letters[i])
        if i != 0:
            inn.setLeftInner(inns[string.ascii_letters[i-1]])
            if inns[string.ascii_letters[i - 1]].getRightInner() == inn:
                print('Successfully set in the dictionary')
            if i == num_verts-1:  # time to close up the circle
                inn.setRightInner(inns[string.ascii_letters[0]])

        # then make the outer
        out = Outer(str(i+1))
        out.setAdjInner(inn)
        if i != 0:
            out.setLeftSegment(segs[str(-i)])
            if segs[str(-i)].getRightOuter() == out:
                print('Successfully set in the dictionary')
            if i == num_verts - 1:  # time to close up the circle
                out.setLeftSegment(segs[str(-1)])

        # then make the segment
        seg = Segment(str(-i-1))
        seg.setLeftOuter(out)
        if i == num_verts - 1:  # time to close up the circle
            seg.setRightOuter(outs[str(1)])

        # add them to our dictionaries
        segs[seg.getName()] = seg
        outs[out.getName()] = out
        inns[inn.getName()] = inn

    return segs, outs, inns


if __name__ == '__main__':
    s, o, i = standardCircle(3)

    

