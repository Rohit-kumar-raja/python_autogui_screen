import pytest;
def fun():
    raise SystemExit()

def test_fun():
    with pytest.raises(SystemExit):
                    fun()
