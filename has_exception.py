#!/usr/bin/env python
# encoding: utf-8
"""
A decorator for auto generating exception classes

About
---------------------------

Today I found myself doing the following thing a lot;

>>class MyClassException(Exception):
>>	def __init__(self,message)
>>		self._message = message
>>		
>>class MyClass(object):
>>	....
>>	....
>>	....
>>		raise MyClassException('Somthing terrible happened')
		
Well, this code -i hope- will let you do the following;

>>@has_exception
>>class MyClass(object):
>>	....
>>		raise MyClass.Exception('something terrible happened again')
		
"""
import unittest

# The decorator
def has_exception(_class):
	def init(self, _message=''):
		self._message = _message
		_message = property(_get_message, _set_message)
		
	def _get_message(self): 
		return self._message
	
	def _set_message(self, message): 
		self._message = message
	
	excname = 'Exception'
	excclass = type(excname, (Exception,), {'__init__': init, '_get_message': _get_message,
					'_set_message': _set_message})
	setattr(_class, excname, excclass)
	return _class


class has_exeption_tests(unittest.TestCase):
	def setUp(self):
		pass
	
	def test_exception(self):
		self.failUnlessRaises(myclass.Exception, myclass, 0)


if __name__ == '__main__':
	@has_exception
	class myclass(object):
		def __init__(self, foo):
			if foo != 1:
				raise self.Exception('OMFG!')
	
	unittest.main()
