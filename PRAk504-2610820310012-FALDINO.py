def reverse(angka):
    hasil = 0
    while angka > 0:
        hasil = (hasil * 10) + (angka % 10)
        angka //= 10
    return hasil

A, B = map(int, input().split())
A = reverse(A)
B = reverse(B)
C = A + B
print(reverse(C))