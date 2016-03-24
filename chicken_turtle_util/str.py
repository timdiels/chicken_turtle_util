# Copyright (C) 2016 VIB/BEG/UGent - Tim Diels <timdiels.m@gmail.com>
# 
# This file is part of Chicken Turtle Util.
# 
# Chicken Turtle Util is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Chicken Turtle Util is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Chicken Turtle Util.  If not, see <http://www.gnu.org/licenses/>.

'''
String manipulation functions
'''

def multiline_lstrip(text, drop_empty=False):
    '''
    Apply `lstrip` to each line
    
    Parameters
    ----------
    text : str
    drop_empty : bool
        Drop empty lines
        
    Returns
    -------
    str
    '''
    return '\n'.join(x for x in map(str.lstrip, text.splitlines()) if (not drop_empty or x))

def multiline_strip(text, drop_empty=False):
    '''
    Apply `strip` to each line
    
    Parameters
    ----------
    text : str
    drop_empty : bool
        Drop empty lines
    
    Returns
    -------
    str
    '''
    return '\n'.join(x for x in map(str.strip, text.splitlines()) if (not drop_empty or x)) 