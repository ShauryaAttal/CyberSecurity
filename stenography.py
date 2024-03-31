from PIL import Image

def getData(data):
    newd = []
    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd

def modifyPixel(newimg,data):
    datalist = getData(data)
    lendata = len(datalist)
    imdata = iter(newimg)
    
    print("Check imdata....")
    print(imdata)

    for i in range(lendata):
        newimg = [value for value in imdata.__next__()[:3] + imdata.__next__()[:3] + imdata.__next__()[:3]]

        for j in range (0,8):
            if (datalist[i][j] == '0' and newimg[j]%2 != 0):
                newimg[j]-=1
            elif (datalist[i][j] == '1' and newimg[j]%2 == 0):
                if (newimg[j]!=0):
                    newimg-=1
                else:
                    newimg[j]+=1
        if (i == lendata - 1):
            if (newimg[-1]%2 ==0):
                if(newimg[-1] !=0):
                    newimg[-1] -=1
                else:
                    newimg[-1] +=1
        else:
            if (newimg[-1]%2 !=0):
                newimg[-1] -=1
        
        newimg= tuple(newimg)
        yield newimg[0:3]
        yield newimg[3:6]
        yield newimg[6:9]

def encode_enc(newimg,data):
    size = newimg.size[0]
    print("Size: ",size)

    (x,y) = (0,0)
    for pixel in modifyPixel(newimg.getdata(), data):
        newimg.putpixel((x,y), pixel)
        if (x == size-1):
            x=0
            y+=1
        else:
            x+=1

def encode():
    img = input("Enter the image file path: ")
    img = Image.open(img, 'r')
    data = input("What data would you like to hide? ")
    if len(data) == 0:
        raise Exception("There is no data entered!")
    newimg = img.copy()
    encode_enc(newimg,data)

    new_img_name = input("Enter the name of new image(with extension) : ")
    newimg.save(new_img_name, str(new_img_name.split(".")[1].upper()))

    main()

def decode():
    img = input("Enter image name(with extension) : ") 
    image = Image.open(img, 'r') 
    data = '' 
    imgdata = iter(image.getdata()) 
    while (True): 
        pixels = [value for value in imgdata.__next__()[:3] + imgdata.__next__()[:3] + imgdata.__next__()[:3]] # string of binary data 
        binstr = '' 
        for i in pixels[:8]: 
            if (i % 2 == 0): 
                binstr += '0' 
            else: 
                binstr += '1' 
        data += chr(int(binstr, 2)) 
        if (pixels[-1] % 2 != 0): 
            return data


def main():
    a = int(input("Welcome to stenography ::\n" "1. Encode\n2. Decode\n"))
    if a==1:
        encode()
    elif a==2:
        print("Decoded word: ",decode())
    else:
        raise Exception("Enter connect input..")


if __name__ == "__main__":
    main()