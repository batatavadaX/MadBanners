from PIL import Image, ImageDraw, ImageFont


def write_text():
    image=Image.open('banner/banner.png')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('fonts/Oswald-VariableFont_wght.ttf', size=45)
    m = open("banner/winners.txt", "r")
    k = m.readlines()
 
    #1
    (x, y) = (210,270)
    m = k[1]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)

    #2
    (x, y) = (210,340)
    m = k[2]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)

    #3
    (x, y) = (210,410)
    m = k[3]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)

    #4
    (x, y) = (210,480)
    m = k[4]
    color = 'rgb(255,255,255)'
    draw.text((x, y), m, fill=color, font=font)

    #5
    (x, y) = (210,550)
    m = k[5]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)

    #6
    (x, y) = (575,275)
    m = k[6]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)

    #7
    (x, y) = (575,340)
    m = k[7]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)

    #8
    (x, y) = (575,410)
    m = k[8]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)

    #9
    (x, y) = (575,480)
    m = k[9]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)

    #10
    (x, y) = (575,550)
    m = k[10]
    color = 'rgb(255, 255, 255)'
    draw.text((x, y), m, fill=color, font=font)
    image.save('banner/banner.png')
    
