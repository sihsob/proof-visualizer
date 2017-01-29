from parse_tree import parse_sentence
from statement import *
import statement

def reit(logic_val, reference):
    if len(reference) > 1:
        return False

    logic_tree = parse_sentence(logic_val)
    ref_tree = parse_sentence(reference[0])

    return compareTree(logic_tree, ref_tree)

def orIntro(logic_val, reference):
    if len(reference) > 1:
        return False

    logic_tree = parse_sentence(logic_val)
    ref_tree = parse_sentence(reference[0])
    temp_tree = logic_tree

    # TODO: Make sure all top level are ors
    #while isinstance(temp_tree, BinaryStatement):
    #    if not temp_tree.value == '|':
    #        return False
    #    temp_tree = temp_tree.left

    ors = getAllOrOperands(logic_tree, [])
    for i in ors:
        print_tree(i)
        if compareTree(i, ref_tree) == True:
            return True
    return False

def orElim(logic_val, reference):
    if len(reference) == 0:
        return False

    logic_tree = parse_sentence(logic_val)
    ref_tree = parse_sentence(reference[0])
    ors = getAllOrOperands(ref_tree, [])

    #TODO: Make sure all top level are ors

    for ref in reference[1:]:
        ref_tree2 = parse_sentence(ref)
        for i in ors:
            if compareTree(ref_tree2.left, i) == True:
                break
        else: return False

    for ref in reference[1:]:
        ref_tree2 = parse_sentence(ref)
        if compareTree(ref_tree2.right, logic_tree) == False:
            return False
    return True

def andIntro(logic_val, reference):
    if len(reference) == 0:
        return False

    logic_tree = parse_sentence(logic_val)
    refs = []
    for i in reference:
        refs.append(parse_sentence(i))

    # TODO: Make sure all top level are ands

    ands = getAllAndOperands(logic_tree, [])
    for i in ands:
        for j in refs:
            if compareTree(i, j) == True:
                break
        else:
            return False
    return True

def andElim(logic_val, reference):
    if len(reference) > 1:
        return False

    logic_tree = parse_sentence(logic_val)
    ref_tree = parse_sentence(reference[0])
    temp_tree = ref_tree

    # TODO: Make sure all top level are ands
    #while isinstance(temp_tree, BinaryStatement):
    #    if not temp_tree.value == '|':
    #        return False
    #    temp_tree = temp_tree.left

    ands = getAllAndOperands(ref_tree, [])
    for i in ands:
        if compareTree(i, logic_tree) == True:
            return True
    return False

def notIntro(logic_val, reference):
    if len(reference) > 1:
        return False

    logic_tree = parse_sentence(logic_val)
    ref_tree = parse_sentence(reference[0]) # this is a subproof
    if not ref_tree.value == "-":           # subproof condition
        return False
    if not isinstance(ref_tree.right, ContradictionStatement):
        return False

    neg = UnaryStatement("~", ref_tree.left)
    return compareTree(neg, logic_tree)

def notElim(logic_val, reference):
    if len(reference) > 1:
        return False
    logic_tree = parse_sentence(logic_val)
    ref_tree = parse_sentence(reference[0])
    if not ref_tree.value == "~":
        return False
    if not ref_tree.child.value == "~":
        return False

    return compareTree(ref_tree.child.child, logic_tree)

def contraIntro(logic_val, reference):
    if len(reference) > 2:
        return False
    if not logic_val == "!":
        return False

    # Statements could have been selected out of order
    ref_tree1 = parse_sentence(reference[0])
    ref_tree2 = parse_sentence(reference[1])
    neg = UnaryStatement("~", ref_tree1)
    if compareTree(ref_tree2, neg) == True:
        return True
    else:
        ref_tree1 = parse_sentence(reference[1])
        ref_tree2 = parse_sentence(reference[0])
        neg = UnaryStatement("~", ref_tree1)
        if compareTree(ref_tree2, neg) == True:
            return True

    return False

def contraElim(logic_val, reference):
    if len(reference) > 1:
        return False

    ref_tree = parse_sentence(reference[0])
    return compareTree(ref_tree, ContradictionStatement())

def impIntro(logic_val, reference):
    if len(reference) > 1:
        return False

    logic_tree = parse_sentence(logic_val)
    ref_tree = parse_sentence(reference[0])

    return compareTree(logic_tree, ref_tree)

def impElim(logic_val, reference):
    if len(reference) > 2:
        return False

    ref_tree = parse_sentence(reference[0])
    logic_tree = parse_sentence("(" + reference[1] + ") - (" + logic_val + ")")

    return compareTree(ref_tree, logic_tree)

def biIntro(logic_val, reference):
    if len(reference) > 2:
        return False

    logic_tree = parse_sentence(logic_val)
    if not logic_tree.value == "=":
        return False

    ref_tree1 = parse_sentence(reference[0])
    ref_tree2 = parse_sentence(reference[1])

    if compareTree(ref_tree1.left, ref_tree2.right) == False:
        return False
    if compareTree(ref_tree2.left, ref_tree1.right) == False:
        return False

    if compareTree(logic_tree.left, ref_tree1.left) == True and \
        compareTree(logic_tree.right, ref_tree1.right) == True:
        return True
    elif compareTree(logic_tree.left, ref_tree2.left) == True and \
        compareTree(logic_tree.right, ref_tree2.right) == True:
        return True
    else: return False


def biElim(logic_val, reference):
    if len(reference) > 2:
        return False

    ref_tree = parse_sentence(reference[0])
    logic_tree = parse_sentence("(" + reference[1] + ") = (" + logic_val + ")")

    if compareTree(ref_tree, logic_tree) == True:
        return True

    logic_tree = parse_sentence("(" + logic_val + ") = (" + reference[1] + ")")
    if compareTree(ref_tree, logic_tree) == True:
        return True

    ref_tree = parse_sentence(reference[1])
    logic_tree = parse_sentence("(" + reference[0] + ") = (" + logic_val + ")")

    if compareTree(ref_tree, logic_tree) == True:
        return True

    logic_tree = parse_sentence("(" + logic_val + ") = (" + reference[0] + ")")
    if compareTree(ref_tree, logic_tree) == True:
        return True

    return False
