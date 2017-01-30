from urllib.request import urlopen, URLError

def pytest_terminal_summary(terminalreporter, exitstatus): # pylint: disable=unused-argument
    _add_patterns()
    if exitstatus == 0:
        _pattern('pytest-success')
    else:
        _pattern('pytest-failure')

def _add_patterns():
    _blink('pattern/add?pname=pytest-success&pattern=0.5,%2300ff00,0.5,%23000000,0.5')
    _blink('pattern/add?pname=pytest-failure&pattern=1,%23ff0000,0.3,1,%23ff0000,0.3,2,%23000000,0.1,0,%23ff0000,0.3,2,%23ff0000,0.3,1,%23000000,0.1,0')

def _pattern(name):
    _blink('pattern/play?pname={}'.format(name))

def _blink(command):
    try:
        urlopen('http://localhost:8934/blink1/{}'.format(command))
    except URLError as e:
        pass
