"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    
    # Your code goes here
    for each in items:
        if str(each) in frequencies:
            frequencies[str(each)] += 1
        else:
            frequencies[str(each)] = 1
    
    return frequencies
