# Lint-Code
history of dummy tries on Lint Code problems

# Oct.28

- No.392 House Robber

the transition function for this dynamic programming problem is as follows:

have a list storing maximum gain so far. 

gain[i] = max(gain[i-1],gain[i-2]+current_gain[i])

emission:

gain[0] = current_gain[0];gain[1] = current_gain[1]

# Oct.27

- No.383 Container With Most Water

this is similar to Trap Water problem. but is actually simpler than that. we just need to find bars and calculate area with two bars found and return the max area. when finding bars, start from very beginning and very end, and let them get closer by moving left bar 1 step right if left bar is lower than right bar, or by moving right bar 1 step left if right bar is no lower than left bar.

- No.384 Longest Substring Without Repeating

this is a dynamic programming problem. the key is to find the transition function so that it keeps longest non-repeating substring. 

here the transition function is min(i-book[s[i]][0],book[s[i-1]\[1]+1]). 

i is the index of current str, book is a dictionary remembering two things:

1. the index of current letter(before visiting current letter, at which index does current letter appears). 

2. the length of substring ending in current letter, after previous current letter appears. eg. given 'abacda', changes in book['a'] would be (0,1),(2,2),(5,3). 

this way will guarantee the right answer because the length of substring will not contain any repeating letters. the last thing I did to solve this problem is simply update result when I'm updating length of substring and that length is > current result

# Oct.26

- No.388 Permutation Sequence

if we know which permutation we're trying to get, we can actually calculate every number. For example, first number(from left to right) is chosen by (k-1)/factorial(n-1). the reason is that factorial(n-1) indicates how many possible permutations will start with same first number, k-1 is because indexing starts from 0 instead of 1.

then when we move to next number, letting n -= 1, and k = k%factorial(n-1) if k%factorial(n-1) != 0 else k, k is calculated like this because when we move to next number, we need to first consider if k > factorial(n-1) (if yes the new k should be the remainder of that factorial) and repeatedly calculate the number like we did above.

- No. 381 Spiral Matrix II

this is relatively easy, given that I've practiced solving Spiral Matrix, this version only needs to create an empty square matrix, and then fill in numbers in an spiral order, like how I read those spiral numbers out of the matrix in first version.

- No.380 Intersection of Two Linked List

since they have intersection, meaning that if we go backwards,the pointer to the longer list should be determined by the beginning of the shorter linked list, once we find the pointer for the longer linked list, we can compare parallely of two linked list until we find nodes with same value.

therefore we only need to calculate how long two linked lists are, then set pointer to the longer one with (len(longer)-len(shorter)) and compare pair by pair until we find same value.

- No.374 Spiral Matrix

just be careful when m is odd or n is odd, and when matrix is of empty lists or the matrix itself is empty.

# Oct.25

- No.363 Trapping Rain Water

key idea is to find bar number(spike numbers may not be bars, eg. [100,50,99,50,100], 100 is bar but 99 is not), and calculate diffs of all numbers between two neighboring bars: first calculate diffs of all numbers against first bar, then diffs against second bar, and take the minimum sum of diffs. add the minimum sum to the result

# Oct.24 

- No.189 First Missing Positive

