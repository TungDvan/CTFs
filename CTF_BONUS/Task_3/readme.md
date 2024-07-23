# Hidden Treasure.

- Chall: [Hidden Treasure](chall/hiddenTreasure/HiddenTreasure.zip)

- Bài cung cấp cho ta 1 file thực thi và một 1 file ảnh.

## Phần 1: Đọc hiểu.

- Trong bài này thì file thực thi không yêu cầu chúng ta điền gì khi chạy chương trình nên hầu như là chúng ta sẽ phải tự đoán, mọi khi thì một là khi chạy chương trình sẽ nhập sau khi chạy chương trình hoặc là nếu truyền vào file thực thi thì nó sẽ hiện cho ta cú pháp truyền vô nhưng chall này thì không làm điều đó, điều chúng ta cần làm là đoán là chính.

- Đọc mã giả thì tui đoán bài này sẽ có 2 tham số cần truyền vào (do khi làm mấy bài truyền tham số nên tự suy ra thoai cũng không chắc chắn lắm đâu).

    ![alt text](IMG/1/image-1.png)

    Lúc này chắc tui đoán tham số đầu tiên (`argv[1]`) sẽ là `file` rùi tham số tiếp theo (`argv[2]`) sẽ là `key`(Tạo thử một file chạy trên IDA thì đúng là như thế thật).

    Lúc làm chall này tui vừa mò, vừa đoán, vừa thử là chính. 

- Sau tầm 1 ngày `F9` liên tục trong `IDA` tui mới có thể hiểu được cái chương trình này đang làm gì và thực hiện **đặt lại tên biến** cho phù hợp, vì cái mã giả này có nhiều đoạn cứ thừa thừa ko cần thiết, rất chi là cồng kềnh.

    ![alt text](IMG/1/image-3.png)

- **Phần 1**:

    ![alt text](IMG/1/image-5.png)

    Ở phần này, chương trình sẽ thực hiện lưu lại các bit của từng byte trong `key` mà ta truyền vào (nên ban đầu). Ví dụ `key` truyền vào là `1234` thì số `1` tương ứng với `0x31` trong mã `ASCII`, chuyển sang bit là `00110001` tuy nhiên `map` sẽ lưu ngược lại các bit là đó là `1` `0` `0` `0` `1` `1` `0` `0`.

- **Phần 2**:

    ![alt text](IMG/1/image-6.png)

    Lúc này ta đọc lệnh check ta thấy chương trình sẽ check 2 byte `_WORD` đầu tiên của file với `0x4D42`, vậy `0x4D42` là gì, nó là phần header của file ảnh **bmp**, đó chính là 2 kí tự `BM` và check kích thước của file với 4 byte `_DWORD` tiếp theo tính từ byte thứ 2 của file. Nếu ta tự tìm hiểu thì thấy file **bmp** sẽ có 2 byte đầu là kí tự BM rùi 4 byte tiếp theo sẽ là kích thước của file. Đến lúc này dường như chương trình đang ám chỉ là phải truyền vào file ảnh **bmp** kia vì không phải file nào cũng lưu trữ kích thước của file cả.

    Đến đoạn này tui thực hiện vừa nhìn dữ liệu trên thanh ghi trong IDA, vừa quan sát từng byte ảnh (tự lấy dữ liệu nhá), vừa xem mã máy thì có thể tóm tắt cái đoạn sau lệnh if như sau.

    - Ban đầu sẽ thực hiện lấy giá trị byte thứ 10 của file (nó có giá trị là 0x36 = 54).

        ![alt text](IMG/1/image-8.png)

    - Tạo một con trỏ có địa chỉ bắt đầu từ byte thứ 54 ở file trên (mấy cái byte thứ 18, 22 của file tui thấy nó chả ảnh hưởng gì đến chương trình cả, mã giả cứ khai báo rất chi là nhiều biến xong cứ gán đi gán lại mấy giá trị đấy hình như có mục đích làm rối mình hay sao ý).

        ![alt text](IMG/1/image-9.png)

    - Thực hiện lưu lần lượt những giá trị của map tại những vị trí mà con trỏ file bắt đầu ở vị trí thứ 54, với bước nhảy cho mỗi lần là 3. Ví dụ như trên hình thì những vị trí khoanh đỏ sẽ là những vị trí mà lưu các phần tử của `map`. (map là mảng mà lưu từng bit của key).

        ![alt text](IMG/1/image-11.png)
        
        ![alt text](IMG/1/image-10.png)

