
#import 4-rectangle as r
r = __import__("4-rectangle")

r1 = r.Rectangle(6,8)
Rectangle = r.Rectangle
print(r1)
r2 = eval(repr(r1))
print("__")
print(r2)
