# CTF_ForFun là những bài RE rời rạc của các giải mà ý tưởng của nó không phải là RE cho lắm, làm cho vui thoai.

## 1_BRAIN_n00bzCTF

- Chall: [FILE](CHALL/1_BRAIN.rar).

- Bài này cho ta mỗi một file `bf.txt`, nội dung của file được biết theo kiểu `BrainF*ck`, sau khi tham khảo về cách nó hoạt động tại [đây](https://www.youtube.com/watch?v=cwuPIugCHl4) thì tui tiến hành chạy chay thử thì thấy sau mỗi vòng lặp nó sẽ trả về một giá trị rùi xóa giá trị đóa đi, tui đoán đây là giá trị của mã ASCII và làm thử thì có vẻ như là đúng. Giải bài thoai:

    ```python
    bf_str = ">+++++++++++[<++++++++++>-]<[-]>++++++++[<++++++>-]<[-]>++++++++[<++++++>-]<[-]>++++++++++++++[<+++++++>-]<[-]>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<++>-]<[-]>+++++++++++++++++++++++++++++++++++++++++[<+++>-]<[-]>+++++++[<+++++++>-]<[-]>+++++++++++++++++++[<+++++>-]<[-]>+++++++++++[<+++++++++>-]<[-]>+++++++++++++[<++++>-]<[-]>+++++++++++[<++++++++++>-]<[-]>+++++++++++++++++++[<+++++>-]<[-]>+++++++++++[<+++++++++>-]<[-]>++++++++[<++++++>-]<[-]>++++++++++[<++++++++++>-]<[-]>+++++++++++++++++[<+++>-]<[-]>+++++++++++++++++++[<+++++>-]<[-]>+++++++[<+++++++>-]<[-]>+++++++++++[<++++++++++>-]<[-]>+++++++++++++++++++[<+++++>-]<[-]>++++++++++++++[<+++++++>-]<[-]>+++++++++++++++++++[<++++++>-]<[-]>+++++++++++++[<++++>-]<[-]>+++++++[<+++++++>-]<[-]>+++++++++++[<++++++++++>-]<[-]>+++++++++++++++++[<++++++>-]<[-]>+++++++[<++++++>-]<[-]>+++++++++++[<+++++++++>-]<[-]>+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++[<+>-]<[-]>+++++++++++[<+++>-]<[-]>+++++++++++++++++++++++++[<+++++>-]<[-]"

    ans = []
    tmp_1 = [1, 0]
    tmp_2 = [0, 0]

    for i in range(len(bf_str)):
        if bf_str[i] == "+":
            if tmp_1[0] == 1: tmp_1[1] += 1
            else: tmp_2[1] += 1
        if bf_str[i] == '[':
            ans.append(tmp_1[1])
            tmp_1[0], tmp_1[1] = 0, 0
            tmp_2[0] = 1
        if bf_str[i] == ']':
            ans.append(tmp_2[1])
            tmp_2[0], tmp_2[1] = 0, 0
            tmp_1[0] = 1

    ans = [x for x in ans if x != 0]

    for i in range(0, len(ans), 2):
        print(chr(ans[i] * ans[i + 1]), end = '')
    ```

- Flag: `n00bz{1_c4n_c0d3_1n_br41nf*ck!}`.


## 2_BRAIN_n00bzCTF

- Chall: [FILE](CHALL/2_VACATION.rar).

- Bài này cho chúng ta 2 file, 1 file là file `output.txt` còn một file là `run.ps1` (file **.ps1** là một tệp script của Windows PowerShell). Chúng ta chuyển qua file txt và đọc được nội dung của tệp đóa như sau:

    ```python
    $bytes = [System.Text.Encoding]::ASCII.GetBytes((cat .\flag.txt))
    [System.Collections.Generic.List[byte]]$newBytes = @()
    $bytes.ForEach({
        $newBytes.Add($_ -bxor 3)
        })
    $newString =  [System.Text.Encoding]::ASCII.GetString($newBytes)
    echo $newString | Out-File -Encoding ascii .\output.txt
    ```

- Tóm lại là sẽ lấy dữ liệu trong file `input.txt` rùi xor với `3` xong lưu vào file `output.txt`.

    ```python
    flag_en = [
        0x6d, 0x33, 0x33, 0x61, 0x79, 0x78, 0x65, 0x71, 0x6c, 0x6e, 
        0x5c, 0x73, 0x62, 0x71, 0x6a, 0x70, 0x5c, 0x74, 0x77, 0x6b, 
        0x5c, 0x7b, 0x6c, 0x71, 0x7e
    ]   # m33ayxeqln\sbqjp\twk\{lq~

    for i in range(len(flag_en)): print(chr(3 ^ flag_en[i]), end = '')
    ```

- Flag: `n00bz{from_paris_wth_xor}`.