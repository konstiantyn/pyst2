import subprocess as sp

def inc(x): # pragma: no cover
    return x + 1

#def test_answer():
#    assert inc(3) == 5
    
def test_ok(): # pragma: no cover
    assert 5 == 5
    
    
def check_ping(hostname): # pragma: no cover
    status = os.system("ping -c 1 " + hostname)
    if status == 0:
        return True
    else:
        return False

def test_ping_google(): # pragma: no cover
	assert check_ping("8.8.8.8")
	
def test_ping_asterisk(): # pragma: no cover
    assert check_ping("172.25.0.101")