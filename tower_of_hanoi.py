"""
Given a tower of [number] disks, initially stacked in decreasing size on
one of three pegs.
The objective is to transfer the entire tower to one of the other pegs,
moving only one disk at a time and never moving a larger one onto a smaller.
"""
from __future__ import print_function

def tower_of_hanoi(num, source, target, helper):
    """Moving num of the disks from source to target using helper"""
    if num == 0:
        return
    else:
        tower_of_hanoi(num - 1, source, helper, target)
        print("move the disk -", num, "from", source, "to", target)
        tower_of_hanoi(num - 1, helper, target, source)

print("tower of 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')

print("\ntower of 5 disks:")
tower_of_hanoi(5, 'A', 'C', 'B')
