node js는 javaScript 코드를 서버에서 실행하게 해주는 것
V8는 구글에서 만든 엔진을 사용하며 c++로 만들어 졌으며 JS를 머신코드로 컴파일한다

js 에서 화살표는 해당 객체가 아닌 전역 범위, 전역 노드 런타임 범위를 참조하므로 해당 객체를 참조하게
하려면 function()을 사용해야한다.

스프레드 연산자: 배열이나 객체에서 원소나 속성을 추출하는데 사용
레스트 연산자: 인수 목록이나 함수에서 여러 인수를 하나의 배열로 묶는데 사용

node js 에서 require은 전역에서 파일을 불러 올 수 있는 키워드
node js event loop를 통해 서버를 작동(event loop를 통해 계속해서 작동) -> process.exit()를 통해 중단가능

buffer는 정류장 같은 역할. 여러개의 청크를 보유 하며 파싱이 끝나기전에 작업 할 수 있도록 한다.

node js는 함수안에 함수를 넣으면 안에 넣은 함수가 나중에 실행됨. 이를 비동기식이라 한다.(항상 나중에 실행
되는건 아니지만 대부분이 그런 방식)

npm start를 통해서 자료 공유시 시작 js를 확인 할 수 있다.
npm start는 특수한 경우여서 npm start만 입력하면 실행 하지만 다른 스크립트의 경우 npm run {start-server}처럼 run을 입력해야함

node js는 수정마다 실행을 다시 시켜야하는데`npm install nodemon` 패키지를 통해 해결 가능 
`npm install nodemon --save` 패키지가 프로덕션 의존성으로 설치됨
`npm install nodemon --save-dev` 단순히 개발 도중 사용하는 것임을 나타냄
`npm install nodemon -g` 머신전체에 설치 어디서든 사용가능
node_modulus 삭제시 `npm install` 을 통해 다시 설치가능

### 에러

Syntax Errors 중괄호를 빼먹거나 철자를 빼먹는등 

Runtume Errors 

Logical Errors 오류 메세지가 안뜸 