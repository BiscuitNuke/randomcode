//npm i infinite-campus
//npm i prompt

const InfiniteCampus = require('infinite-campus')
var prompt = require('prompt');


// County
// State
// User - Lunch ID 
// Pass - Password for Lunch ID
// Term - 0 For 1st Semester, 1 for 2nd Semester

var schema = {
  properties: {
    county: {
      pattern: /^[a-zA-Z\s\-]+$/,
      message: 'Must be county you attend for school',
      required: true
    },
    state: {
      pattern: /^[A-Z\s\-]+$/,
      message: 'Must be state code in caps Ex: "WA"',
      required: true
    },
    username: {
      pattern: /^[0-9]+$/,
      message: 'Username must be your student ID',
      required: true
    },
    pass: {
      hidden: true
    },
    term: {
      pattern: /^[0-1 ]+$/,
      message: 'Must be term, 0 for Semester 1, 1 for Semester 2',
      required: true
      },
    }
  }



prompt.start();

prompt.get(schema, function (err, result) {

// log in                          District Name    State  Username  Password
const user = new InfiniteCampus(result.county, result.state, result.username, result.pass)

user.on('ready', () => {
  user.getCourses().then((terms) => {
    terms[result.term].courses.forEach(course => {
      let grade = (course.grades !== undefined) ? `${course.grades.percent}%` : 'N/A'; 
      console.log(`Name: ${course.name}\nRoom #: ${course.roomName}\nTeacher: ${course.teacher}\nGrade: ${grade}\n`)

      // list notifs now IN DEV
      user.getNotifications(10).then((notifications) => {
        // if the first notification is unread
        console.log(notifications)
})
})
})
})
})
