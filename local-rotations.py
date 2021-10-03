"""
Here we're going to code for the local rotations. We're doing an object oriented approach
Left and right are in reference to the origin
"""

__version__ = 1.0
__author__ = 'Katie Kruzan'

import string  # just to get the alphabet easily iterable
import sys  # This just helps us in our printing
from typing import Dict  # This helps us in our documentation


# Getting the structure for the classes we're putting together
class Segment:
    """
    These are going to represent the outer segments and the mysteries they hold.
    The segments will be adjacent to 2 outer nodes
    """

    def __init__(self, name: str):
        """
        Initialize the segment, keeping a place for the right left outer vertices to which it is adjacent
        :param name: How we will reference this segment. In this implementation, it is expected to be a negative integer
        """
        self.leftOuter = None
        self.rightOuter = None
        self.name = name

    def getName(self) -> str:
        """
        Return the name we gave to this segment.
        :return: name
        """
        return self.name

    def getLeftOuter(self):
        """
        Return the outer node to the left of this segment with respect to the origin
        :return: leftOuter
        """
        return self.leftOuter

    def getRightOuter(self):
        """
        Return the outer node to the right of this segment with respect to the origin
        :return: rightOuter
        """
        return self.rightOuter

    def setLeftOuter(self, left):
        """
        Set the outer node to the left of this segment with respect to the origin
        Also, set left's right segment to this segment.
        :param left: A outer node object to be referenced as this segment's left outer node
        :return: None
        """
        self.leftOuter = left
        if left.getRightSegment() is None:
            left.setRightSegment(self)

    def setRightOuter(self, right):
        """
        Set the outer node to the right of this segment with respect to the origin
        Also, set right's left segment to this segment.
        :param right: A outer node object to be referenced as this segment's right outer node
        :return: None
        """
        self.rightOuter = right
        if right.getLeftSegment() is None:
            right.setLeftSegment(self)

    def isValidObject(self) -> bool:
        """
        Checks to see if this segment has been full initialized.
        :return: valid returns true if it has both the left and right outer nodes set
        """
        if (self.leftOuter is None) or (self.rightOuter is None):
            return False
        return True

    def toString(self) -> str:
        """
        Returns a formatted string of the left and right outer nodes this is associated with
        :return: Description string
        """
        return 'left Outer: ' + self.leftOuter.getName() + '\nright Outer: ' + self.rightOuter.getName()


class Outer:
    """
    Class to represent the outer vertices that are adjacent to an inner vertex and 2 outer segments
    """

    def __init__(self, name: str):
        """
        Initialize the outer node

        Keeping a place for the inner vertex and right and left outer segments to which it is adjacent.
        :param name: How we will reference this outer node. In this implementation, it is expected to be a positive integer
        """
        self.adjInner = None
        self.leftSegment = None
        self.rightSegment = None
        self.name = name

    def getName(self) -> str:
        """
        Return the name we gave to this outer node.
        :return: name
        """
        return self.name

    def getLeftSegment(self) -> Segment:
        """
        Return the segment object to the left of this outer node with respect to the origin
        :return: leftSegment
        """
        return self.leftSegment

    def getRightSegment(self) -> Segment:
        """
        Return the segment object to the right of this outer node with respect to the origin
        :return: rightSegment
        """
        return self.rightSegment

    def getAdjInner(self):
        """
        Return the inner node object adjacent to this outer note object
        :return: adjInner
        """
        return self.adjInner

    def setLeftSegment(self, left: Segment):
        """
        Set the segment to the left of this outer node with respect to the origin
        Also, set left's right outer node to self.
        :param left: A segment object to be referenced as this node's left outer segment
        :return: None
        """
        self.leftSegment = left
        if left.getRightOuter() is None:
            left.setRightOuter(self)

    def setRightSegment(self, right: Segment):
        """
        Set the segment to the right of this outer node with respect to the origin
        Also, set right's left outer node to self.
        :param right: A segment object to be referenced as this node's right outer segment
        :return: None
        """
        self.rightSegment = right
        if right.getLeftOuter() is None:
            right.setLeftOuter(self)

    def setAdjInner(self, inner):
        """
        Set the inner node adjacent to this outer node
        Also, set inner's adjacent outer node to self.
        :param inner: A inner node object to be referenced as this node's adjacent inner node
        :return: None
        """
        self.adjInner = inner
        if inner.getAdjOuter() is None:
            inner.setAdjOuter(self)

    def isValidObject(self) -> bool:
        """
        Checks to see if this outer node has been full initialized.
        :return: valid returns true if it has the left segment, right segment, and inner node set
        """
        if (self.leftSegment is None) or (self.rightSegment is None) or (self.adjInner is None):
            return False
        return True

    def toString(self) -> str:
        """
        Returns a formatted string of the left segment, right segment, and inner node this outer node is associated with
        :return: Description string
        """
        return 'left Segment: ' + self.leftSegment.getName() + '\nright Segment: ' + self.rightSegment.getName() \
               + '\nadj Inner: ' + self.adjInner.getName()


