import os
from PIL import Image, ImageEnhance
i=0
directory = os.chdir('PATH')
for file in os.listdir(directory):
    if file  != '.DS_Store':
        i=+1
        filename = str(file)
        im = Image.open(filename)
        enhancer = ImageEnhance.Brightness(im)
        enhanced_im = enhancer.enhance(0.5)
        enhanced_im.save('PATH'+'darkened'+str(i)+'.jpg')
        print(filename+ " darkening complete")
