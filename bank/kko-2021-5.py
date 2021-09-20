class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

def solution(info, edges):
    
    root = Node(info[0])
    
    for fr, to in edges:
        Node(info[fr])
    
    node.left = Node(2)
    print(node.data)
    print(node.left.data)
        
    return 

# input

info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

print(solution(info, edges))

"""
result:



"""