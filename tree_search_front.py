# 用递归的方法来实现数的遍历
# 这个例子采用的先序遍历法
class Tree:
    # 初始化树类
    # value表示节点的值
    # leftChild表示左节点，rightChild同理
    # python里面没有指针，但是引用与指针实际上功能实现差不多，而且没有内存泄露的风险
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None

    # 增加右节点
    def add_right_node(self, the_right_node):
        self.rightChild = the_right_node

    # 增加左节点
    def add_left_node(self, the_left_node):
        self.leftChild = the_left_node


# 递归函数遍历
# 实际上递归也是一种堆栈的数据结构体现
def pre_order_view(root):
    # 如果当前的节点是空的节点，就结束向下遍历，利用递归返回上一个节点
    if root == None:
        return
    else:
        print(root.value)
        pre_order_view(root.leftChild)
        pre_order_view(root.rightChild)
        return


# 设定每一个节点的权重
node_1 = Tree(1)
node_2 = Tree(2)
node_3 = Tree(3)
node_4 = Tree(4)
node_5 = Tree(5)
node_6 = Tree(6)
node_7 = Tree(7)
node_8 = Tree(8)
node_9 = Tree(9)
node_10 = Tree(10)
node_11 = Tree(11)

# 将节点链接起来
node_1.leftChild = node_3
node_1.rightChild = node_4
node_3.leftChild = node_7
node_3.rightChild = node_8
node_4.leftChild = node_2
node_4.rightChild = node_9
node_2.leftChild = node_5
node_2.rightChild = node_6
node_9.leftChild = node_10
node_9.rightChild = node_11

# 树的遍历
pre_order_view(node_1)
