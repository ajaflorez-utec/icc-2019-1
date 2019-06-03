ladoa = int(input())
ladob = int(input())
ladoc = int(input())

if ladoa > 1 and ladob > 1 and ladoc > 1:
  if ladoa == ladob:
    if ladob == ladoc:
      print("equilátero")
    else:
      print("isósceles")
  elif ladoa == ladoc:
    print("isósceles")
  elif ladob == ladoc:
    print("isósceles")
  else:
    print("escaleno")
else:
  print("error")