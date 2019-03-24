from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutive(self, nums):
        Hash_dict = dict()
        max_length = 0
        for number in nums:
            if number not in Hash_dict:
                min = Hash_dict.get(number-1,0)
                max = Hash_dict.get(number+1,0)
                cur_len = min + max + 1
                if cur_len > max_length:
                    max_length = cur_len
                Hash_dict[number+max] = cur_len
                Hash_dict[number-min] = cur_len
                Hash_dict[number] = cur_len
        return max_length


    def evalRPN(self, tokens: List[str])->int:
        nums = []
        op = ["+","-","*","/"]
        for s in tokens:
            if s not in op:
                nums.append(int(s))
            else:
                num1 = int(nums.pop())
                num2 = int(nums.pop())
                if s == "+":
                    nums.append(num2+num1)
                elif s == "-":
                    nums.append(num2-num1)
                elif s == "*":
                    nums.append(num2*num1)
                elif s == '/':
                    nums.append(int(num2/num1))
        return nums.pop()

    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in  range(32):
            count = 0
            tmp = 1 << i
            for num in nums:
                if tmp & num :
                    count+=1
            if count % 3 == 1:
                result |= tmp
        while result >= 2 ** 31:
            result -= 2 ** 32
        return  result


    def longestWord(self, words: List[str]) -> str:
        sets = set(words)
        print(sets)
        res = ""
        for s in words:
            if len(s) >= len(res):
                flag = True
                for i in range(1,len(s)):
                    if s[0:i] not in sets:
                        flag = False
                        break
                if flag:
                    if (len(s) == len(res) and s < res) or (len(s) != len(res)) :
                        res = s
        return res



if __name__ == '__main__':
    pass



