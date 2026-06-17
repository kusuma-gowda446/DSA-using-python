class Solution(object):
    def processStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        lengths = []
        length = 0

        for ch in s:
            if 'a' <= ch <= 'z':
                length += 1
            elif ch == '*':
                if length > 0:
                    length -= 1
            elif ch == '#':
                length *= 2
            else:  # '%'
                pass

            lengths.append(length)

        if k < 0 or k >= length:
            return '.'

        for i in range(len(s) - 1, -1, -1):
            ch = s[i]
            prev_len = lengths[i - 1] if i > 0 else 0

            if 'a' <= ch <= 'z':
                if k == prev_len:
                    return ch

            elif ch == '*':
                # same index in previous string
                pass

            elif ch == '#':
                if k >= prev_len:
                    k -= prev_len

            else:  # '%'
                k = prev_len - 1 - k

        return '.'
        
