import pytest
from src.mylist import *
from src.mylistsub import *
from src.add_inherent import *

class TestMyListSub:
    @pytest.mark.parametrize("li, k, r", [
        (MyListSub([1,2,3]), 0, 1),
        (MyListSub([1,2,3]),slice(1,3),MyList([2,3]))
    ])
    def test_getitem(self, li, k, r):
        if type(r) == int:
            assert li[k] == r
        elif type(r) == MyList:
            assert type(li[k]) == MyList
            assert li[k].data == r.data 
    @pytest.mark.parametrize("l1, n, l2", [
        (MyListSub([1,2]), 3, MyList([1,2,3]))
    ])
    def test_append(self, l1,n,l2):
        l1.append(n)
        assert l1.data == l2.data

    @pytest.mark.parametrize("l1, l2", [
        (MyListSub([2,1]), MyListSub([1,2]))
    ])
    def test_sort(self, l1, l2):
        l1.sort()
        assert l1.data == l2.data

    def test_iter(self):
        iter = MyListSub([1,2])
        
        i = 0
        for iter_i in iter:
            if i == 0:
                assert iter_i == 1
            elif i == 1:
                assert iter_i == 2

            i += 1

    def test_add(self):
        l1 = MyListSub([1,2])
        l2 = MyList([3,4])
        l3 = MyList([10,11])

        assert type(l1 + l2) == MyList
        assert (l1 + l2).data == MyList([1,2,3,4]).data
        l1 + l3
        assert l1.i == 3