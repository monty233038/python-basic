decimal_num = int(input('enter a decimal no'))
hex_list = {10: 'A',
            11: 'B',
            12: 'C',
            13: 'D',
            14: 'E',
            15: 'F'
}
remainder_dec = []
remainder_hex = []
remainder = 10                  # decimal 256
while decimal_num >= 1:
    if decimal_num < 16:
        remainder_dec.append(decimal_num)
        decimal_num -= decimal_num
    else:
        remainder = decimal_num%16
        decimal_num = int(decimal_num/16)
        remainder_dec.append(remainder)
for i in remainder_dec:
    if i>=10 and i<=15:
        for j in hex_list.keys():
            if i == j:
                remainder_hex.append(hex_list[j])
    else:
        remainder_hex.append(str(i))
remainder_hex.reverse()
for i in remainder_hex:
    print(i, end="")



