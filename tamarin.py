import os, random, shutil, math
from PIL import Image

CD = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(CD, "input")
OUTPUT = os.path.join(CD, "output")
max_dist = 5
times = 5

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

    for pos in data:
        n = random.choice(get_neigbors(pos, len(data)))
        swap(n, pos, data)

    image.putdata(data)
    Image.save(realpath)
        
def swap(n, pos, data):
    data[n], data[pos] = data[pos], data[n]
    return data

def get_neighbors(pos, size):
    pass
      

