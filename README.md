# iter_window.py

A sliding window iterator with padding.

## Synopsis

Module with the function *window* that returns a sliding window iterator with padding.
    
```python
def window( iterable, left, right, padding=None, step=1 )
    """Make a sliding window iterator with padding.
    
    Iterate over `iterable` with a step size `step` producing a tuple for each element:
        ( ... left items, item, right_items ... )
    such that item visits all elements of `iterable` `step`-steps aside, the length of 
    the left_items and right_items is `left` and `right` respectively, and any missing 
    elements at the start and the end of the iteration are padded with the `padding`
    item.

    For example:
    
   >>> list( window( range(1,6), 1, 2 ) )
   [(None, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, None), (4, 5, None, None)]

    """
```
## Example

Iterate over the first 5 positive integers with a window, padded with None items,
that extends 1 item to the left and 2 to the right:

```python
>>> list( window( range(1,6), 1, 2 ) )
[(None, 1, 2, 3), (1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, None), (4, 5, None, None)]
```

## Simplified BSD License

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copyright (c) 2012, Daniel Pena 
All rights reserved.

