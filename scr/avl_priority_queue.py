class PriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_element = Node(value, priority)
        if not self.root:
            self.root = new_element
        else:
            current_element = self.root
            parent = None
            while current_element:
                parent = current_element
                if new_element.priority <= current_element.priority:
                    current_element = current_element.left
                else:
                    current_element = current_element.right
            if new_element.priority <= parent.priority:
                parent.left = new_element
            else:
                new_element.left = parent
                new_element.right = parent.right
                parent.right = new_element
                if self.root == parent:
                    self.root = new_element

    def delete_highest_priority_element(self, current_element=None, parent=None):
        if not current_element:
            current_element = self.root
        if not current_element:
            return None

        if not current_element.right:
            if parent:
                parent.right = current_element.left
            else:
                self.root = current_element.left
            return current_element
        else:
            return self.delete_highest_priority_element(current_element.right, current_element)

    def view_tree(self):
        if not self.root:
            return None

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
