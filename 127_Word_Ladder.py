"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
"""


class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.ladderHelper(beginWord, endWord, wordList, [beginWord])

    def ladderHelper(self, beginWord, endWord, wordList, path):
        print(beginWord)
        if beginWord == endWord:
            print(path)
            return
        for nextWord in self.nextWords(beginWord, wordList):
            wordList.remove(nextWord)
            print(nextWord)
            self.ladderHelper(nextWord, endWord, wordList, path + [nextWord])
            wordList.append(nextWord)

    def nextWords(self, currWord, dictionary):
        """ From current word find one distance words in dictionary """
        nextWords = []
        for word in dictionary:
            if self.oneDistance(currWord, word):
                nextWords.append(word)
        return nextWords

    def oneDistance(self, word1, word2):
        """ Check if two words are one distance different from other """
        if len(word1) != len(word2):
            return False
        numDiff = 0
        for c1, c2 in zip(word1, word2):
            if c1 != c2:
                numDiff += 1
                if numDiff > 1:
                    return False
        return numDiff == 1


s = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
s.ladderLength(beginWord, endWord, wordList)
















