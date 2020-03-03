# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 09:20:34 2020

@author: 10529473
"""

# REPO: https://github.com/10529473/portfolio.git

class Portfolio:
    __value = 0
    __assets = {}
    
    def __init__(self,asset,quantity):
        self.__assets[asset] = quantity
    
    def invest(self,asset,quantity):
        self.__assets[asset] = self.__assets.setdefault(asset,0.0) + quantity
