import { createClient } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    redisClient.unsubscribe(channel);
    redisClient.quit();
  }
});

redisClient.subscribe('holberton school channel');
