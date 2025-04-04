## HTTP 개념과 특징

<br>

### **HTTP(HyperText Transfer Protocol)**

- HTTP는 웹에서 정보를 교환하는 데 사용되는 애플리케이션 계층 프로토콜이다.
- 웹 브라우저(클라이언트)와 웹 서버 간의 통신을 가능하게 하며, HTML 문서, 이미지 등의 리소스를 요청하고 전송받는 데 사용된다.
- **하이퍼텍스트(Hypertext)**: 링크를 통해 웹 상의 다른 문서나 멀티미디어로 이동할 수 있도록 구조화된 텍스트
- HTTP는 데이터를 암호화하지 않으며, 통신 상대방을 확인하지 않기 때문에 보안에 취약하다.

<br>

### **HTTP의 주요 특징**

#### 1. **비상태성(Statelessness)**
- HTTP는 상태를 유지하지 않는 프로토콜이다. 즉, 각 요청은 독립적으로 처리되며 서버는 이전 요청을 기억하지 않는다.
- 이를 해결하기 위해 **쿠키(Cookie)**, **세션(Session)** 같은 기술이 사용된다.

#### 2. **클라이언트-서버 모델**
- 클라이언트는 서버에 요청을 보내고, 서버는 해당 요청에 응답한다.
- 클라이언트는 주로 웹 브라우저이며, 서버는 웹사이트를 호스팅하는 컴퓨터이다.

<br>

### **HTTP의 주요 메서드**

| 메서드 | 설명 |
|--------|------------------------------------------------------|
| GET    | 서버에서 특정 리소스를 요청한다. 데이터를 수정하지 않음. |
| POST   | 서버로 데이터를 전송하여 새로운 리소스를 생성한다.      |
| PUT    | 지정된 URI에 리소스를 생성하거나 기존 리소스를 수정한다. |
| DELETE | 지정된 URI의 리소스를 삭제한다.                        |
| HEAD   | GET과 유사하지만, 응답 본문 없이 HTTP 헤더만 반환한다. |
| OPTIONS| 대상 리소스의 통신 가능 옵션을 조회한다.               |

<br>

### **HTTP 버전별 발전**  

| 버전       | 출시 연도 | 주요 특징 |
|------------|---------|--------------------------------------------------------------|
| **HTTP/0.9** | 1991 | - 최초의 HTTP 버전, 단순한 **텍스트 기반 프로토콜**<br>- **GET 요청만 지원**, 응답으로 HTML 문서만 제공<br>- 헤더 없음, 메타데이터 전송 불가 |
| **HTTP/1.0** | 1996 | - **헤더(Header) 추가**, 요청과 응답의 메타데이터 포함 가능<br>- **다양한 HTTP 메서드 도입**(POST, HEAD 등)<br>- **비연결성(Connectionless)**: 요청마다 새로운 연결을 생성 |
| **HTTP/1.1** | 1997 | - **지속 연결(Persistent Connection) 지원** → 성능 향상<br>- **Chunked Transfer Encoding** 도입 (데이터를 조각으로 전송 가능)<br>- Pipelining 지원 (여러 요청을 순차적으로 보낼 수 있음, 하지만 한계 존재) |
| **HTTP/2** | 2015 | - **멀티플렉싱(Multiplexing) 지원**: 단일 연결로 여러 요청 처리 가능<br>- **헤더 압축(HPACK)**: 불필요한 데이터 전송 최소화<br>- 서버 푸시(Server Push): 클라이언트 요청 없이도 서버가 리소스 전송 가능 |
| **HTTP/3** | 2022 | - **QUIC 프로토콜 사용** → TCP 대신 UDP 기반의 전송 방식 도입<br>- **지연 시간 감소**, 연결 설정 속도 향상<br>- 패킷 손실에도 개별 스트림 간 독립적 전송 가능 |

<br>

#### **HTTP 버전별 차이점 비교**  

| 비교 항목  | HTTP/1.0 | HTTP/1.1 | HTTP/2 | HTTP/3 |
|------------|---------|---------|--------|--------|
| **연결 방식** | 요청마다 새로운 연결 | 지속 연결 (Keep-Alive) | 단일 연결, 멀티플렉싱 | QUIC 기반, 멀티플렉싱 |
| **멀티플렉싱** | 지원 안 함 | 지원 안 함 | 지원 | 지원 |
| **헤더 압축** | 지원 안 함 | 지원 안 함 | HPACK 압축 | QPACK 압축 |
| **성능** | 낮음 | 개선됨 | 빠름 | 가장 빠름 |
| **보안** | TLS 선택적 | TLS 선택적 | TLS 필수 | TLS 필수 |

<br>

### **HTTP vs HTTPS**

| 구분  | HTTP | HTTPS |
|-------|-------------------------------|-------------------------------|
| 보안  | 암호화 없음, 보안에 취약         | SSL/TLS 암호화를 통해 보안 강화 |
| 포트  | 기본적으로 **80번 포트** 사용  | 기본적으로 **443번 포트** 사용 |
| 신뢰성 | 데이터 도청 및 변조 가능       | 인증서를 통해 신뢰성 확보       |
| 성능  | 상대적으로 빠름                | 암호화 오버헤드로 약간 느릴 수 있음 (TLS 1.3 이후 차이 줄어듦) |

<br>

### **정리**
HTTP는 웹 통신의 기본 프로토콜이지만, 보안이 취약하다는 단점이 있다.  
이를 보완하기 위해 HTTPS가 도입되었으며, 오늘날 대부분의 웹사이트는 HTTPS를 사용하여 데이터를 안전하게 보호한다.