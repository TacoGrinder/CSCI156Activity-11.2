__author__ = 'ortus'


#1
transcript = {'Fall 11': [['MATH', '101', '1', 'Calc 1'], ['CHEM', '101', '1', 'Calc 1'],
             ['ENGR', '101', '1', 'Calc 1']], 'Spring 12': [['ENGL', '102', '2', 'Writing 2'],
            ['PSYC', '101', '1', 'Intro to Psychology'], ['RLGS', '105', '1', 'Intro to World Religions']],
            'Fall 12': [['ENGL', '241', '1', 'American Literature'], ['HIST', '211', '1', 'American History'],
            ['POLS', '101', '1', 'American Politics']],
            'Spring 13': [['COMM', '101', '1', 'Introduction to Communications'],
            ['COMM', '110', '1', 'Mass Media in American Life']]}
#2
def prntdef():
    q = 0
    for semester in transcript:
        print(str(semester))
        for i in transcript[semester]:
            q += 1
            print(len(str(semester))*' '+i[0]+' '+i[1]+', Section '+i[2]+', '+i[3])


prntdef()

#3
def semesters(subject, transcript):
    for semester in transcript:
        for course in transcript[semester]:
            if course[0] == subject.upper():
                print(semester)
                break
semesters('comm', transcript)