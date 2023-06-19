a = 'sunilllllllljjjjgh'
# walrus operator assigns variable to an expression so that it can be reuesed again instead of rewriteing the entire expression again
if (n := len(a)) > 10:
    print(f'{n} overflow')
