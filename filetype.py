# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 15:58:13 2021

@author: rochvita
"""


filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))