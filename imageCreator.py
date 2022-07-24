from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import textwrap


class imageCreator():
    def __init__(self, CHOSEN, CHOICE):
        self.CHOSEN = CHOSEN
        self.CHOICE = CHOICE
        self.create()

    def create(self):
        if len(self.CHOSEN) <= 180:
            size = 25
        else:
            size = 23


        self.CHOSEN = textwrap.fill(text=self.CHOSEN, width=50)  # Wraps Text
        width = 690
        height = 447
        message = f"{self.CHOSEN}"

        font = ImageFont.truetype("Courgette-Regular.ttf", size=size)
        bgIMG = Image.open(f"Silmarillion/{self.CHOICE}/{self.CHOICE}.jpg")

        if self.CHOICE != "Chap 7": # Use Black Text instead of White
            shadow = ImageDraw.Draw(bgIMG)
            textWidth, textHeight = shadow.textsize(message, font=font)
            xShad = ((width - textWidth)/2) - 1
            yShad = ((height - textHeight)/2) + 1
            shadow.text((xShad, yShad), message, font=font, fill=(0, 0, 0, 128))

            imgDraw = ImageDraw.Draw(bgIMG)
            textWidth, textHeight = imgDraw.textsize(message, font=font)
            xText = (width - textWidth) / 2
            yText = (height - textHeight) / 2
            imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 255))

            bgIMG.save('result.png')

        else:
            imgDraw = ImageDraw.Draw(bgIMG)
            textWidth, textHeight = imgDraw.textsize(message, font=font)
            xText = (width - textWidth) / 2
            yText = (height - textHeight) / 2
            imgDraw.text((xText, yText), message, font=font, fill=(0, 0, 0))

            bgIMG.save('result.png')
