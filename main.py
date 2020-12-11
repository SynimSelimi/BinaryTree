# Node
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# Binary Tree
class BTree:
  def __init__(self, root):
    self.root = root

  # Find binary tree depth (recursive)
  def find_height(self, node):

    if(node is None):
      return 0

    lheight = self.find_height(node.left) 
    rheight = self.find_height(node.right)

    if(lheight > rheight):
      height = 1 + lheight
    else:
      height = 1 + rheight
      
    return height

  def height(self):
    return self.find_height(self.root)

# Main
def main():
  root = Node(0)
  tree = BTree(root)
  tree.root.right = Node(1)
  print(tree.height())

if __name__ == "__main__":
  main()