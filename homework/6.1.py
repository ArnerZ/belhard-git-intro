def concat(*args, reversed=False):
    cash = ''
    if reversed:
        for i in args[::-1]:
            cash+=i
    else:
        for i in args:
            cash+=i
    print(cash)
