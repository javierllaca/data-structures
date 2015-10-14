class TrieNode:

    def __init__(self, value=None, children=None):
        self.value = value
        self.children = children or {}

    def insert(self, key, value):
        node = self
        i = 0
        n = len(key)

        while i < n:
            if key[i] in node.children:
                node = node.children[key[i]]
                i += 1
            else:
                break

        while i < n:
            node.children[key[i]] = TrieNode()
            node = node.children[key[i]]
            i += 1

        node.value = value

    def find(self, key):
        if not key:
            return self.value
        head = key[0]
        tail = key[1:]
        if head in self.children:
            return self.children[head].find(tail)
        return None

    def __str__(self):
        s = '({} {{'.format(self.value)
        for char, child in self.children.items():
            s += '{}: {} '.format(char, child)
        s += '})'
        return s


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key, value):
        self.root.insert(key, value)

    def find(self, key):
        return self.root.find(key)

    def __str__(self):
        return str(self.root)


t = Trie()

for word in ['hello', 'hell', 'heat']:
    t.insert(word, word)

t.insert('hellow', 3)

print t.find('hello')  # hello
print t.find('hellow')  # 3
