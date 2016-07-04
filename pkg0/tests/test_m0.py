import os
import m0
import m1

TESTS_ROOT = os.path.abspath(os.path.dirname(__file__))

def bar():
	m0.foo()
	m1.hello()