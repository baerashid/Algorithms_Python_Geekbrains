import sys
import ctypes
import struct

a = 5
b = 123.45


print(id(a))
print(sys.getsizeof(a))

print(ctypes.string_at(id(a), sys.getsizeof(a)))
print(struct.unpack('LLLLLLl', ctypes.string_at(id(a), sys.getsizeof(a))))
print(id(int))

print('*'*50)

print(id(b))
print(sys.getsizeof(b))

z = b
b = 122.99
print(ctypes.string_at(id(b), sys.getsizeof(b)))
print(struct.unpack('LLLd', ctypes.string_at(id(b), sys.getsizeof(b))))
print(id(float))

print('*'*50)

c = 'Hello World!'
print(id(с))
print(sys.getsizeof(с))

print(ctypes.string_at(id(с), sys.getsizeof(с)))
print(struct.unpack('L'*10+'li'+'c'*13, ctypes.string_at(id(с), sys.getsizeof(с))))
print(id(str))
