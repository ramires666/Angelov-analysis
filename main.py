import pandas as pd
import cv2
import pytesseract
import os

path2Export = r'/home/alex/Downloads/Telegram Desktop/ChatExport_2021-05-14 (1)'
path2json = os.path.join(path2Export,'result.json')



def readPic2Text(path2Pic):

    path2Pic = os.path.join(path2Export,path2Pic)
    # path2Pic = os.path.join(path2Export,msgs2.loc[6, 'photo'])

    # Подключение фото
    img = cv2.imread(path2Pic)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Будет выведен весь текст с картинки
    config = r'--oem 3 --psm 6'
    # print(pytesseract.image_to_string(img, config=config))

    # Делаем нечто более крутое!!!

    data = pytesseract.image_to_data(img, config=config)

    # Перебираем данные про текстовые надписи
    for i, el in enumerate(data.splitlines()):
        if i == 0:
            continue

        el = el.split()
        # try:
        #     # Создаем подписи на картинке
        #     x, y, w, h = int(el[6]), int(el[7]), int(el[8]), int(el[9])
        #     cv2.rectangle(img, (x, y), (w + x, h + y), (0, 0, 255), 1)
        #     cv2.putText(img, el[11], (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
        # except IndexError:
        #     print("Операция была пропущена")

    # Отображаем фото
    cv2.imshow('Result', img)
    cv2.waitKey(0)



def main():

    df = pd.read_json(path2json)
    messages =df['messages']
    msgs = pd.DataFrame(list(messages))
    msgs2 = msgs[['id','date','text','photo']]
    # msgs2.dropna(subset=['text'],inplace=True)
    msgs2 = msgs2[msgs2['text']!='']
    readPic2Text(msgs2.loc[6,'photo'])

if __name__ == '__main__':
    main()