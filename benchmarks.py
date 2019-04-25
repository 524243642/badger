import gc
import random
import time
from contextlib import contextmanager

from boost_collections.zskiplist.zset_node import ZsetNode
from boost_collections.zskiplist.zset_obj import ZsetObj


@contextmanager
def timeit(name):
    oldgc = gc.isenabled()
    gc.disable()
    print('%s:' % name)
    t1 = time.time()
    yield
    t2 = time.time()
    if oldgc:
        gc.enable()
    print(t2 - t1)


RANDOMLONGS_E4 = [random.randint(1, 1000000) for i in range(100000)]
RANDOMLONGS_E3 = [random.randint(1, 1000000) for i in range(1000)]


def zadd():
    zset_obj = ZsetObj()
    with timeit('add operation of SortedSet'):
        for i in RANDOMLONGS_E4:
            zset_obj.zadd(ZsetNode(str(i), i))

    with timeit('range operation of SortedSet'):
        result = zset_obj.zrange(0, 100000, 1)


def list_contains():
    with timeit('search inside list'):
        for i in RANDOMLONGS_E3:
            i in RANDOMLONGS_E4


def zscore():
    zset_obj = ZsetObj()
    for i in RANDOMLONGS_E4:
        zset_obj.zadd(ZsetNode(str(i), i))
    with timeit('search inside SortedSet'):
        for i in RANDOMLONGS_E3:
            zset_obj.zscore(str(i))


def zrange_by_score():
    zset_obj = ZsetObj()
    for i in RANDOMLONGS_E4:
        zset_obj.zadd(ZsetNode(str(i), i))
    with timeit('search range inside SortedSet'):
        for i in range(0, 10000):
            zset_obj.zrange_by_score(1, 0, 10000, 0)


def zrange():
    zset_obj = ZsetObj()
    for i in RANDOMLONGS_E4:
        zset_obj.zadd(ZsetNode(str(i), i))
    with timeit('search range inside SortedSet'):
        for i in range(0, 10000):
            zset_obj.zrange(1, 10000, 1)


if __name__ == '__main__':
    zrange_by_score()
    # zrange()
    # zadd()
    # list_contains()
    # zscore()