class Inner:
    """
    Class to represent the inner vertices that are adjacent to an outer vertex and 2 neighboring inner vertices
    """

    def __init__(self, name: str):
        """
        Initialize the inner node object

        Keeping a place for the outer vertex and right and left adjacent inner nodes.
        :param name: How we will reference this inner node. In this implementation, it is expected to be a lowercase letter
        """
        self.adjOuter = None
        self.leftInner = None
        self.rightInner = None
        self.name = name

    def getName(self) -> str:
        """
        Return the name we gave to this inner node.
        :return: name
        """
        return self.name

    def getLeftInner(self):
        """
        Return the inner node object to the left of this inner node with respect to the origin
        :return: leftInner
        """
        return self.leftInner

    def getRightInner(self):
        """
        Return the inner node object to the right of this inner node with respect to the origin
        :return: rightInner
        """
        return self.rightInner

    def getAdjOuter(self) -> Outer:
        """
        Return the outer node object adjacent to this inner node
        :return: adjOuter
        """
        return self.adjOuter

    def setLeftInner(self, left):
        """
        Set the inner node to the left of this inner node with respect to the origin
        Also, set left's right inner node to self.
        :param left: An inner node object to be referenced as this node's left inner node
        :return: None
        """
        self.leftInner = left
        if left.getRightInner() is None:
            left.setRightInner(self)

    def setRightInner(self, right):
        """
        Set the inner node to the right of this inner node with respect to the origin
        Also, set right's left inner node to self.
        :param right: An inner node object to be referenced as this node's right inner node
        :return: None
        """
        self.rightInner = right
        if right.getLeftInner() is None:
            right.setLeftInner(self)

    def setAdjOuter(self, outer: Outer):
        """
        Set the outer node adjacent to this inner node
        Also, set outer's adjacent inner node to self.
        :param outer: An outer node object to be referenced as this node's adjacent outer node
        :return: None
        """
        self.adjOuter = outer
        if outer.getAdjInner() is None:
            outer.setAdjInner(self)

    def isValidObject(self) -> bool:
        """
        Checks to see if this inner node has been full initialized.
        :return: valid returns true if it has the left inner node, right inner node, and adjacent outer node set
        """
        if (self.leftInner is None) or (self.rightInner is None) or (self.adjOuter is None):
            return False
        return True

    def toString(self) -> str:
        """
        Returns a formatted string of the left inner node, right inner node, and adjacent outer node this inner node
        is associated with
        :return: Description string
        """
        return 'left Inner: ' + self.leftInner.getName() + '\nright Inner: ' + self.rightInner.getName() \
               + '\nadj Outer: ' + self.adjOuter.getName()


def standardCircle(num_verts: int) -> (Dict[str, Segment], Dict[str, Outer], Dict[str, Inner]):
    """
    This will go through and initialize our standard starting circle
    :param num_verts: the number of outer nodes we will have
    :returns: tuple(segs, outs, inns)
        -segs - dictionary of str: Segment objects in the circle \\
        -outs - dictionary of str: Outer objects in the circle \\
        -inns - dictionary of str: Inner objects in the circle
    """
    # Initializing our dictionaries
    segs = dict()
    outs = dict()
    inns = dict()

    # Running through the number of vertices we will be edning up with
    for i in range(num_verts):
        # start with an inner node - labeling with lowercase letters
        inn = Inner(string.ascii_letters[i])
        # If we aren't on the first one, connect it to the previous one.
        if i != 0:
            inn.setLeftInner(inns[string.ascii_letters[i - 1]])
            # If we've hit the end of the line, go ahead and close up the circle.
            if i == num_verts - 1:
                inn.setRightInner(inns[string.ascii_letters[0]])

        # then make the outer
        out = Outer(str(i + 1))
        # Go ahead and connect the inner we just made with this outer node
        out.setAdjInner(inn)
        # If we aren't on the first one, go ahead and connect it to the previous segment
        if i != 0:
            out.setLeftSegment(segs[str(-i)])

        # Now time to make the segment
        seg = Segment(str(-i - 1))
        # Go ahead and connect the outer node we just made with this segment
        seg.setLeftOuter(out)
        # If we're at the end of the circle, then we close it up. Otherwise, move on
        if i == num_verts - 1:
            seg.setRightOuter(outs[str(1)])

        # add them to our dictionaries
        segs[seg.getName()] = seg
        outs[out.getName()] = out
        inns[inn.getName()] = inn

    # If we've made it here, then we've made the full circle and are ready to return it
    return segs, outs, inns


def findTheFace(source_in: Inner) -> list:
    """
    This will take an inner node and use the algorithm to walk the face that it is on.
    The order of the face will be i, o, s, o, i repeat
    :param source_in: Inner node object we are starting from.
    :return: face: a list representing the face. This list is of inner, outer, and segment objects in the
            order i, o, s, o, i, repeat.
    """
    # initialize the list
    face = list()
    # starting the face with the source inner node.
    face.append(source_in)
    # initialize the ending inner node we will be using for comparison
    end_in = None
    # As long as we haven't looped back around, go through the following process.
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
        # set this inner node as our node to compare to our starting node.
        end_in = face[-1].getLeftInner()
        face.append(end_in)
    return face


