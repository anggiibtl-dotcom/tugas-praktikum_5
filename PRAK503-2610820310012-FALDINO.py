def maksimal(a, b):
    if a > b:
        return a
    return b

def minimal(a, b):
    if a < b:
        return a
    return b

batas = 0
maks = -100000
minim = 100000
bilangan = int(input())
angka_list = list(map(int, input().split()))

while batas < bilangan:
    nilai = angka_list[batas]
    maks = maksimal(maks, nilai)
    minim = minimal(minim, nilai)
    batas += 1

print(f"{maks} {minim}")