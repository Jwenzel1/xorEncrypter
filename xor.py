from bbsRNG import bbsRNG
bitmask = 0xff

def getNextKey(random):
    return (random.nextInt() & bitmask)

def Crypt(data, datalength, initialValue):
    r = bbsRNG(initialValue)
    encodedValue = []
    returnValue = ''
    for byte in bytearray(data, "ascii"):
        encodedValue.append(byte ^ getNextKey(r))
    for b in encodedValue:
        returnValue += chr(b)
        #returnValue += "\\" + str(hex(b))[1:4]
    return returnValue

def main():
    someData = "apple"
    seed = 0x12345678
    print (Crypt(someData, len(someData), seed))

main()
