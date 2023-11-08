class relation:
    def __init__(self, child, parent, grandchild, grandfather, siblings):
        self.child = child
        self.parent = parent
        self.grandchild = grandchild
        self.grandfather = grandfather
        self.siblings = siblings

class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = {}
        self.relation = relation(0, 0, 0, 0, 0)

    def append(self, value):
        node = self.__class__(value, parent=self)
        self.children[value] = node
        return node

    def dfs(self, func):
        func(self)
        for child in self.children.values():
            child.dfs(func)

    def find(self, value):
        if self.value == value:
            return self
        for child in self.children.values():
            result = child.find(value)
            if result:
                return result

    def set_relations(self):
        for child in self.children.values():
            self.relation.child += 1
            child.relation.parent += 1
            child.relation.siblings = len(self.children) - 1
            for grandchild in child.children.values():
                grandchild.dfs(self._set_inderect)
            child.set_relations()

    def _set_inderect(self, node):
        self.relation.grandchild += 1
        node.relation.grandfather += 1

def task(tree):
    rows = [row.split(",") for row in tree.splitlines()]
    root = Node(rows[0][0])
    for row in rows:
        root.find(row[0]).append(row[1])
    root.set_relations()
    nodes = []
    root.dfs(nodes.append)
    result = "\n".join(f"{node.relation.child},{node.relation.parent},{node.relation.grandchild},{node.relation.grandfather},{node.relation.siblings}" for node in sorted(nodes, key=lambda node: node.value))
    return result

if __name__ == "__main__":
    print(task("1,2\n1,3\n3,4\n3,5"))
