#   Рівень 3
#   Варіант 1
#   Для заданого бінарного дерева та конкретної вершини в цьому дереві
#   реалізуйте функцію пошуку наступного елемента під час серединного проходу
#   (in-order traversal). Наступник - це вузол, який має значення більше
#   за заданий вузол і знаходиться найближче до нього при серединному обході.
#
#   Нехай у вас задане бінарне дерево такого вигляду:
#
#       10
#      /  \
#     5    15
#    / \     \
#   3   7    20
#            /
#           12
#
#   Для вершини зі значенням 7, наступник - це вузол зі значенням 10.
#   Функція отримує на вхід корінь бінарного дерева та
#   вершину, для якої потрібно знайти наступника.

import unittest
#   root = BinaryTree(3)
#   root.left = BinaryTree(9)
#   root.right = BinaryTree(20)


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    return node
