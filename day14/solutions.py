# # valid anagram
# s = "anagram"
# t = "nagaram"
# freq_s = {}
# freq_t = {}
# for char in s:
#     freq_s[char] = freq_s.get(char, 0) + 1
# for char in t:
#     freq_t[char] = freq_t.get(char, 0) + 1
# print(freq_s == freq_t)

# # string compression
# chars = ["a","a","b","b","c","c","c"]
# i = 0
# res = 0
# while i < len(chars):
#     group_length = 1
#     while i + group_length < len(chars) and chars[i + group_length] == chars[i]:
#         group_length += 1
#     chars[res] = chars[i]
#     res += 1
#     if group_length > 1:
#         for c in str(group_length):
#             chars[res] = c
#             res += 1
#     i += group_length
# print(res, chars[:res])

# # encode and decode strings
# strs = ["leet","code","love","you"]
# # encode
# encoded = ""
# for s in strs:
#     encoded += str(len(s)) + "#" + s
# print("encoded:", encoded)
# # decode
# decoded = []
# i = 0
# while i < len(encoded):
#     j = i
#     while encoded[j] != "#":
#         j += 1
#     length = int(encoded[i:j])
#     decoded.append(encoded[j + 1 : j + 1 + length])
#     i = j + 1 + length
# print("decoded:", decoded)

# # zigzag conversion
# s = "PAYPALISHIRING"
# numRows = 3
# if numRows == 1 or numRows >= len(s):
#     print(s)
# else:
#     rows = ["" for _ in range(numRows)]
#     current_row = 0
#     going_down = False
#     for char in s:
#         rows[current_row] += char
#         if current_row == 0 or current_row == numRows - 1:
#             going_down = not going_down
#         if going_down:
#             current_row += 1
#         else:
#             current_row -= 1
#     print("".join(rows))

# # partition labels
# s = "ababcbacadefegdehijhklij"
# last_occurrence = {}
# for i in range(len(s)):
#     last_occurrence[s[i]] = i
# res = []
# size = 0
# end = 0
# for i in range(len(s)):
#     size += 1
#     if last_occurrence[s[i]] > end:
#         end = last_occurrence[s[i]]
#     if i == end:
#         res.append(size)
#         size = 0
# print(res)

# # text justification
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# res = []
# cur = []
# num_of_letters = 0
# for w in words:
#     if num_of_letters + len(w) + len(cur) > maxWidth:
#         for i in range(maxWidth - num_of_letters):
#             cur[i % (len(cur) - 1 or 1)] += ' '
#         res.append(''.join(cur))
#         cur = []
#         num_of_letters = 0
#     cur.append(w)
#     num_of_letters += len(w)
# res.append(' '.join(cur).ljust(maxWidth))
# print(res)
