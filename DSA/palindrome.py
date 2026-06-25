def pal(s):
    return True if len(s) <= 1 else s[0] == s[-1] and pal(s[1:-1])

print(pal("madam"))