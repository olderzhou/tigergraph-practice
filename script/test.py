#!/usr/bin/python3

import io
import time


def echo_head(f):
    f.write('id,name,age,gender,state\n')


def echo_data(f):
    for i in range(1, 1000):
        f.write('%d,姓名%d,23,男,1\n' % (i, i))
    for i in range(1001, 2000):
        f.write('%d,姓名%d,33,女,1\n' % (i, i))


def echo_name_head(f):
    f.write('name\n')


def echo_name_data(f):
    for i in range(1, 2000):
        f.write('姓名%d\n' % i)


def echo_search_name_head(f):
    f.write('from,to\n')


def echo_search_name_data(f):
    for i in range(1, 2000):
        f.write('姓名%d,%d\n' % (i, i))


def echo_friend_head(f):
    f.write('from,to\n')


def echo_friend_data(f):
    for i in range(1, 1900):
        f.write('%d,%d\n' % (i, i + 1))
        f.write('%d,%d\n' % (i, i + 2))
        f.write('%d,%d\n' % (i, i + 3))
        f.write('%d,%d\n' % (i, i + 4))
        f.write('%d,%d\n' % (i, i + 20))
        f.write('%d,%d\n' % (i, i + 21))
        f.write('%d,%d\n' % (i, i + 30))
        f.write('%d,%d\n' % (i, i + 31))
        f.write('%d,%d\n' % (i, i + 32))
        f.write('%d,%d\n' % (i, i + 40))
        f.write('%d,%d\n' % (i, i + 41))
        f.write('%d,%d\n' % (i, i + 50))
        f.write('%d,%d\n' % (i, i + 60))
        f.write('%d,%d\n' % (i, i + 70))
        f.write('%d,%d\n' % (i, i + 51))
        f.write('%d,%d\n' % (i, i + 61))
        f.write('%d,%d\n' % (i, i + 71))
        f.write('%d,%d\n' % (i, i + 81))
        f.write('%d,%d\n' % (i, i + 22))


def echo_school_head(f):
    f.write('id,name\n')


def echo_school_data(f):
    for i in range(0, 10):
        f.write('%d,most famous school in china as range %d\n' % (i, i))


def echo_study_head(f):
    f.write('from,to,start_time, end_time\n')


def echo_study_data(f):
    for i in range(1, 1900):
        f.write('%d,%d,%s,%s\n' % (i, i % 10, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())),
                                   time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))))


if __name__ == '__main__':
    # with open('D:/file/person.csv', 'w') as f:
    # 	echo_head(f)
    # 	echo_data(f)
    # with open('D:/file/name.csv', 'w') as f:
    # 	echo_name_head(f)
    # 	echo_name_data(f)
    # with open('D:/file/search_name.csv', 'w') as f:
    # 	echo_search_name_head(f)
    # 	echo_search_name_data(f)
    # with open('D:/file/friend.csv', 'w') as f:
    # 	echo_friend_head(f)
    # 	echo_friend_data(f)
    with open('D:/file/school.csv', 'w') as f:
        echo_school_head(f)
        echo_school_data(f)
    with open('D:/file/study.csv', 'w') as f:
        echo_study_head(f)
        echo_study_data(f)
