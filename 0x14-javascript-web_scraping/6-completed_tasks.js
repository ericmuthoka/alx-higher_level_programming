#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from the first command line argument

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Make a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const tasks = JSON.parse(body);

      // Create an object to count completed tasks for each user
      const completedTasksByUser = {};

      // Loop through the tasks and count completed tasks
      tasks.forEach((task) => {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      });

      // Print the results
      console.log(completedTasksByUser);
    } else {
      console.error(`Request failed with status code: ${response.statusCode}`);
    }
  }
});
