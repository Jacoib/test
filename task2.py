import numpy as np
arr = np.array([1,2,3,4,5])
arr.dtype
dtype('int32')
float_arr = arr.astype(np.float64)
float_arr.dtype
dtype('float64')
dtype('float64')
arr = np.array([3.7,-1.2,-2.6,0.5,12.9,10.1])
arr
array([ 3.7, -1.2, -2.6,  0.5, 12.9, 10.1])
arr.astype(mp.int32)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'mp' is not defined
arr.astype(np.int32)
array([ 3, -1, -2,  0, 12, 10])
arr.astype(np.int32)
array([ 3, -1, -2,  0, 12, 10])
arr.astype(np.int32)
array([ 3, -1, -2,  0, 12, 10])
arr.astype(np.int32)
array([ 3, -1, -2,  0, 12, 10])
numeric_strings = np.array(['1.25','-9.6','42'],dtype = np.string_)
numeric_strings.astype(float)
array([ 1.25, -9.6 , 42.  ])
arr = np.array([[1.,2.,3.],[4.,5.,6.]])
arr
array([[1., 2., 3.],
       [4., 5., 6.]])
arr * arr
array([[ 1.,  4.,  9.],
       [16., 25., 36.]])
arr - arr
array([[0., 0., 0.],
       [0., 0., 0.]])
1/arr
array([[1.        , 0.5       , 0.33333333],
       [0.25      , 0.2       , 0.16666667]])
arr * 0.5
array([[0.5, 1. , 1.5],
       [2. , 2.5, 3. ]])
arr ** 0.5
array([[1.        , 1.41421356, 1.73205081],
       [2.        , 2.23606798, 2.44948974]])
arr2 = np.array([[0.,4.,1.],[7.,2.,12.]])
arr2
array([[ 0.,  4.,  1.],
       [ 7.,  2., 12.]])
arr2 > arr
array([[False,  True, False],
       [ True, False,  True]])
arr2
array([[ 0.,  4.,  1.],
       [ 7.,  2., 12.]])
#基本的索引和切片
arr = np.arange(10)
arr
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[5]
5
arr[5:8]
array([5, 6, 7])
arr[5:8] = 12
arr
array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
arr
array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
arr
array([ 0,  1,  2,  3,  4, 12, 12, 12,  8,  9])
arr_slice = arr[5:8]
arr_slice
array([12, 12, 12])
arr_slice[1] = 12345
arr
array([    0,     1,     2,     3,     4,    12, 12345,    12,     8,
           9])
#切片[：]会给数组中所有值赋值
import numpy as np
arr = np.arange(10)
arr_slice = arr[5:8]
arr_slice
array([5, 6, 7])
arr_slice[:] = 64
ar
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'ar' is not defined
arr
array([ 0,  1,  2,  3,  4, 64, 64, 64,  8,  9])
# 如果你想要得到的是ndarray切片的一份副本而非视图，就需要明确地进行复制操作，例如arr[5:8].copy()
# 如果你想要得到的是ndarray切片的一份副本而非视图，就需要明确地进行复制操作，例如arr[5:8].copy()
#二维数组
arr2d = np.array([[1,2,3],4,5,6],[7,8,9])
Traceback (most recent call last):
  File "<input>", line 1, in <module>
TypeError: data type not understood
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2
Traceback (most recent call last):
  File "<input>", line 1, in <module>
NameError: name 'arr2' is not defined
arr2d
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d
array([[[ 1,  2,  3],
        [ 4,  5,  6]],
       [[ 7,  8,  9],
        [10, 11, 12]]])
        arr3d[0]
array([[1, 2, 3],
       [4, 5, 6]])
arr3d[1,0]
array([7, 8, 9])
x = arr3d[1]
x
array([[ 7,  8,  9],
       [10, 11, 12]])
x[0]
array([7, 8, 9])
arr3d[1,0]
array([7, 8, 9])
arr3d[1,1,1]
11
old_value = arr3d[0].copy()
old_value
array([[1, 2, 3],
       [4, 5, 6]])
arr3d
array([[[ 1,  2,  3],
        [ 4,  5,  6]],
       [[ 7,  8,  9],
        [10, 11, 12]]])
arr3d[0] = old_value
arr3d
array([[[ 1,  2,  3],
        [ 4,  5,  6]],
       [[ 7,  8,  9],
        [10, 11, 12]]])
arr3d[0]
array([[1, 2, 3],
       [4, 5, 6]])
arr3d[1,0]
array([7, 8, 9])
x = arr3d[1]
x
array([[ 7,  8,  9],
       [10, 11, 12]])
