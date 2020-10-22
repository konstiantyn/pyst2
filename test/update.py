#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set et sw=4 fenc=utf-8:
#
import asterisk.config

  
def add(a, b):
  
    # returning sum of a and b 
    return a + b 
  
def is_true(a): 
  
    # returning boolean of a 
    return bool(a) 
  
# calling function 
res = add(2, 3) 
print("Result of add function is {}".format(res)) 
  
res = is_true(2<5) 
print("\nResult of is_true function is {}".format(res)) 
