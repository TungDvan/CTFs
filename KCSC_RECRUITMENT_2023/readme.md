# Dynamic Function

- Chall: [file RAR](Dynamic_Function_DONE/rev_dynamic_function.rar)

- Đọc qua mã giả của bài này thì thấy như sau:

    ![alt text](IMG/1/image.png)

    Chương trình thực hiện check chiều dài của chuỗi với `30` xong rùi thực hiện tách `KCSC{` và `}` ra rùi thực hiện check chiều dài của nội dung của nó với `24`.

- Ở phần tiếp theo, chương trình cấp phát một vùng nhớ ảo cho biến `lpAddress`, sau đó `xor` từng byte với `0x41`. Lúc này `lpAddress` đã trở thành `1 hàm` và sau đó chương trình gọi đến hàm này (chắc có lẽ vì đây là bài có tên là **Dynamic Function**).

    ![alt text](IMG/1/image-1.png)

- Đến đây là thực hiện nhảy vô hàm lpAddress xem nội dụng của hàm là gì:

    ![alt text](IMG/1/image-2.png)

    Đến lúc này ta nhấn chuột phải chọn `Create Function` hoặc bôi đen nhấn `P`:

    ![alt text](IMG/1/image-3.png)

    Ta thấy chương trình sẽ thực hiện mã hoá flag bằng hàm lpaddress roài thực hiện so sánh với `flag_en`, như sau:

    ![alt text](IMG/1/image-4.png)

    ![alt text](IMG/1/image-5.png)

- Tui thấy mấu chốt bài này đó chính là chúng ta biết lpAddress là một hàm và biết cách để đọc nội dung hàm đó thoai chứ về phần mã hoá input thì khá dễ dàng, các bạn có thể tham khảo source python.

    ```python
    flag_en = [
        0x44, 0x93, 0x51, 0x42, 0x24, 0x45, 0x2E, 0x9B, 0x01, 0x99, 
        0x7F, 0x05, 0x4D, 0x47, 0x25, 0x43, 0xA2, 0xE2, 0x3E, 0xAA, 
        0x85, 0x99, 0x18, 0x7E
    ]

    RIPC = [
        0x72, 0x65, 0x76, 0x65, 0x72, 0x73, 0x69, 0x6E, 0x67, 0x5F, 
        0x69, 0x73, 0x5F, 0x70, 0x72, 0x65, 0x74, 0x74, 0x79, 0x5F, 
        0x63, 0x6F, 0x6F, 0x6C
    ]   # reversing_is_pretty_cool

    for i in range(len(flag_en)): flag_en[i] ^= RIPC[i]
    for i in range(len(flag_en)):
        for j in range(256):
            if flag_en[i] == 16 * (j % 16) + j // 16: print(chr(j), end = '')
    ```

- Flag: `KCSC{correct_flag!submit_now!}`.