# iter_window.py, a sliding window python iterator with padding.
# License: Simplified BSD.
# Copyright (C) 2012 Daniel Pena 
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

def window( iterable, left, right, padding=None, step=1 ):
    """Make a sliding window iterator with padding.
    
    Iterate over `iterable` with a step size `step` producing a tuple for each element:
        ( ... left items, item, right_items ... )
    such that item visits all elements of `iterable` `step`-steps aside, the length of 
    the left_items and right_items is `left` and `right` respectively, and any missing 
    elements at the start and the end of the iteration are padded with the `padding`
    item.

    For example:
    
    >>> list( window( range(5), 1, 2 ) )
    [(None, 0, 1, 2), (0, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, None), (3, 4, None, None)]

    """
    from itertools import islice, repeat, chain
    from collections import deque

    n = left + right + 1

    iterator = chain(iterable,repeat(padding,right)) 
    
    elements = deque( repeat(padding,left), n )
    elements.extend( islice( iterator, right - step + 1 ) )

    while True: 
        for i in range(step):
            elements.append( next(iterator) ) 
        yield tuple( elements ) 

if __name__ == '__main__':
    import doctest
    doctest.testmod()

