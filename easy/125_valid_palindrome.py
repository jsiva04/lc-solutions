class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = "".join(filter(str.isalnum, s))
        res = res.lower()
        print(res)

        i = 0
        j = len(res) - 1

        while i < j:
            if res[i] != res[j]:
                return False
            i += 1
            j -= 1
        return True