#-------------------------------------------------------------------
# @author 
# @copyright (C) 2018, 
# @doc
#
# @end
# Created : 29. Apr 2018 8:57 PM
#-------------------------------------------------------------------

import os
import sys
import numpy as np


class Sample():
    def __init__(self):
        binary = bin(50)[2:]
        comp = ''
        print(str(binary))
        for i in str(binary):
            if int(i) == 0:
                comp = comp + '1'
            elif int(i) == 1:
                comp = comp + '0'

        print(comp)


if __name__ == '__main__':
    Sample()