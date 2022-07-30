from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import textwrap


class imageCreator():
    def __init__(self, CHOSEN, CHOICE):
        self.CHOSEN = CHOSEN
        self.CHOICE = CHOICE
        self.create()
    
    def shadow_box(self,w, h, draw):
        shape = [352+(w/2), 217-(h/2), 338-(w/2), 230+(h/2)]  # Specifies Bottom Left and Top Right Coordinates for Box (with some padding)
        draw.rectangle(shape, fill=(0, 0, 0, 70))

    def create(self):
        if len(self.CHOSEN) <= 180:  # Font size determined by char length
            size = 26
        else:
            size = 24

        self.CHOSEN = textwrap.fill(text=self.CHOSEN, width=55)  # Wraps Text
        width = 690  
        height = 447 
        message = f"{self.CHOSEN}"
        font = ImageFont.truetype("Courgette-Regular.ttf", size=size)
        bgIMG = Image.open(f"Silmarillion/{self.CHOICE}/{self.CHOICE}.jpg")

        imgDraw = ImageDraw.Draw(bgIMG, "RGBA")
        textWidth, textHeight = imgDraw.textsize(message, font=font)
        self.shadow_box(textWidth, textHeight, imgDraw)
        xText = (width - textWidth) / 2
        yText = (height - textHeight) / 2
        imgDraw.text((xText, yText), message, font=font, fill=(255, 255, 255))

        bgIMG.save('result.png')
