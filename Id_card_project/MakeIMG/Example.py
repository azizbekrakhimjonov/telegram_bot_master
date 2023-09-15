# from PIL import Image, ImageDraw
# img1 = Image.open(r'pic1.png')
# img2 = Image.open("user.png")
# img2 = img2.resize((320, 370))
#
# hexagon_size = (310, 370)
# mask_im = Image.new("L", img2.size, 0)
# draw = ImageDraw.Draw(mask_im)
# draw.polygon([(hexagon_size[0] // 2, 0), (hexagon_size[0], hexagon_size[1] // 4),
#               (hexagon_size[0], 3 * hexagon_size[1] // 4), (hexagon_size[0] // 2, hexagon_size[1]),
#               (0, 3 * hexagon_size[1] // 4), (0, hexagon_size[1] // 4)], fill=255)
#
# kichik_rasim = Image.composite(img2, Image.new("RGBA", img2.size), mask_im)
# back_im = img1.copy()
# # back_im.paste(img2, (163, 160), mask_im)
# # back_im.show()
# back_im.paste(kichik_rasim, (163, 160), mask_im)
# back_im.show()






# from PIL import Image, ImageFont, ImageDraw
# i=Image.open('lena.png')
# Im = ImageDraw.Draw(i)
# mf = ImageFont.truetype('font.ttf', 25)
# Im.text(
#     (600, 500),
#     "Marilyn Monroe",fill=(255, 0, 0),
#     font=mf)
# i.save("mm.png")


# from PIL import Image, ImageFont, ImageDraw
# # creating a image object
# image = Image.open(r'pic1.jpg')
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype(r'arial.ttf', 70)
# text = 'Testing'
# draw.text((250, 200), text, font=font, anchor='la')
# # image.save('s.png')
# image.show()


# from PIL import Image
# img1 = Image.open(r"pic2.jpg")
# img2 = Image.open(r"qr.jpg")
# img2 = img2.resize((136, 136))
# img1.paste(img2, (242, 820))
# img1.show()
# img1.save('pic3.jpg', quality=100)


# from PIL import Image, ImageDraw, ImageFilter
# im1 = Image.open('rocket.png')
# im2 = Image.open('lena.png')
# back_im = im1.copy()
# back_im.paste(im2, (100, 50))
# mask_im = Image.new("L", im2.size, 0)
# draw = ImageDraw.Draw(mask_im)
# draw.ellipse((140, 50, 260, 170), fill=255)
# back_im = im1.copy()
# back_im.paste(im2, (0, 0), mask_im)
# back_im.show()





# from PIL import Image
# def crop_center(pil_img, crop_width, crop_height):
#     img_width, img_height = pil_img.size
#     return pil_img.crop(((img_width - crop_width) // 2,
#                          (img_height - crop_height) // 2,
#                          (img_width + crop_width) // 2,
#                          (img_height + crop_height) // 2))
#
#
# img = Image.open('user.png')
# img = img.resize((400, 500))
# img.save('user_3.png')
