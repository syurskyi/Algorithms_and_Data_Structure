from matmul import Matrix


def test_matmul():
    mat1 = Matrix([[1, 2], [3, 4]])
    mat2 = Matrix([[11, 12], [13, 14]])
    mat3 = mat1 @ mat2
    assert mat3.values == [[37, 40], [85, 92]]


def test_rmatmul():
    mat1 = Matrix([[11, 12], [13, 14]])
    mat2 = Matrix([[1, 2], [3, 4]])
    mat3 = mat1 @ mat2
    assert mat3.values == [[47, 70], [55, 82]]


def test_imatmul():
    mat1 = Matrix([[11, 12], [13, 14]])
    mat2 = Matrix([[1, 2], [3, 4]])
    mat1 @= mat2
    assert mat1.values == [[47, 70], [55, 82]]

    mat1 = Matrix([[11, 12], [13, 14]])
    mat2 = Matrix([[1, 2], [3, 4]])
    mat2 @= mat1
    assert mat2.values == [[37, 40], [85, 92]]


def test_matmul_bigger():
    mat1 = Matrix([[11, 12], [13, 14], [15, 16]])
    mat2 = Matrix([[1, 2, 3], [4, 5, 6]])
    mat3 = mat1 @ mat2
    assert mat3.values == [[59, 82, 105], [69, 96, 123], [79, 110, 141]]


def test_imatmul_bigger():
    mat1 = Matrix([[11, 12], [13, 14], [15, 16]])
    mat2 = Matrix([[1, 2, 3], [4, 5, 6]])
    mat1 @= mat2
    assert mat1.values == [[59, 82, 105], [69, 96, 123], [79, 110, 141]]