# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # method1
        # if not root:
        #     return ""

        # queue = [root]
        # res = []

        # while queue:
        #     for _ in range(len(queue)):
        #         node = queue.pop(0)

        #         if not node:
        #             res.append("null")
        #             continue

        #         res.append(str(node.val))

        #         queue.append(node.left)
        #         queue.append(node.right)

        # return ",".join(res)

        # method2
        def dfs(node):
            if not node:
                return "null,"
            return f"{node.val},{dfs(node.left)}{dfs(node.right)}"

        return dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        # method1
        # if not data:
        #     return None

        # vals = data.split(",")
        # root = TreeNode(int(vals[0]))
        # queue = [root]
        # idx = 1

        # while queue:
        #     node = queue.pop(0)

        #     if vals[idx] != "null":
        #         node.left = TreeNode(int(vals[idx]))
        #         queue.append(node.left)
        #     idx += 1

        #     if vals[idx] != "null":
        #         node.right = TreeNode(int(vals[idx]))
        #         queue.append(node.right)
        #     idx += 1

        # return root

        # method2
        vals = data.split(",")
        self.idx = 0

        def dfs():
            if vals[self.idx] == "null":
                self.idx += 1
                return None

            node = TreeNode(int(vals[self.idx]))
            self.idx += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
