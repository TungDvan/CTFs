# Callfuscate

- Chall: [callfuscate](callfuscate/callfuscate.exe)

## B1: Đọc hiểu.

- Sau khi nhìn sơ lượt qua mã giả thì chúng ta có thể thấy chương trình này cấp cho chúng ta 3 hàm nhưng chỉ có cái hàm đầu tiên là `print` thì chúng ta mới đoán được thoai, còn 2 cái hàm `sub_7FF6067F2500`, `sub_7FF6067F35B0`,`sub_7FF6067F4680` thì thực sự là rất khó hình dung khi mới bắt tay vào làm bài này. 

    ![alt text](IMG/1/image-1.png)

- Ta thử click vào hàm `sub_7FF6067F2500` thì thấy hiện ra một số thứ trông rất là kinh dị.

    ![alt text](IMG/1/image-2.png)
    
    Nhưng khi ta debug chạy qua hàm đó thì hàm `sub_7FF6067F2500` chỉ có mục đích đơn giản là kiểu `scan` thui nhưng mà trong cái hàm đó nó không được biểu diễn trực tiếp là `scanf` mà thông qua hàm loạt các phép tính kinh tởm kia. Dường như bài toán đang gợi ý cho ta cách xử lý hàm sú sú này thông qua một hàm có chức năng đơn giản là `scan` để ta tự suy ra được các hàm sau nó như thế nào (thực ra là ban đầu tui nhìn vào cx sợ z ò ra, chứ chưa có kiểu suy luận như thế này, sau khi làm xong mới kiểu logic lại những gợi ý từ đề bài và thấy cũng hợp lý, nếu mà hàm `scan` này nó không kiểu thực hiện các phép tính như thế kia mà chỉ những hàm `encrypt` với cả `check` thì thực sự làm cho người chơi rất khó hình dung).

    Quay trở lại với hàm sú sú có chức năng `scan`, ta thấy ban đầu truyền vào hàm là một biến (tui đặt là `input`) thì trong cái hàm scan đó nó thực hiện một loạt các phép tính toán nhưng mà các phép tính đó không phụ thuộc gì vào biến `input` truyền vào cả, biến `input` đó chỉ xuất hiện ở cuối hàm đó thoai. Mục đích là chương trình không thực hiện gọi trực tiếp chúng ra mà thực hiện rất nhiều các phép toán tính ra địa chỉ của hàm có chức năng scan. Rồi ép kiểu và `__fastcall`.

    ![alt text](IMG/1/image-3.png)

    Khi ta thực hiện nhảy vào lệnh call đó thì hàm thực hiện chức năng scan sẽ xuất hiện. Cụ thể như sau:

    ![alt text](IMG/1/image-4.png)

- Như vậy thông qua hàm scan trên ta có thể biết được chính xác các hàm `sub_7FF6067F35B0` và `sub_7FF6067F4680` có chức năng là gì.

    ![alt text](IMG/1/image-5.png)

    **sub_7FF6067F35B0**: `encrypt` input trong đó có hàm con là `encrypt_chr` thực hiện mục đích đó.
    
    ![alt text](IMG/1/image-6.png)

    ![alt text](IMG/1/image-7.png)

    **sub_7FF6067F4680**: check flag.

    ![alt text](IMG/1/image-8.png)

- Tóm lại sau phần đọc hiểu này là chúng ta hiểu là chương trình có hiện tại có 3 phần, những hàm không được gọi trực tiếp mà mình phải tìm chúng.

## B2: Khai thác.

- Khi nhìn qua chall này thi chúng ta không thể thấy trực tiếp chiều dài của flag, nhưng mà nếu ta để ý hàm `check_flag` ở cuối thì flag sẽ có chiều dài `48`.

    ![alt text](IMG/1/image-9.png)

- Đến lúc này ta thực hiện kết hợp đọc mã giả và debug thì sẽ hiểu được chương trình đang làm gì. (với input đầu vào là **tungdva1tungdva2tungdva3tungdva4tungdva5tungdva6**)

- Trong hàm `encrypt`, trước khi vào hàm `encrypt_chr` thì chương trình sẽ thực hiện lấy lần lượt 8 kí tự của `input` rùi nối nó với chuỗi có tên là `confused`, xong mới truyền vào hàm `encrypt_chr`. Cụ thể như hình sau:

    ![alt text](IMG/1/image-10.png)

- Trong hàm `encrypt_chr` thì nó chỉ thực hiện chức năng là gán lại những giá trị của 8 kí tự của flag thông qua một phép dịch trái bit của một giá trị của `map` cho trước, rùi trả về 8 kí tự mới sau `100` vòng lặp thoai.

    ![alt text](IMG/1/image-11.png)

    Map có những giá trị sau:

    ![alt text](IMG/1/image-13.png)

- Còn trong hàm `check_flag` thì chúng ta tìm được cái `flag_en` với các giá trị như sau:

    ![alt text](IMG/1/image-12.png)

