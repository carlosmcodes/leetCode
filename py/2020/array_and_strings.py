    # dict[key] = value
import collections
def main():
    print("start...")
    # nums = [1,0,1]
    # nums = [2,14,18,22,22]
    # nums = [4,1,2,1,2]
    nums2 = [1,2,3]
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
    print(plus_one(nums2))
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
    # print(pascalTriangle(5))
    # print(validparenthesis("([])"))
    s = [1,2,3,4,2,6]

    # print(s[1:])
    # print(s[:-1])
    # getmaxscore(s)
    # print(getmaxscore(s))
    # print(maxproduct(s))
    # print(coin_change([1,5,10,25], 98))
    # climbstairs(10)
    # print(magicindex_ctci([0,1,2,3,4,5,6,7,8],5))
    # cell(l,7)
    # l = [20,4,8,2, 2, 100, 0, 0]
    # print(minsum(4, l))

    k = [[1,0,12],
         [1,0,0],
         [1,9,1]]
    # print(mindistance(3,3,k))
    # 23280669604858 amazontestid
"""
[0, 1, 0, 1, 1, 0, 0, 1]
[0, 1, 1, 0, 0, 0, 0, 0] r
[0, 0, 0, 0, 1, 1, 1, 0]
[0, 1, 1, 0, 0, 1, 0, 0]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 1, 1, 1, 0, 1, 0, 0]
[0, 0, 1, 0, 1, 1, 0, 0]
[0, 0, 1, 1, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 1, 1, 0]
[0, 1, 1, 1, 0, 0, 0, 0]
[0, 0, 1, 0, 0, 1, 1, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 1, 0, 1, 1, 1, 0]
[0, 0, 1, 1, 0, 1, 0, 0]
[0, 0, 0, 0, 1, 1, 0, 0]
[0, 1, 1, 0, 0, 0, 0, 0] r
"""

def mindistance(numRows: int, numColumns, area: list):
    return checkhit(area, 0,0, numRows, numColumns, 0)

def checkhit(area: list, row: int, col: int, rowsize: int, colsize: int , val):
    # print(f'row: {row}, col: {col}')
    if row+1 < rowsize:
        if area[row+1][col] == 9:
            return val+1
    if  col+1< colsize:
        if area[row][col+1]  == 9:
            return val+1
    # if row+1 >= rowsize or col+1>= colsize: return val
    if area[row][col] == 9:
        return val
    if area[row+1][col] == 1:
        area[row+1][col] = 0
        return checkhit(area, row+1, col,rowsize, colsize, val+1)
    if area[row][col+1] == 1:
        area[row][col+1] = 0
        return checkhit(area, row, col+1,rowsize, colsize, val+1)


def minsum(numOfSubFiles, fileSizes: list):
    if not fileSizes: return
    fileSizes.sort()
    maxtime = 0
    for i in range(len(fileSizes)-1):
        maxtime = maxtime + fileSizes[i+1] + fileSizes[i]
        print(maxtime)
        fileSizes[i+1] = fileSizes[i+1] + fileSizes[i]
        print(fileSizes)
    return maxtime


def cell(cells: list, N: int):
    """
    still unsure why 14 is magic number. pulled from LC
    if N > 14:
            N = N%14
    if N%14 == 0:
        N = 14
    """
    for i in range( N):
        temp = [0]*len(cells)
        for i in range(1, len(cells)-1):
            temp[i] = 1 if cells[i-1] == cells[i+1] else 0
        cells = temp
        print(cells)
    return cells


def magicindex_ctci(a:list, n:int) -> int:
    if not a or n > a[-1] or n <a[0] : return 0
    return sorthelper(a, n)

def find_subset(a: list):
    dp = [[i] for i in a]
    for subset in range(len(a), "inf"):
        temp = dp[i - subset]
        dp[subset] = dp[i - subset]

def sorthelper(a: list, n: int):
    if not a: return -1
    if n == a[0]: return n
    mid = int(len(a)/2)
    print(f'-----------\nmid: {mid}')
    end = len(a)
    left = a[0: mid]
    right = a[mid: end]
    print(f'left:{left}, right: {right}')
    return sorthelper(left, n) if n < a[mid] else sorthelper(right, n)


def climbstairs(n: int) -> int:
    if n ==1: return 1
    dp = [-1 for i in range(n)]
    dp[0] = 1
    dp[1] = 2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]



def coin_change(coins: list, amount: int) -> int:
    #  we creat a maxtemp because our subproblem of zero is already solved therefore we
    # are at a base of 1
    maxtemp = amount + 1
    table = [0] + [maxtemp] * amount
    for subprob in range(1, maxtemp):
        for coin in coins:
            if coin <= subprob:
                table[subprob] = min(table[subprob], table[subprob - coin] + 1)
    return table[-1] if table[-1] != maxtemp else -1

    # recursive fib.
def fib(self, N):
    cache = {}
    return recur_fib(N, cache)

def recur_fib(N, cache):
    if N in cache:
        return cache[N]

    if N < 2:
        result = N
    else:
        result = recur_fib(N-1) + recur_fib(N-2)

    # put result in cache for later reference.
    cache[N] = result
    return result

def getmaxscore(integerArray: list):
    score = 0
    dup = integerArray
    for i in range(1, len(integerArray)):
        if dup:
            if i % 2 == 0:
                if len(dup) ==1:
                    score += dup[0]
                    break
                score -= sum(dup)
                if sum(dup[1:]) > sum(dup[:-1]):
                    dup = dup[:-1]
                else:
                    dup = dup[1:]
            else:
                if len(dup) ==1:
                    score += dup[0]
                    break
                score += sum(dup)
                if sum(dup[1:]) > sum(dup[:-1]):
                    dup = dup[1:]
                else: dup = dup[:-1]
    return score

def maxproduct(nums: list):
    print(len(nums))
    if len(nums) < 3: return 0
    nums.sort()
    nums.reverse()
    val = 0
    i = 1
    j = 0
    for k in range(2, len(nums)):
        if nums[i] * nums[j] * nums[k] > val: val = nums[i] * nums[j] * nums[k]
        i+=1
        j+=1
    return val




def mergelistAtIndex(nums1: list, m: int, nums2: list, n: int):
    # starting at m positions ahead of index 0 = 0..n positions from nums2
    nums1[m:] = nums2[:n]
    # nums1[:] = nums1[:m] + nums2[:n]
    nums1.sort()


def sorting(n: int):
        low = 1
        high = n
        while(low < high):
            mid = (low + high)/2
            if check(mid) == True:
                high = mid
            else:
                low = mid + 1
        return int(high)

def check(): return
()
def missingNumber(nums: list) -> int:
    n = len(nums)
    return int(n * (n+1) / 2 - sum(nums))

def validparenthesis(s:str) -> bool:
    # option1:
    # while '[]' in s or '()' in s or '{}' in s:
    #         s = s.replace('[]','').replace('()','').replace('{}','')
    #     return not len(s)
    # option2:
    dict = {')':'(', '}':'{', ']':'['}
    st = []
    for e in s:
    # e in dict checks keys; st[-1] gets last item and matches it with dict[e] which returns val
        if st and (e in dict and st[-1] == dict[e]):
            st.pop()
        else:
            st.append(e)
    return not st

def pascalTriangle(numRows: int):
    # [1] puts it there, (i+1) puts it there X times. +1 because inclusive
    resultset = [[1]* (i+1) for i in range(numRows)]
    # print(resultset)
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
    return s1 == s2



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
