import nose


def setup_single_matrix_func():
    #"set up test fixtures"
    Matrix = [ [ 0.0 for i in range(bound) ] for j in range(bound)]

def teardown_single_matrix_func():
    #"tear down test fixtures"
    pass

@with_setup(setup_func, teardown_func)
def test_getTransitionSum():
    