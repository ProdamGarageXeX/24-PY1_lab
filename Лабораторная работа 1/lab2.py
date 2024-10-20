# TODO Найдите количество книг, которое можно разместить на дискете

sizevmb = 1.44
pages = 100
linesonpage = 50
symbvline = 25
bytenasymb = 4
sizevbytes = sizevmb * 1024 * 1024
booksizevbytes = pages * linesonpage * symbvline * bytenasymb
booksnadisk = int(sizevbytes // booksizevbytes)

print("Количество книг, помещающихся на дискету:", booksnadisk)