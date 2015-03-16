#-*- coding: utf-8 -*-
import requests
import json


class HackBulgariaAPI():

    def __init__(self):
        self.dict_of_courses = {}
        self.set_of_courses = set()
        self.list_of_names = []
        self.reduced_list = []
        self.list_of_students = []

    def collect_data_from_server(self):
        hack_bulgaria_url = "https://hackbulgaria.com/api/students/"
        my_request = requests.get(hack_bulgaria_url, verify=False)
        #print(my_request.encoding)
        if my_request.status_code == 200:
            data = my_request.json()
            for student in data:
                self.list_of_students.append(student)

    def generate_set_of_courses(self):
        for student in self.list_of_students:
            for course in student["courses"]:
                self.set_of_courses.add(course["name"])

    def list_courses(self):
        for num, course in enumerate(self.set_of_courses):
            self.dict_of_courses[num + 1] = course
            print ("[{}]  -  {}".format(num + 1, course))

    def fill_courses_with_names_and_groups(self, course_num):
        course_name = self.dict_of_courses[course_num]
        for student in self.list_of_students:
            for course in student["courses"]:
                #print(course["name"])
                if course["name"] == course_name:
                    #print("yes")
                    self.list_of_names.append(
                        {'name': student["name"], 'group': course["group"]})

    def match_teams(self, course_id, number_of_programmers, group_id):
        self.fill_courses_with_names_and_groups(course_id)
        self.reduse_students_by_group(group_id)
        separator = "================"
        for num, student in enumerate(self.reduced_list):
            if num % number_of_programmers == 0:
                print("{}\n{}".format(separator, student))
            else:
                print(student)

    def reduse_students_by_group(self, group_id):
        for student in self.list_of_names:
            if student["group"] == group_id:
                #print(student["name"])
                name = str(student["name"])
                print(name)
                self.reduced_list.append(name)
        #for item in self.reduced_list:
            #print (item)

if __name__ == '__main__':
    the_api = HackBulgariaAPI()
    the_api.collect_data_from_server()
    the_api.generate_set_of_courses()
    the_api.list_courses()
    #the_api.reduse_students_by_group(7)
    #the_api.fill_courses_with_names_and_groups(7)
    the_api.match_teams(7, 3, 1)
