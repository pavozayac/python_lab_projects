def odpluskw(f):
    def odpluskwiona(*args, **kwargs):
        print(args)
        print(kwargs)

        result = f(*args, **kwargs)
        
        print(result)

        return result
    
    return odpluskwiona


@odpluskw
def dodaj(a, b, c = None):
    if c is None:
        return a + b
    else:
        return a + b + c

dodaj(1, 2, c=5)