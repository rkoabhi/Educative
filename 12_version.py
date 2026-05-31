'''
Understand how to compare version strings by breaking them into revisions and using two pointers to evaluate their integer values. Learn to handle leading zeros and unequal lengths to determine if one version is greater, lesser, or equal to another.
Statement
Given two version strings, version1 and version2, compare them. A version string is composed of revisions separated by dots ('.'). Each revision’s value is determined by converting it to an integer, disregarding any leading zeros.

Compare the two version strings by evaluating their revision values from left to right. If one version string contains fewer revisions than the other, treat each missing revision as 0.

Return the result of the comparison as follows:

Return 
−1
 if version1 is less than version2.

Return 
1
 if version1 is greater than version2.

Return 
0
 if both versions are equal.



'''




def compareVersion(version1, version2):

    # Replace this placeholder return statement with your code
    v1 = version1.split('.')
    v2 = version2.split('.')
    print(v1)
    print(v2)
    n = max(len(v1), len(v2))
    print(n)
    
    for i in range(n):
        rev1 = int(v1[i]) if i < len(v1) else 0
        rev2 = int(v2[i]) if i < len(v2) else 0
        
        print(rev1)
        print(rev2)
        
        if rev1 < rev2:
            return -1
        if rev1 > rev2:
            return 1
    
    return 0
    
    
    '''
Compare Version Numbers

Core Idea:
Compare revisions one by one.

Example:
1.0.1
1

Treat missing revisions as 0.

Steps:
1. Split both strings using '.'
2. Compare corresponding revisions
3. Convert revisions to int()
   to ignore leading zeros
4. Return:
   -1 if version1 < version2
    1 if version1 > version2
    0 if equal

Python:
split('.') -> separates revisions

int('001') -> 1

Time Complexity: O(n+m)
Space Complexity: O(n+m)

Pattern:
String Parsing + Sequential Comparison
'''