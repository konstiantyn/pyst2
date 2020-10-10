import subprocess as sp

def inc(x):
    return x + 1

#def test_answer():
#    assert inc(3) == 5
    
def test_ok():
    assert 5 == 5
    
    
def pingOk(sHost):
    status,result = sp.getstatusoutput("ping -c1 -w2 " + str(sHost))
    if status == 0:
        return True
    else:
        return False

def test_ping_google():
	assert pingOk("8.8.8.8")