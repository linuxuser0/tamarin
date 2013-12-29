import os, random, shutil, math
from PIL import Image

CD = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(CD, "input")
OUTPUT = os.path.join(CD, "output")
max_dist = 5
times = 1 

def tamarin():
    images = os.listdir(INPUT) 
    for n in range(times):
        for image in images:
            output(image)
            mutate(image)
        print n

def output(image):
    realpath = os.path.join(INPUT, image)
    shutil.copy(realpath, OUTPUT)

def mutate(path):
    realpath = os.path.join(INPUT, path)
    image = Image.open(realpath)
    data = image.getdata()
    size = image.size

    for pos in data:
        n = random.choice(get_neigbors(pos, size[0], len(data)))
        swap(n, pos, data)

    image.putdata(data)
    Image.save(realpath)
        
def swap(n, pos, data):
    data[n], data[pos] = data[pos], data[n]
    return data

def get_neighbors(a, width, total_len):
    # Uses "night's move" geometry for speed

    works = []

    for b in range(len(size)):
         arow, brow = int(a / width), int(b / width)
         acol, bcol = a % width, b % width
         if abs(acol - bcol) + abs(arow - brow) <= max_dist:
             works.append(b)

    return works
    
    
      

