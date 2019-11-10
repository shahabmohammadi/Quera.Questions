def get_func(args):
    lambda_list = []
    for task in args:
        if task == "square":
            lambda_list.append(lambda x: x * x)
        elif task == "circle":
            lambda_list.append(lambda x: (x * x) * 3.141592653589793)
        elif task == "rectangle":
            lambda_list.append(lambda x, y: x * y)
        elif task == "triangle":
            lambda_list.append(lambda x, y: (x * y) / 2)
    return lambda_list