def faceCannonOrder(face: list) -> list:
    """
    Just list the face with the face elements in order.
    We will do it with the first numerical face, and then go right before it for an order that will be consistent.
    :param face: a list representing the face. This list is of inner, outer, and segment objects in the
            order i, o, s, o, i, repeat.
    :return: ordered face in canonical order
    """
    # find the first numerical face then go right before it
    # initialize face num as a relatively high number we won't encounter
    facenum = 333
    # initialize the int for where we will split the list
    start_ind = 0
    # loop through and find the face we want to find
    for i in range(len(face)):
        try:
            if int(face[i].getName()) < facenum:
                # To get here, we must have found a lower face
                # keep track of where this is located in the list
                start_ind = i - 1
                # make our current lowest face the new lowest face to keep comparing to.
                facenum = int(face[i].getName())
        # if we try casting a letter to a number, python will get upset, but that also means we're looking at
        # an inner node, which we don't want for this anyways.
        except ValueError:
            continue

    # make our ordered face getting from the starting index to the end, then wrapping around and getting the rest of
    # the face
    ord_face = face[start_ind:] + face[:start_ind]
    # go through and make sure we don't have any duplicate elements right by each other. If we do, then drop them.
    for i in range(len(ord_face) - 1):
        if ord_face[i].toString() == ord_face[i + 1].toString():
            ord_face.pop(i)
            break

    # return the ordered face
    return ord_face


def grabAllTheFaces(inns: Dict[str, Inner]) -> list:
    """
    Function to get the list of unique faces for our circle.
    :param inns: dictionary of Inner objects. We will loop through these to get the faces
    :return: faces: List of distinct faces in canonical order.
    """
    # initialize the list of faces
    faces = list()
    # a set of all the elements we have covered by the faces. Will use this for a completeness check
    covered = set()
    # run through every inner node we've been given
    for inn in inns:
        # Generate the face that inner node lies on
        face = findTheFace(inns[inn])
        # put the face we've gotten in canonical order
        face = faceCannonOrder(face)
        # Check if we've already captured it.
        if face not in faces:
            # If not, then add it to our list of faces
            faces.append(face)
            # Go ahead and add the elements in this face to our covered set
            covered.update(face)

    # check we've gotten all the elements
    if len(covered) == (3 * len(inns)):
        print('We got em!!!')

    # Now return a list of all the faces we have.
    return faces


def printCircleStatus(segs: Dict[str, Segment], outs: Dict[str, Outer], inns: Dict[str, Inner]):
    """
    Helper function that prints the status of the circle to the console
    :param segs: dictionary of str: Segment objects in the circle
    :param outs: dictionary of str: Outer objects in the circle
    :param inns: dictionary of str: Inner objects in the circle
    :return: None
    """
    # Run through the segments
    print('\nSegments:')
    for k in segs:
        print()
        print(k)
        print(segs[k].toString())

    # Run through the Outer nodes
    print('\nOuters:')
    for k in outs:
        print()
        print(k)
        print(outs[k].toString())

    # Run through the Inner nodes
    print('\nInners:')
    for k in inns:
        print()
        print(k)
        print(inns[k].toString())


if __name__ == '__main__':
    # This is where you change the variables.
    # must be a positive integer > 2
    verts = 12
    # Must be a string with spaces between each element. If you want to denote multiple cycles, you must add a |
    switch_txt = '2 3 4 5 | 12 7'

    # we're going to make a list of all the switches and all the cycles
    switches = list()
    # first, we get the cycles, split by '|'
    cycles = switch_txt.split('|')
    for c in cycles:
        # We're going to split the switch into a list split by the whitespace
        s = c.strip().split()
        # Then we're going to append the switches in the cycle to the new list
        switches.append(s)

    # Go ahead and make the standard circle given the number of vertices we want to use.
    segments, outers, inners = standardCircle(verts)

    # Go through and grab the faces for our standard circle
    facs = grabAllTheFaces(inners)
    print('\nPrinting the faces')
    for f in facs:
        print()
        for p in f:
            sys.stdout.write(p.getName() + ' ')

    # Go through and do the switches for each cycle
    for switch in switches:
        for num in range(len(switch)):
            # store the current part of the switch we're working on
            cs = switch[num]
            # store the next part of the switch we're working on, looping to the beginning if we're at the end
            ns = switch[(num + 1) % len(switch)]
            # Do the actual switch
            # Getting the new inner and outer validly switched up
            inners[string.ascii_letters[int(cs) - 1]].setAdjOuter(outers[ns])
            outers[ns].setAdjInner(inners[string.ascii_letters[int(cs) - 1]])

    # print how the final rotation sits
    printCircleStatus(segments, outers, inners)

    # Go through and generate and print the new faces
    new_facs = grabAllTheFaces(inners)
    print('\nPrinting the new faces')
    for f in new_facs:
        print()
        for p in f:
            sys.stdout.write(p.getName() + ' ')