- Trước khi bước sang bước thứ 3 là tìm flag thì ta sẽ thực hiện build lại bài này (sương sương thoai không phải y hệt) bằng ngôn ngữ python để xem bản thân đã hiểu đúng mục đích của bài này chưa.

    ```python
    map = [
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 
        0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D, 
        0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 
        0x72, 0xC0, 0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 
        0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15, 0x04, 0xC7, 
        0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 
        0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 
        0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84, 
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 
        0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF, 0xD0, 0xEF, 0xAA, 0xFB, 
        0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 
        0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 
        0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C, 
        0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 
        0x64, 0x5D, 0x19, 0x73, 0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 
        0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB, 
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 
        0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79, 0xE7, 0xC8, 0x37, 0x6D, 
        0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 
        0xAE, 0x08, 0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 
        0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A, 0x70, 0x3E, 
        0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 
        0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 
        0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF, 
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 
        0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    ]

    input = [
        0x74, 0x75, 0x6e, 0x67, 0x64, 0x76, 0x61, 0x31, 0x74, 0x75,
        0x6e, 0x67, 0x64, 0x76, 0x61, 0x32, 0x74, 0x75, 0x6e, 0x67,
        0x64, 0x76, 0x61, 0x33, 0x74, 0x75, 0x6e, 0x67, 0x64, 0x76,
        0x61, 0x34, 0x74, 0x75, 0x6e, 0x67, 0x64, 0x76, 0x61, 0x35,
        0x74, 0x75, 0x6e, 0x67, 0x64, 0x76, 0x61, 0x36
    ]   # tungdva1tungdva2tungdva3tungdva4tungdva5tungdva6

    confused = [
        0x00, 0x63, 0x6F, 0x6E, 0x66, 0x75, 0x73, 0x65, 0x64
    ]

    def rol(a, b):
        return  ((a << b) | (a >> (8 - b))) & 0xff

    def function_1(pos):
        a = input[pos : pos + 8: 1]
        a += confused
        return a

    def function_2(a):
        for i in range(100):
            a[1] = rol((map[(a[0] + a[9]) & 0xff] + a[1]) & 0xff, 1)
            a[2] = rol((map[(a[1] + a[10]) & 0xff] + a[2]) & 0xff, 1)
            a[3] = rol((map[(a[2] + a[11]) & 0xff] + a[3]) & 0xff, 1)
            a[4] = rol((map[(a[3] + a[12]) & 0xff] + a[4]) & 0xff, 1)
            a[5] = rol((map[(a[4] + a[13]) & 0xff] + a[5]) & 0xff, 1)
            a[6] = rol((map[(a[5] + a[14]) & 0xff] + a[6]) & 0xff, 1)
            a[7] = rol((map[(a[6] + a[15]) & 0xff] + a[7]) & 0xff, 1)
            a[0] = rol((map[(a[7] + a[16]) & 0xff] + a[0]) & 0xff, 1)
        a = a[0 : 8 : 1]
        return a


    if __name__ == "__main__":
        ans = []
        for i in range(0, 48, 8):
            tmp = function_1(i)
            tmp_1 = function_2(tmp)
            ans += tmp_1
        for i in range(len(ans)):
            if i % 10 == 9: print(f"{hex(ans[i])},")
            else: print(hex(ans[i]), ", ", sep = '', end = '')
    ```

- Sau khi chạy xong thì thấy kết quả trên IDA khớp với kết quả ủa chương trình trên, vậy là chúng ta tạm yên tâm với với những suy nghĩ ở trên roài.

    ![alt text](IMG/1/image-14.png)

    ![alt text](IMG/1/image-15.png)

## B3: Tìm flag.

- Bài này lúc ban đầu tui làm thì tui không thể nghĩ ra cách nào để có thể làm ngược lại bài toán cả, chỉ dừng lại ửo bước hiểu chương trình mà thoai, nhưng sau khi tham khảo thì với bài này chúng ta vẫn có thể **bruteforce** được.

- Ta chú ý vào cái hàm chính cần **bruteforce** đó chính là `function_2` sau:
    
    ```python
    def function_2(a):
        for i in range(100):
            a[1] = rol((map[(a[0] + a[9]) & 0xff] + a[1]) & 0xff, 1)
            a[2] = rol((map[(a[1] + a[10]) & 0xff] + a[2]) & 0xff, 1)
            a[3] = rol((map[(a[2] + a[11]) & 0xff] + a[3]) & 0xff, 1)
            a[4] = rol((map[(a[3] + a[12]) & 0xff] + a[4]) & 0xff, 1)
            a[5] = rol((map[(a[4] + a[13]) & 0xff] + a[5]) & 0xff, 1)
            a[6] = rol((map[(a[5] + a[14]) & 0xff] + a[6]) & 0xff, 1)
            a[7] = rol((map[(a[6] + a[15]) & 0xff] + a[7]) & 0xff, 1)
            a[0] = rol((map[(a[7] + a[16]) & 0xff] + a[0]) & 0xff, 1)
        a = a[0 : 8 : 1]
        return a
    ```

    Bây giờ chúng ta cần suy nghĩ ngược lại, sau 100 vòng lặp thì cuối cùng nó sẽ return về kết quả. Ví dụ ở vòng lặp thứ 100 thì thứ tự các kí tự đó chính là biết kí tự `a[1] `rùi đến `a[2]` rùi ... đến `a[7]`, `a[0]`. Điều đặc biệt đó chính là những `a[i]` ở đằng sau được tính dựa trên `a[j]` ở trước đó và chính giá trị `a[i]` ở vòng lặp trước đấy, tức là `a[2]` (vòng lặp thứ **100**) được tính bằng thông qua `a[1]` (vòng lặp thứ **100**) và chính giá trị `a[2]` (vòng lặp thứ **99**),... Vậy nên kết quả trả về là kết quả thứ 100, theo quy nạp thì chúng ta hoàn toàn có thể tính được tất cả các giá trị `a[i]` ở mỗi vòng lặp thứ i (i từ 1 đến 100). Vậy tức là chúng ta hoàn toàn có thể tìm `a[i]` ở vòng lặp thứ 0, tức là **flag** ban đầu dựa trên `flag_encrypt`. Vậy điều chúng ta cần tìm đó chính là các giá trị a[i] sau mỗi vòng lặp (từ 100 về 1).

    Cụ thể như sau:

    ```python
    flag_encryp = [
        0xE5, 0xA8, 0x07, 0x2E, 0xE8, 0x67, 0xB5, 0x0C, 0xF9, 0x05, 
        0xA1, 0xA8, 0xFA, 0x05, 0x0A, 0x66, 0xA0, 0xC1, 0x20, 0x4E, 
        0xE3, 0x7D, 0xD0, 0x04, 0x21, 0x67, 0xEC, 0x9E, 0x7D, 0xBC, 
        0x2D, 0x8D, 0x9B, 0x65, 0xDC, 0x71, 0xE4, 0x57, 0x81, 0x11, 
        0x1A, 0x71, 0x7F, 0x84, 0x2C, 0x88, 0x25, 0x94
    ]

    map = [
        0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 
        0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76, 0xCA, 0x82, 0xC9, 0x7D, 
        0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 
        0x72, 0xC0, 0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 
        0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15, 0x04, 0xC7, 
        0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 
        0xEB, 0x27, 0xB2, 0x75, 0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 
        0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84, 
        0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 
        0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF, 0xD0, 0xEF, 0xAA, 0xFB, 
        0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 
        0x9F, 0xA8, 0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 
        0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2, 0xCD, 0x0C, 
        0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 
        0x64, 0x5D, 0x19, 0x73, 0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 
        0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB, 
        0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 
        0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79, 0xE7, 0xC8, 0x37, 0x6D, 
        0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 
        0xAE, 0x08, 0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 
        0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A, 0x70, 0x3E, 
        0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 
        0x86, 0xC1, 0x1D, 0x9E, 0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 
        0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF, 
        0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 
        0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
    ]

    confused = [
        0x00, 0x63, 0x6F, 0x6E, 0x66, 0x75, 0x73, 0x65, 0x64
    ] #confused

    def rol(a, b):
        return  ((a << b) | (a >> (8 - b))) & 0xff

    def function_1(pos):
        a = flag_encryp[pos : pos + 8: 1]
        a += confused
        return a

    def function_rev2(a):
        for i in range(100):
            for j in range(256):
                if a[0] == rol((map[(a[7] + a[16]) & 0xff] + j) & 0xff, 1):
                    a[0] = j
                    break
            for j in range(256):
                if a[7] == rol((map[(a[6] + a[15]) & 0xff] + j) & 0xff, 1):
                    a[7] = j
                    break
            for j in range(256):
                if a[6] == rol((map[(a[5] + a[14]) & 0xff] + j) & 0xff, 1):
                    a[6] = j
                    break
            for j in range(256):
                if a[5] == rol((map[(a[4] + a[13]) & 0xff] + j) & 0xff, 1):
                    a[5] = j
                    break
            for j in range(256):
                if a[4] == rol((map[(a[3] + a[12]) & 0xff] + j) & 0xff, 1):
                    a[4] = j
                    break
            for j in range(256):
                if a[3] == rol((map[(a[2] + a[11]) & 0xff] + j) & 0xff, 1):
                    a[3] = j
                    break
            for j in range(256):
                if a[2] == rol((map[(a[1] + a[10]) & 0xff] + j) & 0xff, 1):
                    a[2] = j
                    break
            for j in range(256):
                if a[1] == rol((map[(a[0] + a[9]) & 0xff] + j) & 0xff, 1):
                    a[1] = j
                    break
        a = a[0 : 8 : 1]
        return a


    if __name__ == "__main__":
        ans = []
        for i in range(0, 48, 8):
            tmp = function_1(i)
            tmp_1 = function_rev2(tmp)
            ans += tmp_1
        for i in range(len(ans)): print(chr(ans[i]), end = '')
    ```

    ![alt text](IMG/1/image-16.png)

    ![alt text](IMG/1/image-17.png)

    Flag: `KMA{e81eabf0-db79-463d-b227-ea47dcf6cac6}`

