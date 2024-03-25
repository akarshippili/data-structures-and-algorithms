class Page:
    
    def __init__(self, tuple_=None, key=None):
        self.tuple = tuple_
        self.key = key
    
    def __str__(self) -> str:
        nl = '\n'
        return f'Page: [tuple: {self.tuple}, key: {self.key}]'


class BTreeNode:
    def __init__(self, degree=3):
        self.degree = degree
        self.childNodes = []
        self.isLeaf = False
        self.prevNode = None
        self.nextNode = None
        self.parent = None

    def add(self, page: Page):
        if self.isLeaf:
            index = 0
            while (
                index < len(self.childNodes) and self.childNodes[index].key < page.key
            ):
                index += 1
            self.childNodes = [*self.childNodes[:index], page, *self.childNodes[index:]]
            self.balanceUp()
            return

        index = 1
        while index < len(self.childNodes) and self.childNodes[index].key < page.key: index += 2
        self.childNodes[index - 1].add(page)

    def balanceUp(self):
        '''
            leaf Node:
                can have degree + 1 elements
                [page1, page2, .., page(degree+1)]
            
            other Node (non-leaf):
                degree pointers to child nodes
                degree-1 elements
        '''
        if self.isLeaf and len(self.childNodes) <= self.degree + 1: return
        if(not self.isLeaf and len(self.childNodes) <= (2*self.degree - 1)): return
            
        new_node1, new_node2 = self.split()
        assert new_node1.parent == new_node2.parent
        parent = new_node1.parent

        if(not parent):
            parent = BTreeNode()
            page = Page(tuple_ = None, key = new_node2.childNodes[0].key)
            parent.childNodes = [new_node1, page, new_node2]
            new_node1.parent = parent
            new_node2.parent = parent
            return
        
        index = 0
        key = new_node2.childNodes[0].key
        while(index < len(parent.childNodes) and parent.childNodes[index] != self): index += 2
        page = Page(tuple_ = None, key = new_node2.childNodes[0].key)
        parent.childNodes = [*parent.childNodes[:index+1], page, new_node2, *parent.childNodes[index+1:]]
        parent.balanceUp()

    def split(self):
        length = len(self.childNodes)
        arr1, arr2 = (
            self.childNodes[: length // 2][::],
            self.childNodes[length // 2 :][::],
        )

        node1, node2 = self, BTreeNode()
        node1.isLeaf = node2.isLeaf = True
       
        node1.prevNode = self.prevNode
        node2.nextNode = self.nextNode
        node1.parent = node2.parent = self.parent
        node1.nextNode, node2.prevNode = node2, node1
        node1.childNodes, node2.childNodes = arr1, arr2

        if node1.prevNode: node1.prevNode.nextNode = node1
        if node2.nextNode: node2.nextNode.prevNode = node2
        return node1, node2
    
    def __str__(self) -> str:
        return f"BTreeNode: {[str(child) for child in self.childNodes]}"



class BTree:

    def __init__(self, degree=3):
        self.degree = degree
        self.root = BTreeNode()
        self.root.isLeaf = True

    def add(self, page: Page):
        self.root.add(page = page)
        while(self.root.parent): self.root = self.root.parent
        # temp = self.root
        
        # while temp and not temp.isLeaf:
        #     index = 0
        #     while index < len(temp.childNodes) and temp.childNodes[index].key <= val:
        #         index += 1
        #     temp = temp.childNodes[index]

        # # we are at left node
        # index = 0
        # while index < len(temp.childNodes) and temp.childNodes[index].key <= val:
        #     index += 1

        # temp.childNodes = [
        #     *temp.childNodes[:index],
        #     Page(val, val),
        #     *temp.childNodes[index:],
        # ]

        # if len(temp.childNodes) >= self.degree + 2:
        #     "we have to split node"
        #     node1, node2 = temp.split()

    def remove(self):
        pass
    
    def __str__(self) -> str:
        return f"root: {self.root}"

tree = BTree()
tree.add(Page(tuple_= "b", key = 2))
tree.add(Page(tuple_= "a", key = 1))
tree.add(Page(tuple_= "a", key = 3))
tree.add(Page(tuple_= "a", key = 0))
tree.add(Page(tuple_= "a", key = -10))
tree.add(Page(tuple_= "a", key = 11))
tree.add(Page(tuple_= "a", key = -1001))
tree.add(Page(tuple_= "a", key = 1234555))
tree.add(Page(tuple_= "a", key = 69))
print(tree)
