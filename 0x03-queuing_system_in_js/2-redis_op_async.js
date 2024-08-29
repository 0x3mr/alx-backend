import { print, createClient } from 'redis';
import { promisify } from 'util';

const redisClient = createClient();

redisClient.on('error', (error) => {
  console.log(`Redis client not connected to server: ${error.message}`);
  redisClient.quit();
});

const getAsync = promisify(redisClient.get).bind(redisClient);

function setNewSchool(schoolName, value) {
  redisClient.set(schoolName, value, print);
}

async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  if (value) console.log(value);
}

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}

redisClient.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
