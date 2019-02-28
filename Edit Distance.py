# import numpy as np
from nltk import edit_distance as levDist
from nltk import jaccard_distance as jacDist
from nltk import word_tokenize as tokenise


# def levDist(string1, string2):
#     """Checks the simolarity of two strings. Penalises by 1 for every operation(addition, removal, swap)"""
#     x_len = len(string1) + 1
#     y_len = len(string2) + 1
#     matrix = np.zeros((x_len, y_len))
#     for x in range(x_len):
#         matrix[x, 0] = x
#     for y in range(y_len):
#         matrix[0, y] = y
#     for x in range(1, x_len):
#         for y in range(1, y_len):
#             if string1[x - 1] == string2[y - 1]:
#                 matrix[x, y] = min(matrix[x - 1, y] + 1, matrix[x - 1, y - 1], matrix[x, y - 1] + 1)
#             else:
#                 matrix[x, y] = min(matrix[x - 1, y] + 1, matrix[x - 1, y - 1] + 1, matrix[x, y - 1] + 1)
#     return matrix[x_len - 1, y_len - 1]


# st1 = "This is a string."
# st2 = "This, too, is a string."
# st3 = "Here's the foxglove"
#
# print(levDist(st1, st2))
# print(levDist(st1, st3))
# print(levDist(st2, st3))
# print(jacDist(set(st1), set(st2)))
# print(jacDist(set(st1), set(st3)))
# print(jacDist(set(st2), set(st3)))
#
# st1 = tokenise("This is a string.")
# st2 = tokenise("This, too, is a string.")
# st3 = tokenise("Here's the foxglove")
#
# print(levDist(st1, st2))
# print(levDist(st1, st3))
# print(levDist(st2, st3))
# print(jacDist(set(st1), set(st2)))
# print(jacDist(set(st1), set(st3)))
# print(jacDist(set(st2), set(st3)))
