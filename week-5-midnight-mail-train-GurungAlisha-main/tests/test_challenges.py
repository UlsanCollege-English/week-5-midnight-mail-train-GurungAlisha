from src.challenges import (
    MidnightMailDLL,
    clean_radio_message,
    count_priority_labels,
    is_valid_ticket_code,
)


# Problem 1: DLL

def test_append_and_reverse_list_basic() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    train.append_car("C3")
    assert train.to_reverse_list() == ["C3", "B2", "A1"]


def test_detach_last_car_basic() -> None:
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    assert train.detach_last_car() == "B2"
    assert train.to_reverse_list() == ["A1"]


def test_detach_last_car_empty() -> None:
    train = MidnightMailDLL()
    assert train.detach_last_car() is None


def test_append_single_car_reverse_list() -> None:
    """Single node: reverse list should contain just that car."""
    train = MidnightMailDLL()
    train.append_car("X9")
    assert train.to_reverse_list() == ["X9"]


def test_detach_last_car_single_node() -> None:
    """Detaching the only node should leave head and tail as None."""
    train = MidnightMailDLL()
    train.append_car("Z1")
    assert train.detach_last_car() == "Z1"
    assert train.to_reverse_list() == []
    assert train.head is None
    assert train.tail is None


def test_detach_all_cars_sequentially() -> None:
    """Detach every car one by one; list should be empty at the end."""
    train = MidnightMailDLL()
    train.append_car("A1")
    train.append_car("B2")
    train.append_car("C3")
    assert train.detach_last_car() == "C3"
    assert train.detach_last_car() == "B2"
    assert train.detach_last_car() == "A1"
    assert train.detach_last_car() is None


def test_reverse_list_empty_dll() -> None:
    """Reverse list on an empty DLL should return []."""
    train = MidnightMailDLL()
    assert train.to_reverse_list() == []


# Problem 2: ticket code
# Valid case, 2 invalid cases, 1 edge case

def test_ticket_code_valid_example() -> None:
    assert is_valid_ticket_code("MM-1234") is True


def test_ticket_code_invalid_wrong_prefix() -> None:
    """Wrong prefix should fail even if the suffix is valid."""
    assert is_valid_ticket_code("XX-1234") is False


def test_ticket_code_invalid_letters_in_suffix() -> None:
    """Suffix with letters instead of digits should fail."""
    assert is_valid_ticket_code("MM-12AB") is False


def test_ticket_code_edge_too_few_digits() -> None:
    """Only 3 digits after MM- should fail (need exactly 4)."""
    assert is_valid_ticket_code("MM-123") is False


def test_ticket_code_edge_too_many_digits() -> None:
    """5 digits after MM- should also fail."""
    assert is_valid_ticket_code("MM-12345") is False


def test_ticket_code_edge_empty_string() -> None:
    """Empty string has no prefix or suffix; should fail."""
    assert is_valid_ticket_code("") is False


def test_ticket_code_edge_prefix_only() -> None:
    """Just 'MM-' with no suffix should fail."""
    assert is_valid_ticket_code("MM-") is False


# Problem 3: recursion on a list

def test_count_priority_labels_basic() -> None:
    labels = ["PRIORITY", "NORMAL", "PRIORITY", "LATE"]
    assert count_priority_labels(labels, "PRIORITY") == 2


def test_count_priority_labels_empty() -> None:
    assert count_priority_labels([], "PRIORITY") == 0


def test_count_priority_labels_no_match() -> None:
    """Target not present at all should return 0."""
    labels = ["NORMAL", "LATE", "NORMAL"]
    assert count_priority_labels(labels, "PRIORITY") == 0


def test_count_priority_labels_all_match() -> None:
    """Every element matches; count should equal list length."""
    labels = ["PRIORITY", "PRIORITY", "PRIORITY"]
    assert count_priority_labels(labels, "PRIORITY") == 3


def test_count_priority_labels_single_match() -> None:
    """Target appears exactly once at the end."""
    labels = ["NORMAL", "LATE", "PRIORITY"]
    assert count_priority_labels(labels, "PRIORITY") == 1


# Problem 4: recursion on a string

def test_clean_radio_message_basic() -> None:
    assert clean_radio_message("go now") == "gonow"


def test_clean_radio_message_empty() -> None:
    assert clean_radio_message("") == ""


def test_clean_radio_message_no_spaces() -> None:
    """String with no spaces should be returned unchanged."""
    assert clean_radio_message("ALLCLEAR") == "ALLCLEAR"


def test_clean_radio_message_all_spaces() -> None:
    """String of only spaces should return an empty string."""
    assert clean_radio_message("   ") == ""


def test_clean_radio_message_leading_trailing_spaces() -> None:
    """Spaces at both ends should be stripped along with internal ones."""
    assert clean_radio_message("  send it  ") == "sendit"


def test_clean_radio_message_single_char_space() -> None:
    """A single space character should return empty string."""
    assert clean_radio_message(" ") == ""


def test_clean_radio_message_single_char_non_space() -> None:
    """A single non-space character should be returned as-is."""
    assert clean_radio_message("X") == "X"