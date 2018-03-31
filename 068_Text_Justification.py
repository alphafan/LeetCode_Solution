"""
Given an array of words and a length L, format the text such that each line has
exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as
you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
"""


class Solution(object):

    """  Not interesting """

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        splitStrs = self.splitWordsToString(words, maxWidth)
        pass

    def splitWordsToString(self, words, maxWidth):
        if len(words) == 0 or maxWidth <= 0:
            raise Exception('Empty words or invalid maxWidth')
        wordStr = ' '.join(words)
        splitStrs = []
        while len(wordStr) != 0:
            if len(wordStr) >= maxWidth:
                substring = wordStr[:maxWidth]
                endIndex = substring.rfind(' ')
                splitStrs.append(wordStr[:endIndex])
                wordStr = wordStr[endIndex+1:]
            else:
                splitStrs.append(wordStr)
                wordStr = ''
        return splitStrs

    def extendStrToLength(self, s, maxWidth):
        diff = maxWidth - len(s)
        if diff == 0:
            return s
        # Find the blank space and extend
        resultStr = s
        for i, char in enumerate(s):
            if char == ' ':
                s = resultStr[:i] + ' ' + resultStr[i:]
                pass


s = Solution()
r = s.splitWordsToString(["This", "is", "an", "example", "of", "text", "justification."], 16)
print(r)