# Copyright (C) 2015 VIB/BEG/UGent - Tim Diels <timdiels.m@gmail.com>
# 
# This file is part of Chicken Turtle.
# 
# Chicken Turtle is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Chicken Turtle is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with Chicken Turtle.  If not, see <http://www.gnu.org/licenses/>.

'''
Extensions to functools
'''

from functools import reduce

def compose(*functions):
    '''
    Compose functions
    
    E.g. compose(f1, f2) returns f1 o f2, i.e. lambda x: f1(f2(x))
    
    Parameters
    ----------
    functions : list-like of (function : func(x) -> y)
    '''
    apply = lambda x, y: y(x) 
    return lambda x: reduce(apply, functions, x)