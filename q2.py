def silme(s):
    i = 0

    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            return s
        i += 1

    return s

            
            
                
                
                       



def remove_adjacent_duplicates(s):

    onceki = ""

    while onceki != s:
        onceki = s
        s = silme(s)

    return s