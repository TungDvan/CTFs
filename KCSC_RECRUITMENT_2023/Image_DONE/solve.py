a = [-1] * 51

for i in range(51):
    num1, num2 = map(int, input().split())
    a[num1] = num2

for i in range(len(a)): print(chr(a[i]), end = '')

# KCSC{Cam_on_vi_da_kien_nhan_nhin_het_dong_anh_nay`}