- Như vậy tóm lại, chương trình sẽ cần 2 tham số truyền vào, tham số đầu tiên là file ảnh, tham số tiếp theo là key. Chương trình sẽ thực hiện lưu key dưới dạng bit rùi lần lượt ghi những giá trị key đó vào trong file ảnh kia tại những vị trí cố định cho trước (cụ thể là từ byte thứ 54 với bước nhảy mỗi vị trí là 3).

## Phần 2: Khai thác.

- Source code đọc từng byte của ảnh:

    ```python
    def read_file():
        source_file = 'inside-the-mind-of-a-hacker-memory.bmp'
        destination_file = 'picture_.txt'

        with open(source_file, 'rb') as src, open(destination_file, 'w', encoding='utf-8') as dest:
            i = 0
            while True:
                i += 1
                byte = src.read(1)
                if not byte:
                    break
                hex_value = format(byte[0], '02x')
                dest.write(f'{i}: {byte}: {hex_value}\n')

    if __name__ == "__main__":
        read_file() 
    ```

- Như phần phân tích ở trên thì chương trình này chỉ đơn giản là ghi lại key chúng ta truyền vào file ảnh (không có mã hoá gì cả) vậy nên điều chúng ta suy nghĩ đến đầu tiên đó chính là key chính là flag và trong file ảnh này đã có flag roài. Điều chúng ta cần là lấy flag từ ảnh đoá ra. 

    Chú ý: file ảnh phải nguyên vẹn. Ban đầu tui nghĩ chương trình này là mã hoá vậy nên tui truyền key bất kì xong bị ghi đè lên vùng chứa flag và mất lun flag.

- Do ta đoán là `flag` sẽ được lưu như thế nên bây giờ ta sẽ thực hiện lấy dữ liệu từ file ảnh từ vị trí byte thứ 54, với bước nhảy là 3, chỉ lấy những byte có kí tự là 0 và 1 (do ta chưa biết được flag sẽ dài bao nhiêu kí tự cả nên sẽ lấy hết).

    ```python
    def read_file():
        source_file = 'inside-the-mind-of-a-hacker-memory.bmp'
        destination_file = 'find_flag.txt'

        with open(source_file, 'rb') as src, open(destination_file, 'w', encoding='utf-8') as dest:
            i = 0
            while True:
                byte = src.read(1)
                if not byte:
                    break
                if i >= 54 and (i - 54) % 3 == 0 and (byte == b'\x00' or byte == b'\x01'):
                    hex_value = format(byte[0], '02x')
                    dest.write(f'{i}: {hex_value}\n')
                i += 1

    if __name__ == "__main__":
        read_file() 
    ```

    Sau khi lọc xong thì ta thấy có tận `14934` byte thoả mãn điều kiện, chã nhẽ flag lại dài như thế.

    ![alt text](IMG/1/image-12.png)

    Nhưng khi ta thực hiện xem qua file thì ta sẽ thấy được vùng mà lưu flag đã kết thúc (byte 771), như ảnh bên dưới:

    ![alt text](IMG/1/image-13.png)

    Như vậy lúc này ta chỉ lấy từ byte thứ 54 đến byte thứ 771 thôi, còn từ byte 2868 thoả mãn thì ta bỏ qua. Thực hiện tính toán lại thì thấy rất là hợp lý (771 - 54) / 3 = 239. Tức là có 240 bit được lưu, tương đương với 30 byte, chiều dài flag là 30 nghe cũng thấy hợp lý đó.

## Phần 3: Tìm flag.

- Sau khi phân tích như trên roài thì tìm flag chỉ là thủ tục thoai:

    ```python
    def read_file():
        source_file = 'inside-the-mind-of-a-hacker-memory.bmp'
        ans = []
        with open(source_file, 'rb') as src:
            i = 0
            while True:
                byte = src.read(1)
                if not byte:
                    break
                if i >= 54 and (i - 54) % 3 == 0 and (byte == b'\x00' or byte == b'\x01') and i <= 771:
                    hex_value = format(byte[0], '01x')
                    ans.append(hex_value)
                i += 1
        return ans

    def _bit(map, pos):
        ans = []
        for i in range(pos, pos + 8):
            ans.append(map[i])
        ans = ans[::-1]
        return ans

    if __name__ == "__main__":
        flag = read_file()
        for i in range(0, len(flag), 8):
            ans = _bit(flag, i)
            binary = ''.join(map(str, ans))
            value = int(binary, 2)
            chr = chr(value)
            print(chr, end = '')
    ```

- Chú ý:

    1. File ảnh bmp phải là file ảnh ban đầu.

    2. Do mảng map lưu ngược nên khi mà ta lấy dữ liệu ta phải đảo lại toàn bộ 8 bit trong 1 byte.

    ![alt text](IMG/1/image-14.png)

- Flag: `flag{dont_forget_the_treasure}`.
