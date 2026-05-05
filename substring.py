from collections import Counter
def smallest(s,p):
    if not s or not p :
        return ""
    need=Counter(p)  # length of the p unique elements 
    have={}    # dictories for present values
    formed=0    # checking if the requirement is matching
    required=len(need)   # length of the need variable
    left=0    # left pointer
    min_len=float("inf")    # assigning min_substring value to +ve infinity
    result=""     # resulting variable

    for right in range(len(s)):
        char=s[right]
        have[char]=have.get(char,0)+1 

        if char in need and need[char]==have[char]:
            formed+=1

        while formed==required:  #timetopractice
            window_len=right-left+1

            if window_len<min_len:
                min_len=window_len
                result=s[left:right+1]

            left_char=s[left]
            have[left_char]-=1
            if left_char in need and have[left_char]<need[left_char]:
                formed-=1
                
            left+=1
    return result
    
s="timetopractice"
p="toc"
smallest(s,p)
