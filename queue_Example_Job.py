import unittest
import random

class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []


class Job:

    def __init__(self):
        self.pages = random.randint(1, 11)

    def print_page(self):
        if self.pages > 0:
            self.pages = self.pages - 1

    def check_complete(self):
        if self.pages == 0:
            return True
        return False


class Printer:

    def __init__(self):
        self.current_job = None

    def get_job(self, queue):
        try:
            self.current_job = queue.dequeue()
        except IndexError:  # Queue is empty
            return "No more jobs to print."

    def print_job(self, job):

        while job.pages > 0:
            job.print_page()

        if job.check_complete():
            return "JOB_COMPLETE"
        else:
            return "An error occurred."




class MyTests(unittest.TestCase):
 def test1(self):
        job1 = Job()
        printq = Queue()
        printer = Printer()
        printq.enqueue(job1)
        printer.get_job(printq)
        self.assertEqual("JOB_COMPLETE", printer.print_job(printer.current_job))


unittest.main()
