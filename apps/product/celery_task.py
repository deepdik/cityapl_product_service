from app import celery


@celery.task()
def add_together(a, b):
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()
