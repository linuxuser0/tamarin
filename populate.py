import os, shutil, random 

for directory in os.listdir("corpus"):
    print directory
    all_images = os.listdir(os.path.join("corpus", directory))
    images = random.sample(all_images, 30)
    for image in images: 
        shutil.copy(os.path.join("corpus", directory, image), "input")

print "Done."
