import { createClient } from 'redis';

const publisher = createClient();

//establish connection to the redis server
publisher.on('connect', function () {
    console.log('Redis client connected to the server');
});

publisher.on('error', function(error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

//broadcasting messages to Herberton School Channel
function publishMessage(message, time) {
  //message (str): message that will be released, (int): waiting period in milliseconds before sending message
  setTimeout(function () {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
