def reverse(a):
    if len(a)==0:
        return
    else:
        print(a[-1])
        reverse(a[:-1])#(:) is used to excluding the last values.
reverse=[3,4,5]       