this is a tricky solution, the first step is to find out range of possible missing positive first(that's why we need a len() to decide range of possible missings). then since we need to do it in O(1) space we basically can only mutate the list itself, therefore by treating values in list that are smaller than n as 'index' of list, we assign negative signs to those positions, then finaly if we find some number that is positive then we know that we haven't visited that position, in this case we don't have the value, and since the positions are in order(0th,1th,2nd...) if we loop through the mutated list, the first one we encountered that is positive should be the one we're looking for.

# Oct.23 

- No.191 Maximum Product Array

1. use three helper variables: maximum(maximum product), minimum(minimum product(usually negative)), and curr(current number)
2. update three variables as we loop through list:
 
  a. maximum = max(maximum \* curr, minimum \* curr, curr)
  b. minimum = min(maximum \* curr, minimum \* curr, curr)
  
then just update result if maximum > result

# Oct.22

- No.187 Gas Station

I figured it out by myself, use remaining gas list and a greedy method: basically I use a max function to decide whether it's better to start from current position, or continue from previous position, by judging max(current_position_gas,current_position_gas+previous_remaining_gas). Then from results of this list if previous position is negative, and current position is positive, and current position has max remaining gas, I choose to start from here.

# Oct.20 

- No.184 Largest Number

this is to my surprise not a simple problem, it has 3 key take aways for me.

1. the most difficult one for me is that I'm not familiary with cmp parameter in sorted(). 
2. also there's a lstrip function help delete first element same as value given in lstrip(). 
3. last take away is that empty string is None, so can return some string or '' on the same line.

# Oct.19

- No.171 Anagrams

this is an easy problem, simply store all anagrams of same origin into dictionary, with set value as their key value, value will be a list with first element saying how many anagrams(if only 1 then don't return it) and second having specific anagram strings.

then loop through the keys in dict, and append second elements in dict, then return
# Oct.10

- No.170 Rotate list

to rotate a linked list. trick is to form a circle using the linked list, then use k%n to define how many rotate steps the circle should perform. then cut the circle at final step. return the linked list.

- No.164 Unique Binary Search Trees II

this problem needs to return all possible trees. use dfs to do that. store all subsequent trees into a list, when generating n+1 nodes tree, use trees generating n nodes(stored in the list) and adding the n+1th new node on the top.

# Oct.9

- No.163 Unique Binary Search Trees

use a list to memorize # of trees that from 1 to i have, then use dynamic programming to calculate dp[n] = sum(dp[i] * dp[n-i]) for i from 1 to n-1

- No.162 Set Matrix Zeroes

this is easy. just be careful when looping through every row, instead of set all to zeroes once we meet one 0, we should use a list to store all col numbers that have such 0s, then transform rows. and in another for-loop,set all rows at same col that have 0s to 0.

- No.161 Rotate Image

difficult parts about this problem are:

1. define pattern to rotate 90 degrees

the pattern for rotating 90 degree is : clockwise: (row,col) -> (col,n-1-row); counter-clockwise:(row,col) -> (n-1-col,row)

2. how to do it in space, i.e. swapping

when rotating, define 4 positions whose rotating positions are other 3's current position as a cycle.(eg. 4 corner elements are a pair)

to do it in space, need to rotate same value 3 times backwards to the position it is supposed to be, that way when performing the cycle the other three elements will also be placed in the right position when they are swapping with that element.

then move to next element on the same row((row,col+1)) and repeat the above cycle swapping.

then move into more center layer(i.e. the inner n-1 by n-1 matrix) and repeat cycle swapping of all elements(except the last one since it's in the cycle with the first element) on the first row

- No.160 Find Minimum In Rotated Array II

this version has duplicate elements in list. eg. [9,9,9,1,1,1]

when writing logic expressions need to consider special cases like this, first judge if distinct numbers in left half and right half are the same and are greater than 1 or not. 

1. if they both have more than 1 distinct element, same as previous version just need to see if first element > last element.

2. if one of them has only 1 distinct but the other one has more than 1 distinct, see if the list with more than 1 distinct element has its first element > last element, or if the first element of that list is NO LESS than first element of the other list. eg.[1,1,1,1,-1,1]. if true find in that diversified list, else return the value of the other list

- No.159 Find Minimum In Rotated Array

this version suppose elements in array are distinct

uses idea from merge-sort, divide list into half and decide which part the minimum element is at, then divide again

- No.152 Combinations

basically it is an implementation of forming all distinct combinations of C(n,k)

# Oct.8

- No.151 Best Time to Buy and Sell Stock III

this one is harder than previous two, since we are only allowed to make 2 transactions, we can use two lists to store maximum profit before time i and after time i. then add them up. the tricky point is, when we create the list storing maximum profit after time i, we keep track of highest price, instead of keeping track of lowest price, like we did in previous two problems. the reason is that this list is made after the first transaction, so the lowest price is not the actual lowest price of the whole list. so equivalently we memorize the highest price and get the maximum profit.

- No.150 Best Time to Buy and Sell Stock II

since we're able to make multiple transactions, the best strategy to gain more profit is to trade before the price is about to go down, when the price goes down, find the lowest price during downtrend , when the price goes up, find the highest price during uptrend. add all these profits up.

- No.149 Best Time to Buy and Sell Stock

this problem is easy. Just use a variable to store the lowest price and get maximum profit by comparing the historical max profit with current profit.

# Oct.7
- No.148 Sort Colors

reference:
http://www.cnblogs.com/zuoyuan/p/3775832.html

main idea is to use two pointers for 3 categories(0s,1s and 2s). First pointer starts from 0, second pointer starts backwards from last position. whenever current posision is 2, swap current element with element at second pointer, then second pointer moves backwards to next, if is 0 first pointer moves to next, and at the same time move cursor to next one. tricky part is when to move cursor forward, if it moves forward when current position is 2, then the swapped element of color 2 will escape being checked and swapped to other positions. but if it's color 0 and will be swapped with first pointer, it is safe to say that we can move cursor forward since all elements behind are 0s.

the reference does not AC because when cursor moves beyond second pointer,second pointer will point to color 1 or 0, the program needs to stop when cursor approaches second pointer.

- No.137 Clone Graph

use dictionary to remember if the node is cloned or not

DFS here is implemented recursively, BFS used a queue.

- No.135 Combination Sum

keep a list of values within range of target value, l[value] = [l[value-i].append(i) for i in candidates]

reference: http://www.cnblogs.com/zuoyuan/p/3753507.html


- No.127 Topological Sort - BFS and DFS implementation

previous days were busy so I didn't do daily updates.

1. BFS implementation:

adding all nodes with 0 in degree(nodes at the top or leftmost) to a queue, and pop up first element in queue, store 0 in-degrees in result, update following nodes of the popped up node their in degrees, and loop the pop-up update process . return [] if graph does not contain all nodes in graph, else return result

2. DFS implementation:

using coloring dictionary to decide the status of node we're visitng: 

  -- if it's white then we haven't visited them before. 
  
  -- if it's grey then we have visited them along the way(and haven't finished the whole branch searching), that means we have a cycle

after we done searching the whole branch, we mark those nodes black, and start a new branch for searching.

reference: https://algocoding.wordpress.com/2015/04/05/topological-sorting-python/

# Oct.3

- No.123 Word Search

we only need to find if the path is possible so just use DFS will be enough. the tricky part is under every path we need to memorize if the positions we have visited or not, and if the path is not a solution how we can restore it. the solution to this part is to temporarily change the visited position to '#', if its next dfs is not successful, restore it back to its original letter on the board

- No.120 Word Ladder

search for elements in sets has same time complexity as dictionary, so use BFS to try all possible mutations at every step, then check if new mutations is what we're looking for. if not, continue to find mutations of mutations.

- No.124 Longest Consecutive Sequence

using dictionary to decide if adjacent numbers of current number also exist in dictionary, and memorize the longest length of those consecutive numbers. test for every number in the dictionary, and update the longest length

# Oct.2

- No.117 Jump Game II

use the greedy approach will solve this in O(n) time.

basic idea is to keep track of farthest position that current and all the past position can go, using 'farthest' to keep that information. 'curr' will remember where we are currently, and 'steps' will memorize how many steps we need to take to go to the farthest position.

therefore, in the end we can just simply return steps we need to take to the farthest position. as long as the farthest position is no smaller than the last position in the list, it is safe to say that we can go to the end of list using same amount of steps.

- No.116 Jump Game

two implementations:

1. greedy. always choose next step with most available steps on that step.

2. dynamic programming. keep a boolean dp list showing if current step can be reached by previous steps.

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
