"""
Here we're going to code for the local rotations. We're doing an object oriented approach
Left and right are in referene to the center
"""

__version__ = 1.0
__author__ = 'Katie Kruzan'

import string  # just to get the alphabet easily itterable
import sys


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
            if i == num_verts-1:  # time to close up the circle
                inn.setRightInner(inns[string.ascii_letters[0]])

        # then make the outer
        out = Outer(str(i+1))
        out.setAdjInner(inn)
        if i != 0:
            out.setLeftSegment(segs[str(-i)])
            # if i == num_verts - 1:  # time to close up the circle
            #     out.setLeftSegment(segs[str(-1)])

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


def findTheFace(source_inner):
    # order will be i, o, s, o, i repeat
    face = []
    source_in = source_inner
    face.append(source_in)
    end_in = None
    while source_in != end_in:
        # inner: find adjacent outer
        face.append(face[-1].getAdjOuter())
        # outer: go to right seg
        face.append(face[-1].getRightSegment())
        # segment: go to right outer
        face.append(face[-1].getRightOuter())
        # outer: then adj inner
        face.append(face[-1].getAdjInner())
        # then left inner and repeat.
        end_in = face[-1].getLeftInner()
        face.append(end_in)
    return face


def grabAllTheFaces(inns):
    # do this based on the inner verts
    faces = []
    covered = set()
    for inn in inns:
        # check if we already have it in a face
        if inns[inn] not in covered:
            face = findTheFace(inns[inn])
            faces.append(face)
            covered.update(face)

    # check we've gotten all the elements
    if len(covered) == (3*len(inns)):
        print('We got em!!!')

    return faces


def printCircleStatus(segs, outs, inns):
    print('\nSegments:')
    for k in segs:
        print()
        print(k)
        print(segs[k].toString())

    print('\nOuters:')
    for k in outs:
        print()
        print(k)
        print(outs[k].toString())

    print('\nInners:')
    for k in inns:
        print()
        print(k)
        print(inns[k].toString())


if __name__ == '__main__':
    segments, outers, inners = standardCircle(3)
    printCircleStatus(segments, outers, inners)
    print(inners['a'].getName())

    facs = grabAllTheFaces(inners)
    # run through the inner verticies. But check if they are already in our faces
    print('\nPrinting the faces')
    for f in facs:
        print()
        for p in f:
            sys.stdout.write(p.getName() + ' ')

    switch = '23'
    for num in range(len(switch)):
        cs = switch[num]
        ns = switch[0]
        if num != (len(switch)-1):
            ns = switch[num+1]
        inners[string.ascii_letters[int(cs)-1]].setAdjOuter(outers[ns])
        outers[ns].setAdjInner(inners[string.ascii_letters[int(cs) - 1]])

    printCircleStatus(segments, outers, inners)

    new_facs = grabAllTheFaces(inners)
    print('\nPrinting the faces')
    for f in new_facs:
        print()
        for p in f:
            sys.stdout.write(p.getName() + ' ')



