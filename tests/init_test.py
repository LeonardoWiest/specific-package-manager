from core.init import init
import os
import sys
import json
sys.path.append("..")  # Adds higher directory to python modules path.


def test_simple_noFile():
    if (os.path.isfile('output/packages.json')):
        os.remove('output/packages.json')
    assert init.simple('', '') == []



def test_simple_invalidFile():
    open('output/packages.json', 'w').write('')
    assert init.simple('', '') == 'There is an invalid file, please remove it: packages.json'



def test_full():
    assert init.full('test', 'master') == 'All Done'
    assert json.loads(open('output/packages.json', "r").read()) == {'dependencies': ['https://github.com/charoleizer/specific-package-manager.git: master']}
    assert json.loads(open('output/failed-packages.json', "r").read()) == {'dependencies': []}


def test_full_noConfig():
    assert init.full('test_non_exists', 'master') == 'Project test_non_exists cant be found on configuration file'



def test_simple_fake():
    assert init.simple('', '') == {'dependencies': [
        'https://github.com/charoleizer/specific-package-manager.git: master']}



def test_simple():
    assert init.simple('https://github.com/charoleizer/about-me.git', 'master') == {'dependencies': ['https://github.com/charoleizer/specific-package-manager.git: master', 'https://github.com/charoleizer/about-me.git: master']}



def test_full_invalidProject():
    assert init.full('test', 'Trololo') == 'All Done'
    assert json.loads(open('output/failed-packages.json', "r").read()) == {'dependencies': ['https://github.com/charoleizer/specific-package-manager.git: Trololo']}