# Crackme

- Chall: [crackme](crackme/crackme.exe)

## B1: Đọc hiểu.

- Với bài toán này khi ta đọc mã giả thì thấy nó qua ư là dễ nhìn ạ. Bài này mọi thứ đã hiện lên trước mắt hết rùi ạ.

    ![alt text](IMG/2/image.png)

- Nhìn sơ qua là thấy bài này nhập input vào xong xử lý `10` kí tự đầu thông qua vòng `for` rùi nếu mà thoả mãn thì gán vô `str1`, xong rùi so sánh với `str2`, nếu thoả thì in ra thành công.

## B2: Khai thác.

- Trước hết điều ta lấy được đầu tiên đó chính là `str2`.

    ![alt text](IMG/2/image-1.png)

- Ta thấy các giá trị rằng `map` là lưu các giá trị, nhưng mà `map` ko lưu giá trị bình thường mà lại lưu địa chỉ.

    ![alt text](IMG/2/image-3.png)

- Ta phân tích kĩ đoạn này:

    ![alt text](IMG/2/image-4.png)

    Đầu tiên là `str2` chỉ có 10 kí tự, mà vòng `for` này chỉ lặp có 10 lần, từ đó ra suy ra một điều đó chính là chắc chắn phải cố tình để `input[i] - 0x30 < 0xA`, tức là `input[i] < 58`.

    ![alt text](IMG/2/image-5.png)

    Từ đây ta có thể suy ra **90%** đó chính là input đầu vào sẽ là các số trong khoảng từ 0 đến 9.

    Bây giờ ta sẽ phân tích kĩ chỗ này:

    ![alt text](IMG/2/image-6.png)

    Nếu mà chỗ này chỉ đọc ở mã giả thì đúng là có hơi lú lú đấy, chúng ta kết hợp debug nữa thì sẽ dễ hiểu hơn.

    ![alt text](IMG/2/image-7.png)

    Nếu ta đọc mã máy thì thấy trên mã máy chỉ có `map[eax * 8]` nhưng mà trên mã giả lại là `(&map)[2 * v4]`, có một chút sự khác biệt ở đây ạ, ưu tiên hiểu mã giả hơn.

    Ví dụ trong vòng lặp này thì chương trình thực hiện đọc kí `7` cho vào thanh `eax` (câu lệnh **eax, [ebp+var_8]**), rùi nó sẽ chuyển giá trị của map vị trí thứ **8*eax**. 

    ![alt text](IMG/2/image-8.png)

    Chúng ta thực hiện click vô `map` thì thấy `map` có kiểu dữ liệu `byte`, có địa chỉ bắt đầu từ `.data:008BD012`.

    ![alt text](IMG/2/image-9.png)

    Vậy chúng ta thực hiện tính lấy 0x008BD012 + 0x38 (vì 0x38 = 56 = 7.8) = 0x008BD04C. Vậy tức là nó sẽ đến địa chỉ 0x008BD04C và gán giá trị tại địa điểm đó cho eax. Ta thực hiện tìm và đối chiếu thì nó hoàn toàn khớp.

    ![alt text](IMG/2/image-10.png)

    Sau đó sẽ chuyển giá trị đó vào thành `eax` thông qua câu lệnh `[ebp+var_C], ecx` và `eax, [ebp+var_C]`, rùi xong đưa giá trị của địa chỉ đó vào thành cl bằng câu lệnh `cl, [eax]`.

