import subprocess as sp

def inc(x): # pragma: no cover
    return x + 1

#def test_answer():
#    assert inc(3) == 5
    
def test_ok(): # pragma: no cover
    assert 5 == 5
    
    
def pingOk(sHost): # pragma: no cover
    status,result = sp.getstatusoutput("ping -c1 -w2 " + str(sHost))
    if status == 0:
        return True
    else:
        return False

def test_ping_google(): # pragma: no cover
	assert pingOk("8.8.8.8")
	
def test_ping_asterisk(): # pragma: no cover
    assert pingOk("172.25.0.101")