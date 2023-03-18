import colorgram

colors_list = colorgram.extract('hirst_painting_image.jpeg', 20)
color_palette = []

for count in colors_list:
    r = count.rgb.r
    g = count.rgb.g
    b = count.rgb.b
    color = (r,g,b)
    color_palette.append(color)

print(f"color_palette : {color_palette}")
