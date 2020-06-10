from PIL import Image
mona_list = [132, 128, 126, 123, 137, 129, 130, 145, 158,
170, 172, 161, 153, 158, 162, 172, 159, 152, 139, 136,
127, 125, 129, 134, 143, 147, 150, 146, 157, 157, 158,
166, 171, 163, 154, 144, 144, 135, 125, 119, 124, 135,
121, 62, 29, 16, 20, 47, 89, 151, 162, 158, 152, 137,
146, 132, 125, 125, 132, 89, 17, 19, 11, 8, 6, 9, 17,
38, 134, 164, 155, 143, 142, 130, 124, 130, 119, 15,
46, 82, 54, 25, 6, 6, 11, 17, 33, 155, 173, 156, 134,
132, 138, 148, 47, 92, 208, 227, 181, 111, 33, 9, 6,
14, 16, 70, 180, 178, 151, 139, 158, 117, 22, 162, 242,
248, 225, 153, 62, 19, 8, 8, 11, 13, 159, 152, 153, 135,
157, 46, 39, 174, 207, 210, 205, 136, 89, 52, 17, 7, 6,
6, 70, 108, 167, 168, 128, 17, 63, 169, 196, 211, 168,
137, 121, 88, 21, 9, 7, 5, 34, 57, 166, 170, 93, 16, 34,
63, 77, 140, 28, 48, 31, 25, 17, 10, 9, 8, 22, 36, 136,
111, 83, 15, 48, 69, 57, 124, 55, 86, 52, 112, 34, 11,
9, 6, 15, 30, 49, 39, 46, 11, 83, 174, 150, 128, 103,
199, 194, 108, 23, 12, 12, 10, 14, 34, 26, 24, 18, 14,
53, 175, 153, 134, 98, 172, 146, 59, 13, 14, 13, 12, 12,
46, 21, 16, 11, 14, 21, 110, 126, 47, 62, 142, 85, 33,
10, 13, 13, 11, 11, 15, 17, 14, 10, 11, 11, 69, 102, 42,
39, 74, 71, 28, 9, 13, 12, 12, 11, 18, 18, 19, 11, 12,
8, 43, 126, 69, 49, 77, 46, 17, 7, 14, 12, 11, 12, 19,
24, 30, 17, 11, 12, 6, 73, 165, 79, 37, 15, 12, 10, 12,
13, 10, 10, 16, 24, 40, 18, 9, 9, 2, 2, 23, 16, 10, 9,
10, 10, 11, 9, 8, 6, 10, 43, 40, 25, 6, 10, 2, 0, 6, 20,
8, 10, 16, 18, 10, 4, 3, 5, 7, 39, 34, 23, 5, 7, 3, 2,
6, 77, 39, 25, 31, 36, 11, 2, 2, 5, 2, 17, 16, 9, 4, 6,
5, 6, 36, 85, 82, 68, 75, 72, 27, 5, 7, 8, 0, 4, 8, 5,
6, 8, 15, 65, 127, 135, 108, 120, 131, 101, 47, 6, 11,
7, 4, 2, 9, 6, 6, 7, 74, 144, 170, 175, 149, 162, 153,
110, 48, 11, 12, 3, 5, 11, 9, 3, 7, 21, 127, 176, 190,
169, 166, 182, 158, 118, 44, 10, 11, 2, 5, 8, 0, 5, 23,
63, 162, 185, 191, 186, 181, 188, 156, 117, 38, 11, 12,
25, 33, 3, 5, 6, 64, 147, 182, 173, 190, 221, 212, 205,
181, 110, 33, 19, 42, 57, 50, 5, 3, 7, 45, 160, 190, 149,
200, 253, 255, 239, 210, 115, 46, 30, 25, 9, 5, 9, 4, 10,
16, 24, 63, 93, 187, 223, 237, 209, 124, 36, 17, 4, 3, 2,
1, 7, 8, 13, 8, 9, 12, 17, 19, 26, 41, 42, 24, 11, 5, 0,
1, 7, 4]
monaLisaIm = Image.new('L', (18,29))
width, height = monaLisaIm.size
i=0
for y in range(height):
	for x in range(width):
		monaLisaIm.putpixel((x,y),mona_list[i])
		i=i+1
	
monaLisaIm.save("monalisa.jpg")
monaLisaIm.show()