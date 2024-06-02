/*const express = require("express");

const app = express();

app.get('/hi', (req, res) => {
  res.send('Successful response.');
});


app.listen(1234, () => {
  console.log("Server is listening on port: 1234");
}); */

const express = require('express');
const app = express();

app.get('/hi', (req, res) => {
  res.send('Successful response.');
});

const svgs = require("../src/svg");

app.get('/', (req, res) => {
  const { type, text1, text2, height, width } = req.query;

  res.setHeader("Content-Type", "image/svg+xml");

  const error_svg = "origin";

  let svg;

  if (type in svgs) {
    svg = svgs[type];
  } else {
    svg = svgs[error_svg];
    console.log(svg("Type not valid", "refer readme for details !!"));
    return res.send(svg("Type not valid", "refer readme for details !!"));
  }

  res.send(svg({ text1, text2, height, width }));
});

app.listen(1234, () => {
  console.log("Server is listening on port: 1234");
});
