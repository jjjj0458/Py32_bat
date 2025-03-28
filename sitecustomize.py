# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 16:10:29 2022

@author: JackCCChang
"""
import sys
import site
#insert current path to sys path
sys.path.insert(0, '')

#insert user site package to sys path
site.ENABLE_USER_SITE = True
site.addusersitepackages(None)
