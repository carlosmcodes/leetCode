def main():
    d = "abab"
    print(repeatedSubstringPattern(d))
    ilist = []
    


def repeatedSubstringPattern(s: str) -> bool:
    print(f's+s {(s+s)}')
    print(f's+s[1:-1] {(s+s)[1:-1]}')
    return s in (s+s)[1:-1]


def serialize(root):
    vals = []
    traverse_se(root, vals)
    return ' '.join(vals)
    
def traverse_se(node, vals):
    if node:
        vals.append(str(node.val))
        traverse_se(node.left)
        traverse_se(node.right)
    else:
        vals.append('#')

def deserialize(data):
    vals = iter(data.split())
    return traverse_de()

def traverse_de():
    val = next(vals)
    if val == '#':
        return None
    node = TreeNode(int(val))
    node.left = traverse_de()
    node.right = traverse_de()
    return node
    




def findPeakElement(nums: list):
    i = 0
    j = 1
    if len(nums) <3: 
        for k in range(i+1, len(nums)):
            if nums[k] > nums[i]: return k
        i+=1
    i = 0
    j = 1
    for k in range(2, len(nums)):
        if nums[i] < nums[j] and nums[j] > nums[k]: 
            return j
        if k == len(nums) -1:
            if nums[k] > nums[j]: return k
        j+=1
        i+=1
    return 0
    
def longestPalindromeSubStr(s: str) -> str:
    if not s or len(s) < 1: return ""
    start= 0
    end = 0
    for i in range(len(s)):
        len1 = center(s, i,i)
        len2 = center(s, i, i+1)
        leng = max(len1,len2)
        if leng > end - start:
            start =int( i - (leng -1)/2)
            end = int( i + leng /2)

    return s[start:end+1]

def center(s: str, left: int, right: int):
    while(left >=0 and right < len(s) and s[left] == s[right]):
        left-=1
        right+=1
    return right - left + 1
    
def lengthOfLongestSubstring(s: str) -> int:
    window = {}
    max_length = start = 0
    for i, val in enumerate(s):
        if val in window and start <= window[val]:
            start = window[val] + 1
        else:
            max_length = max(max_length, i - start + 1)
        window[val] = i
    print(window)
    return max_length


if __name__ == "__main__":
    main()