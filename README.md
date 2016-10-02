# Lint-Code
history of dummy tries on Lint Code problems

# Oct.2

- No.107 Word Break

reference:http://www.cnblogs.com/zuoyuan/p/3760660.html

the above reference provides implementation of the core concept of this problem: dynamic programming. it's easier to just ask if it's possible to break the word, so dynamic programming will be enough. however, the code in reference does not pass Lint Code tests for time limits. so I modified and added some cases besides simply using dynamic programming:

1. if dictionary is empty: then see if s is empty string or not

2. if dictionary only has single letters: just create distinct letter lists in s and decide if the list is the same as dictionary keys

3. if dictionary has all keys of same length: break s into pieces of that length, take the distinct list of those pieces, and decide if it is the same as dictionary keys

4. finally if the above situation does not apply, using dynamic programming

the modified code successfully solved the problem on Lint Code

this problem share similarity with the Palindrome Partition II problem in that:

they both use boolean dynamic programming

but Palindrome should have a table to store minimum # of cuts, so this problem is actually easier to solve than Palindrome. but still I didn't think of the solution by myself, so I still need more practice on dynamic programming problems.

# Sep.30 & Oct.1

- No. 118 Distinct Subsequences

also referenced from:
http://www.cnblogs.com/zuoyuan/p/3767256.html

first I rephrased the problem for quite some time. turns out it is phrased as: find # of times of subsequence T appears in S.

this is also a dynamic programming problem.

let s be our source word and t be our target subsequence. basically, if s[i] == t[j], then # of times of subsequence t[:j+1] in s[:i+1] depends on # of subsequences t[:j] in s[:i], plus # of times of subsequence t[:j+1] appear in s[:i]. if s[i] != t[j], then timesOf(t[:j+1]) in s[:i+1] = timesOf(t[:j]) in s[:i]

build dynamic programming table, table[i][j] represents # of times of subsequences t[:j+1] appear in s[:i+1]

- No.119 Edit Distance

this is a classic problem using dynamic programming. no doubt using DFS will be too slow. this solution is based on reference online:
http://www.cnblogs.com/zuoyuan/p/3773134.html

some tricks when designing this dp table:

there are 3 methods: add, delete and replace. if s is our source word and t is our target word(final state), then adding in s == deleting in t. realizing this will help make the table. for example, table[s][t] = table[s-1][t] + 1(adding in s) = table[s][t-1] + 1(adding in t, or deleting in s). 

then decide if s[i] == t[j], if yes then we only need to care about min edit among three:table[s-1][t-1],table[s-1][t] + 1 and table[s][t-1] + 1, if no then also consider among three:table[s-1][t-1]+1,table[s-1][t] + 1 and table[s][t-1] + 1. notice here the first operation got extra +1 because it is actually doing 'replacing'.

- No.108 Palindrome Partition II

my own attempt was not successful, by using LCS to calculate s and its reverse string, it was not correct for this problem because LCS does not distinguish continuous and discontinuous palindromes. The reference I found online actually was way easier than my solution, using a simple idea as well, by creating table and see if 
1. s[i]==s[j] and if 
2. j and i are adjacent(j-i<2) or previous letters are the same:s[i-1]=s[j+1]

the trick here is instead of judging previous letters through s itself, use a boolean table to check if all previous letters are same. using string s will not have that information.

finally keep a dp list to decide the minimum # of cuts

# Sep.29

- No.106 Convert Sorted List to Balanced BST

divide linked list into two halfs, and recursively use sortedListToBST function to build tree. if left or right half has only one element,return that element as single root, if has two elements, use the smaller one as root and build its right child node using its next node.

it should be very easy to implement this.

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
