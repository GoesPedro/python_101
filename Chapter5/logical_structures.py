# "unary" operator: not
# binary operators: and, or, is

active = True
logged = False

if active and logged:
    print('Welcome, user!')
elif active and logged is not True:
    # = not logged
    print('You need to log in first.')
else:
    print('You need to activate your account.')
