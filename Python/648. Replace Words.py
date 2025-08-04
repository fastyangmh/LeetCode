from typing import List


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # let length of dictionary is n and length of sentence is m
        # time O(n*m), space O(n)
        new_sentence = []
        for s in sentence.split(' '):
            replace = False
            index = -1
            min_len_word = 100
            for idx, word in enumerate(dictionary):
                len_word = len(word)
                if s[:len_word] == word and len_word <= min_len_word:
                    replace = True
                    index = idx
                    min_len_word = len_word
            if replace:
                new_sentence.append(dictionary[index])
            else:
                new_sentence.append(s)
        return ' '.join(new_sentence)


if __name__ == '__main__':
    # ex1    ans "the cat was rat by the bat"
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dictionary=dictionary, sentence=sentence))

    # ex2    ans "a a b c"
    dictionary = ["a", "b", "c"]
    sentence = "aadsfasf absbs bbab cadsfafs"
    print(Solution().replaceWords(dictionary=dictionary, sentence=sentence))

    # ex3    ans "a a a a a a a a bbb baba a"
    dictionary = ["a", "aa", "aaa", "aaaa"]
    sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
    print(Solution().replaceWords(dictionary=dictionary, sentence=sentence))

    # ex4    ans "the cat was rat by the bat"
    dictionary = ["catt", "cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dictionary=dictionary, sentence=sentence))

    # ex5    ans "it is ab that this solution is ac"
    dictionary = ["ac", "ab"]
    sentence = "it is abnormal that this solution is accepted"
    print(Solution().replaceWords(dictionary=dictionary, sentence=sentence))
