
import upload
import globals
import time

fnames = ["01.png","02.png","03.png", "04.png","05.png"]

#could make something to recursivley search directory for file names and apped to list but like, can i be fucked? (not really)


def shitspammer():

    try:
        print("Spammer started - will stop on kb interrupt")
        print(globals.mime,globals.passwd,globals.url)
        print("These better be correct bc its too late now tbh")
        #time.sleep(0.5)

        for i in fnames:

            print(i)
            kekw = "files/"+i
            print(upload.user_upload(kekw))
            time.sleep(globals.delay)

    except KeyboardInterrupt:

            exit(0)


while True:
    shitspammer()
