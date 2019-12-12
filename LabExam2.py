# Write a python class to represent a 3D Vector


# import math to use for the magnitude calculation
import math


# defining the class
class Vector:
    # the constructor
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # method to add 2 vectors
    def __add__(self, v2):
        """V1(x,y,z) + V2(a,b,c) = V3 (x+a, y+b, z+c)"""
        v3 = Vector(self.x + v2.x, self.y + v2.y, self.z + v2.z)
        return v3

    # method to subtract 2 vectors
    def __sub__(self, v2):
        """V1(x,y,z) - V2(a,b,c) = V3(x-a, y-b, z-c)"""
        v3 = Vector(self.x - v2.x, self.y - v2.y, self.z - v2.z)
        return v3

    # method to multiply 2 vectors OR a vector and an integer
    def __mul__(self, n):
        """Multiplication by an int: if V is (x, y, z), the V*n is the vector (x*n,y*n, z*n),
           where n is an integer number
           vector multiplication with another vector: implement the dot product. If V1     is (x,y,z) and V2 is (a,b,c),
           then V1*V2 = x*a + y*b + z*c, a scalar.
           Thus the dot product yields a scalar (number), not a vector"""
        if type(n) == int:
            new_v = Vector(self.x * n, self.y * n, self.z * n)
        else:
            new_v = ((self.x * n.x) + (self.y * n.y) + (self.z * n.z))
        return new_v

    # method to calculate the magnitude of a Vector
    def magnitude(self):
        """The magnitude is the square root of each coordinate squared"""
        return math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2) + math.pow(self.z, 2))

    # method for printing a vector
    def __str__(self):
        """This is so the objects print properly"""
        return "({}, {}, {})".format(self.x, self.y, self.z)


# test the vector class is working correctly
vec1 = Vector(1, 2, 3)
vec2 = Vector(5, 5, 5)
print("V1 = ", vec1)
print("v2 = ", vec2)
print("")

# test addition
vec3 = vec1 + vec2
print("Printing addition")
print("v1 + v2 = ", vec3)
print("")

# Test subtraction
vec4 = vec1 - vec2
print("Printing Subtraction")
print("v1 - v2 = ", vec4)
print("")

# test dot product
vec5 = vec1 * vec2
print("Printing dot product")
print("v1 * v2 = ", vec5)
print("")

# test integer multiplication
vec6 = vec1 * 2
print("Printing integer multiplication")
print("v1 * 2 = ", vec6)
print("")

# test vector magnitude
print("v1 magnitude is ", vec1.magnitude())
