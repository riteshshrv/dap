from collections.abc import MutableMapping

"""Abstract Base Class for map using hash-table with MAD compression and
        also implements Chaining.  #Import UnsortedTableMap
    ---------------------------------------------------------------------------
        Author:     Ritesh Shrivastav
        email:      ritesh.shrv@outlook.com
        @github:    riteshshrv
    ---------------------------------------------------------------------------"""

class MapBase(MutableMapping):

    class _item:
        """nested class to store key-value pairs as map items."""

        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

    def __eq__(self, other):
        return self._key == other._key              # compare items based on their key

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self._key < other._key

class HashMapBase(MapBase):
    
    def __init__(self,cap=11,p=109345121):
        '''Create an empty hash-table map.'''
        self._table=cap*[None]
        self._n=0                                   # number of entries in the map
        self._prime=p                               # prime for MAD compression
        self._scale=1+randrange(p-1)                # scale from 1 to p-1 for MAD
        self._shift=randrange(p)                    # shift from 0 to p-1 for MAD

    def _hash_function(self,k):
        return (hash(k)*self._scale + self._shift)%self._prime%len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self,k):
        j=self._hash_function(k)
        return self._bucket_getitem(j,k)            # may raise KeyError

    def __setitem__(self,k,v):
        j=self._hash_function(k)
        self._bucket_setitem(j,k,v)                 # subroutine maintains self._n
        if self._n>len(self._table)//2:             # keep load factor <= 0.5
            self._resize(2*len(self._table)-1)      # number 2^x-1 is often prime

    def __delitem__(self,k):
        j=self._hash_function(k)
        self._bucket._delitem(j,k):                 # may raise KeyError
        self._n -= 1

    def _resize(self,c):                            # resize bucket array to capacity c
        old=list(self.items())                      # use iteration to record existing items
        self._table=c*[None]                        # then reset table to desired capapcity
        self._n=0                                   # n computed during subsequent adds
        for (k,v) in old:
            self[k]=v                               # reinsert old key-value pair

class ChainHashMap(HashMapBase):
    '''Hash map implemented with separate chaining for collision resolution.'''

    def _bucket_getitem(self,j,k):
        bucket=self._table[j]
        if self._table[j] is None:
            raise KeyError("Key Error: ",repr(k))   # no match found
        return bucket[k]                            # may raise KeyError

    def _bucket_setitem(self,j,k,v):
        if self._table[j] is None:
            self._table[j]=UnsortedTableMap()       # bucket is new to the table
        oldsize=len(self._table[j])
        self._table[j][k]=v
        if len(self._table[j])>oldsize:             # key was new to the table
            self._n += 1

    def _bucket_delitem(self,j,k):
        bucket=self._table[j]
        if bucket is None:
            raise KeyError("Key Error: ",repr(k))   # no match found
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket is None:                      # a non-empty slot
                for key in bucket:
                    yield key

if __name__ == '__main__':
    print("This is an Abstract Base Class for implementing Hash Map wiht Chaining.")