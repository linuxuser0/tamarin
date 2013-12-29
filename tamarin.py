import os, random, shutil, math
from PIL import Image

CD = os.path.dirname(os.path.realpath(__file__))
INPUT = os.path.join(CD, "input")
OUTPUT = os.path.join(CD, "output")
max_dist = 5
pixels_to_modify = 10 
times = 1 

def tamarin():
    print "Type DELETE OUTPUT to delete output folder and continue"
    if raw_input().lower() != "delete output":
        print "Way to fail."
        exit()

    reset_output()
    images = os.listdir(INPUT) 
    done = 0
    total = times*len(images)
    for n in range(times):
        for image in images:
            output(image)
            mutate(image)
            done += 1
            print "%d%% done." % (float(done)/float(total)*100.0)

def reset_output():
    try:
        shutil.rmtree(OUTPUT)
    except Exception:
        pass

    os.makedirs(OUTPUT)
    print "Output has been reset."

def output(image):
    realpath = os.path.join(INPUT, image)
    shutil.copy(realpath, OUTPUT)

def mutate(path):
    realpath = os.path.join(INPUT, path)
    image = Image.open(realpath)
    data = list(image.getdata())
    size = image.size

    for _ in range(pixels_to_modify):
        pos = random.randint(0, len(data))
        n = random.choice(get_neighbors(pos, size[0], len(data)))
        swap(n, pos, data)
        #print "pos is %d" % pos

    image.putdata(data)
    image.save(get_new_name(realpath))
        
def swap(n, pos, data):
    data[n], data[pos] = data[pos], data[n]
    return data

def get_neighbors(a, width, total_len):
    # Uses "night's move" geometry for speed

    works = []

    for b in range(total_len):
         arow, brow = int(a / width), int(b / width)
         acol, bcol = a % width, b % width
         if abs(acol - bcol) + abs(arow - brow) <= max_dist:
             works.append(b)

    return works

def get_new_name(realpath):
    filename, extension = os.path.splitext(realpath)
    return filename + "_edit" + extension
    
    
tamarin()
