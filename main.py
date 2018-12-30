#!/usr/bin/env python3

from newsdb import first_query, second_query, third_query


def main():
    print('\nGrabbing info from database...\n')
    print('Most Popular Three Articles:-\n')

    for title, count in first_query():
        print(str(title) + " - " + str(count) + " views")

    print('\nMost Popular Article Authors of All Time:-\n')

    for title, count in second_query():
        print(str(title) + " - " + str(count) + " views")

    print('\nErrors of more than 1 percent:-\n')

    for count in third_query():
        print(str(count))
        #print("{} - {:.2f}% errors".format(str(title), round((float(count) * 100), 2)))


if __name__ == '__main__':
    main()
