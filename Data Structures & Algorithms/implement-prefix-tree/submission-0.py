class TrieNode:
    def __init__(self, letter):
        self.is_end = False
        self.children = {} #key = letter, val = TrieNode()
        self.letter = letter

class PrefixTree:

    def __init__(self):
        self.root = TrieNode(None);
        

    def insert(self, word: str) -> None:
        #check from root.children
        children = self.root.children
        for index, letter in enumerate(word):
            if letter not in children:
                #need to add to children
                children[letter] = TrieNode(letter)
            if index == len(word) - 1:
                #make this node end
                children[letter].is_end = True
            children = children[letter].children

    def search(self, word: str) -> bool:
        children = self.root.children
        for index, letter in enumerate(word):
            if letter in children:
                if index == len(word) - 1:
                    last_letter = children[letter]
                    if last_letter.is_end != True:
                        return False
                children = children[letter].children
            else:
                return False
        
        return True
        

    def startsWith(self, prefix: str) -> bool:
        children = self.root.children
        for letter in prefix:
            if letter in children:
                children = children[letter].children
            else:
                return False
        
        return True
        
        