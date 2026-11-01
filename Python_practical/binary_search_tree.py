class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(root,key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left,key)
    else:
        root.right = insert(root.right,key)
    return root
def search(root,key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left,key)
    else:
        return search(root.right,key)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
root = None
for key in [50,30,70,20,40,60,80]:
    root = insert(root,key)
print("Inorder Traversal:")
inorder(root)
key = int(input("Enter value to search:"))
if search(root,key):
    print("Element found")
else:
    print("Element not found")

