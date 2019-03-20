from typing import List

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


if __name__ == '__main__':
   pass

