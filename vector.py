class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
    
    
    def add(self, v):
        try :
            if self.dimension != v.dimension:
                raise ValueError
            c = [None for x in range(v.dimension)]
            for i in range((v.dimension)):
                c[i] = self.coordinates[i] + v.coordinates[i]
            return tuple(c)
        except ValueError:
            raise ValueError("Length of both vectors must be same")
    
    
    def sub(self, v):
        try :
            if self.dimension != v.dimension:
                raise ValueError
            c = [None for x in range(v.dimension)]
            for i in range((v.dimension)):
                c[i] = self.coordinates[i] - v.coordinates[i]
            return tuple(c)
        except ValueError:
            raise ValueError("Length of both vectors must be same")
    
    
    def scalMult(self, scal):
        try:
            if not scal:
                raise ValueError
            c = [None for x in range(self.dimension)]
            for i in range((self.dimension)):
                c[i] = scal * self.coordinates[i]
            return tuple(c)
        except ValueError:
            raise ValueError("Scalar cannot be empty")
            
            
vector1 = Vector([1,2])
vector2 = Vector([-1,-2])
vector3 = Vector([1,2,3])
vector4 = vector1.sub(vector2)
print(vector1.scalMult(3))
print(vector4)