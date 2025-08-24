import express from 'express';
const app = express();
const port = process.env.PORT ? Number(process.env.PORT) : 3000;

app.get('/', (req, res) => {
  res.send('Hello World from Ramesh TypeScript container!');
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
