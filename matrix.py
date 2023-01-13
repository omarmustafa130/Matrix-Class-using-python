# File:             matrix.py
# Author:           Omar Mustafa
# Date:             Jan 12, 2022
# Email:            omarmustafa130@gmail.com
# Description:      A small project related to the Intro to self-driving cars nanodegree,
#                   made to practice object oriented programming in python and math matrix skills.
#                   I implemented the following functions: determinant, trace, inverse, and transpose. 
#                   I also implemented some overloaded operators such as: __add__, __sub__, __mult__, __neg__, and __rmul__

import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.

        Parameter
        ---------
        width, heigh
            number of rows and coloumns of the new initiaized matrix

        Returns
        -------
        a new matrix of zeroes
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.

        Parameter
        ---------
        n
            number of rows and coloumns of the new initiaized matrix

        Returns
        -------
        a new identity matrix of rows and coloumns n
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        """
        Initialises a Matrix object.

        Parameter
        ---------
        gird
            the matrix

        Returns
        -------
        None
        """
        self.g = grid
        self.h = len(grid) #rows    
        self.w = len(grid[0])#cols
    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.

        Parameter
        ---------
        None

        Returns
        -------
        determinant of the original matrix
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        det = 0.0

        if (self.h == 1):
            return self.g[0][0]
        else:
            det = (self.g[0][0]*self.g[1][1]) - (self.g[0][1]*self.g[1][0])
            return det
            

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).

        Parameter
        ---------
        None

        Returns
        -------
        trace of the original matrix
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")


        sum = 0.0
        for i in range(self.h):
            sum+=self.g[i][i]
        return sum
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.

        Parameter
        ---------
        None

        Returns
        -------
        a new matrix that is the inverse of the original matrix
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        if (self.determinant() == 0):
            raise(ZeroDivisionError, "Determinant is zero, the matrix does not have an inverse.")

        m = zeroes(self.h, self.w)
        if (self.h == 1):
            if(self.g[0][0] != 0):
                m.g[0][0] = 1/self.g[0][0]
                return m
        else:
            i = identity(self.h)
            m = (1/self.determinant()) * ((self.trace()*i)-self)
            return m

    def T(self):
        """
        Returns a transposed copy of this Matrix.

        Parameter
        ---------
        None

        Returns
        -------
        a new matrix that is the transposed copy of the original matrix
        """
        m = zeroes(self.w, self.h)
        for i in range (self.w):
            for j in range (self.h):
                m.g[i][j] = self.g[j][i]
                
        return m
                      
    def is_square(self):
        """
        checks if a mtrix is square

        Parameter
        ---------
        None

        Returns
        -------
        True if matrix square, false otherwise
        """
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator

        Parameter
        ---------
        other
            Another matrix

        Returns
        -------
        a new matrix tha equals the original matrix after adding other to it
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 

        m = zeroes(self.h, self.w)

        for i in range (self.h):
            for j in range (self.w):
                m.g[i][j]= self.g[i][j] + other.g[i][j]
        return m
    def __neg__(self):

        """
        Defines the behavior of - operator (NOT subtraction)

        Parameter
        ---------
        None

        Returns
        -------
        a new matrix tha equals the original matrix after multiplying -1 to every element of itt
        """
        m = zeroes(self.h, self.w)
        for i in range (self.h):
            for j in range(self.w):
                m.g[i][j]=self.g[i][j] * (-1)
        return m
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)

        Parameter
        ---------
        other
            another matrix

        Returns
        -------
        a new matrix that equals the original matrix - other matrix
        """
        m = zeroes(self.h, self.w)
        for i in range (self.h):
            for j in range (self.w):
                m.g[i][j]=self.g[i][j]-other.g[i][j]
        return m

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)

        Parameter
        ---------
        other
            another matrix

        Returns
        -------
        a new matrix that equals the original matrix after multiplying another matrix to it
        """
        if (self.w == other.h):
            
            m = zeroes(self.h, other.w)
            for i in range(self.h):
                for j in range(other.w):
                    for k in range(self.w):
                        m.g[i][j] += self.g[i][k] * other.g[k][j]
            return m

    def __rmul__(self, other):
        """
        Defines the behavior of * operator (variable to matrix multiplication)

        Parameter
        ---------
        other
            variable

        Returns
        -------
        a new matrix that equals the original matrix after multiplying other variable to it
        """
        if isinstance(other, numbers.Number):
            pass

            m = zeroes(self.h, self.w)
            for i in range (self.h):
                for j in range (self.w):
                    m.g[i][j]=self.g[i][j]*other
            return m