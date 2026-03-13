import random

questions = [

"Explain time complexity of binary search",

"Write Python code to reverse a linked list",

"What is polymorphism in OOP?",

"Explain BFS vs DFS",

"Difference between list and tuple",

"Explain recursion",

"Implement stack using python",

"Explain dynamic programming",

"Two sum problem approach",

"Explain hash tables"
]

def generate_test():

    return random.sample(questions,5)
