import datetime

FMT = '%d %H:%M:%S'
STEP = datetime.timedelta(minutes=1)


# timeslot
# section
# course
# schedule

class time_slot(object):
    def __init__(self, start_time="00 00:00:00", end_time="00 00:00:00"):
        self.start_time = datetime.datetime.strptime(start_time, FMT)
        self.end_time = datetime.datetime.strptime(end_time, FMT)
        self.date_range = []
        self.generate_date_range()

    def generate_date_range(self):
        while self.start_time < self.end_time:
            self.date_range.append(self.start_time.strftime(FMT))
            self.start_time += STEP

    def print_date_range(self):
        print(self.date_range)

    def get_date_range(self):
        return self.date_range


def compare_time_slots(time1, time2):
    conflict = bool(set(time1).intersection(time2))
    return conflict


def compare_sections(section1, section2):
    a, b = 0, 0
    conflict_present = False
    while b < len(section2):
        if compare_time_slots(section1[a].get_date_range(), section2[b].get_date_range()):
            conflict_present = True
            break
        a += 1
        if a == len(section1):
            a = 0
            b += 1
    return conflict_present


def compare_section_to_course(section, course):
    x = 0
    conflict = False
    while x < len(course):
        conflict = compare_sections(section, course[x])
        if conflict:
            break
        x += 1
    return conflict


def check_course(course):
    x = 0
    conflict = False
    while x < len(course):
        conflict = compare_section_to_course(course[x], REQUIRED_SECTIONS)
        if conflict:
            del course[x]
        else:
            x += 1
    if len(course) == 0:
        print("Invalid course selections. No possible timetable")
    if len(course) == 1:
        REQUIRED_SECTIONS.append(course[0])
    return len(course)


REQUIRED_SECTIONS = []
course = []
course2 = []

section1 = [time_slot('05 11:00:00', '05  12:00:00'), time_slot('05 11:00:00', '05 12:00:00'),
            time_slot('05 11:00:00', '05 12:00:00')]
section2 = [time_slot('03 11:00:00', '03  12:00:00'), time_slot('03 11:00:00', '03 12:00:00'),
            time_slot('03 11:00:00', '03 12:00:00')]
section3 = [time_slot('02 11:00:00', '02  12:00:00'), time_slot('02 11:00:00', '02 12:00:00'),
            time_slot('02 11:00:00', '02 12:00:00')]



required_section1 = [time_slot('02 11:00:00', '02  12:00:00'), time_slot('02 11:00:00', '02 12:00:00'),
                     time_slot('02 11:00:00', '02 12:00:00')]
course3= []
course3.append(required_section1)

course.append(section1)
course.append(section2)
course.append(section3)
course2.append(section1)
course2.append(section2)
course2.append(section3)


for x in range(0,3):
    print("course1")
    hello = check_course(course)
    print(hello)
    print(len(REQUIRED_SECTIONS))

    print("course2")
    hi = check_course(course2)
    print(hi)
    print(len(REQUIRED_SECTIONS))

    print("course3")
    dd = check_course(course3)
    print (dd)
    print(len(REQUIRED_SECTIONS))

