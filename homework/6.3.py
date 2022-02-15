def inspect(variable):
    def e1_variable(*args: str, **kwargs: bool):
        print(f'Args : {args}')
        print(f'Kwargs : {kwargs}')
        retvalue = variable(*args, **kwargs)
        print(f"Retvalue : {retvalue}")
        return retvalue
    return e1_variable 
@inspect
def concat(*args, reversed=False):
    cash = ''
    if reversed:
        for i in args[::-1]:
            cash+=i
    else:
        for i in args:
            cash+=i
    print(cash)
