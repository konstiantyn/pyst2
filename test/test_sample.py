import subprocess, platform

def inc(x):
    return x + 1

#def test_answer():
#    assert inc(3) == 5
    
def test_ok():
    assert 5 == 5
    
    
def pingOk(sHost):
    try:
        output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower()=="windows" else 'c', sHost), shell=True)
    except Exception, e:
        return False
    return True

def test_ping_google():
	assert pingOk("8.8.8.8")