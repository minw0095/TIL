const fs = require('fs');

const requestHandler = (req,res) => {
    const url = req.url;
    const method = req.method

    if (url === '/' ) {
        res.write('<html>');
        res.write('<head><title>Enter Message</title></head>');
        res.write('<body><form action="/message" method="POST"><input type="text" name="message"><button type="submit">send</button></form></body>');
        res.write('</html>');
        return res.end();
        // 뒤의 코드들을 중단하기 위한 반환 res.end 이후에는 write나 헤더를 호출 하면 안됌
    }
    if (url === '/message' && method === 'POST') {
        const body = [];
        req.on('data', (chunk) => {
            console.log(chunk)
            body.push(chunk);
        } );
        return req.on('end', () => {
            const parsedBody = Buffer.concat(body).toString();
            const message = parsedBody.split('=')[1];
            fs.writeFile('message.txt', message, (err) => {
    
                res.statusCode = 302;
                res.setHeader('Location', '/');
                return res.end();
            });
        });
        //302는 경로 재지정을 의미
        //res.writeHead(302, {});
    }
    // console.log(req.url, req.method, req.headers);
    res.setHeader('Content-Type', 'text/html');
    res.write('<html>');
    res.write('<head><title>My First Page</title></head>');
    res.write('<body><h1> Hello !!</h1></body>');
    res.write('</html>');
    res.end();

};
//내보내기 module.exports에 requestHandler를 저장
// module.exports = requestHandler

// module.exports = {
//     handler: requestHandler,
//     someText: 'some hard coded text'
// }; 아래와 같은 방식
module.exports.handler = requestHandler
module.exports.someText = 'some hard coded text'
