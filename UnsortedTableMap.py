from collections.abc import MutableMapping


class MapBase(MutableMapping):

    """My own Abstract Base Class that includes a nonpublic _item class.
    ---------------------------------------------------------------------------
        Author:     Ritesh Shrivastav
        email:      ritesh.shrv@outlook.com
        @github:    riteshshrv
    ---------------------------------------------------------------------------"""

    class _item:

        """nested class to store key-value pairs as map items."""

        __slots__ = '_key', '_value'

        def __init__(self, key, value):
            self._key = key
            self._value = value

    def __eq__(self, other):
        return self._key == other._key  # compare items based on their key

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self._key < other._key


class UnsortedTableMap(MapBase):

    """Map implementation using an unordered list."""

    def __init__(self):
        """Create an empty map."""
        self._table = []

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('KeyError: ', repr(k))

    def __setitem__(self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:				# found a match
                item._value = v 				# reassign value
                return 						# and quit
        # did not find any match for key
        self._table.append(self._item(k, v))

    def __delitem__(self, k):
        """Remove an item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key:		# found a match
                self._table.pop(j)			# remove item
                return 						# and quit
        raise KeyError('Key Error: ', repr(k))

    def __iter__(self):
        """Generate iteration of the maps's keys."""
        for item in self._table:
            yield item._key					# yield the key
