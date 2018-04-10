def ussv():
    """
    Unpacking a Sequence into Separate Variables
    """
    p = (4, 5)
    x, y = p
    print(x)
    print(y)

    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    name, shares, price, date = data
    print(name)
    print(date)
    name, shares, price, (year, mon, day) = data
    print(name)
    print(year)
    print(mon)
    print(day)

    # mistmatch in the number of elements
    p = (4, 5)
    try:
        x, y, z = p
    except ValueError as e:
        print(e)

    # Unpacking with any itterable (sttring, files iterators and generators)
    s = "Hello"
    a, b, c, d, e = s
    print(a, b, e)

    # Discard certain values (throwaway variable name)
    data = ['ACME', 50, 91.1, (2012, 12, 21)]
    _, shares, price, _ = data
    print(shares, price)


def ueial():
    """
    Unpacking Elements from Iterables of Arbitrary Length
    """

    def drop_first_last(grades):
        def avg(x): return sum(x) / len(x)
        first, *middle, last = grades
        print(middle)
        return avg(middle)
    grades = [2, 3, 4, 5, 4, 2, 3, 2, 4]
    print(drop_first_last(grades))

    user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    name, email, *phone_numbers = user_record
    print(name)
    print(email)
    print(phone_numbers)

    # use stared variable in the beginning
    *trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
    print(trailing)
    print(current)

    ###
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]

    def do_foo(x, y):
        print('foo', x, y)

    def do_bar(s):
        print('bar', s)

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)
    ###

    # string processing operations

    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fields, homedir, sh = line.split(':')

    print(uname)
    print(homedir)
    print(sh)

    # Discard certain values (throwaway variable name)
    record = ('ACME', 50, 123.45, (12, 18, 2012))
    name, *_, (*_, year) = record
    print(name)
    print(year)

    items = [1, 10, 7, 4, 5, 9]
    head, *tail = items
    print(head)
    print(tail)

    # use in recurcive function
    def sum_r(items):
        head, *tail = items
        return head + sum_r(tail) if tail else head

    print(sum_r(items))


def ipq():
    """
    Implementing a Priority Queue
    """
    import heapq

    class PriorityQueue:
        def __init__(self):
            self._queue = []
            self._index = 0

        def push(self, item, priority):
            heapq.heappush(self._queue, (-priority, self._index, item))
            self._index += 1

        def pop(self):
            return heapq.heappop(self._queue)[-1]

    class Item:
        def __init__(self, name):
            self.name = name

        def __repr__(self):
            return "Item({!r})".format(self.name)

    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())

    # discussion

    # instances of Item can`t be ordered
    a = Item('foo')
    b = Item('bar')
    try:
        a > b
    except TypeError as e:
        print(e)

    # adding priority with tuples
    a = (1, Item('foo'))
    b = (5, Item('bar'))

    print(a > b)
    # If two tuples with equal priorities are compared, the comparison fails as before
    c = (1, Item('grok'))
    try:
        c > a
    except TypeError as e:
        print(e)

    # add an extra index
    a = (1, 0, Item('foo'))
    b = (5, 1, Item('bar'))
    c = (1, 2, Item('grok'))

    print(a > b)
    print(a > c)


def mkmvd():
    """
    Mapping Keys to Multiple Values in a Dictionary
    """
    from collections import defaultdict
    dl = defaultdict(list)
    dl['a'].append(1)
    dl['a'].append(2)
    dl['b'].append(4)
    print(dl)

    ds = defaultdict(set)
    ds['a'].add(1)
    ds['a'].add(2)
    ds['b'].add(1)
    ds['b'].add(1)
    ds['c'] = "sdf"
    print(ds)

    # regular dict vs default dict
    pairs = [("a", 1), ("a", 2), ("b", 12)]
    # regular
    d = {}
    for key, value in pairs:
        if key not in d:
            d[key] = []
        d[key].append(value)
    print(d)

    # defaultdict
    d = defaultdict(list)
    for key, value in pairs:
        d[key].append(value)
    print(d)


def dko():
    """
    Keeping Dictionaries in Order
    """
    from collections import OrderedDict

    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4

    for key in d:
        print(key, d[key])

    # useful when you want to build a mapping that you may want to later 
    # serialize or encode into a different format
    import json
    print(json.dumps(d))


def cv():
    """
    Calculating with Dictionaries
    """
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    min_price = min(zip(prices.values(), prices.keys()))
    print(min_price)

    max_price = max(zip(prices.values(), prices.keys()))
    print(max_price)

    prices_sorted = sorted(zip(prices.values(), prices.keys()))
    print(prices_sorted)

    # zip creates a iterator !
    prices_and_names = zip(prices.values(), prices.keys())
    print(min(prices_and_names))
    try:
        print(min(prices_and_names))
    except ValueError as e:
        print(e)

    # when the values are equal the sorting will be performed by the key
    prices = {'AAA': 45.23, 'ZZZ': 45.23}
    print(min(zip(prices.values(), prices.keys())))
    print(max(zip(prices.values(), prices.keys())))


def fctd():
    """
    Finding Commonalities in Two Dictionaries
    """

    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    # Find keys in common
    print(a.keys() & b.keys())

    # Find keys in a that are not in b
    print(a.keys() - b.keys())

    # Find (key, value) pair in common
    print(a.items() & b.items())

    # Make a new dictionary with certain keys removed
    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)

    # dict_keys (a.keys()) and dict_items (a.items()) behaive like set and
    # support all set operations

if __name__ == '__main__':
    # ussv()
    # ueial()
    # ipq()
    # mkmvd()
    # dko()
    # cv()
    fctd()
