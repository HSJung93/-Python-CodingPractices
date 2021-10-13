class Trie:
  def __init__(self):
    self.head = {}

  def add(self, word):
    cur = self.head

    for char in word:
      if char not in cur:
        cur[char] = {}
      cur = cur[char]
    cur['*'] = True

  def search(self, word):
    cur = self.head

    for char in word:
      print(cur, char)
      if char not in cur:
        return False
      cur = cur[char]
    if '*' in cur:
      return True
    return False

trie1 = Trie()
trie1.add("ac")
trie1.add("ab")
trie1.add("a")

print(trie1.search("abcd"))
print(trie1.search("abcdf"))