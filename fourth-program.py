def fun(arg,*argv):
  print("first argument",arg)
  for arg1 in argv:
    print("from the second argument",arg1)

fun("Hi","Welcome","to","Python")