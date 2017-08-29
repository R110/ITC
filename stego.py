from PIL import Image

def fib():
    a, b = 0, 1
    while 1:
        yield a
        a, b = b, a + b

def getBit(input, index):
    value = input & (1 << index)
    if value > 0:
        return "1"
    else:
        return "0"

def DecodeMessage():
    img = Image.open("input.bmp")
    width, height = img.size

    hiddenBitsOrder = fib()

    message = ""
    currentByte = ""
    messageLength = 0
    
    for row in range(height):
        for col in range(width):
            bitIndex = next(hiddenBitsOrder) % 8
            pixel = img.getpixel((col, row))
            for byte in pixel:
                bit = getBit(byte, bitIndex)
                currentByte += bit
                if len(currentByte) == 8:
                    nextChar = chr(int(currentByte, 2))
                    currentByte = ""
                    if messageLength == 0 and nextChar == ':':
                        messageLength = int(message)
                        message = ""
                        nextChar = ""
                    message += nextChar
                    if len(message) == messageLength:
                        return message

message = DecodeMessage()
print(message)
