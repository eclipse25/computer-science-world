## CORS

### CORS(Cross-Origin Resource Sharing)는 뭘까


**브라우저가 동일 출처 정책(Same-Origin Policy)을 우회하도록 허용하기 위해 사용하는 메커니즘**

- 브라우저는 기본적으로 보안상 이유로 서로 다른 도메인 간의 리소스 요청을 차단하는데, 이때 CORS라는 메커니즘을 통해 서버가 특정 조건 하에 이 요청을 허용하도록 한다.
- 서버에서 설정하지만, 브라우저가 적용하는 보안 메커니즘일 뿐 서버가 데이터를 직접 보호하거나 차단하는 장치는 아니다.
    - 브라우저 밖에서 HTTP 요청을 직접 보내는 도구(Postman, curl 등)를 사용하면 CORS에 관계없이 데이터를 받을 수 있다.
    - 따라서 단순히 데이터를 `get`하는 경우보다, 특정 인증 정보(세션 쿠키 등)를 가지고 브라우저를 통해 `get`하는 경우의 악성 요청을 막는 것이 주 목적이다.

<br>

### CORS가 필요한 이유

1. 기본 상황: 동일 출처 정책(Same-Origin Policy)
    - 웹 브라우저는 기본적으로 같은 출처(Origin) 에 있는 리소스만 접근하도록 허용한다.
        - 여기서 **출처(Origin)** 는 다음 세 가지 요소로 정의된다 > 프로토콜(protocol) + 도메인(domain) + 포트(port)
    - 

2. 그런데 현대 웹 환경은 출처가 다른 API 요청이 빈번함
    - 현대적인 웹은 주로 프론트엔드와 백엔드가 서로 다른 도메인에서 운영되어 출처가 달라지는 일이 매우 흔하다. 
    - 이 경우, 브라우저의 기본 보안정책으로는 자바스크립트가 API 서버로 요청을 못 하게 된다.

3. CORS의 역할은 **예외 허용**
    - 브라우저가 기본적으로 요청을 막기 때문에, 서버는 브라우저에게 **이 특정 요청은 예외적으로 허용해도 좋다**고 알려줄 필요가 있다.
    - CORS를 통해 서버는 응답 헤더에 다음과 같이 전달한다.
        - `Access-Control-Allow-Origin: https://frontend.example.com`
    - 이렇게 서버가 허용 정책을 설정하면, 브라우저는 이 헤더를 보고 프론트엔드 JavaScript에서 응답을 사용할 수 있도록 허용한다.


<br>

#### 예시 상황

> 사용자가 `bank.com`에 로그인하여 인증된 세션 쿠키를 가지고 있다.  
> 사용자는 실수로 악성 사이트(`hacker.com`)에 접속했다.  
> `hacker.com`이 사용자의 브라우저를 통해 은행의 민감한 API를 호출하려고 한다.


```javascript
fetch("https://bank.com/api/user-info", {
  credentials: "include", // 쿠키를 포함해서 요청하도록 설정
});
```

그런데 실제 요청이 전송되기 전에 브라우저는 먼저 서버로부터 요청 허용 여부를 확인하는 사전 요청(Preflight)을 보낸다.

```http
OPTIONS /api/user-info HTTP/1.1
Origin: https://hacker.com
Access-Control-Request-Method: GET
Access-Control-Request-Headers: Cookie
```

서버는 요청을 검토한 뒤 허용되지 않은 출처에서 온 요청임을 판단하고 다음과 같은 응답을 돌려준다.

```http
HTTP/1.1 403 Forbidden
Access-Control-Allow-Origin: null
```

서버가 허용하지 않았으므로 브라우저는 실제 데이터가 포함된 요청(GET 요청)을 서버에 보내지 않고, 악성 사이트는 민감한 데이터를 얻을 수 없게 된다.

정리하면 CORS는 서버가 신뢰할 수 없는 출처에서 오는 요청을 브라우저 단계에서 사전적으로 차단하도록 설정하여, 서버 보안을 보조적으로 수행한다.


<br>

### 작동 순서

1. 클라이언트(브라우저)가 다른 도메인의 리소스를 요청한다.
2. 서버가 응답 시 HTTP 헤더(Access-Control-Allow-Origin 등)를 설정하여, 클라이언트에게 특정 도메인에 대해 접근 허용 여부를 알려준다.
3. 브라우저가 이 응답 헤더를 보고 최종적으로 리소스를 허용하거나 거부한다.

<br>

### FastAPI에서 CORS 설정 예시

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # 허용할 도메인 목록
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # 허용할 HTTP 메서드
    allow_headers=["*"]  # 허용할 헤더 (모두 허용)
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}
```

<br>

### CORS 에러 해결 방법

웹 어플리케이션 개발 중에 브라우저 개발자 도구 콘솔에서 CORS 관련 오류가 발생한다면, 다음 사항을 확인한다.

1. 서버에서 정확한 허용 도메인을 지정했는지
2. 클라이언트는 서버가 허용한 메서드 및 헤더를 요청에서 올바르게 사용했는지
3. 사전 요청(Preflight)이 성공적으로 응답하고 있는지 확인한다.

<br>
