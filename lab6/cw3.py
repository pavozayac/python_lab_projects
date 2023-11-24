from typing import Iterable

def _mt(num: int, a: Iterable):
    i = iter(a)

    yield from make_tree(num, i)

def make_tree(num: int, a: Iterable):
    if num != 0:
        yield make_tree(num // 2, a)

        yield next(a) 

        yield make_tree(num // 2, a)
    else:
        yield None
    
    

def walk(tree: Iterable, preorder: bool, inorder: bool, postorder: bool):
    assert int(preorder) + int(postorder) + int(inorder) == 1

    if tree is None:
        return
    else:
        left = next(tree)
        middle = next(tree)
        right = next(tree)
        if preorder:
            print(middle)

        walk(left, preorder, inorder, postorder)

        if inorder:
            print(middle)
        
        walk(right, preorder, inorder, postorder)

        if postorder:
            print(middle)

print(list(_mt(7, "alakota")))

print(walk(_mt(7, "alakota"), False, True, False))