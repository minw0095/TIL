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



### express

`npm install --save express`로 설치

use(): 새로운 미들웨어 함수 추가 가능. 상당히 유연함

next():  다음 미들웨어로 이동하게 해줌

```js
app.use('/',(req, res, next) => {
    console.log('1');
    next(); //다음 미들웨어로 이동하게 해줌
});
```

body-parser

req를 분석해주는 역할을 해준다.

`npm intall body-parser` 명령어를 통해 설치

``` js
const bodyParser = require('body-parser')
```

`body-parser` 모듈을 불러준후

```js
app.use(bodyParser.urlencoded({extended:false}));
```

이런 식으로 사용해 주면 된다



### 미들웨어

#### 미들웨어는 순서가 매우 중요하다!!

express에서 정의하는 use 메서드를 사용

다음 미들웨어를 접근할려면 next()를 사용해야함

하지만 send()를 사용할 시 next()를 호출하지 않는 것이 좋음.(다른 응답 관련 코드를 실행하면 안되기 때문에 하나 이상의 응답을 보내려 하면 오류가 발생함.)

```js
app.use((req, res, next) => {
    console.log('in the middleware!');
    next();
});

app.use((req, res, next) => {
    console.log('in the middleware!');
});
```

GET 요청만 받고 싶을때

```javascript
app.use() 대신 app.get()
```





### 라우팅 파일을 다른 파일로 보내는 방법

라우팅한 코드들을 다른 파일로 보내준후 

```js
const express = require('express');

const router = express.Router();
```

이런 식으로 Router를 실행

메인 js 파일에서 

```js
const adminRoutes = require('./routes/admin');
```

라우터를 불러준다

-> router의 장점:  위에서 정의한 `adminRoutes` 는 미들웨어 함수로 바로 app.use에 사용가능

만약

2개 이상의 router를 불렀을 때 순서를 바꾼다면?

정상 작동:

```js
const adminRoutes = require('./routes/admin');
const ShopRoutes = require('./routes/shop');

app.use(ShopRoutes);
app.use(adminRoutes);
```

adminRoutes가 작동 안하는 경우:

```js
const adminRoutes = require('./routes/admin');
const ShopRoutes = require('./routes/shop');

app.use(adminRoutes);
app.use(ShopRoutes);
```

이는 라우터 파일에서

```js
router.use('/', (req, res, next) => {
    res.send('<h1>Hello, everyone!</h1>')
})
```

use을 사용했기 때문. 이를 `get` `post`를 사용히면 이런 오류가 발생하지 않음

`get` `post`는 경로와 정확히 일치하는 요청만 처리하기 때문에 가능한 것.



라우터의 파일 경로가 같은 경우

```js
//admin.js
router.get('/admin/add-product',(req, res, next) => {
    console.log('2');
    res.send('<form action="/add-product" method="POST"><input type="text" name="title"><button type="submit">Add Product</button> </form>');
});

router.post('/admin/add-product', (req, res, next) => {
    console.log(req.body);
    res.redirect('/');
})
```

라우터의 /admin을 생략 하고

```js
//app.js
app.use('/admin', adminRoutes);
```

해당 경로를 메인 js에 작성 해주면 된다.







### 파일을 정적으로 제공하기(파일 시스템으로 직접 포워딩하기)

```js
app.use(express.static(path.join(__dirname, 'public')));
```

이때 'public'을 통해서 자동으로 public 폴더로 포워딩을 해주므로 link에서 따로 public 폴더 경로를 적을 필요가 없다

```html
<link rel="stylesheet" href="/css/main.css">
```



### 동적컨텐츠

ejs, pug, handlebars

```bash
npm install --save ejs pug express-handlebars
```

view에 대한 기본설정은 메인 디렉토리와 views폴더로 돼있다. 변경하고 싶다면

```javascript
app.set('views', 'templates')
```

동적 컨텐츠는 send()방식이 아닌 render()를 통해 송신

```javascript
router.get('/', (req, res, next) => {
    const products = adminData.products
    res.render('shop', {prods: products});
});
```

이때 딕셔너리 형태인 이유는 이름의 혼동을 피하기위해



* handler 사용방법

```javascript
//app.js
const expressHbs  = require('express-handlebars')
app.engine('handlebars', expressHbs()); //('전해줄이름', 무슨툴인지)
app.set('view engine', 'handlebars');	//위에서 정의한 handlebars를 넘겨줘서
```

--> 이렇게 했더니 expressHbs() is not function 이라는 오류발생

```bash
//해결
npm install --save express-handlebars@3.0
```

handlebars의 버전 문제인듯 싶다.

hbs에서 조건문을 사용할려면

```javascript
//shop.js
router.get('/', (req, res, next) => {
    const products = adminData.products
    res.render('shop', {prods:products, pageTitle: 'Shop', path: '/', hasProducts: products.length > 0});
});
```

shop.js에서 논리연산에 해당하는 값을 전달해줘야한다.

```handlebars
{{# if prods.length}} {{/if}} --> (X)
{{# if hasProducts}} {{/if}} --> (o)
```

루프를 만들고 싶다면

```handlebars
 {{#each prods}}
 {{ this.title }}
 {{/else}}
```



* ejs

ejs는 레이아웃을 제공하지 않는다.

ejs는 태그를 다음과 같은 형식으로 나타낸다.

```ejs
<%  %>
```

ejs는 Vanilla javascript 코드를 쓸수 있는 장점이 있음

```ejs
<% if (prods.length > 0) { %>
<div class="grid">
    ...
<% } %>
```

