"""Задача 2. Поміняти місцями кожні два сусідні вузли зв'язаного списку.

Значення у вузлах не змінюються - переставляються самі вузли.
Розв'язок рекурсивний, без жодного циклу.
"""


class ListNode:
    """Вузол однозв'язного списку."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_pairs(head):
    """Міняє місцями кожну пару вузлів і повертає нову голову списку."""
    # Базовий випадок: 0 або 1 вузол - міняти нічого
    if head is None or head.next is None:
        return head
    first = head
    second = head.next
    # Рекурсивно обробляємо решту списку, яка починається з третього вузла
    first.next = swap_pairs(second.next)
    # Другий вузол стає першим у парі
    second.next = first
    return second


def build_list(values):
    """Створює зв'язаний список з Python-списку (рекурсивно)."""
    if not values:
        return None
    return ListNode(values[0], build_list(values[1:]))


def to_python_list(head):
    """Перетворює зв'язаний список на Python-список (рекурсивно)."""
    if head is None:
        return []
    return [head.val] + to_python_list(head.next)
