    # dict[key] = value
import collections
def main():
    print("start...")
    # nums = [1,0,1]
    # nums = [2,14,18,22,22]
    # nums = [4,1,2,1,2]
    # nums2 = [1,2,3]
    # nums= [4,1,2,1,2]
    # removeDuplicates(0, nums)
    # rotate(nums, 3)
    # print(f'{contains_duplicates(nums)}')
    # v = singleNumber(nums)
    # print(f'single:  {v}')
    
    # TODO LIST COMPREHENTION - START
    # [print(i) for i in range(5) if i <3]
    # x = [i for i in range(5) if i <3]
    # x = [i+y for i in [2,5,10] for y in [8,5,10]]
    # print(x)
    # l = []
    # for i in [2,5,10]:
    #     for y in [8,5,10]:
    #         l.append(i+y)
    # print(l)
    # obj = ["Even" if i%2==0 else "Odd" for i in range(10)]
    # print(f'obj:    {obj}')

    # BOTH CONDITIONS HAVE TO BE TRUE TO SUCCEED --- START
    # num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
    # print(num_list)
    # BOTH CONDITIONS HAVE TO BE TRUE TO SUCCEED --- END    
    # matrix = [[1, 2], [3,4], [5,6], [7,8]]
    # transpose = [[row[i] for row in matrix] for i in range(2)]
    # print (transpose)
    # TODO LIST COMPREHENTION - END

    # flip(31)
    # intersect(nums, nums2)
    # print(plus_one(nums2))
    # moveZeroes(nums)
    # nums = [3,2,4]
    # target = 6
    # twosum(nums, target)
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # rotatell(matrix)
    # revstring(["h","e","l","l","o"])
    # reverseint(1220)
    # firstUniqChar("cc")
    # isAnagram("aaccc","ccacaa")
    # print(isPalindrone("0P"))
    # print(myAtoi("4193 with words"))
    
    # longestCommonPrefix(["flower","flow","flight"])
    # print(hammingDistance(1,2))
def PascalTriangle(numRows: int) -> list[list[int]]:
    resultset = [[1]* (i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,  i):
                resultset[i][j] = resultset[i-1][j-1] + resultset[i-1][j]
    return resultset
    
def hammingWeight(n: int) -> int:
    # gets the number in bit form then counts 1's. very elegant and simple
    return bin(n).count('1')


def hammingDistance(x: int, y: int) -> int:
# this takes the bit XOR operator and counts the # of 1's // which is also the difference
    return bin(x^y).count('1')

def longestCommonPrefix(strs: list) -> str:
    if not strs:
        return ""
    shortest = min(strs,key=len)
    print(shortest)
    for i, ch in enumerate(shortest):
        print(i, ch)
        for other in strs:
            if other[i] != ch:
                return shortest[:i]
    return shortest 

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)
        

def myAtoi(string: str) -> int:
    l = []
    string = string.strip()
    phen = False
    if len(string) == 0: return 0
    if string[0].isalpha(): return 0
    if string[0] == '-':
        string = string[1:]
        phen = True
    x = string.find('.')
    if x:
        l[0:x]
        l = str(l)
        x = int(l)
        print(x)
    s = [i for i in string if i.isdigit()]
    if phen:
        s.insert(0, '-')
    s = ''.join(map(str, s))   
    x = int(s)
    return x if -(2**31)-1 < x < 2**31 else -(2**31)


def isPalindrone(s:str)-> bool:
    s1 = [i for i in s.lower() if i.isalnum()]
    s2 = s1[:]
    s1.reverse()
    return True if s1 == s2 else False
    


def isAnagram(s: str, t: str) -> bool:
    maps = {}
    mapt = {}
    for c in s:
        # +1 increases the value if key is found, else returns 0
        maps[c] = maps.get(c,0)+1
    for c in t:
        mapt[c] = mapt.get(c,0)+1
    return maps == mapt




def firstUniqChar(s: str) -> int:
    d = {}
    for i in range(len(s)):
         d[s[i]] = False if s[i] in d else i
    for key in d:
        if d[key] is not False:
            return d[key]
    return -1

def reverseint(x: int) -> int:
    x = str(x)
    hyphen = x.find('-')
    if hyphen == 0:
        x = x[hyphen+1:][::-1]
        x = str(x)
        x = '-' + x
    else:
        x = x[::-1]
    x = int(x)
    return x if -(2**31)-1 < x < 2**31 else 0
    

def revstring(s: list):
    s.reverse()
    j = len(s)-1
    for i in range(len(s)):
        if j <= i:
            # print(s)
            return s
        s[j], s[i] = s[i], s[j]
        print(s)
        j-=1
    print(s)




def rotatell(matrix: list):
    print(f'pre:{matrix}')
    print(f'-1:{matrix[::-1]}')
    print(*matrix)
    print(f"zip:    {zip(*matrix[::-1])}")
    matrix[:] = zip(*matrix[::-1])
    print(f'last: {matrix}')

def twosum(nums: list, target: int) -> list:
    d = {}
    for index, value in enumerate(nums):
        if value in d:
            return [d[value], index]
        else:
            d[target - value] = index

def moveZeroes(nums: list):
    oldlist = len(nums)
    nums[:] = [i for i in nums if i != 0]
    for i in range(len(nums), oldlist):
        nums.append(0)
    print(nums)

def plus_one(digits: list) -> list:
    num = 0
    for i in range(len(digits)):
        num = num + digits[i] * pow(10, (len(digits)-1-i))
        print(num)
    num+=1
    return [int(i) for i in str(num)]


def intersect(nums1: list, nums2: list) -> list:
    allresults = []
    # makes deep copy
    temp = nums2[:]
    for x in nums1:
        # if values of nums1 are in temp
        if x in temp:
            # removes from temp so we wont have doubles
            temp.remove(x)
            # adds to returning list
            allresults.append(x)    
    print(allresults)
    return allresults



def singleNumber(nums: list) -> int:
    a = 0
    for i in nums:
        print(f'pre-a:  {a}')
        a ^= i
        print(f'a=a^1:  {a^1}')
        print(f'post-a:  {a}')
    return a

def flip(val: int):
    j = 0
    for i in range(val):
        if i +1 == 14 or i-1 == 14:
            print(j)




def removeDuplicates(self, nums: list) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i +=1
            nums[i] = nums[j]
    
    print(i+1)
    return i + 1

def rotate(nums: list, k:int) -> None:
    temp = nums[:]
    last = nums[-k:]
    for i in range(len(nums)):
        if k + i >= len(nums):
            break
        temp[k+i] = nums[i]
    for i in range(len(last)):
        temp[i] = last[i]
    nums = temp[:]

def contains_duplicates(nums: list) -> bool:
    nums.sort()
    print(nums)
    j = 0
    if len(nums)<= 2:
        if nums[0]^nums[1] == 0:
            return True
    for i in range(j+1, len(nums)):
        if nums[j]^nums[i] == 0:
            return True
        j+=1

    return False
            


def movelast(num: list, k: int):
    last = num[:-k]
    print(last)
    return last

        



if __name__ == "__main__":
    main()