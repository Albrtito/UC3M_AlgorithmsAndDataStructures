def isPalindrome(self):
    from_head_node = self.head
    from_tail_node = self.tail
    is_palindrome = True

    i = 0
    int_half_size = len(self) // 2
    while i < int_half_size and is_palindrome:
        if from_head_node != from_tail_node:
            is_palindrome = False
        else:
            from_tail_node = from_tail_node.prev
            from_head_node = from_head_node.next
            i += 1
    return is_palindrome