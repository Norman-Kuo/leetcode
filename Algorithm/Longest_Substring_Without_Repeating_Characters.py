class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        substring = ""
        prev_sub = []
        previous = ""
        print(s)
        for i in s:
            if i not in substring:
                if i != previous:
                    substring +=i
                    prev_sub.append(substring)
                else:
                    prev_sub.append(substring)
                    substring = ""
                    substring +=i
            else:
                if i != previous:
                    prev_sub.append(substring)
                    location = substring.find(i)
                    substring = substring[location+1:]
                    substring+=i
                else:
                    prev_sub.append(substring)
                    substring = ""
                    substring +=i
            previous = i

        number = 0
        for i in prev_sub:
            if len(i)> number:
                number = len(i)
        return number
