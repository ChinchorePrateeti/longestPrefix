def longestPrefix(strs):
    
    s = list(zip(*strs))
    required_str = ""
    for item in s:
        if len(set(item)) > 1:
            break
        required_str += item[0]
    return required_str


strs = ["flower","flow","flight"]
call_func = longestPrefix(strs)
print(call_func)