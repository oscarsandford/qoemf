const express = require("express");
const app = express();
const PORT = 5000;


app.listen(PORT, () => {
	console.log(`qoemf express server listening on port ${PORT}.`);
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
//server.listen(3000, () => {
//	console.log("qoemf server: listening on http://localhost:3000");	
//});