- Tóm lại nãy giờ tui phân tích đó chính là `map` này sẽ lưu địa chỉ (hay một con trỏ trỏ tới một giá trị) và nó sẽ lấy giá trị của địa chỉ mà map lưu rùi gán lại cho từng `str[i]`.

## B3: Tìm flag.

- Như vậy bây giờ chúng ta muốn tìm flag thì chỉ cần lọc những giá trị của địa chỉ mà map lưu lần lượt thoai, do có mỗi 10 kí tự nên cũng nhanh. Cụ thể như sau:

    |i|map[i]|giá trị mà map[i] trỏ tới|
    |--|--|--|
    |0|unk_8BD040|8|
    |1*8|unk_8BD028|f|
    |2*8|byte_8BD018|0|
    |3*8|unk_8BD048|3|
    |4*8|byte_8BD020|d|
    |5*8|unk_8BD030|b|
    |6*8|aA|a|
    |7*8|unk_8BD038|c|
    |8*8|unk_8BD058|e|
    |9*8|unk_8BD050|7|

- Mà str2 là chuỗi `a0dfbc837e` nên đối chiếu bảng trên ta được str1 cần nhập đó chính là `6241570398`

    ![alt text](IMG/2/image-11.png)

# Encryptor

- Chall: [encryptor.exe](encryptor/encryptor.exe) và [flag.bmp.encrypted](encryptor\flag.bmp.encrypted)

## B1: Đọc hiểu.

- Trước hết điều đầu tiên ta cần chú ý với bài này là bài này có tham số truyền vào chứ không phải là chạy chương trình mới nhập.

    ![alt text](IMG/3/image.png)

    Vậy tức là mình cần truyền một file vào roài truyền một số nào đó có vẻ như là key để chương trình làm một cái gì đó.

- Ta thực hiện đọc mã giả, thấy chương trình có bố cụ khá là dễ đọc.

    ![alt text](IMG/3/image-1.png)

- Trước hết, chúng ta cần biết dòng `input = atoi(argv[2])` là gì.

    ![alt text](IMG/3/image-3.png)

    `argv[2]` sẽ là key mà ta truyền vô, sau khi gọi hàm call xong thì input sẽ là key dưới dạng số (chứ trước đó vẫn là dạng chuỗi).

    ![alt text](IMG/3/image-4.png)

    Tương tự như thế ta cx có thể biết argv[1] là file ta truyền vào.

    ![alt text](IMG/3/image-5.png)

- Khi ta vào trong hàm `file_encrypt` thì ta sẽ thấy như sau:

    ![alt text](IMG/3/image-6.png)

- Hàm **RC4**: Đến dòng 24 của mã giả, ta thực hiện xem giá trị truyền vào hàm là gì, khi ta đọc ta biết được truyền và `va` nhưng mà chúng ta không thực sự biết `va` là gì, thì kết hợp với việc debug ta có thể biết `va` chính là một mảng được tạo ra bởi chính `key` mà chúng ta truyền vào ở trên, và số 4 chính là số lượng phần tử của mảng đoá.

    ![alt text](IMG/3/image-7.png)

    Như ở trên thì ta truyền vào số `1234567` thì máy sẽ chuyển từ chuỗi sang số dưới dạng hexa là `12D687` rồi từ số đó chuyển thành mảng có các phần tử lần lượt là `0x87`, `0xD6`, `0x12`, `0x00`.

    Sau hàm này cx chỉ đơn giản là sinh ra một mảng thoai.

    ![alt text](IMG/3/image-8.png)

- Hàm **encrypt**: Dòng 28, hàm này cần truyền vào nội dung của file và kích thước size của file (tại sao tui lại biết điều đó, vì tui thử truyền một file txt vào với nội dung là tui soạn sẵn chứ nếu không thử tui cũng chả biết đâu).

    ![alt text](IMG/3/image-9.png)

    Bên trong cũng chỉ là mã hoá `input` thui.

- Những hàm ở bên dưới là hàm đưa nội dung mã hoá vào một file rùi đặt tên file đó thêm đuôi .encrypted, nói chung cx không quan trọng mấy.

- Tóm lại, đến lúc này ta biết bài này là một bài mã hoá file theo kiểu RC4 với key là số mà ta truyền vào.

## B2: Khai thác.

- Bài cho ta thêm một file nữa đã được mã hoá đó chính là `flag.bmp.encrypted`. Như vậy ta sẽ biết là file gốc của chúng ta sẽ là file `flag.bmp`, đây là một file ảnh, xong đó là tất cả những gì mà chúng ta có thể biết.

## B3: Tìm flag.

- Đến chỗ này thực sự là tui không thể nào có ý tưởng gì cho bài này, đây cx là lần đầu tui làm bài dạng mã hoá file nên gần như ban đầu tui chả có ý tưởng gì để `bruteforce` cả, sau khi được gợi ý về phần header của file bmp thì lúc đó tui mới biết.

- File bmp: sẽ luôn có phần header là `BM`, các 8 byte tiếp theo sẽ là kích thước của file ảnh đó, các bạn có thể thử bằng việc lấy một file ảnh bmp bất gì rùi thực hiện đọc dữ liệu từ file đó nhá (có thể tham khảo trong **readme_file.py** của tui).

- Như vậy chúng ta sẽ biết được kích thước của file `flag.bmp` thông qua file `flag.bmp.encrypted` vì việc mã hoá RC4 không làm tăng thêm kích thước của file. Vậy file sẽ có kích thước là `551766`, vậy tức là byte để biểu thị sau phần header BM là `0x56`, `0x6b`, `0x08`. Vậy chắc chắn ảnh flag.bmp ban đầu sẽ có 5 byte đầu tiên là `0x42`, `0x4d`, `0x56`, `0x6b`, `0x08`.

