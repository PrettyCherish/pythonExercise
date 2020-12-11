"""
@Time     :   2020/12/4 10:15
@Author   :   Winter
@File     :   Binary_tree.py
@Software :   PyCharm
@Blog     :   https://blog.csdn.net/hdd871532887
"""
# coding=utf-8


class NodeTree:
    def __init__(self,  data=None,  lchild=None,  rchild=None):
        """

        :param data:    节点数据
        :param lchild:  左子树
        :param rchild:  右子树
        """
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinTree:
    #   ------前序遍历------（根左右node,lchild,rchild）
    #   递归算法
    def pre_order(self, t):
        # 判断二叉树为空
        if t == None:
            return 0
        print(t.data,   end=' ')
        self.pre_order(t.lchild)
        self.pre_order(t.rchild)

    #   ------中序遍历------(左根右lchild,node,rchild)
    #   递归算法
    def middle_order(self, t):
        # 判断二叉树为空
        if t == None :
            return 0
        self.middle_order(t.lchild)
        print(t.data, end=' ')
        self.middle_order(t.rchild)

    #   ------后序遍历------(左右根lchild,rchild,node)
    #   递归算法
    def post_order(self, t):
        # 判断二叉树为空
        if t == None:
            return 0
        self.post_order(t.lchild)
        self.post_order(t.rchild)
        print(t.data, end=' ')

    # 计算二叉树深度
    def depth(self, t):
        # 判断二叉树为空
        if t == None:
            return 0
        else:
            m = self.depth(t.lchild)
            n = self.depth(t.rchild)
            # 返回max(左子树,右子树）深度+1（根节点）
            return m+1 if m > n else n+1

    # 计算二叉树节点个数
    def nodecount(self, t):
        # 判断二叉树为空
        if t == None:
            return 0
        else:
            return self.nodecount(t.lchild)+self.nodecount(t.rchild)+1


if __name__ == '__main__':
    nodeTree = NodeTree(1,
                        lchild=NodeTree(2,
                                        lchild=NodeTree(4,  rchild=NodeTree(7))),
                        rchild=NodeTree(3,
                                        lchild=NodeTree(5), rchild=NodeTree(6)))
    T = BinTree()
    print("二叉树前序遍历结果为：")
    T.pre_order(nodeTree)
    print('\n')
    print("二叉树中序遍历结果为：")
    T.middle_order(nodeTree)
    print('\n')
    print("二叉树后序遍历结果为：")
    T.post_order(nodeTree)
    print('\n')
    print("此二叉树的深度为：")
    print(T.depth(nodeTree))
    print("此二叉树的节点个数为：")
    print(T.nodecount(nodeTree))
