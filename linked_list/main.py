from __future__ import annotations
from typing import Any, Optional

class Node(object):
  def __init__(self, data: Any, next_node: Node = None):
    self.data = data
    self.next = next_node

class LinkedList(object):
  def __init__(self, head: Optional[Node] = None) -> None:
    self.head = head

  def append(self, data: Any) -> None:
    new_node = Node(data)
    if self.head is None:
      self.head = new_node
      return
    
    # 先頭のノードをlast_nodeとして保持する。
    last_node = self.head
    # 次のノードが存在すれば値を更新する。
    while last_node.next:
      last_node = last_node.next
    # 最後のノードの次のノードとして新しいノードを登録する。
    last_node.next = new_node

  def insert(self, data: Any) -> None:
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def print(self) -> None:
    current_node = self.head
    while current_node:
      print(current_node.data)
      current_node = current_node.next

  def remove(self, data: Any) -> None:
    current_node = self.head

    # 1件目の場合
    if current_node and current_node.data == data:
      self.head = current_node.next
      current_node = None
      return
    
    # 削除対象を探すための走査
    previous_node = None
    while current_node and current_node.data != data:
      previous_node = current_node
      current_node = current_node.next
    
    # 削除対象が存在しなかった場合
    if current_node is None:
      return
    
    # 削除対象の場合
    previous_node.next = current_node.next
    
if __name__ == '__main__':
  l = LinkedList()
  l.append(1)
  l.append(2)
  l.append(3)
  l.insert(0)
  l.remove(2)
  l.print()



