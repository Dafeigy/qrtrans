import qrcode
qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=0,
)

data = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
""".split()
import time
import os
c, l = os.get_terminal_size()
print(c)
i = 0 

while True:

    each = data[i]
    print("\033[H\033[J")
    qr.add_data(each)
    qr_matrix = qr.get_matrix()
    matrix = [["██" if each else "  " for each in rows] for rows in qr_matrix]
    for row in matrix:
        print("".join(row).center(c))
    qr.clear()
    time.sleep(0.06)
    print('\r',end = '')
    i = (i + 1) % len(data)