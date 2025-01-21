# def xor(a, b):
#     # Đảm bảo a và b có cùng độ dài
#     result = []
#     length = max(len(a), len(b))

#     for i in range(length):
#         result.append(chr(ord(a[i % len(a)]) ^ ord(b[i % len(b)])))
    
#     return ''.join(result)

# def main():
#     # Nhập chuỗi từ người dùng
#     input_string = input("Enter Something: ")

#     # Chia chuỗi thành 4 phần
#     num = len(input_string)
#     array2 = input_string[:num // 4]
#     array3 = input_string[num // 4:num // 2]
#     array4 = input_string[num // 2:3 * num // 4]
#     array5 = input_string[3 * num // 4:]

#     # Thực hiện XOR giữa các phần
#     array2 = xor(array2, array3)
#     array3 = xor(array3, array4)
#     array4 = xor(array4, array5)
#     array5 = xor(array5, array2)

#     # Nối các phần lại thành một chuỗi
#     array6 = array2 + array3 + array4 + array5

#     # Chuỗi URL bí mật
#     text = "https://www.youtube.com/watch?v=L8XbI9aJOXk"

#     # XOR kết quả với chuỗi URL
#     array6 = xor(array6, text)

#     # Mảng byte đã cho
#     source = [
#         85, 122, 105, 71, 17, 94, 71, 24, 114, 78, 107, 11, 108, 106, 107, 113,
#         121, 51, 91, 117, 86, 110, 100, 18, 124, 104, 71, 66, 123, 3, 111, 99,
#         74, 107, 69, 77, 111, 2, 120, 125, 83, 99, 62, 99, 109, 76, 119, 111,
#         59, 32, 1, 93, 69, 117, 84, 106, 73, 85, 112, 66, 114, 92, 61, 80, 80,
#         104, 111, 72, 98, 28, 88, 94, 27, 120, 15, 76, 15, 67, 86, 117, 81,
#         108, 18, 37, 34, 101, 104, 109, 23, 30, 62, 78, 88, 10, 2, 63, 43, 72,
#         102, 38, 76, 23, 34, 62, 21, 97, 1, 97
#     ]
    
#     # Chuyển mảng byte source thành chuỗi ký tự
#     source_string = ''.join(chr(byte) for byte in source)

#     # Kiểm tra nếu kết quả sau XOR khớp với mảng byte đã cho
#     if array6 != source_string:
#         print("Wrong!!")
#     else:
#         print("Decode It!!")

# if __name__ == "__main__":
#     main()

def xor(a, b):
    # Đảm bảo a và b có cùng độ dài
    result = []
    length = max(len(a), len(b))

    for i in range(length):
        result.append(chr(ord(a[i % len(a)]) ^ ord(b[i % len(b)])))
    
    return ''.join(result)

def reverse():
    # Chuỗi URL bí mật
    text = "https://www.youtube.com/watch?v=L8XbI9aJOXk"
    
    # Mảng byte đã cho
    source = [
        85, 122, 105, 71, 17, 94, 71, 24, 114, 78, 107, 11, 108, 106, 107, 113,
        121, 51, 91, 117, 86, 110, 100, 18, 124, 104, 71, 66, 123, 3, 111, 99,
        74, 107, 69, 77, 111, 2, 120, 125, 83, 99, 62, 99, 109, 76, 119, 111,
        59, 32, 1, 93, 69, 117, 84, 106, 73, 85, 112, 66, 114, 92, 61, 80, 80,
        104, 111, 72, 98, 28, 88, 94, 27, 120, 15, 76, 15, 67, 86, 117, 81,
        108, 18, 37, 34, 101, 104, 109, 23, 30, 62, 78, 88, 10, 2, 63, 43, 72,
        102, 38, 76, 23, 34, 62, 21, 97, 1, 97
    ]
    
    # Chuyển mảng byte source thành chuỗi ký tự
    source_string = ''.join(chr(byte) for byte in source)

    # XOR với chuỗi URL bí mật để khôi phục lại array6
    array6 = xor(source_string, text)
    
    # Chia chuỗi đã khôi phục thành các phần tương ứng với array2, array3, array4, array5
    num = len(array6)
    array2 = array6[:num // 4]
    array3 = array6[num // 4:num // 2]
    array4 = array6[num // 2:3 * num // 4]
    array5 = array6[3 * num // 4:]

    # Thực hiện XOR ngược lại giữa các phần
    array5 = xor(array5, array2)
    array4 = xor(array4, array5)
    array3 = xor(array3, array4)
    array2 = xor(array2, array3)

    # Kết hợp các phần để khôi phục lại chuỗi ban đầu (flag)
    flag = array2 + array3 + array4 + array5
    print(f"Flag: {flag}")

if __name__ == "__main__":
    reverse()
