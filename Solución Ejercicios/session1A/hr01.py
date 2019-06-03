# encontrar la aceleración en MURA
# a = (vf - vi) / t

vf = int(input('vf: '))
vi = int(input('vi: '))
t = int(input('t: '))
if t==0:
    print('ERROR')
else:
    a = (vf - vi) / t
    print ('aceleración: ' + str(a))
