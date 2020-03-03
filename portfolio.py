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
        if quantity < 0:
            raise ValueError("Negative invest not permitted")
        
        self.__assets[asset] = self.__assets.setdefault(asset,0.0) + quantity
        __value = __value + quantity
        return True
    
    def divest(self,asset,quantity):
        if quantity < 0:
            ValueError("Negative divest not permitted")
        if __assets.get(asset) = None:
            raise Exception("Asset doesn't exist")
        elif __assets.get(asset) < quantity:
            raise ValueError("Negative asset not permitted")
        
         __value = __value - quantity
        __assets[asset] = __assets.get[asset] - quantity:
        return True
    
    def getAssetValue(self,asset):
        return __assets.get(asset)
    
    def getPortfolioValue(self,asset):
        return __value