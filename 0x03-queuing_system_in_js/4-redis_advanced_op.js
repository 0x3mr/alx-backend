import { createClient, print } from 'redis';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
});

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
});

redisClient.hset('HolbertonSchools', 'Portland', 50, print);
redisClient.hset('HolbertonSchools', 'Seattle', 80, print);
redisClient.hset('HolbertonSchools', 'New York', 20, print);
redisClient.hset('HolbertonSchools', 'Bogota', 20, print);
redisClient.hset('HolbertonSchools', 'Cali', 40, print);
redisClient.hset('HolbertonSchools', 'Paris', 42, print);
redisClient.hgetall('HolbertonSchools', (_error, value) => console.log(value));
