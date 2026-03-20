from src.maths_calculations import add, mul

def test_add():
    assert add(2,3)==5
    assert add(-1,4)==3
    assert add(1,0)==1
def test_mul():
    assert mul(0,1)==0
    assert mul(4,1)==4
    assert mul(2,4)==8