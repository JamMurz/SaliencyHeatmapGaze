const PORT = 3001;
const fs = require("fs");
const mime = require("mime");
let {PythonShell} = require('python-shell')

const serverOptions = {
  key: fs.readFileSync(__dirname + "/secret/key.pem"),
  cert: fs.readFileSync(__dirname + "/secret/cert.pem")
};

const spawn = require("child_process").spawn;
let pyshell = new PythonShell('main.py');

pyshell.on('message', function (message) {
  console.log(message);
});


const http2 = require("http2");

const sendFile = (stream, fileName) => {
  const fd = fs.openSync(fileName, "r");
  const stat = fs.fstatSync(fd);
  const headers = {
    "content-length": stat.size,
    "last-modified": stat.mtime.toUTCString(),
    "content-type": mime.getType(fileName)
  };
  stream.respondWithFD(fd, headers);
  stream.on("close", () => {
    console.log("closing file", fileName);
    fs.closeSync(fd);
  });
};

const server_push = (stream, path, fileName) => {
  stream.pushStream({ ":path": path }, (err, pushStream) => {
    if (err) {
      throw err;
    }
    sendFile(pushStream, fileName);
  });
};

const http2Handlers = (req, res) => {
  console.log(req.url);
  if (req.url === "/") {
    server_push(res.stream, "/style.css", "style.css");

    const imageFiles = fs.readdirSync(__dirname + "/images");
    for (let i = 0; i < imageFiles.length; i++) {
      const fileName = __dirname + "/images/" + imageFiles[i];
      const path = "/images/" + imageFiles[i];
      server_push(res.stream, path, fileName);
    }

    sendFile(res.stream, "index.html");
  } else {
    if (req.url === "/favicon.ico") {
      res.stream.respond({ ":status": 200 });
      res.stream.end();
      return;
    }
    const fileName = __dirname + req.url;
    sendFile(res.stream, fileName);
  }
};

http2
    .createSecureServer(serverOptions, http2Handlers)
    .listen(PORT, () => {
      console.log("http2 server started on port", HTTP2_PORT);
    });