- Vậy bây giờ ta chỉ cần biết được 5 byte ban đầu sau phần mã hoá rùi bruteforce để tìm ra key chính xác là được. Dễ dàng để ta có thể tìm ta 5 byte đầu tiên của file `flag.bmp.encrypted` là `0xe0`, `0x3b`, `0xe1`, `0x66`, `0xf8`.

- Như vậy ta viết sc để tìm key thoai, bạn có thể tham khảo:

    ```python
    data_encrypt = [
        0xe0, 0x3b, 0xe1, 0x66, 0xf8
    ]

    data_mau = [
        0x42, 0x4d, 0x56, 0x6b, 0x08
    ]   # BMVk

    def copy_list():
        ans = []
        for i in range(len(data_mau)):
            ans.append(data_mau[i])
        return ans

    def convert(a):
        ans = []
        for i in range(4):
            ans.append(a & 0xff)
            a = a >> 8
        return ans

    def RC4(key):
        map = []
        for i in range(256): map.append(i)
        tmp = 0
        for i in range(256):
            tmp = (key[i % 4] + map[i] + tmp) % 256
            tmp_i = map[i]
            map[i] = map[tmp]
            map[tmp] = tmp_i
        return map

    def RC4_en(map, data):
        tmp1, tmp2 = 0, 0
        for i in range(len(data)):
            tmp1 = (tmp1 + 1) % 256
            tmp2 = (map[tmp1] + tmp2) % 256
            tmp = map[tmp1]
            map[tmp1] = map[tmp2]
            map[tmp2] = tmp
            data[i] ^= map[(map[tmp1] + map[tmp2]) % 256]
            if data[i] != data_encrypt[i]: return False
        return True

    if __name__ == "__main__":
        for i in range(4294967296):
            key = convert(i)
            map = RC4(key)
            data = copy_list()
            if RC4_en(map, data): 
                print(i)
                break
    ```

- Dễ dàng tìm ra được key là `25110`, do việc mã hoá RC4 là mã hoá đối xứng nên ta chỉ cần mã hoá một lần nữa file encrypt là sẽ ra file ban đầu. Thực hiện đổi lại tên về đúng định dạng file bmp là ta sẽ được flag.

    ![alt text](encryptor/flag.bmp)

- Flag: `KMACTF{th3_k3y_is_t00_w3ak}`.

# Guess.

- Chall: [guess.exe](guess/guess.exe)

## B1: Đọc hiểu.

- Nhìn qua mã giả của bài này chúng ta thấy bài này khá là ít thao tác, và những hàm trong bài này cũng kiểu quen thuộc (cũng na ná giống RC4 nên về bài này vấn đê đọc hiểu khá là dễ dàng).

    ![alt text](IMG/4/image.png)

    ![alt text](IMG/4/image-1.png)

    ![alt text](IMG/4/image-2.png)

    ![alt text](IMG/4/image-3.png)

- Tóm lại qua việc đọc mã giả thì thấy bài này khai báo một mảng cipher, xong từ input đầu vào thực hiện mã hoá nana giống CR4 rùi thực hiện in ra kết quả sau khi mã hoá.

## B2: Khai thác.

- Bài này hầu như khá là quen thuộc, cũng ít dữ liệu, may mắn thay tui khi làm bài này thì lúc lấy dữ liệu trên IDA thì tự nhiên tui phát hiện ra trong mã máy có một đoạn khai báo mà trong mã giả không có, tui sẽ đặt nó là `data_X` chứ lúc này vẫn chưa biết nó để làm gì.

    ![alt text](IMG/4/image-4.png)

    ```python
    data_X = [
        0x45, 0x32, 0x55, 0x35, 0x14, 0x0F, 0x5D, 0x63, 0x26, 0x76, 
        0x74, 0x06, 0x02, 0x31, 0x05, 0x34, 0x51, 0x77, 0x5C, 0x2C, 
        0x3F, 0x2B, 0x3E, 0x36, 0x28, 0x07, 0x50, 0x7D, 0x40, 0x58, 
        0x24, 0x15, 0x65, 0x79, 0x6F, 0x5A, 0x3A, 0x59, 0x3B, 0x04, 
        0x5C, 0x4C, 0x2F, 0x3D, 0x26, 0x11, 0x38, 0x2A, 0x17, 0x42, 
        0x30, 0x4E, 0x1B, 0x05, 0x06, 0x49
    ]

    cipher = [
        0x22, 0x70, 0x6A, 0x0C, 0x58, 0x3F, 0x05, 0x08, 0x74, 0x3A, 
        0x53, 0x0C, 0x79, 0x55, 0x77, 0x51, 0x4F, 0x4A, 0x2A, 0x37, 
        0x45, 0x70, 0x5C, 0x52, 0x45, 0x7E, 0x71, 0x61, 0x51, 0x56, 
        0x4F, 0x04, 0x5E, 0x59, 0x69, 0x10, 0x26, 0x50, 0x28, 0x68, 
        0x06, 0x3B, 0x39, 0x30, 0x29, 0x01, 0x69, 0x71, 0x33, 0x41, 
        0x47, 0x70, 0x2A, 0x7E, 0x14, 0x72, 0x1B, 0x5B, 0x42, 0x11, 
        0x7C, 0x51, 0x2B, 0x78, 0x23, 0x68, 0x0C, 0x76, 0x27, 0x05, 
    ]
    ```

## B3: Tìm flag.

- Bài này trước tiên khi tui làm tui nhận ra đó chính là bài này không có cái đoạn `check_flag`, tức với mấy bài ở trên thì `input` sẽ được mã hoá rùi sẽ được check với một dữ liệu nào đó ở chương trình, nhưng bài này thì không, nó sẽ in ra kết quả mã hoá tuỳ thuộc vào `input` của mình nhập vô, không có một đoạn nào là check cả. Vậy nên việc và biết chiều dài `input` là không có, vét cạn cũng chả khả thi.

