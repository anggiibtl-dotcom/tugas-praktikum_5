#include <stdio.h>

int reverse(int angka) {
    int hasil = 0;
    while (angka > 0) {
        hasil = (hasil * 10) + (angka % 10);
        angka /= 10;
    }
    return hasil;
}

int main() {
    int A, B;
    scanf("%d %d", &A, &B);
    A = reverse(A);
    B = reverse(B);
    int C = A + B;
    printf("%d", reverse(C));
    return 0;
}