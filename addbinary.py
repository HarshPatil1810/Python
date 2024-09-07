class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum=bin(int(a,2)+int(b,2))[2:]
        return sum
a = "1010"
b = "1101"
result = add_binary(a, b)
print("Sum:", result
