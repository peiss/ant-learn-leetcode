class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for s in word:
            if s not in node:
                node[s] = {}

            node = node[s]
        node["is_word"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for s in word:
            if s in node:
                node = node[s]
            else:
                return False
        return "is_word" in node and node["is_word"]

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for s in prefix:
            if s in node:
                node = node[s]
            else:
                return False
        return True


trie = Trie()

trie.insert("apple")
print(trie.search("apple"))
print(trie.search("applea"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
