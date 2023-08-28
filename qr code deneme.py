import qrcode

code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 100,     #boyut
    border = 4          #kenar kalınlığı
)

code.add_data("HELLO")
code.make(fit=True)

image = code.make_image(fill_color=(0,0,0),back_color="white")
image.save("QR.png")