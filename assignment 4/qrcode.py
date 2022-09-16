import qrcode
code=input("what do you want convert to qrcode: ")
QR=qrcode.make(code)
QR.save('qrcode_result.jpg')