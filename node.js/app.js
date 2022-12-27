const http = require('http');

const routes = require('./routes');

//req는 요청에 대한 데이터 res는 응답에 사용
// EDA(event driven architecture)
// const server = http.createServer((routes) => {
   
// });
const server = http.createServer(routes.handler);

console.log(routes.someText)

// listen은 스크립트를 바로 종료 x 계속 실행됨
server.listen(3000);
