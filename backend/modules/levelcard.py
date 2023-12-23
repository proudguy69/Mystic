from PIL import Image, ImageDraw, ImageFont

image = Image.new("RGBA", (400,200), (244, 243, 252,128))


font = ImageFont.truetype("calibri.ttf",size=24)
pfp = Image.open("ardens.png")
text = ImageDraw.Draw(image, "RGBA")
text.text((158,20),"Ardens\nLevel: 1\nxp:50/100", font=font,)


image.paste(pfp, (20,20))



image.show()