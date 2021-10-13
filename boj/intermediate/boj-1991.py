import sys

class Node:
  def __init__(self, item, left, right):
    self.item = item
    self.left = left
    self.right = right

def pre_order(node):
  print(node.item, end="")
  if node.left != ".":
    pre_order(tree[node.left])
  if node.right != '.':
    pre_order(tree[node.right])
    
def in_order(node):  # 중위 순회
    if node.left != '.':
        in_order(tree[node.left])
    print(node.item, end='')
    if node.right != '.':
        in_order(tree[node.right])

def post_order(node):  # 후위 순회
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.item, end='')

if __name__=="__main__":
  N = int(sys.stdin.readline())
  
  # 서브 트리들을 저장하는 dictionary
  tree = {}
  
  for _ in range(N):
    node, left, right = sys.stdin.readline().split()
    tree[node] = Node(node, left, right)
    
  pre_order(tree['A'])
  print()
  in_order(tree['A'])
  print()
  post_order(tree['A'])