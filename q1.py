def longest_palindromic_substring(s):
    
    
    en_iyi = ""
    i = 0

    while i < len(s):

        sol = i
        sag = i
        while sag < len(s) and s[sol] == s[sag] and sol >= 0:
            sol -= 1
            sag += 1

        aday = s[sol + 1 : sag]
        if len(aday) >= 2 and len(aday) > len(en_iyi):
            en_iyi = aday

        sol = i
        sag = i + 1
        while sol >= 0 and sag < len(s) and s[sol] == s[sag]:
            sol -= 1
            sag += 1

        aday = s[sol + 1 : sag]
        if len(aday) >= 2 and len(aday) > len(en_iyi):
            en_iyi = aday

        i += 1

    return en_iyi