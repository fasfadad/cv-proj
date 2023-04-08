from PIL import Image,ImageDraw,ImageFont

image=Image.open("hotel.jpg")
draw=ImageDraw.Draw(image)
font1=ImageFont.truetype("arial.ttf",100)
points=100,30
string="Looking for a hotel?"
color="black"

draw.text(points,string,color,font=font1)
image.show()