# Names Part 1

def namesPart1(list):
    for count in range(0, len(list)):
        print list[count]['first_name'] + " " + list[count]['last_name']
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}]
namesPart1(students)

# Names Part 2

def namesPart2(dictionary):
    for k, v in dictionary.iteritems():
        print k
        for values in v:
            length = str(len(values['first_name']) + len(values['last_name']))
            print str(v.index(values) + 1) + " - " + values['first_name'].upper() + " " + values['last_name'].upper() + " - " + length
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
namesPart2(users)
