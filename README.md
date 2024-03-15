3 РІВЕНЬ
Варіант 3
Для заданого бінарного дерева реалізуйте функцію, яка обчислює та повертає значення максимального діаметра у бінарному дереві - найвіддаленішу відстань між двома листками. Максимальний діаметр у бінарному дереві визначає найбільшу відстань між будь-якою парою листків (кінцевих вузлів) у дереві. Діаметр вимірюється як кількість ребер, які потрібно пройти, щоб дістатися одного листка від іншого. Максимальний діаметр не обов'язково має включати в себе кореневий вузол

Нехай у вас задане бінарне дерево такого вигляду:

        1
       /  \
      3    2
     / \
    7   4
   /     \
  8       5
 /         \
9           6
Для даного дерева максимальний діаметр становить 6: 9 -> 8 -> 7 -> 3 -> 4 -> 5 -> 6 - для проходження від листка 9 до листка 6 слід пройти 6 ребер.

Реалізована вами функція binary_tree_diameter(tree: BinaryTree) -> int отримує на вхід корінь бінарного дерева та повертає максимальний діаметр дерева.

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
