## import modules here 

################# Question 0 #################


def add(a, b):  # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x):  # do not change the heading of the function
    low = 0
    mid = 0
    up = x + 1
    flag = False
    while not flag:
        mid = (low + up) // 2
        if mid ** 2 <= x < (mid + 1) ** 2:
            flag = True
        else:
            if mid ** 2 > x:
                up = mid
            else:
                low = mid
    return mid


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON=1E-7, MAX_ITER=1000):  # do not change the heading of the function
    x = x_0
    x_new = x_0 - f(x_0)/fprime(x_0)
    count_iter = 1
    while abs(x_new - x) >= EPSILON and count_iter < MAX_ITER:
        x = x_new
        x_new = x - f(x)/fprime(x)
        count_iter += 1
    return x_new


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)


def make_tree(tokens):  # do not change the heading of the function
    assert len(tokens) > 0
    tmp_stack = []
    tmp_tree = Tree(tokens[0])
    tmp_stack.append(tmp_tree)
    for token in tokens[2:-1]:
        if token == '[':
            tmp_stack.append(tmp_tree)
        elif token == ']':
            tmp_stack.pop()
        else:
            tmp_tree = Tree(token)
            tmp_stack[-1].add_child(tmp_tree)
    return tmp_stack[-1]


def max_depth(root):  # do not change the heading of the function
    if len(root.children) == 0:
        return 1
    else:
        return max([1 + max_depth(i) for i in root.children])



# if __name__ == "__main__":
#     ## test question 1
#     # print(nsqrt(1))
#     # print(nsqrt(11))
#     # print(nsqrt(1369))
#     #
#     ## test question 2
#     # def f(x):
#     #     return x * math.log(x) - 16.0
#     #
#     # def fprime(x):
#     #     return 1.0 + math.log(x)
#     #
#     # x = find_root(f, fprime)
#     # print(x)
#     # print(f(x))
#
#     # test question 3-1
#     def print_tree(root, indent=0):
#         print(' ' * indent, root)
#         if len(root.children) > 0:
#             for child in root.children:
#                 print_tree(child, indent + 4)
#
#     toks = ['1', '[', '2', '[', '3', '4', '5', ']', '6', '[', '7', '8', '[', '9', ']', '10', '[', '11', '12', ']', ']', '13', ']']
#     tt = make_tree(toks)
#     print_tree(tt)
#
#     ## test question 3-2
#     depth = max_depth(tt)
#     print(depth)
#     pass
