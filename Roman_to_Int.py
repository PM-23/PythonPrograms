# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 18:17:11 2022

@author: Acer
"""

class Ok:
    
    
    
    def rToInt(self,s:str):
        val = {"I":1,"V":5}
        int_num = 0
        num = 0
        for c in s:
            if c in val.keys():
                print(val.get(c))
                int_num = val.get(c) + int_num
                
        print(int_num)
 
o = Ok()       
o.rToInt("VII")