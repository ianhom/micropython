# test errno's and uerrno module

try:
    import uerrno
except ImportError:
    print("SKIP")
    import sys
    sys.exit()

# check that constants exist and are integers
print(type(uerrno.EIO))

# check that errors are rendered in a nice way
msg = str(OSError(uerrno.EIO))
print(msg[:7], msg[-5:])
