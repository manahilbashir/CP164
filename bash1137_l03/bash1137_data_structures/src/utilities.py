"""
-------------------------------------------------------
Utilities
-------------------------------------------------------
Author:  Manahil Bashir 
ID:     169061137
Email:   bash1137@mylaurier.ca
__updated__ = "2024-05-25"
-------------------------------------------------------
"""
from Stack_array import Stack
from Queue_array import Queue


def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) > 0:

        stack.push(source.pop())

    return None


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not stack.is_empty():

        target.append(stack.pop())

    target.reverse()

    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()

    x = s.is_empty()
    print("Stack should be empty (True): {}".format(x))

    s.push(source.pop())

    x = s.is_empty()
    print("Stack should be non-empty (False): {}".format(x))

    y = s.pop()
    print("Should return and remove top value: {}".format(y))

    x = s.is_empty()
    print("Stack should be empty (True): {}".format(x))

    s.push(source.pop())

    y = s.peek()
    print("Should return top value: {}".format(y))

    s.push(source.pop())

    y = s.peek()
    print("Should return top value: {}".format(y))

    return None


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        queue.insert(source.pop(0))

    return None


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())
    return


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here

    print("Length of Queue: {}".format(len(q)))
    print("Length of list: {}".format(len(a)))

    while a != []:
        value = a[0]
        q.insert(value)
        a.remove(value)

    print("Length of Queue: {}".format(len(q)))
    print("Length of list: {}".format(len(a)))

    if q.is_empty() == False:
        print("Queue is not empty")
        value = q.peek()
        print("Peek: {}".format(value))
        n = len(q)
        print("Queue length: {}".format(n))
    else:
        print("Queue is empty")
        n = len(q)
        print("Queue length: {}".format(n))

    # print the results of the method calls and verify by hand

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:

        pq.insert(source.pop(0))

    return


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():

        target.append(pq.remove())

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    # tests for the priority queue methods go here

    print("Length of Queue: {}".format(len(pq)))
    print("Length of list: {}".format(len(a)))

    while a != []:
        value = a[0]
        pq.insert(value)
        a.remove(value)

    print("Length of Queue: {}".format(len(pq)))
    print("Length of list: {}".format(len(a)))

    if pq.is_empty() == False:
        print("Queue is not empty")
        value = pq.peek()
        print("Peek: {}".format(value))
        n = len(pq)
        print("length of queue: {}".format(n))
    else:
        print("Queue is empty")
        n = len(pq)
        print("length of queue: {}".format(n))

    # print the results of the method calls and verify by hand

    return
