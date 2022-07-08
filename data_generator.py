from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import os

"""
PIL 최신버전(현재기준 0.9.2) 사용 필수
낮은 버전의 PIL Package를 사용할 경우  PIL.ImageDraw.text 모듈에서 anchor 파라메터가 인식 되지 않아 글자가 잘림
"""

# 모든 한글 
#for font_file in os.listdir("./fonts"):
#    for i in range(44032, 55204):
#        letter = chr(i)
#        img = Image.new("RGB", (48,48), color=(255,255,255))
#
#        draw = ImageDraw.Draw(img) 
#        # font = ImageFont.truetype(<font-file>, <font-size>)
#        font = ImageFont.truetype(f"./fonts/{font_file}", 46)
#        # draw.text((x, y),"Sample Text",(r,g,b))
#        draw.text((1, 1),letter,(0,0,0),font=font)
#        # make directory if not exsist    
#        path = f"./data/{font_file[:-4]}"
#        if not os.path.isdir(path):
#              os.mkdir(path)
#        img.save(f'{path}/{letter}.jpg')

# 상용한글 2350자

## 컬러 jpg파일로 생성
# with open("./상용한글2350자.txt", "r") as f:
#     lst = list(f.read())

# for font_file in os.listdir("./fonts"):

#     for letter in lst:
#         img = Image.new("RGB", (48,48), color=(255,255,255))

#         draw = ImageDraw.Draw(img) 
#         # font = ImageFont.truetype(<font-file>, <font-size>)
#         font = ImageFont.truetype(f"./fonts/{font_file}", 44)
#         # draw.text((x, y),"Sample Text",(r,g,b))
#         draw.text((24, 24),letter,(0,0,0),anchor="mm", font=font)
#         # make directory if not exsist    
#         path = f"./data/{font_file[:-4]}"
#         if not os.path.isdir(path):
#             os.mkdir(path)
        
#         img.save(f'{path}/{letter}.jpg')


## 흑백 jpg파일로 생성
with open("./상용한글2350자.txt", "r") as f:
    lst = list(f.read())

for font_file in os.listdir("./fonts"):

    for letter in lst:
        img = Image.new("L", (48,48), color=255)

        draw = ImageDraw.Draw(img) 
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype(f"./fonts/{font_file}", 44)
        # draw.text((x, y),"Sample Text",(r,g,b))
        draw.text((24, 24),letter,0,anchor="mm", font=font)
        # img.convert("L")
        # make directory if not exsist    
        path = f"./data/{font_file[:-4]}"
        if not os.path.isdir(path):
            os.mkdir(path)
        
        img.save(f'{path}/{letter}.jpg')


