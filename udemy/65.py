l = [1, 2, 3]
i = 5

try:
     l[0]
except IndexError as exc:
    print('dont worry: {}', format(exc))
except NameError as ex:
    print(ex)
except Exception as ex:
    print('other:{}'.format(ex))
else:
    print('done')
finally:
    print('clean up')
