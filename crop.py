from PIL import Image, ImageDraw, ImageOps


def crop_logo():
    size = (350,350)
    mask = Image.new('L', size, 0)
    draw = ImageDraw.Draw(mask) 
    draw.ellipse((0, 0) + size, fill=255)
    main=Image.open('banner/logo.png').resize((350,350))
    output = ImageOps.fit(main, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    output.save('banner/transparent_logo.png', format="png")
