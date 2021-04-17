from random import randint
from math import sin, cos, atan2, sqrt

class Vec2d:
    #region INIT
    def _get_xy(self, args):
        """Generates a x and y from any input
        Returns:
            [tuple]: x, y
        """
        number_of_args = len(args)

        if   number_of_args == 0 : return 0, 0 # no arguments
        elif number_of_args == 2 : x, y = args ; return x, y # both x and y passed in

        if number_of_args == 1: # one argument
            arg_type = type(args[0])

            if arg_type is float or arg_type is int: # single int or float argument
                return args[0], args[0]
            if arg_type is list or arg_type is tuple:
                return args[0][0], args[0][1] # single list argument
            if arg_type is Vec2d:
                return args[0].x, args[0].y

    def __init__(self, *args):
        self.x, self.y = self._get_xy(args)
    #endregion

    #region AUTO CREATE METHODS

    def random_pos():
        """Returns a vector in normalised 0-1 space
        Returns:
            Vec2d: a vector in normal space
        """
        return Vec2d(randint(0, 1000)/1000, randint(0, 1000)/1000)

    def random_unit():
        """Generates a unit vector with a random heading
        Returns:
            Vec2d: unit vector
        """
        pos = Vec2d(randint(-1000, 1000), randint(-1000, 1000))
        pos.normalise()
        return pos

    def from_angle(angle):
        """Creates a unit vector with the same heading as the angle
        Args:
            angle (float): angle of direction in radians
        Returns:
            Vec2d: unit vector
        """
        return Vec2d(cos(angle), sin(angle))

    #endregion

    #region CUSTOM METHODS

    def get(self):
        """Gets the x and y components as an integer tuple
        Returns:
            tuple: contains x and y as integers
        """
        return (int(self.x), int(self.y))

    def set(self,  *args):
        """Sets the x and y components
        """
        x, y = self._get_xy(args)
        self.x = x ; self.y = y

    def copy(self):
        """Gets a copy of this vector
        Returns:
            Vec2d: a copy of this vector
        """
        return Vec2d(self.x, self.y)

    def clear(self):
        """Sets both components to 0
        """
        self.x = self.y = 0

    #endregion

    #region CUSTOM MATHEMATICAL METHODS
    def dist_sqrt(self, *args):
        """Gets the distance between this point and another (uses square root)
        Returns:
            float: distance
        """
        x, y = self._get_xy(args)
        return sqrt((self.x - x)**2 + (self.y - y)**2)

    def dist(self, *args):
        """Gets the distance between this point and another (does not use square root)
        Returns:
            float: distance
        """
        x, y = self._get_xy(args)
        return (self.x - x)**2 + (self.y - y)**2

    def get_heading_angle(self):
        """Returns the heading angle in radians assuming 0 is aligned with x
        Returns:
            float: angle in radians
        """
        return atan2(self.x, self.y)

    def get_magnitude(self):
        """Gets the magnitude/length of the vector
        Returns:
            float: magnitude
        """
        return sqrt(self.x**2 + self.y**2)

    def normalise(self):
        """Normalises this vector making it a unit vector
        """
        mag = self.get_magnitude()
        if mag == 0 : return
        self.div(mag)
    def normalize(self):
        """Normalises this vector making it a unit vector
        """
        self.normalise()

    def truncate(self, max_val):
        """Clamps the x and y components to be in range -max_val to max_val
        Args:
            max_val (float): max and min for each component
        """
        if self.x > max_val : self.x = max_val
        if self.y > max_val : self.y = max_val

        if self.x < -max_val : self.x = -max_val
        if self.y < -max_val : self.y = -max_val

    def add(self, *args):
        x, y = self._get_xy(args)
        self.x += x ; self.y += y

    def sub(self, *args):
        x, y = self._get_xy(args)
        self.x /= x ; self.y /= y

    def mult(self, *args):
        x, y = self._get_xy(args)
        self.x *= x ; self.y *= y

    def div(self, *args):
        x, y = self._get_xy(args)
        self.x /= x ; self.y /= y

    def linear_interpolate(self, *args, t=0.5):
        """Linearly interpolates between current position and passed in position
        Args:
            t (float, optional): speed. Defaults to 0.5.
        """
        x, y = self._get_xy(args)

        x = self.x + t * (x - self.x)
        y = self.y + t * (y - self.y)

        self.set(x, y)

    def dot_product(self, *args):
        """Dot product of this and another vector
        Returns:
            float: dot product result
        """
        x, y = self._get_xy(args)
        return sum([self.x * x, self.y * y])
    #endregion

    #region MAGIC METHODS
    def __iadd__(self, *args):
        x, y = self._get_xy(args)
        self.x += x ; self.y += y
        return self
    def __isub__(self, *args):
        x, y = self._get_xy(args)
        self.x -= x ; self.y -= y
        return self
    def __imul__(self, *args):
        x, y = self._get_xy(args)
        self.x *= x ; self.y *= y
        return self
    def __idiv__(self, *args):
        x, y = self._get_xy(args)
        self.x /= x ; self.y /= y
        return self

    def __add__(self, *args):
        x, y = self._get_xy(args)

        return Vec2d(self.x + x, self.y + y)
    def __sub__(self, *args):
        x, y = self._get_xy(args)

        return Vec2d(self.x - x, self.y - y)
    def __mul__(self, *args):
        x, y = self._get_xy(args)

        return Vec2d(self.x * x, self.y * y)
    def __div__(self, *args):
        x, y = self._get_xy(args)

        return Vec2d(self.x / x, self.y / y)
    #endregion
