class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.right = None
        self.left = None

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

    def display_queue(self):
        if not self.root:
            return None

        result = []
        queue = [self.root]
        while queue:
            current_element = queue.pop(0)
            result.append(current_element.value)
            if current_element.left:
                queue.append(current_element.left)
            if current_element.right:
                queue.append(current_element.right)
        return result
