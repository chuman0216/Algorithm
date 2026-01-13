def solution(n_str):
    idx = 0

    for ch in n_str:
        if ch == '0':
            idx += 1
        else:
            break

    return n_str[idx:]