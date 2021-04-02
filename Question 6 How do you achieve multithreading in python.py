from os import times
from typing import type_check_only


Python has a multi-threading package but if you want to multi-thread to speed 
your code up, then it's usually not a good ideal to use it.

Python has a construct called the Global Interpreter Lock(GIL).
The GIL makes sure that onlu on of your threads can execute at any one times

A thread acquires the GIL, does a little work then passes the GIL onto the next thread.
This happens very quickly it may seem like your threads are executing in parallel
but they're really taking turn using the same CPU core All this GIL passing add 
overhead to the execution this mean tha if you want to make your code
run faster then using the threading package is often not good idea