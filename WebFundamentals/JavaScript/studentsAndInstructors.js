function studentsAndInstructors(arr) {
  for(var x = 0; x < arr.length; x++) {
    console.log(arr[x].first_name + ' ' + arr[x].last_name)
  }
}
studentsAndInstructors([
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
])

console.log('----');

//Optional
function studentsAndInstructors1(object) {
  console.log('Students');
  for(var x = 0; x < object.Students.length; x++) {
    console.log((x + 1) + ' - ' + object.Students[x].first_name + object.Students[x].last_name + ' - ' + (object.Students[x].first_name.length + object.Students[x].last_name.length))
  }
  console.log('Instructors');
  for(var x = 0; x < object.Instructors.length; x++) {
    console.log((x + 1) + ' - ' + object.Instructors[x].first_name + object.Instructors[x].last_name + ' - ' + (object.Instructors[x].first_name.length + object.Instructors[x].last_name.length))
  }
}
studentsAndInstructors1({
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 })
