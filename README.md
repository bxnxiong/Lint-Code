# Lint-Code
history of dummy tries on Lint Code problems

# Sep.27
No.99 Reorder List problem - naive divide implementation and half-reverse-combine implementation

The first implementation does not pass time complexity, the latter I learned from source:
http://www.cnblogs.com/zuoyuan/p/3700846.html
and it should work. 
--updated tonight for reverse.py for special cases where head1/head2 could be null.
Passed the test on lint code successfully.

# Sep.26
No.98 Sort List problem - quick sort implementation

quick sort has swapping operations, if changing links I think might be very troublesome, so I simply exchange values of two positions. Sadly this program does not pass time complexity. Maybe I should try Hoare implementation.

# Sep.25
No.98 Sort List problem - merge sort implementation

This is the first time I encounter linked list. The takeaway is the manipulation of linked list, plus I learned to use yield to make a generator of linked list and do the common iterations.
My code does not pass the time complexity because I store all (partial) linked lists inside another list, which will bring in extra computation to initialize such list first. The successful implementation I found on https://lefttree.gitbooks.io/leetcode/content/linkedList/sortList.html
actually partition linked list into two halves, which I didn't know previously. Also by sorting linked lists, this program actually changes the links instead of values which is new to me too.
