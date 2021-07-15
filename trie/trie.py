
class TrieNode:
    def __init__(self, value="", children=None, pos=-1):
        self.value = value
        self.children = children or [None for _ in range(26)]
        self.pos = pos
        self.end = False
    def __str__(self):
        return f"{self.value}  {self.pos}"

    def __repr__(self):
        return self.__str__()


class Dictionary:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for letter in word:
            pos = ord(letter.lower()) -97
            new_node = node.children[pos]
            if new_node is None:
                new_node =  TrieNode(value=letter, pos = node.pos+1)
                node.children[pos]  = new_node
            node = node.children[pos]
        node.end = True
        return True
            

    def search(self, word):
        node = self.root
        for letter in word:
            pos = ord(letter.lower()) -97
            next_node = node.children[pos]
            if not next_node:
                print(letter)
                return False
            node = next_node
        return node.end

    def autocomplete(self, word):
        node = self.root
        res = []
        for letter in word:
            pos = ord(letter.lower()) -97
            new_node = node.children[pos]
            if new_node is None:
                return res
            node = new_node
        res = self.get_contents(node)
        return [word + a[1:] for a in res]

    def remove(self, word):
        self.root = self.remover(self.root, word)

    def remover(self, node, word, index=0):
        if index == len(word):
            if any(node.children):
                print("word is a prefix")
                node.end = False
                return node
            else:
                return None
        else:
            pos = ord(word[index].lower()) - 97
            next_node = node.children[pos]
            next_node = self.remover(next_node, word, index + 1)
            node.children[pos] = next_node
            if not any(node.children):
                print("----------------")
                if not node.end:
                    node = None
        return node



    def get_contents(self, node=None):
        contents = []
        contents = self.dfs(node or self.root)
        return contents
        
    def dfs(self, node, word="", store=set()):
        word += node.value
        if node.end:
            store.add(word)
        for child in node.children:
            if child:
                self.dfs(child, word, store)
        return store



if __name__ == "__main__":
    dictionary = Dictionary()
    dictionary.insert("Hungaria")
    dictionary.insert("pap")
    dictionary.insert("papa")
    dictionary.insert("rocinante")
    dictionary.insert("abaddon")
    dictionary.insert("caliban")
    dictionary.insert("callisto")
    dictionary.insert("canismajoris")
    dictionary.insert("persegedae")
    dictionary.insert("Gordi")
    dictionary.insert("jinjun")
    dictionary.insert("jinj")
    dictionary.insert("persepolis")
    dictionary.insert("achaemnid")
    dictionary.insert("sargon")
    dictionary.insert("Memmeth")
    dictionary.insert("Suleiman")
    dictionary.insert("Cyrus")
    dictionary.insert("xerxes")
    print(dictionary.get_contents())
    # print(dictionary.autocomplete("ca"))
    print(dictionary.search("jinjun"))
    dictionary.remove("callisto")
    print(dictionary.get_contents())
