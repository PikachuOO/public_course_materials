#!/usr/bin/python3
#stolen from 5074963
# List operations
a = [];
a.append(1);
a.append(2);
a[1] = 3;
print(a[0], a[1]);

b = [ 1, 2, 4, 8, 16, 32, 64, 128, 256 ];
b[0:3] = [0, 0, 0];
print(b.pop(-5));
print(b[2], b[3], b[5]);
