from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        return ''.join(ch * cnt for ch, cnt in sorted(freq.items(), key=lambda x: -x[1]))
