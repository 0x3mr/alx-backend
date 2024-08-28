import { createClient } from 'redis';

const client = await createClient()
  .on('error', err => console.log('Redis client not connected to the server: ', err))
  .connect();

await client.set('key', 'value');
const value = await client.get('key');
await client.disconnect();