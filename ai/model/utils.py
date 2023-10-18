# 找到停用的词进行截断
def find_substrings(s, lst):
    substrings_found = []
    for i in lst:
        if i in s:
            substrings_found.append(s[:s.index(i) + len(i)])
            break

    if len(substrings_found) == 0:
        ret_str = s
    else:
        ret_str = substrings_found[0]

    return ret_str