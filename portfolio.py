# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 09:20:34 2020

@author: 10529473
"""

# REPO: https://github.com/10529473/portfolio.git

class Portfolio:
    def __init__(self,asset,quantity):
        self.__assets = {}
        self.__value = 0
        self.invest(asset,quantity)
    
    def invest(self,asset,quantity):
        if quantity < 0:
            raise ValueError("Negative invest not permitted")
        
        self.__assets[asset] = self.__assets.setdefault(asset,0.0) + quantity
        self.__value = self.__value + quantity
        return True
    
    def divest(self,asset,quantity):
        if quantity < 0:
            ValueError("Negative divest not permitted")
        if self.__assets.get(asset) == None:
            raise Exception("Asset doesn't exist")
        elif self.__assets.get(asset) < quantity:
            raise ValueError("Negative asset not permitted")
        
        self.__value = self.__value - quantity
        self.__assets[asset] = self.__assets.get[asset] - quantity
        return True
    
    def getAssetValue(self,asset):
        return self.__assets.get(asset)
    
    def getPortfolioValue(self):
        return self.__value

#class PortfolioCollection