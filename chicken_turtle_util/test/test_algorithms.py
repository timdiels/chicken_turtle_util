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
Test chicken_turtle_util.algorithms
'''

import pytest
import numpy as np
from chicken_turtle_util.algorithms import spread_points_in_hypercube, multi_way_partitioning
from scipy.spatial.distance import euclidean
from itertools import product
from more_itertools import ilen
from collections_extended import bag, frozenbag

class TestSpreadPointsInHypercube(object):
     
    def test_invalid_point_count(self):
        '''When point_count < 0, ValueError'''
        with pytest.raises(ValueError):
            spread_points_in_hypercube(point_count=-1, dimension_count=1)
            
    def test_invalid_dimension_count(self):
        '''When dimension_count < 1, ValueError'''
        with pytest.raises(ValueError):
            spread_points_in_hypercube(point_count=1, dimension_count=-1)
        
    @pytest.mark.parametrize('dims', range(1,5))    
    def test_no_points(self, dims):
        '''When point_count = 0, returns empty np.array, regardless of dimension_count'''
        assert np.array_equal(spread_points_in_hypercube(point_count=0, dimension_count=dims), np.empty(shape=(0,dims)))
        
    @pytest.mark.parametrize('dims', range(1,5))    
    def test_one_point(self, dims):
        '''When point_count = 1, it should lay in the hypercube'''
        points = spread_points_in_hypercube(point_count=1, dimension_count=dims)
        assert np.all((points >= 0) & (points <= 1))
        
    @pytest.mark.parametrize('point_count,dim_count', product((2,5,10,30), range(1,5)))    
    def test_happy_days(self, point_count, dim_count):
        '''When any other input, perform at least as well as a hypergrid layout of points'''
        points = spread_points_in_hypercube(point_count=point_count, dimension_count=dim_count)
        assert points.shape == (point_count, dim_count)
        
        # points must lay in the hypercube
        assert np.all((points >= 0) & (points <= 1))
        
        # actual min distance >= min distance in a hypergrid 
        min_distance = min(euclidean(points[i], points[j]) for i in range(point_count) for j in range(i+1, point_count))
        points_per_side = np.ceil(point_count ** (1/dim_count))
        hypergrid_min_distance = 1 / (points_per_side - 1)
        assert min_distance > hypergrid_min_distance or np.isclose(min_distance, hypergrid_min_distance)         
        
        # Note: alternatively we could test that relative error stays within
        # some constant, relative to the ideal solution (found through brute force)

class TestMultiWayPartitioning(object):
    
    # From http://stackoverflow.com/a/18354471/1031434
    def _groups(self, list_, group_count):
        if list_:
            prev = None
            for t in self._groups(list_[1:], group_count):
                tup = sorted(t)
                if tup != prev:
                    prev = tup
                    for i in range(group_count):
                        yield tup[:i] + [[list_[0]] + tup[i],] + tup[i+1:]
        else:
            yield [[] for _ in range(group_count)]
            
    def _multi_way_partitioning_brute_force(self, items, bin_count):
        '''Brute force that generates ideal solution'''
        assert bin_count > 1
        best_bins = [items, []*(bin_count-1)]
        best_diff = np.inf
        for bins in self._groups(items, bin_count):
            diff= self.get_distance(bins)
            if diff < best_diff:
                best_bins = bins
                best_diff = diff
        return best_bins
    
    def get_distance(self, bins):
        sums = set()
        for bin_ in bins:
            sums.add(sum(weight for _, weight in bin_))
        return max(sums) - min(sums)
        
    def reapply_weights(self, items, bins):
        weights = dict(items)
        return [[(x, weights[x]) for x in bin_] for bin_ in bins]
        
    def generate_test_data(self):
        items = list(enumerate(list(range(1,4))*20))
        params = list(product((2,5,10,12), range(2,6)))
        params = [(items[:item_count], bin_count) for item_count, bin_count in params]
        solutions = []
        for items, bin_count in params:
            bins = self._multi_way_partitioning_brute_force(items, bin_count)
            distance = self.get_distance(bins)
            solutions.append((items, bin_count, distance))
            print('+', end='', flush=True)
        print()
        print(repr(solutions))
    
    def test_invalid_bin_count(self):
        '''When bin_count < 1, ValueError'''
        with pytest.raises(ValueError):
            multi_way_partitioning({(1,2)}, bin_count=0)
            
    def test_no_items(self):
        '''When no items, return empty bins'''
        assert multi_way_partitioning([], bin_count=2) == bag([frozenbag(), frozenbag()])
        
    def test_one_item(self):
        '''When one item, return 1 singleton and x empty bins'''
        assert multi_way_partitioning([(1,2)], bin_count=2) == bag([frozenbag([1]), frozenbag()])
        
    def test_one_bin(self):
        '''When one bin, return single bin containing all items'''
        assert multi_way_partitioning([(1,2), (2,3)], bin_count=1) == bag([frozenbag([1,2])])
    
    params=[([(0, 1), (1, 2)], 2, 1), ([(0, 1), (1, 2)], 3, 2), ([(0, 1), (1, 2)], 4, 2), ([(0, 1), (1, 2)], 5, 2), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2)], 2, 1), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2)], 3, 0), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2)], 4, 1), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2)], 5, 2), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3), (6, 1), (7, 2), (8, 3), (9, 1)], 2, 1), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3), (6, 1), (7, 2), (8, 3), (9, 1)], 3, 1), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3), (6, 1), (7, 2), (8, 3), (9, 1)], 4, 1), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3), (6, 1), (7, 2), (8, 3), (9, 1)], 5, 1), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3), (6, 1), (7, 2), (8, 3), (9, 1), (10, 2), (11, 3)], 2, 0), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3), (6, 1), (7, 2), (8, 3), (9, 1), (10, 2), (11, 3)], 3, 0), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3), (6, 1), (7, 2), (8, 3), (9, 1), (10, 2), (11, 3)], 4, 0), ([(0, 1), (1, 2), (2, 3), (3, 1), (4, 2), (5, 3), (6, 1), (7, 2), (8, 3), (9, 1), (10, 2), (11, 3)], 5, 1)]
    @pytest.mark.parametrize('items,bin_count,ideal_distance', params)
    def test_happy_days(self, items, bin_count, ideal_distance):
        '''When any other input, ...'''
        bins = multi_way_partitioning(items, bin_count)
        
        # Fill as many bins as possible
        assert bins.count(frozenbag()) == max(bin_count - len(items), 0)
        
        # Relative error to ideal solution should be acceptable
        actual_distance = self.get_distance(self.reapply_weights(items, bins))
        assert actual_distance >= (ideal_distance - 1e8), 'bug in test'
        assert actual_distance <= 1.3 * ideal_distance
        
        # XXX could use more varied input
        
# TestMultiWayPartitioning().generate_test_data()

'''     
cli
===
from click.test import CliRunner

