const express = require("express");
const app = express();
const PORT = 5000;
const IP = (process.argv.length===3) ? process.argv[2] : "127.0.0.1";

app.listen(PORT, IP, () => {
	console.log(` >> qoemf express server listening at ${IP}/${PORT}.`);
});

app.get("*", (req,res) => {
	res.write("<h1>qoemf server hello!!</h1>");
});


//const server = http.createServer((req,res) => {
//	res.statusCode = 200;
//	res.setHeader("Content-Type", "text/html");
//	res.write("<h1>qoemf server hello!</h1>");
//	res.end();
//});
//
//server.listen(PORT, IP, () => {
//	console.log(` >> qoemf express server listening at ${IP}/${PORT}.`);
//});
