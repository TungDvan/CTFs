// #include<stdio.h>
// #include<string.h>
// int main(){
//     char a[100];
//     gets(a);
//     for (int i = 0; i < strlen(a); i++){
//         if (i % 10 == 9) printf("0x%x,\n", a[i]);
//         else printf("0x%x, ", a[i]);
//     }
// }

// // 12345678901234567890123456789012
// // tungdvandeptraicomotkhonghainhaa

#include<stdio.h>



int main(){
    int v12, v13, v14, v15, v16, v17, v18;
    int a[16];
    for (int i = 0; i < 16; i++) a[i] = i;
    for (int i = 0; i < 16; i++) printf("%d ", a[i]);
    printf("\n");

    v12 = a[1];
    a[1] = a[5];
    a[5] = a[9];
    a[9] = a[13];
    a[13] = v12;
    
    v14 = a[2];
    a[2] = a[10];
    a[10] = v14;

    v16 = a[6];
    a[6] = a[14];
    a[14] = v16;

    v18 = a[3];
    a[3] = a[15];
    a[15] = a[11];
    a[11] = a[7];
    a[7] = v18;

    for (int i = 0; i < 16; i++) printf("%d ", a[i]);
}

// 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15       
// 0 5 10 15 4 9 14 3 8 13 2 7 12 1 6 11 