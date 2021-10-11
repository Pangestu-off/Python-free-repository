from PIL import Image

mi = Image.open("foto.jpg")

print("format berkas: " + im.format)
print("ukuran berkas: " + str(im.size))
print("mode berkas: " + im.mode)

im.show()
