from urllib.request import urlopen, URLError

def pytest_terminal_summary(terminalreporter, exitstatus): # pylint: disable=unused-argument
    _add_patterns()
    if exitstatus == 0:
        _pattern('pytest-success')
    else:
        _pattern('pytest-failure')

def _add_patterns():
    try:
        urlopen('http://localhost:8934/blink1/pattern/add?pname=pytest-success&pattern=0.5,%2300ff00,0.5,%23000000,0.5')
        urlopen('http://localhost:8934/blink1/pattern/add?pname=pytest-failure&pattern=3,#ff0000,0.3,1,#ff0000,0.3,2,#000000,0.1,0,#ff0000,0.3,2,#ff0000,0.3,1,#000000,0.1,0')
    except URLError as e:
        pass

def _pattern(name):
    try:
        urlopen('http://localhost:8934/blink1/pattern/play?pname={}'.format(name))
    except URLError as e:
        pass
