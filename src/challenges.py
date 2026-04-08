"""Week 5 homework: Midnight Mail Train.

Complete the required functions and classes.
Use recursion only where the instructions require recursion.
"""

from __future__ import annotations


class TrainCarNode:
    """A node in a doubly linked list of train cars."""

    def __init__(self, car_id: str) -> None:
        self.car_id = car_id
        self.prev: TrainCarNode | None = None
        self.next: TrainCarNode | None = None


class MidnightMailDLL:
    """A doubly linked list for train cars."""

    def __init__(self) -> None:
        self.head: TrainCarNode | None = None
        self.tail: TrainCarNode | None = None

    def append_car(self, car_id: str) -> None:
        """Add a train car to the end of the list."""
<<<<<<< HEAD
        new_node = TrainCarNode(car_id)
        if self.tail is None:          # list is empty
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
=======
        raise NotImplementedError
>>>>>>> 0b419c9470ca7d4bddc2c90931a7154e9bddd1e3

    def detach_last_car(self) -> str | None:
        """Remove the last train car and return its ID.

        Return None if the list is empty.
        """
<<<<<<< HEAD
        if self.tail is None:          # empty list
            return None

        removed_id = self.tail.car_id

        if self.tail is self.head:     # only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return removed_id

    def to_reverse_list(self) -> list[str]:
        """Return all train car IDs from tail to head."""
        result = []
        current = self.tail
        while current is not None:
            result.append(current.car_id)
            current = current.prev
        return result
=======
        raise NotImplementedError

    def to_reverse_list(self) -> list[str]:
        """Return all train car IDs from tail to head."""
        raise NotImplementedError
>>>>>>> 0b419c9470ca7d4bddc2c90931a7154e9bddd1e3


def is_valid_ticket_code(code: str) -> bool:
    """Return True only if the code starts with 'MM-' and ends with exactly 4 digits."""
<<<<<<< HEAD
    if not code.startswith("MM-"):
        return False
    suffix = code[3:]               # everything after 'MM-'
    return len(suffix) == 4 and suffix.isdigit()
=======
    raise NotImplementedError

>>>>>>> 0b419c9470ca7d4bddc2c90931a7154e9bddd1e3


def count_priority_labels(labels: list[str], target: str) -> int:
    """Recursively count how many times target appears in labels."""
<<<<<<< HEAD
    if not labels:                  # base case: empty list
        return 0
    match = 1 if labels[0] == target else 0
    return match + count_priority_labels(labels[1:], target)
=======
    raise NotImplementedError

>>>>>>> 0b419c9470ca7d4bddc2c90931a7154e9bddd1e3


def clean_radio_message(message: str) -> str:
    """Recursively return a new string with all spaces removed."""
<<<<<<< HEAD
    if not message:                 # base case: empty string
        return ""
    first = "" if message[0] == " " else message[0]
    return first + clean_radio_message(message[1:])
=======
    raise NotImplementedError
>>>>>>> 0b419c9470ca7d4bddc2c90931a7154e9bddd1e3


# Optional stretch

def count_priority_labels_iterative(labels: list[str], target: str) -> int:
    """Optional stretch: iterative version of count_priority_labels."""
<<<<<<< HEAD
    count = 0
    for label in labels:
        if label == target:
            count += 1
    return count
=======
    raise NotImplementedError

>>>>>>> 0b419c9470ca7d4bddc2c90931a7154e9bddd1e3


def clean_radio_message_iterative(message: str) -> str:
    """Optional stretch: iterative version of clean_radio_message."""
<<<<<<< HEAD
    return "".join(ch for ch in message if ch != " ")
=======
    raise NotImplementedError
>>>>>>> 0b419c9470ca7d4bddc2c90931a7154e9bddd1e3
