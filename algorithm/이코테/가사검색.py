"""
["frodo", "front", "frost", "frozen", "frame", "kakao"]
["fro??", "????o", "fr???", "fro???", "pro?"]
"""
import sys
from ast import literal_eval
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def solution(words, queries):
    answer = []

    word_dict = {}
    reversed_dict = {}

    for word in words:
        length = len(word)
        if length not in word_dict:
            word_dict[length] = []
        word_dict[length].append(word)

        if length not in reversed_dict:
            reversed_dict[length] = []
        reversed_dict[length].append(word[::-1])

    for length in word_dict:
        word_dict[length].sort()
        reversed_dict[length].sort()

    def count_range(arr, left_word, right_word):
        left = bisect_left(arr, left_word)
        right = bisect_right(arr, right_word)
        return right - left

    for query in queries:
        length = len(query)
        if length not in word_dict:  # 해당 길이의 단어가 없으면
            answer.append(0)
            continue

        if query[0] == '?':  # 접두사에 와일드카드
            query = query[::-1]
            q = query.replace('?', 'a'), query.replace('?', 'z') #q = (froaa, frozz)
            cnt = count_range(reversed_dict[length], q[0], q[1])
        else:  # 접미사에 와일드카드
            q = query.replace('?', 'a'), query.replace('?', 'z')
            cnt = count_range(word_dict[length], q[0], q[1])
        answer.append(cnt)


    return answer

words = literal_eval(input())
queries = literal_eval(input())
print(solution(words, queries))