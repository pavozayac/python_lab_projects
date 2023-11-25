from typing import Iterable

def _mt(num: int, a: Iterable):
    i = iter(a)

    return make_tree(num, i)

def yield_single(f, *args, **kwargs):
    yield tuple(f(*args, **kwargs))

def make_tree(num: int, a: Iterable):
    if num > 1:
        # l = yield from make_tree(num - 2, a)
        yield from yield_single(make_tree, num // 2, a)

        # b = next(a)
        # print(b)

        # print('n ', next(a))
        yield next(a)

        # right = list(make_tree(num // 2, a))
        # yield right
        # yield from make_tree(num // 2, a)
        yield from yield_single(make_tree, num // 2, a)

    else:
        yield None
        yield next(a)
        yield None
        # yield None
    
    

def walk(tree: Iterable, preorder: bool, inorder: bool, postorder: bool):
    assert int(preorder) + int(postorder) + int(inorder) == 1

    if tree is None:
        return
    else:
        tree = iter(tree)
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

print(list(_mt(3, "ala")))
# print(list(list(_mt(3, "ala"))[0]))
print(list(_mt(7, 'alakota')))

walk(_mt(7, 'alakota'), False, True, False)