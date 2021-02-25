import numpy as np
import timeit

python_time = timeit.timeit(setup="myArray = range(1000)", stmt='[x ** 2 for x in myArray]', number=1000)
numpy_time = timeit.timeit(setup="import numpy as np; numpyArray = np.arange(1000)", stmt='numpyArray ** 2', number=1000) 

print('Regular python time:', python_time)
print('NumPy time:', numpy_time)

print('NumPy is', python_time/numpy_time , 'times faster')