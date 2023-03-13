import slistH
class dlist2(slistH):
    def delLargestSeq(self):
        if self._head.next is None:
            self._head = None
            return self
        seq1 = 0  # Variable to check the length of the sequences
        seq2 = 1  # Variable to store the length of the sequences
        node = self._head  # First node
        index = 0  # Tracks the index the iteration is on
        seqstart = 0  # Stores the index of the start of the sequence to remove
        afterseq = None  # Stores the object of the element after the sequence. It defaults to None if the sequence is at the end
        posibleindex = -1  # It will store the index of the posible sequence
        while node.next is not None:  # Iterates all the list
            if node.elem == node.next.elem:  # Checks if we are in a sequence of same values
                seq1 += 1
            else:  # Changes the index of the start of the posible sequence since it is not in the current iteration
                posibleindex = index
            if seq2 <= seq1 and node.elem != node.next.elem:  # Checks if we are exiting a sequence and stores the values in case
                ## its the one
                afterseq = node.next
                seqstart = posibleindex
            if node.next.next != None:  # Helps exclude the case the sequence ends due to the end of the list
                if node.elem != node.next.elem and node.next.elem == node.next.next.elem:  # Checks that the start of the
                    # sequence moves if there are two sequences together
                    posibleindex = index
            if node.elem != node.next.elem:  # Checks if we are not in a sequence and resets the seq parameters
                if seq1 > 0:
                    seq2 = seq1
                seq1 = 0
            node = node.next
            index += 1
        if seq2 <= seq1:
            afterseq = node.next
            seqstart = posibleindex
        if seqstart == -1 and seq2 > 1:
            seqstart = posibleindex
        node = self._head
        if seqstart == -1:
            self._head = afterseq
        else:
            for e in range(seqstart):
                node = node.next
            node.next = afterseq

        return self
