import { createClient } from 'redis';

const redisClient = createClient();

//connect redis server
redisClient.on('connect', function () {
    console.log('Redis client connected to the server');
});

redisClient.on('error', function (error) {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

//subscribes holberton school channel
redisClient.subscribe('holberton school channel');

//Channel for messages and print them as soon as you get them
redisClient.on('message', function (channel, message) {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
//Terminate server connect and unsubscribe from channel
    redisClient.unsubscribe('holberton school channel');
    redisClient.end(true);
  }
});
