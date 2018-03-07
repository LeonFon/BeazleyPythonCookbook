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

if __name__ == '__main__':
    # ussv()
    ueial()
