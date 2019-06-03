# encontrar el tiempo en MURA
# t = (vf - vi) / a

vf = int(input('vf: '))
vi = int(input('vi: '))
a = int(input('a: '))
if a==0:
    print('ERROR')
else:
    t = (vf - vi) / a
    print ('tiempo: ' + str(a))
    # print "{0:.2f}".format(5.1234554321)
