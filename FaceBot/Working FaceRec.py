import keras
from keras import applications
from matplotlib import pyplot
from PIL import Image
from numpy import asarray
from scipy.spatial.distance import cosine
from mtcnn.mtcnn import MTCNN
from keras_vggface.vggface import VGGFace
from keras_vggface.utils import preprocess_input
import time
import os
import datetime
import shutil
import tkinter as tk
from PIL import ImageTk
from gtts import gTTS


def extract_face(filename, required_size=(224, 224)):
    face_array = []
    pixels = pyplot.imread(filename)
    detector = MTCNN()
    results = detector.detect_faces(pixels)
    for faces in results:
        x1, y1, width, height = faces['box']
        x2, y2 = x1 + width, y1 + height
        face = pixels[y1:y2, x1:x2]
        image = Image.fromarray(face)
        image = image.resize(required_size)
        face_array.append(asarray(image))
    return face_array


def get_embeddings(filenames):
    yhat = []
    faces = []
    #faces is only as big as file names
    for f in filenames:
        things = extract_face(f)
        if len(things) > 1:
            for t in things:
                p = []
                p.append(t)
                faces.append(p)
        else:
            faces.append(things)
    #faces = [extract_face(f) for f in filenames]
    for face in faces:
        print(str(len(face)))
        samples = asarray(face, 'float32')
        samples = preprocess_input(samples, version=2)
        model = VGGFace(model='resnet50', include_top=False, input_shape=(224, 224, 3), pooling='avg')
        yhat.append(model.predict(samples))
    print('hat ' + str(len(yhat)))
    return yhat



def is_match(known_embedding, candidate_embedding, thresh=0.5):
    score = cosine(known_embedding, candidate_embedding)
    return score


Files = os.listdir('C:/Users/Administrator/downloads/Bases')
KnownFaces = []
Key = []
for file in Files:
    name = ''
    for i in range(len(file)):
        if not file[i] == '.':
            name += file[i]
        else:
            break
    Key.append('C:/Users/Administrator/downloads/Bases/' + file)
    KnownFaces.append(name)
Bases = get_embeddings(Key)

pixals = []

def CheckFace(Guess, Bases):
    try:
        Unknowns = get_embeddings(Guess)
    except:
        print('No face found')
        return None
    pixels = extract_face(Guess[0])
    #for face in pixels:
        #pyplot.imshow(face)
        #pyplot.show()
    peeps = []
    for face in Unknowns:
        probs = []
        for people in Bases:
            Chance = is_match(people[0], face[0])
            probs.append(Chance)
        peeps.append(probs)
        print(len(Unknowns))
    peeps = MakeGuess(peeps)
    return peeps

def MakeGuess(Peeps):
    Final = []
    print(Peeps)
    if Peeps[0]:
        for Probs in Peeps:
            Guess = min(Probs)
            Chance = (1-Guess)*100
            if(Guess < 0.5):
                Final.append(KnownFaces[Probs.index(Guess)])
            else:
                Final.append('Unknown')
        return Final
    return None


def takePic():
    Cool = True
    if Cool == True:
        import cv2 
        cam_port = 0
        cam = cv2.VideoCapture(cam_port)
        result, image = cam.read()
        if result:
            cv2.imwrite('C:/Users/Administrator/downloads/Guesses/image.jpg',image)
        else:
            print('Image failed')
    else:
        import pyautogui
        screen = pyautogui.screenshot()
        screen.save('C:/Users/Administrator/downloads/Guesses/image.jpg')



def CheckPic():
    peopleSeen = []
    NewPeople = os.listdir('C:/Users/Administrator/downloads/Guesses')
    Guesses = []
    for file in NewPeople:
        Guesses.append(['C:/Users/Administrator/downloads/Guesses/' + file])
    for Guess in Guesses:
        peopleSeen = CheckFace(Guess, Bases)
    return peopleSeen


def createTime(name):
    cleaned_name = '' 
    for letter in name:
        if letter == ':':
            letter = '.'
        cleaned_name += letter
    for i in range(len(cleaned_name)):
        if cleaned_name[i] == ' ':
            time1 = cleaned_name[i:]
    time1 = time1[:9]
    new_time = ''
    hour = time1[1]+time1[2]
    suffex = 'am'
    if int(hour) >= 13:
        suffex = 'pm'
        new_time = int(hour) -12
        time1 = str(new_time) + time1[3:] 

    time1 += ' ' + str(suffex)
    return time1

def createDate():
    date = datetime.datetime.today()
    m = str(date.month)
    d = str(date.day)
    y = str(date.year)
    date = m + '-' + d + '-' + y
    return date


def makeLogs(names):
    people = ''
    if names:
        for name in names: 
            people += name + '+'
        people = people[:-1]
        try:
            os.mkdir('C:/Users/Administrator/downloads/logs/'+str(createDate()))
        except:
            print('file exists')
        print(people)
        shutil.copy('C:/Users/Administrator/downloads/Guesses/image.jpg', 'C:/Users/Administrator/downloads/logs/'+str(createDate())+'/'+people + ' ' + createTime(str(datetime.datetime.now())) +'.jpg')


names = []
window = tk.Tk()
window.geometry("1000x500")
photo_images = []
labels = []
timer = 120
start = time.time()
labs = []

def placePics(arrays):
    if arrays:
        for array in arrays:
            image = Image.fromarray(array)
            photo = ImageTk.PhotoImage(image)
            photo_images.append(photo)
            label = tk.Label(window, image=photo)
            labels.append(label)
        Lx = 50
        Ly = 25
        for l in labels:
            l.place(x = Lx, y = Ly)
            Lx += 300
            Ly += 0

def LabelTheLabels(names):
    if names:
        for name in names:
            label = tk.Label(window, text = name)
            labs.append(label)
        Lx = 150
        Ly = 300
        for l in labs:
            l.place(x = Lx, y = Ly)
            Lx += 300
            Ly += 0

def talk(mytext):
    language = 'en'
    for name in mytext:
        if name == mytext[-1]:
            break
        name += 'and'
    print(mytext)
    myobj = gTTS(text=str('hello') + mytext, lang=language, slow=False)
    myobj.save("TalkingFolder/welcome.mp3")
    os.system("start TalkingFolder/welcome.mp3")
    time.sleep(1)

def createAttendece(names):
    with open('C:/Users/Administrator/downloads/logs/' + str(createDate()) + '/Attendence.txt', 'w') as f:
        for name in names:
            f.write(name + ', ')

while True:
    pixals = []
    takePic()
    names = CheckPic()
    if names:
        for name in names:
            if KnownFaces.__contains__(name):
                KnownFaces.pop(KnownFaces.index(name))
    makeLogs(names)
    createAttendece(KnownFaces)  
    mytext = str(names)
    #talk(mytext)
    if time.time() - start > timer:
        break
print(KnownFaces)
print('done')

  





