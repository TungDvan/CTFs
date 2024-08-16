#include <windows.h>
#include <stdio.h>
#include <stdbool.h> 
#include <stdlib.h>

// Định nghĩa con trỏ hàm với kiểu trả về và tham số phù hợp với hàm check
typedef bool (*CheckFunction)(const char*);

int main() {
    // Tải thư viện Puzzle_v2.dll
    HMODULE hDll = LoadLibrary("Puzzle_v2.dll");
    
    // Lấy địa chỉ hàm check từ Puzzle_v2.dll
    CheckFunction check_func = (CheckFunction)GetProcAddress(hDll, "check");

    char input[100];
    printf("Flag: ");
    gets(input);

    // Gọi hàm check_t và kiểm tra kết quả
    int result = check_func(input);
    if (result) printf("Correct :>\n");
    else printf("Wrong :<\n");

    // Giải phóng thư viện
    FreeLibrary(hDll);
    return 0;
}