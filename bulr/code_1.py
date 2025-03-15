from PIL import Image  


im = Image.open('images/terrifying.png')   #You'r image location
image_size = im.size        # width , height
pixels = list( im.getdata())
width = image_size[0]
height = image_size[1]
lst_new = []


for i in range(0,width * height,16):
    p_16 = pixels [i:i+16]
    g_r = 0
    g_g = 0
    g_b = 0

    # print(p_16)
    for p in p_16 :     ####avg of 16  pixels
        g_r = g_r + p[0]
        g_g = g_g + p[1]
        g_b = g_b + p[2]
    avg_16 = (g_r // 16, g_g // 16, g_b //16)       #(6,7,4)
    for j in range(16):
        lst_new.append 
        lst_new.append(avg_16)

new_im = Image.new(size=image_size, mode='RGB' , color=(0,0,0) )
new_im.putdata(lst_new)
im.show()
new_im.show()
# new_im.save('my_bin_2.png')      # new_im.show()