def test_everything():
    \'''
    Check all cli for trivial bugs
    
    The implementation itself doesn't leave much room for complex bugs
    \'''

db_args = dict(
    database_host='db_host',
    database_user='db_user',
    database_password='db_password',
    database_name='db_name'
)

Database = some mock class
    return 'database'

class MyAppContext(DatabaseMixin(Database), Context):
    pass
    
@cli.command()
@cli.option('--option')
@cli.argument('argument')
@cli.password_option('--password')
@MyAppContext.cli_options()
def main(option, argument, password, **kwargs):
    assert option == 'hi'
    assert password == 'pass
    assert argument == 'arg'
    
    context = MyAppContext(**kwargs)
    assert Database.called once with **db_args
    assert context.database == 'database'

print(main.params) # print it to see how to assert it for:
- -h --help must exist
- --option has show_default=True and required=True
- argument has required=True
- password_option has prompt=True, hide_input=True, show_default=False, required=True 

args = ['--option', 'hi', '--password', 'pass', 'arg']
args += list(iterable.flatten(('--' + k.replace('_', '-'), v) for k, v in db_args.items()))
result = CliRunner().invoke(main, args)
assert not result.exception

data_frame
==========

fillna_none(df, inplace=False)
------------------------------
class ReplaceNAWithNone(object):

@pytest.fixture
def df():
    return pd.DataFrame({
        'a' : ['magic', np.nan, 2],
        'derp' : [np.nan, np.nan, np.nan],
        5 : [7, 8, 9]  
    })

@pytest.fixture    
def df_replaced():
    return pd.DataFrame({
        'a' : ['magic', None, 2],
        'derp' : [None, None, None],
        5 : [7, 8, 9]  
    })
  
def test_not_inplace(df, df_replaced):
    \'''When df contains NaN and inplace=False, df contains NaN, return has NaN replaced\'''
    df_original = df.copy()
    retval = replace_na_with_none(df)
    assert df == df_original
    assert retval == df_replaced
  
def test_not_inplace(df, df_replaced):
    \'''When df contains NaN and inplace=True, df and return have NaN replaced\'''
    retval = replace_na_with_none(df)
    assert df == df_replaced
    assert retval == df_replaced
    
split_array_like(df, columns)
-----------------------------
class SplitArrayLike(object):
@pytest.fixture
def df():
    return pd.DataFrame({
        'check': [1, 1, 2, 3],
        'a': [[1, 2], [1, 2], [1], []],
        'b': [[1]], [3, 4, 5], [1, 2], [5,6]]
    })
    
@pytest.fixture
def df_split_a_b():
    return pd.DataFrame({
        'check': [1, 1, 1, 1, 1, 1, 1, 1, 2, 2],
        'a': [1, 2, 1, 1, 1, 2, 2, 2, 1, 1],
        'b': [1, 1, 3, 4, 5, 3, 4, 5, 1, 2]
    })

@pytest.fixture
def df_split_a():
    return pd.DataFrame({
        'check': [1, 1, 1, 1, 2],
        'a': [1, 2, 1, 2, 1],
        'b': [[1], [1], [3, 4, 5], [3, 4, 5], [1, 2]]
    })

def dfs_equal(df1, df2):
    return df1 == df2 and df1.columns == df2.columns
    
def test_split_a_b(df, df_split_a_b):
    \'''When split on 'a' and 'b', correct split\'''
    assert dfs_equal(split_array_like(('a', 'b')), df_split_a_b)
    assert dfs_equal(split_array_like(iter(('a', 'b'))), df_split_a_b)

def test_split_a(df, df_split_a):
    \'''When split on 'a', correct split\'''
    assert dfs_equal(split_array_like('a'), df_split_a) 
    assert dfs_equal(split_array_like(('a',)), df_split_a) 

debug
=====
def test_pretty_memory_info():
    assert 'memory usage' in pretty_memory_info()
    
dict
====

class PrettyPrintHead(object)

pretty_print_head(dict_, count=10)
----------------------------------
- When count < 1, ValueError
- When large enough dict, print only 10 items
- When smaller than count, print whole dict

DefaultDict
-----------
def test_default_dict():
    dict_ = DefaultDict(lambda key: key)
    assert dict_['missing'] == 'missing'
    
    dict_['present'] = 5
    assert dict_['present'] == 5
    
    del dict_['present']
    assert dict_['present'] == 'present'


invert(dict_)
-------------
>>> invert({1: 2, 3: 4})
    {2: {1}, 4: {3}}
    
>>> invert({1: 2, 3: 2, 4: 5})
{2: {1,3}, 5: {4}}

function
========
compose(*functions)
-------------------
class TestCompose(object)
    double = lambda x: 2*x
    add = lambda x: x+1
        
    def test_empty():
        \'''Composing nothing is
        with pytest.raises(ValueError):
            compose()
        
    def test_one():
        \'''Allow 'composing' just 1 function
        assert compose(double)(2) == 4
        
    def test_order():
        \'''Compose in the right order
        assert compose(double, add)(2) == 2 * (2+1)
        assert compose(add, double)(2) == 1 + 2*2 

http
====

download_file(url, destination)
-------------------------------
url = some lorem ipsum we include in our git repo and push, in test/data/lorem_ipsum.txt
OR figure out a way to launch a mini http server that serves a file via pytest

params = (
    ('.', 'lorem_ipsum.txt'), 
    ('existing_file', 'existing_file'), 
    ('new_file', 'new_file')
)
@pytest.parametrize('destination, path_expected', params)
def test_download(tmpdir, destination, path_expected):
    \'''
    - When destination is directory, README.md is saved in it
    - When destination is a file, it is overwritten with README.md contents
    - When destination does not exist, it is overwritten with README.md contents
    \'''
    tmpdir = Path(tmpdir)
    path_expected = tmpdir / path_expected
    path, name = download(url, destination)
    write_file(Path('existing_file'), 'exists')
    assert path == path_expected
    assert path.exists()
    assert name == 'README.md' 
    assert read_file(path_expected) == read_file(actual file in our repo)
    
    
iterable
========

# The implementation comes from: http://stackoverflow.com/a/6822773/1031434
sliding_window(iterable, size=2)
--------------------------------
- When size < 1, ValueError
- When size > ilen(iterable), ValueError
    with pytest.raises(ValueError):
        list(sliding_window(range(5), size=6))
- Try a couple of sizes
    assert list(sliding_window(range(5), size=1)) == [0,1,2,3,4]
    assert list(sliding_window(range(5), size=2)) == [(0,1),(1,2),(2,3),(3,4)]
    assert list(sliding_window(range(5), size=3)) == [(0,1,2),(1,2,3),(2,3,4)]
    assert list(sliding_window(range(5), size=4)) == [(0,1,2,3),(1,2,3,4)]
    assert list(sliding_window(range(5), size=5)) == [(0,1,2,3,4)] 
        
partition(iterable, key)
------------------------
def test_partition():
    assert partition(range(5), lambda x: x % 2) == {
        0: [0,2,4]
        1: [2,3]
    }

is_sorted(iterable)
-------------------
def test_is_sorted():
    assert is_sorted(range(7))
    assert not is_sorted((1,4,3))

flatten(iterable, times=1)
--------------------------
- When times < 0, ValueError
- 
    >>> list(flatten([[2, 3], 1, [5, [7, 8]]]))
    [2, 3, 1, 5, [7, 8]]
    
    >>> list(flatten([[2, 3], 1, [5, [7, 8]]], times=2))
    [2, 3, 1, 5, 7, 8]
    
    >>> list(flatten([[2, 3], 1, [5, [7, 8]]], times=3))
    [2, 3, 1, 5, 7, 8]
    
    >>> flatten([iter([2, 3]), 1, [5, iter([7, 8])]])
    iter([2, 3, 1, 5, iter([7, 8])])
    
    >>> list(flatten([[2, 3], 1, [5, [7, 8]]], times=0))
    [[2, 3], 1, [5, [7, 8]]]

logging
-------

def test_set_level
----------------------------
    logger = create dummy logger that still uses enough of logging, so maybe you'll need to capture root log output? or how know whether it emits or not?
        caplog?
    with set_level(logger, logging.INFO):
        logger.info('not ignored')
        logger.warning('not ignored')
    logger.info('ignored')
    logger.warning('not ignored')
    assert log output == 'INFO not ignored', WARNING not ignored, WARNING not ignored

multi_dict
==========

class MultiDict(object):

    def test_empty(object):
        actual = MultiDict({})
        assert set(actual.items()) == set()
        assert set(actual.keys()) == set()
        assert set(actual.values()) == set()
        assert actual.invert() == {}
        
    def test_normal(object):
        original = {
            1: {1,2,3},
            2: {1},
            3: {4,5}
        }
            
        actual_dict = original.copy()
        actual = MultiDict(actual_dict)
        
        assert actual.dict == actual_dict
        assert set(actual.items()) == {(1,1), (1,2), (1,3), (2,1), (3,4), (3,5)}
        assert set(actual.keys()) == {1, 2, 3}
        assert set(actual.values()) == {1, 2, 3, 4, 5}
        assert actual.invert() == {
            1: {1,2},
            2: {1},
            3: {1},
            4: {3},
            5: {3}
        }

pyqt
====
def test_block_signals():
    obj = QObject()
    
    with block_signals(obj):
        assert obj.blockSignals()
    assert not obj.blockSignals()
    
    obj.blockSignals(True)
    with block_signals(obj):
        assert obj.blockSignals()
    assert obj.blockSignals()
    
series
======

invert(series)
--------------
def test_invert():
    inverted = series.invert(pd.Series([1,2,3], index=[4,5,6], name='named'))
    inverted == pd.Series([4,5,6], index=[1,2,3], name='named')
    assert False # TODO does it check name and index equality?
    
set
===

merge_sets_by_overlap(sets)
--------------------------- 
    
def test_merge_sets_by_overlap():
    sets = [{1,2}, set(), {2,3}, {4,5,6}, {6,7}]
    merge_sets_by_overlap(sets)
    assert sets == [{1,2,3}, {4,5,6,7}]  # Note the order doesn't actually matter

sqlalchemy
==========

# Note: we don't expect too much atm. Code for pprint sql must exist somewhere already, we should go look for that
expected = \'''
SELECT meh, *
FROM (
SELECT magic FROM table
) as t1
UNION (
SELECT magic2 FROM TABLE
) t2
INNER JOIN table_thing t3 ON t2.id = t3.id
WHERE t3.thing = 5
GROUP BY t3.meh
\'''.lstrip()

def test_pretty_sql():
    input = expected.replace('\n', ' ').replace('  ', ' ')
    assert pretty_sql(input) == expected

str
===

input = \'''   
  the big
     white nose 
is
    very white
\'''.lstrip()

expected = \'''
the big
white nose 
is
very white
\'''

def test_multiline_lstrip():
    assert multiline_lstrip(input) == expected
    
    
various
=======
def test_object():
    Object('ignore')
    Object(ignore='ignore')
    
TODO update Raises sections of all added ValueErrors
- spread_points_in_hypercube
    When point_count < 0
    When dimension_count < 1
'''