# Node
class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# Main
def main():
  root = Node(0)
  print(root.value)

if __name__ == "__main__":
  main()