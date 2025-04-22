from pythonds3 import Stack, BinaryTree
import operator

def build_parse_tree(expression):
    """Parse tree for mathematical expression"""
    expr = expression.split(" ")
    expr_tree = BinaryTree("")
    parent_track = Stack()
    parent_track.push(expr_tree)
    current_parent = expr_tree
    
    for token in expr:
        
        if token == '(':
            current_parent.insert_left("")
            parent_track.push(current_parent)
            current_parent = current_parent.left_child
        
        elif token in ['+', '-', '*', '/']:
            current_parent.root = token
            current_parent.insert_right("")
            parent_track.push(current_parent)
            current_parent = current_parent.right_child
        
        elif token.isdigit():
            current_parent.root = int(token)
            parent = parent_track.pop()
            current_parent = parent
        
        elif token == ')':
            current_parent = parent_track.pop()
        
        else:
            raise ValueError(f"Unknown token {token}")
    
    return expr_tree


def evaluate_parse_tree(expr_tree):
    """evaluates the parse tree to return the total"""
    
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    
    left_child = expr_tree.left_child
    right_child = expr_tree.right_child
    
    if left_child and right_child:
        fn = operators[expr_tree.root]
        return fn(
            evaluate_parse_tree(left_child), evaluate_parse_tree(right_child)
        )
    
    return expr_tree.root


e = '( 3 + ( 4 * 5 ) )'
a = build_parse_tree(e)
print(evaluate_parse_tree(a))