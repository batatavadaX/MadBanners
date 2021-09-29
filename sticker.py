from PIL import Image


def stick_logo():
    base = Image.open('banner/base.jpg').convert("RGBA")
    logo = Image.open('banner/transparent_logo.png').convert("RGBA")
    base.paste(logo, (920,190), logo)
    base.save("banner/banner.png")
