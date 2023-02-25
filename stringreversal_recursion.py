//-------------recursive--------------
import time
start=time.time()
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
s=input()
print(reverse(s))
end=time.time()
print(end-start)
