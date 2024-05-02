from __future__ import annotations
from typing import Any

class Node(object):
  def __init__(self, data: Any, next_node: Node = None):
    self.data = data
    self.next = next_node

class LinkedList(object):
  def __init__(self, head=None) -> None:
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