class Solution(object):
    def minimumLength(self, s):
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            char = s[l]
            # Soldan karakteri temizle
            while l <= r and s[l] == char:
                l += 1
            # Sağdan karakteri temizle
            while l <= r and s[r] == char:
                r -= 1
        return r - l + 1
