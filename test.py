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
i = 0 

while True:

    each = data[i]
    print("\033[H\033[J")
    print("\n" * 5)
    qr.add_data(each)
    qr_matrix = qr.get_matrix()
    matrix = [["██" if each else "  " for each in rows] for rows in qr_matrix]
    for row in matrix:
        print(" "*20 + "".join(row))
    qr.clear()
    time.sleep(0.3)
    i = (i + 1) % len(data)