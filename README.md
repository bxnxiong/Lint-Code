# Lint-Code
history of dummy tries on Lint Code problems

# Sep.30 & Oct.1

- No.108 Palindrome Partition II

my own attempt was not successful, by using LCS to calculate s and its reverse string, it was not correct for this problem because LCS does not distinguish continuous and discontinuous palindromes. The reference I found online actually was way easier than my solution, using a simple idea as well, by creating table and see if 
1. s[i]==s[j] and if 
2. j and i are adjacent(j-i\<2) or previous letters are the same:s[i-1]==s[j+1]

the trick here is instead of judging previous letters through s itself, use a boolean table to check if all previous letters are same. using string s will not have that information.

finally keep a dp list to decide the minimum # of cuts

# Sep.29

- No.105 Copy List with Random Pointer

first I tried naive way: using deepcopy, but it will exceed the memory limit, probably because when using deepcopy to copy a node in linked list, it will also copy the next and random node too.

then I referenced:http://www.cnblogs.com/zuoyuan/p/3745126.html

and improved the code a bit. three steps are involved in the reference and in my code:

-- step 1: insert node of same label between original node and its next node, i.e. 1->1->2->2->3->3 compared to old list 1->2->3

-- step 2: to fill up random node information of new nodes, reference the old node, if pointer points to old node(where random is not None, if it's None then don't bother), set its next node's pointer to next node of its random node, i.e. new_node.random = old_node.random.next, where new_node = old_node.next

-- step 3: set step = 2 and change next pointers to every other node in the list, then return.


# Sep.28

- No.104 Merge K Lists

first I tried naive way: loop through every list and see if its first element is minimum, if yes then move pointer to next element, if not check next linked list. It is correct but does not pass time complexity for cases where every linked list looks like: X->null. 

the improved version is to use merge-sort like implementation, divide and sort two half lists recursively. now it passes all the test.

# Sep.27
- No.113 Remove Duplicates from Sorted List

the main idea is to have three pointers and one linked list to return the result. one pointer 'pre' will start from position '0', one pointer 'head' start from index 1 and the other pointer 'pointer' (I could use a better name but originally this one moves a lot so pointer may indicate its activeness) start from index 2. having pre always one step prior to head will help link pre and pointer.next(i.e. to delete duplicate values)

- No.102 Detect Linked List Cycle - first time successful implementation

when I was looking for reorder list problem solution, I learned the trick of quick and slow pointers. I thought since the linked list is a cycle, I can use same two pointers trick to decide if they meet after some loops, therefore using while loop to decide if they meet at the same node. Or if they end up having None value then it's not a cycle. 

Simply judging if there's an end will not solve this problem, since the while loop will never ends(stop when there's a None will never be satisfied)

- No.99 Reorder List problem - naive divide implementation and half-reverse-combine implementation

The first implementation does not pass time complexity, the latter I learned from source:
http://www.cnblogs.com/zuoyuan/p/3700846.html
and it should work. 
--updated tonight for reverse.py for special cases where head1/head2 could be null.
Passed the test on lint code successfully.

# Sep.26
- No.98 Sort List problem - quick sort implementation

quick sort has swapping operations, if changing links I think might be very troublesome, so I simply exchange values of two positions. Sadly this program does not pass time complexity. Maybe I should try Hoare implementation.

# Sep.25
- No.98 Sort List problem - merge sort implementation

this is the first time I encounter linked list. The takeaway is the manipulation of linked list, plus I learned to use yield to make a generator of linked list and do the common iterations.
My code does not pass the time complexity because I store all (partial) linked lists inside another list, which will bring in extra computation to initialize such list first. The successful implementation I found on https://lefttree.gitbooks.io/leetcode/content/linkedList/sortList.html
actually partition linked list into two halves, which I didn't know previously. Also by sorting linked lists, this program actually changes the links instead of values which is new to me too.

- No.97 Validate Binary Tree

the idea is to not only check the validity of left and right child node of their parent node, also check the validity of:

-- all right nodes of the left child

-- and all left nodes of the right child

using while loop can do that
