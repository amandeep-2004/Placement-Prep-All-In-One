def compress_by_substring(s):
    n = len(s)
    i = 0
    res = []

    while i < n:
        compressed = False

        # try all possible substring lengths
        for l in range(1, (n - i) // 2 + 1):
            sub = s[i:i+l]
            count = 1

            while i + count*l + l <= n and s[i + count*l : i + (count+1)*l] == sub:
                count += 1

            if count > 1:
                res.append(sub + str(count))
                i += count * l
                compressed = True
                break

        if not compressed:
            res.append(s[i])
            i += 1

    compressed_str = ''.join(res)
    return compressed_str if len(compressed_str) < len(s) else s

s=input("enter the string: ")
print(compress_by_substring(s))