- Đến lúc này tui nghĩ khả năng cao sẽ dùng `data_X` ở trên có liên quan, có thể là để thay cho input, bởi vì đề bài chỉ thực hiện in ra không có đoạn check nên tui nghĩ khả năng cao là dùng `data_X` thay cho input roài, lúc thay thế `data_X` cho input thì ta được `flag` ạ. Lúc đó tKOui cũng kiểu "ơ ảo nhỉ".

    ```python
    data_X = [
        0x45, 0x32, 0x55, 0x35, 0x14, 0x0F, 0x5D, 0x63, 0x26, 0x76, 
        0x74, 0x06, 0x02, 0x31, 0x05, 0x34, 0x51, 0x77, 0x5C, 0x2C, 
        0x3F, 0x2B, 0x3E, 0x36, 0x28, 0x07, 0x50, 0x7D, 0x40, 0x58, 
        0x24, 0x15, 0x65, 0x79, 0x6F, 0x5A, 0x3A, 0x59, 0x3B, 0x04, 
        0x5C, 0x4C, 0x2F, 0x3D, 0x26, 0x11, 0x38, 0x2A, 0x17, 0x42, 
        0x30, 0x4E, 0x1B, 0x05, 0x06, 0x49
    ]

    cipher = [
        0x22, 0x70, 0x6A, 0x0C, 0x58, 0x3F, 0x05, 0x08, 0x74, 0x3A, 
        0x53, 0x0C, 0x79, 0x55, 0x77, 0x51, 0x4F, 0x4A, 0x2A, 0x37, 
        0x45, 0x70, 0x5C, 0x52, 0x45, 0x7E, 0x71, 0x61, 0x51, 0x56, 
        0x4F, 0x04, 0x5E, 0x59, 0x69, 0x10, 0x26, 0x50, 0x28, 0x68, 
        0x06, 0x3B, 0x39, 0x30, 0x29, 0x01, 0x69, 0x71, 0x33, 0x41, 
        0x47, 0x70, 0x2A, 0x7E, 0x14, 0x72, 0x1B, 0x5B, 0x42, 0x11, 
        0x7C, 0x51, 0x2B, 0x78, 0x23, 0x68, 0x0C, 0x76, 0x27, 0x05, 
    ]   

    input = [
        0x45, 0x32, 0x55, 0x35, 0x14, 0x0F, 0x5D, 0x63, 0x26, 0x76, 
        0x74, 0x06, 0x02, 0x31, 0x05, 0x34, 0x51, 0x77, 0x5C, 0x2C, 
        0x3F, 0x2B, 0x3E, 0x36, 0x28, 0x07, 0x50, 0x7D, 0x40, 0x58, 
        0x24, 0x15, 0x65, 0x79, 0x6F, 0x5A, 0x3A, 0x59, 0x3B, 0x04, 
        0x5C, 0x4C, 0x2F, 0x3D, 0x26, 0x11, 0x38, 0x2A, 0x17, 0x42, 
        0x30, 0x4E, 0x1B, 0x05, 0x06, 0x49
        # 0x74, 0x75, 0x6e, 0x67, 0x64, 0x76, 0x61, 0x6e # tungdvan
    ]   # tungdvan


    #############
    map = []
    for i in range(128): map.append(i)
    tmp = 0
    for i in range(128):
        tmp = (input[i % len(input)] + tmp + map[i]) % 128
        tmp1 = map[tmp]
        map[tmp] = map[i]
        map[i] = tmp1
    #############
    tmp1, tmp2 = 0, 0
    ans = []
    for i in range(len(cipher)):
        tmp1 = (tmp1 + 1) % 128
        tmp2 = (tmp2 + map[tmp1]) % 128
        tmp3 = map[tmp1]
        map[tmp1] = map[tmp2]
        map[tmp2] = tmp3
        ans.append(map[(map[tmp1] + map[tmp2]) % 128] ^ cipher[i])

    # 00CF9598
    ans = [chr(x) for x in ans]
    for i in range(len(ans)): print(ans[i], end = '')
    ```

    ![alt text](IMG/4/image-5.png)

- Flag: `KMA{haycuvotuvalacquanlenemoichilakhongyeuthuongthoisaonuocmatphairoi}`.

# Little_challenge

- Chall: [little_challenge.exe](little_challenge/pack_little_challenge.exe).

## B1: Đọc hiểu.

