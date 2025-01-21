#include <stdio.h>

unsigned int map[] = {0x126575, 0x5190323, 0x8AAB8F5, 0x0CA51930};

void reverse_sub(unsigned int *a1, unsigned int *a2)
{
    unsigned int input1 = *a1;
    unsigned int input2 = *a2;
    unsigned int v6 = 0x9E3779B9 * 20;  // Giá trị v6 sau 20 vòng lặp (sử dụng với 20 vòng lặp)
    
    for (int i = 0; i < 20; ++i)
    {
        unsigned int map_val2 = map[(v6 >> 11) & 3] + v6;
        
        // Reverse input2
        input2 -= (((input1 >> 5) ^ (16 * input1)) + input1) ^ map_val2;

        v6 -= 0x9E3779B9;  // Lùi lại v6
        unsigned int map_val1 = map[v6 & 3] + v6;
        
        // Reverse input1
        input1 -= (((input2 >> 5) ^ (16 * input2)) + input2) ^ map_val1;
    }
    
    *a1 = input1;
    *a2 = input2;
}

int main() {
    unsigned int input1 = 0x0DB1D77F3;  // Ví dụ giả định giá trị input1
    unsigned int input2 = 0x7DEBD37;  // Ví dụ giả định giá trị input2
    
    printf("Original input1: %x\n", input1);
    printf("Original input2: %x\n", input2);

    reverse_sub(&input1, &input2);  // Reverse hàm sub

    printf("Reversed input1: %x\n", input1);
    printf("Reversed input2: %x\n", input2);

    return 0;
}
