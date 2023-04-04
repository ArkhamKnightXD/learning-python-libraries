import numpy

# La libreria numpy me sirve para trabajar con ndarray que son mucho mas rápidos que los list de python
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)

print(type(arr))

# Aqui muestro las distintas dimensiones que puede tener un array en numpy
zero_dimension_array = numpy.array(42)
one_dimension_array = numpy.array([1, 2, 3, 4, 5])
two_dimension_array = numpy.array([[1, 2, 3], [4, 5, 6]])
three_dimension_array = numpy.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

# Aqui muestro las dimensiones de cada arreglo
print(zero_dimension_array.ndim)
print(one_dimension_array.ndim)
print(two_dimension_array.ndim)
print(three_dimension_array.ndim)

# Forma de iterar arreglos
for x in one_dimension_array:
    print(x)
