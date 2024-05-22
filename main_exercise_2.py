from collections import deque

def is_polindrome(s):
    s = ''.join(s.lower().split())
    d = deque(s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False 
# Якщо символи не збігаються, рядок не є паліндромом
    return True

print(is_polindrome("Terrible"))
print(is_polindrome("Maoam"))