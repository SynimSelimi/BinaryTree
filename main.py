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

  # Main insert
  def insert(self, values):
    if(isinstance(values, int)):
        self.insert_rec(self.root, values)
    elif(isinstance(values, list)):
        for value in values:
            self.insert_rec(self.root, value)

  # Recursive insert
  def insert_rec(self, node, value):
    if (value < node.value):
      if (node.left is not None):
          self.insert_rec(node.left, value)
      else:
          node.left = Node(value)
    else:
      if (node.right is not None):
          self.insert_rec(node.right, value)
      else:
          node.right = Node(value)

  # Iterative insert
  def insert_iter(self, value):
    cnode = self.root
    height = self.find_height(cnode)
    
    for i in range(0, height):
      if(cnode.value < value):
        cnode.left = Node(value) if cnode.left is None else cnode.left
        cnode = cnode.left
      else:
        cnode.right = Node(value) if cnode.right is None else cnode.right
        cnode = cnode.right

  # Find binary tree depth (recursive)
  def find_height(self, node):

    if(node is None):
      return 0

    lheight = self.find_height(node.left) 
    rheight = self.find_height(node.right)

    return 1 + max(lheight, rheight)

  def height(self):
    return self.find_height(self.root)

# Main
def main():
  root = Node(0)
  tree = BTree(root)
  tree.insert([2, -1, 1, 5, -5])
  print(tree.height())

if __name__ == "__main__":
  main()