- Khi ném file này vào DIE thì ta thấy hiện như sau:

    ![alt text](IMG/5/image.png)

    Có một cái dòng nó đỏ đỏ ở đây thông báo cho chúng ta biết là file này đã bị pack, việc của chúng ta là unpack nó nhá (dùng `UPX`).

    Tải `UPX` ở [đây](https://github.com/upx/upx/releases/tag/v4.2.4) và thực hiện unpack file đoá thoai.

    Khi tải file về sẽ dùng như sau:

    ![alt text](IMG/5/image-1.png)

    ![alt text](IMG/5/image-2.png)

    Nếu mà không unpack được file thì chúng ta dùng cmd hoặc powershell (run as administrator) thì sẽ được nhá

    ![alt text](IMG/5/image-3.png)

    Lúc này ta ném vào `DIE` sẽ ko còn dòng chữ đo đỏ nữa:

    ![alt text](IMG/5/image-4.png)

- Ta chạy thử thì thấy chương trình này cần đầu vào:

    ![alt text](IMG/5/image-8.png)

- Quăng vào IDA thì ta thấy đập vào mắt là 2 chương trình với 2 hàm sub, mà click vào mỗi hàm sub thì loạn ko chịu được:

    ![alt text](IMG/5/image-5.png)

    ![alt text](IMG/5/image-6.png)

    ![alt text](IMG/5/image-7.png)

    Có 2 cách để tìm hàm mà thực thi yêu cầu: (1) Tra tìm từ `Wrong secret key!` hoặc tìm hàm sub nào có chuyền argv hoặc một thứ tương tự như argv vào là xong. Sau khi mò ta sẽ được hàm main như sau:

    ![alt text](IMG/5/image-10.png)

    Vậy là bài này sẽ lại là một bài liên quan đến RC4 nữa.

- Tóm lại, đọc xong mã giả thì ta thấy bài trên dựa vào input đề bài cho, thực hiện tạo mảng; thực hiện kiểm tra 3 điều kiện là kiểm tra chiều dài input với `23`, so sánh chuỗi input với `Mai ben nhau ban nhe :)` và một cái hàm sida gì trả về một số `370416652` nữa, nếu vi phạm cả 3 điều kiện trên thì chương trình sẽ thực hiện in `flag` từ `cipher` khai báo ở trên.

## B2: Khai thác.

- Sau khi đọc hiểu xong ở trên thì điều để in ra flag đó chính là chiều dài phải bằng 23 và chuỗi input sẽ là `Mai ben nhau ban nhe :)`. Mía sida ở một chỗ đó chính ta khi chúng ta nhập input là `Mai ben nhau ban nhe :)` thì chương trình không nhận được, cụ thể như sau:

    ![alt text](IMG/5/image-11.png)

    Sau khi tui thử đưa chuỗi trên sang các số thập lục phân rùi tự build lại chương trình thì kết quả flag nhận được cũng chỉ là những byte rác

    `Troll VN`

    Như vậy là bài này đang hướng chúng ta sang một điều khác chứ ko chỉ đơn thuần làm như thế này, chúng ta đã quá ngây thơ roài. Ban đầu khi làm bài này thì đến đây là tui tắc, bí ý tưởng lun roài nhưng mà thực sự bài này là một ý tưởng hoàn toàn khác ở trên đó chính là kĩ thuật đa luồng (`TLS`: Thread Local Storage).

    > Thread-local storage (TLS) là một kỹ thuật trong lập trình đa luồng cho phép các biến được khai báo là local cho mỗi thread. Mỗi thread có một bản sao của các biến này, do đó mỗi thread có thể đọc và ghi các biến này mà không ảnh hưởng đến các thread khác.

    > TLS callback là một hàm được gọi khi một thread được tạo ra hoặc kết thúc. Hàm này có thể được sử dụng để khởi tạo các biến local cho mỗi thread.

    Vậy có những cái dấu hiệu nào để chúng ta có thể biết chương trình của chúng ta đang chạy đa luồng. Trong bài này có 2 cách nhận biết:

    - **Cách 1:** Nhận ra từ hàm `strcmp` trông rất là cồng kềnh:

        ![alt text](IMG/5/image-12.png)

        Như ta biết thì nếu mà hàm `strcmp` thì chỉ cần `strcmp(input, "Mai ben nhau ban nhe :)")` là đủ, mà trong bài này lại còn mấy thứ lâu xâu ở trước đó (đây chỉ là nhận định cá nhân nhưng mà chưa chắc đây là một dấu hiệu nhận biết chuẩn, muốn chuẩn thì sang cách 2).
    
    - **Cách 2:** Trong `IDA` mục function thì ta tìm hàm có tên là `TLS`, nếu có những hàm có `TLS` thì khả năng cao là bài đa luồng.

        ![alt text](IMG/5/image-13.png)

        Vào 2 hàm `TlsCallback_1` và `TlsCallback_0` thực hiện đặt breakpoint xem khi chạy chương trình có nhảy vô 2 hàm đó không. Thật không có điều gì bất ngờ khi 2 hàm này được gọi trước hàm `main`.

- Bây giờ ta ngồi phân tích cái `TlsCallback_1`:

    ![alt text](IMG/5/image-14.png)

    Như vậy trong hàm TlsCallBack_1 này sẽ thực hiện check debugger, nếu ta đang **debug** thì chương trình sẽ nhảy tới và thực hiện khối lệnh bên trong, ta thực hiện set IP để nhảy vào bên trong, chú ý là chúng ta trước khi muốn `set IP` ở bên trong thì chúng ta check là debugger, tức là hàm này gọi ra cố tình cho ta khi biết ta đang debug.

    Sau khi chạy xong dòng thứ 13 `lpAddress = (void *)sub_401180(v3->Ldr->InMemoryOrderModuleList.Flink->Flink[2].Flink, 479434334);` thì ra click vào lpAddress lúc này thì thấy:

    ![alt text](IMG/5/image-15.png)

    ![alt text](IMG/5/image-16.png)

    Tui đoán chắc đây đúng là hàm thực hiện chức năng `strcmp`, nhưng nếu mà chúng ta chạy tiếp xuống dòng bên dưới thì sẽ khác (à thực hiện F9 lại chương trình nhé, tui không hiểu là tại sao nếu chúng ta chạy từng câu lệnh rùi kiểm tra ở mỗi câu lệnh thì chương trình ko định nghĩa lại hàm cho chúng ta còn nếu chúng ta chạy hết câu lệnh rùi check một thể thì hàm đó mới được định nghĩa lại):

    ![alt text](IMG/5/image-17.png)

    ![alt text](IMG/5/image-18.png)

    Lúc này strcmp không còn là hàm check string bình thướng nữa mà nó được định nghĩa lại bằng hàm `sub_4015D0` như này.

- Sau khi làm xong thủ tục ở hàm TlsCallback_1 thì ta thực hiện vô hàm main_ khám phá tiếp, sau khi thực hiện nhảy vào hàm `TlsCallback_1` xong thì khi ở trong hàm main_ thì ta thấy strcmp được định nghĩa lại bằng hàm `sub` ở trên, như vậy nó đã có sự khác biệt trong `B1: Đọc hiểu` của chúng ta và bây giờ chúng ta cần suy nghĩ lại, tức là bh cứ gọi hàm strcmp thì nó sẽ được thay thế bằng hàm sub ở trên chứ không phải là hàm so sánh string thông thường.

    ![alt text](IMG/5/image-19.png)

- Thực ra thì trong hàm main_ có mỗi một chỗ gọi hàm strcmp nên chúng ta cũng chỉ cần quan tâm ở chỗ đoá thoai chứ cũng chả cần phải suy nghĩ lại từ đâu, và nó ở đoạn kiểm tra điều kiện để in ra sai, với những biến truyền vào hàm sub đó là `input` và `Mai ben nhau ban nhe :)`.

    ![alt text](IMG/5/image-20.png)

- Bây giờ chúng ta ngồi phân tích hàm `sub_4015D0` này:

    Nhìn vô dòng thứ 13 `v7 = IsDebuggerPresent() ^ 0xAA;`

    > `IsDebuggerPresent` là một hàm của Windows, nó kiểm tra xem chương trình có đang bị debug hay không. Đây dường như là cách chống debug đơn giản nhất.

    > Điều thú vị xảy ra khi `IsDebuggerPresent` trả về `0` (chương trình không bị debug) và trả về 1 (chương trình đang bị debug).

    Vậy đến lúc này ta nên để là `0` hay là `1` (quá sida để lựa chọn, nếu bí quá thì chạy cả 2 TH xem TH nào ra kết quả đẹp đẹp thì chọn), nhưng nếu mà chúng ta thử logic với cái hàm `TlsCallback_1` ở trên thì đoạn này chúng ta phải để là số 1, bởi vì trước khi muốn nhảy vào những điều kiện của hàm `TlsCallback_1` ta đã bước qua một đoạn check là debugger (và hàm đó check là debugger nên mới check điều kiện tiếp), nên ở đây chúng ta phải giữ nguyên là `1` chứ ko được sửa lại thành `0` (phỏng đoán cá nhân thoai, lúc làm xong roài tui mới có những cái suy nghĩ mang tính chất logic lại toàn bộ bài toán để đúc rút ra kinh nghiệm cho những lần sau chứ lúc làm bài ta tui mò chay ở trên nhá, đó là thử cả 2 TH).

    ![alt text](IMG/5/image-21.png)

    Tui nghĩ đến đây là một bài RC4 quá là quen thuộc roài nên tự làm để tìm ra input để hàm này trả về kết quả là đúng nhé. Source code python tui sẽ để ở đây:

    ```python
    MBNBN = [
        0x4D, 0x61, 0x69, 0x20, 0x62, 0x65, 0x6E, 0x20, 0x6E, 0x68, 
        0x61, 0x75, 0x20, 0x62, 0x61, 0x6E, 0x20, 0x6E, 0x68, 0x65, 
        0x20, 0x3A, 0x29
    ]   # Mai ben nhau ban nhe :)

    buf2 = [
        0xE3, 0x2E, 0xD0, 0xA6, 0xD6, 0x7D, 0x54, 0x3F, 0xAC, 0x0F, 
        0x24, 0x10, 0x9C, 0xCB, 0x26, 0xBC, 0xB3, 0x89, 0x84, 0x24, 
        0x80, 0xBD, 0x48
    ]   # 0019FE78

    def RC4_map(key):  
        map = []
        for i in range(256): map.append(i)
        tmp = 0
        for i in range(256):
            tmp = (key[i % len(key)] + map[i] + tmp) %  256
            map[i], map[tmp] = map[tmp], map[i]
        return map

    def RC4_en(map, data):
        tmp1, tmp2 = 0, 0
        for i in range(len(data)):
            tmp1 = (tmp1 + 1) % 256
            tmp2 = (map[tmp1] + tmp2) % 256
            map[tmp1], map[tmp2] = map[tmp2], map[tmp1]
            data[i]  ^= map[(map[tmp1] + map[tmp2]) % 256]
        return data

    def input_xor(data):
        for i in range(len(data)):
            data[i] ^= 0xAB
        return data

    if __name__ == "__main__":
        map = RC4_map(MBNBN)
        ans = RC4_en(map, buf2)
        ans = input_xor(ans)
        ans = [chr(x) for x in ans]
        for i in range(len(ans)): print(ans[i], end = '')
    ```

- Kết thúc bước 2 tại đây.

## B3: Tìm flag.

- Sau khi xong B2 ta được input chuẩn là `9FPIU6vUxfQOHaisOChDY1F` thì việc tìm flag chỉ là thủ tục. Tui để source code python ở đây:

    ```python
    cipher = [
        0x40, 0x46, 0xCE, 0xA9, 0x8C, 0xC4, 0x6D, 0x80, 0x5F, 0xB1, 
        0xFE, 0x0F, 0xC2, 0x7E, 0xAA, 0x17, 0xC2, 0xF7, 0x34, 0x27, 
        0x62, 0x0A, 0x99, 0xAC, 0x58, 0x30, 0xC1, 0xAC, 0x1D, 0x10, 
        0xED, 0x8A, 0xCE
    ]

    input_chuan = [
        0x39, 0x46, 0x50, 0x49, 0x55, 0x36, 0x76, 0x55, 0x78, 0x66,
        0x51, 0x4f, 0x48, 0x61, 0x69, 0x73, 0x4f, 0x43, 0x68, 0x44,
        0x59, 0x31, 0x46
    ]   # 9FPIU6vUxfQOHaisOChDY1F

    def RC4_map(key):  
        map = []
        for i in range(256): map.append(i)
        tmp = 0
        for i in range(256):
            tmp = (key[i % len(key)] + map[i] + tmp) %  256
            map[i], map[tmp] = map[tmp], map[i]
        return map

    def RC4_en(map, data):
        tmp1, tmp2 = 0, 0
        for i in range(len(data)):
            tmp1 = (tmp1 + 1) % 256
            tmp2 = (map[tmp1] + tmp2) % 256
            map[tmp1], map[tmp2] = map[tmp2], map[tmp1]
            data[i]  ^= map[(map[tmp1] + map[tmp2]) % 256]
        return data

    def input_xor(data):
        for i in range(len(data)):
            data[i] ^= 0xAB
        return data

    if __name__ == "__main__":
        map = RC4_map(input_chuan)
        ans = RC4_en(map, cipher)
        ans = [chr(x) for x in ans]
        for i in range(len(ans)): print(ans[i], end = '')
    ```

    ![alt text](IMG/5/image-22.png)

- Flag: `KMACTF{A_littl3_tricky_chall3ng3}`.

- Sơn ơi Sơn, nếu đchi đọc được dòng này thì đồng chí push file thực thi của challenge `HEA` lên đi nhé. Tui sẽ ngồi thử sức xem sao, kiểu tui đọc qua cái phần đó trên wu của đchi hình như đây là một kiểu mã hoá mới nên tui cũng tò mò, tui muốn thử sức nếu mà bản thân mình không biết kiểu mã hoá đấy thì mình có làm được bài đó không. Cảm ơn đồng chí nhiều nhá (^.^).
