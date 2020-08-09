# coding: utf-8
import cv2

video = cv2.VideoCapture('bad_apple.mp4')

fps = video.get(cv2.CAP_PROP_FPS)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fnums = video.get(cv2.CAP_PROP_FRAME_COUNT)

print('fps:', fps, 'size:', size, 'fnums: ', fnums)


f = open('demo.txt', 'w')

mm=0
success, frame = video.read()
while success:
    for i in range(size[1]//20):
        img = ''
        for j in range(size[0]//10):
            if frame[i*20,j*10,1] == 0:
                img = img + '.'
            else:
                img = img + ' '
        f.write(img)
        f.write('\n')
    mm = mm + 1
    success, frame = video.read()


f.close()
print(mm)


#print(img)

# while success :
    
