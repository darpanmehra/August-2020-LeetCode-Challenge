'''
Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''
class TrieNode:
    def __init__(self):
        self.children ={}
        self.endofWord = False

class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.endofWord = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        current = self.root
        return self.Searchword(word, current)

    def Searchword(self, word, current):

        for i in range(len(word)):
            char = word[i]
            if char not in current.children and char != ".":
                return False
            if char == ".":
                for child_char in current.children:
                    if self.Searchword(word[i+1:], current.children[child_char]):
                        return True
                return False
            else:
                current = current.children[char]
        return current.endofWord



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)