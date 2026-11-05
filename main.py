class Node:
  """Клас вузла стеку"""

  def __init__(self, data):
    self.data = data  # Зберігає дані вузла
    self.next = None  # Посилання на попередній вузол (або None)


class NodeStack:
  """Реалізація стеку на основі вузлів (посилань)"""

  def __init__(self):
    self.top = None  # Якщо стек порожній, top дорівнює None
    self._count = 0  # Лічильник елементів

  def push(self, item):
    """Вставляє об'єкт на вершину стеку"""
    new_node = Node(item)
    new_node.next = self.top
    self.top = new_node
    self._count += 1

  def pop(self):
    """Повертає елемент з вершини стеку та видаляє його"""
    if self.top is None:
      raise IndexError("Спроба pop() з порожнього стеку")
    removed_data = self.top.data
    self.top = self.top.next
    self._count -= 1
    return removed_data

  def peek(self):
    """Повертає елемент з вершини стеку (без видалення)"""
    if self.top is None:
      return None
    return self.top.data

  def clear(self):
    """Видаляє всі елементи з стеку"""
    self.top = None
    self._count = 0

  def count(self):
    """Повертає кількість елементів стеку"""
    return self._count

  def size(self):
    """Повертає кількість елементів у стеку"""
    return self._count

  def toString(self):
    """Виводить всі елементи стеку від вершини до дна (без видалення)"""
    elements = []
    current = self.top
    while current is not None:
      elements.append(str(current.data))
      current = current.next
    return " -> ".join(elements) if elements else "Стек порожній"

  def __str__(self):
    return self.toString()