from PIL import Image
square_length = 1272/8;#159
im = Image.open("chessboard_precise.jpg");
pix = im.load();

ranger = 4;
x_base = 0;
y_base = 0;
stringer = '';
brown_counter = 0;
black_counter = 0;
#for each square
for i in range(1,65):
    for x in range(0,156):
        for y in range(0,156):
            dummy = pix[x + x_base, y + y_base]
            if dummy[0] < 189+ranger and dummy[0] > 189-ranger and dummy[1] < 131+ranger and dummy[1] > 131-ranger and dummy[2] < 83+ranger and dummy[2] > 83-ranger:
                brown_counter = brown_counter + 1;
            elif dummy[0] < 71+ranger and dummy[0] > 71-ranger and dummy[1] < 65+ranger and dummy[1] > 65-ranger and dummy[2] < 65+ranger and dummy[2] > 65-ranger:
                black_counter = black_counter + 1;
    #brown
    if brown_counter > 12:
        #print('W')
        stringer += 'W';
    #black
    elif black_counter > 12:
        stringer += 'B';
    #space
    else:
        stringer += 'S';

    #reset counters
    brown_counter = 0;
    black_counter = 0;

    #choose whether to icrement x, or increment y and reset x
    if(i % 8 == 0):
        y_base = y_base + 159;
        x_base = 0;
        print(stringer);
        stringer = '';
    else:
        x_base = x_base + 159;
###iterate x
###iterate y
