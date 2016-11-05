  """Computes the convex hull of a set of 2D points.

    Input: an iterable sequence of (x, y) pairs representing the points.
    Output: a list of vertices of the convex hull in counter-clockwise order,
      starting from the vertex with the lexicographically smallest coordinates.
    Implements Andrew's monotone chain algorithm. O(n log n) complexity.
    """

from collection import namedtuple
import matplotlib.pyploy as plt
import random

Point = namedtuple('Point', 'x y')

class ConvexHull(object):
    _points = []
    _hull_points = []


    def __init__(self):
        pass

    def add(self, point):
        self._points.append(point)
    
    def _get_orientation(self, origin, p1, p2):
        difference = ((p2.x - origin.x) * (p1.y - origin.y)) - ((p1.x - origin.x) - (p2.y - origin.y))

        return difference




