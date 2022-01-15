# Problem 1
# Function to return indices of the numbers that add up to the Target
def sumIndices(nums=[],target=0):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return ([i],[j])
# Problem 2
#Function to find if a given number is a palindrome or not
def palindrome(i:int):
    # palindrome exists only for positive numbers
    if i > 0:
     num=[int(x) for x in str(i)] # Converting the given number to a list
     rev_num=(num[::-1])# reversing the list
    # Comparing elements of the two lists
     if num == rev_num:
         return True
    return False
# Problem 3
# Function to find the index of the `Target` element
def numInList(nums: [], target: int):
    # When the `Target` number is in the `nums` list
    if target in nums:
        for i in range(len(nums)):
            if nums[i] == target:
                print("Target found in Nums list and index position is", i)
    # When the `Target` number is NOT in the `nums` list
    else:
        start = 0
        end = len(nums) - 1
        target_pos = 0
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
                target_pos = mid
            else:
                start = mid + 1
                target_pos = mid + 1
        print("Target NOT found in Nums list and index position is", target_pos)
# Problem 4
# Function to return the element that's repeated only once in the list
def singleEle(nums):
    nums.sort()
    n=len(nums)
    count= n+1
    out=-1
    curr_count=1
    for i in range (1,n):
        if (nums[i]==nums[i-1]):
            curr_count=curr_count+1
        else:
            if(curr_count<count):
                count=curr_count
                out=nums[i-1]
            curr_count=1
    if (curr_count<count):
        count=curr_count
        out=nums[n-1]
    return out
#Problem 5
# Function to find the element that is repeated the most in the list
def maxrepeated(nums):
    count=0
    max_count=nums[0]
    for i in nums:
        current_count=nums.count(i)
        if(current_count>count):
            count=current_count
            max_count=i
    return max_count
# Problem 6
# Creating a class Node, which has a node value and pointers
class Node:
    # Initializing values to the node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Creating a class Tree which contains the root node
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
# Function to check if two trees are structurally similar
def strucSimilar(root1, root2):
    # If the roots of the two trees point to None, the trees are structurally similar
    if root1 == None and root2 == None:
        return True
    if root1 != None and root2 != None:
        # Recursive function to find if the trees are structurally similar
        return (strucSimilar(root1.left, root2.left) and
                strucSimilar(root1.right, root2.right))
    return False
# Creating Trees and assigning values to root and child nodes
# Tree 1
Tree1 = BinaryTree('a')
Tree1.left = Node('1')
Tree1.left.left=Node('2')
# Tree 2
Tree2 = BinaryTree('b')
Tree2.left = Node('3')
Tree2.right = Node('1')
# Tree 3
Tree3 = BinaryTree('c')
Tree3.left = Node('4')
Tree3.right = Node('3')

# output of functions
# Prob 1
print("Problem 1:")
# Calling the function and printing output
a= [2,7,5,-3,15]
b= 7
k=sumIndices(a,b)
print("Indices of the numbers that add up to the Target number :",k)
# Problem 2
print("\nProblem 2:")
a=-141
b=1221
# Calling the function and printing output
print("Is the given number",a,"a palindrome?",palindrome(a))
print("Is the given number",b,"a palindrome?",palindrome(b))
# Prob 3
print("\nProblem 3:")
a= [1,3,5,7]
print("nums list:",a)
b=2
print("a) Target Number:",b)
n=numInList(a,b)# Calling the function and printing output
c= 7
print("b) Target Number:",c)
m=numInList(a,c) # Calling the function and printing output
# Prob 4
print("\nProblem 4:")
k=[1,2,1,2,4]
# Calling function and printing output
print("The single element in the list",k, "is",singleEle(k))
# Prob 5
print("\nProblem 5:")
l=[1,0,0,0,1,2,2]
# Calling function and printing output
print("The most repeated element",l," is:",maxrepeated(l))
# Prob 6
print("\nProblem 6:")
# Calling the function to find if the two trees are structurally similar
print("Are the trees structurally similar?",strucSimilar(Tree1,Tree2))
print("Are the trees structurally similar?",strucSimilar(Tree2,Tree3))
