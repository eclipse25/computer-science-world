## DNS (Domain Name System)

<br>

- 계층적인 도메인 구조와 분산된 데이터베이스를 이용한 시스템으로 FQDN(Fully Qualified Domain Name)을 IP로 변환하는 시스템
  - `www.example.com`에서 `www`는 호스트 또는 서브도메인, `example.com`은 도메인 이름이다.

<br>

### 1. DNS 구성 요소
- **리졸버(Resolver)**: DNS 관련 요청을 네임 서버로 전달하고, 응답을 클라이언트에게 반환
- **네임 서버(Name Server)**: 도메인 이름을 IP 주소로 변환

#### 1.1 네임 서버의 기능
1. **도메인 이름 해석**  
   - 사용자가 입력한 도메인 이름을 IP 주소로 변환  
2. **DNS 레코드 관리**  
   - 다양한 유형의 DNS 레코드를 관리  
     - `A` 레코드: 도메인을 IP 주소와 매핑  
     - `MX` 레코드: 메일 서버 정보  
     - `CNAME` 레코드: 도메인의 별칭 지정  
     - `NS` 레코드: 네임 서버 정보  
3. **네트워크 요청 응답**  
   - 인터넷을 통해 들어오는 DNS 조회 요청에 대응하여 적절한 응답을 제공  

<br>

### 2. `www.naver.com`을 입력했을 때 발생하는 일

1. **리다이렉트 확인**  
   - 특정 주소(`www.naver.com → naver.com` 등)로 리다이렉트되는지 확인  
2. **캐싱 확인**  
   - 캐싱된 DNS 정보가 있는 경우 바로 반환  
   - **DNS 캐싱 종류**:
     - **브라우저 캐시**: JS, CSS, 이미지 등 브라우저에 저장된 리소스  
     - **OS 캐시**: `gethostbyname()` 같은 시스템 호출 결과 저장  
     - **공유 캐시**: CDN, 프록시 서버에서 공유되는 캐시  
     - **ISP(인터넷 서비스 제공자) 캐시**: 자주 조회되는 DNS 정보를 ISP에서 캐싱  
3. **DNS 조회**
4. **IP 라우팅, ARP(Address Resolution Protocol)**  
   - **IP 라우팅**: 패킷이 목적지까지 갈 수 있도록 최적의 경로를 선택  
   - **ARP**: IP 주소를 MAC 주소로 변환 (단, 로컬 네트워크에서만 사용)  
5. **TCP 연결 (3-Way Handshake)**  
   - 클라이언트와 서버 간 안정적인 데이터 전송을 위해 3-Way Handshake 수행  
     1. 클라이언트 → 서버: `SYN` 패킷 전송 (연결 요청)  
     2. 서버 → 클라이언트: `SYN-ACK` 패킷 응답 (연결 수락)  
     3. 클라이언트 → 서버: `ACK` 패킷 전송 (연결 완료)  
6. **컨텐츠 요청 후 다운로드**  
   - 처음부터 다운로드가 시작되는 순간까지의 시간을 **TTFB(Time To First Byte)** 라고 한다.  
   - TTFB는 다음 요소들로 구성된다.  
     - DNS 조회 시간  
     - TCP 핸드셰이크 시간  
     - 서버의 HTTP 요청 처리 시간  
   - 즉, 단순한 "다운로드 시작 시간"이 아니라 **서버 응답을 받기까지의 총 대기 시간**을 의미한다.  
7. **브라우저 렌더링**

<br>

### 3. DNS 쿼리 프로세스

- Root domain → Top Level Domain → Second Level Domain → Third Level Domain  
- 오른쪽부터 역순으로 주소를 찾아 IP 주소를 매핑한다.  

1. **Root Domain (`.`)**  
   - DNS 쿼리는 루트 네임 서버에서 시작된다.  
   - 루트 네임 서버는 TLD(최상위 도메인) 네임 서버의 위치를 알려준다.  

2. **Top-Level Domain (TLD) 서버**  
   - `.com`, `.net`, `.org` 등의 최상위 도메인을 관리  
   - 예: `www.example.com` 요청 시 `.com` 도메인을 관리하는 네임 서버 주소를 제공  

3. **Second-Level Domain 서버**  
   - `example.com` 같은 도메인의 네임 서버를 관리  
   - TLD 서버는 해당 도메인의 네임 서버 정보를 반환  

4. **Third-Level Domain (Subdomain) 서버**  
   - 서브도메인(예: `www.example.com`의 `www`)은 보통 Second-Level Domain 네임 서버에서 처리  
   - 하지만 Google, AWS 같은 대형 서비스에서는 서브도메인마다 별도 네임 서버를 운영할 수도 있음  

<br>

### 4. DNS 캐싱이 동작하는 과정

1. 사용자가 `www.example.com`을 입력하면 브라우저는 **로컬 캐시**를 먼저 확인  
2. 로컬 캐시에 없으면 OS 캐시 확인  
3. OS 캐시에 없으면 **ISP의 캐싱 DNS 서버**에서 확인  
4. ISP에서도 찾지 못하면 **DNS 쿼리 과정 (Root → TLD → SLD)** 진행  
5. 결과를 사용자에게 반환하고, 이후 동일 요청이 있을 경우 캐싱된 데이터를 활용  

<br>

### 5. 추가 개념 정리

#### 5.1 DNS 레코드 종류
| 레코드 타입 | 설명 |
|------------|--------------------------|
| A (Address) | 도메인을 IPv4 주소로 매핑 |
| AAAA | 도메인을 IPv6 주소로 매핑 |
| CNAME (Canonical Name) | 도메인의 별칭 설정 |
| MX (Mail Exchange) | 메일 서버 정보 저장 |
| NS (Name Server) | 네임 서버 정보 저장 |
| TXT (Text) | 다양한 텍스트 데이터 저장 (예: SPF, DKIM) |

#### 5.2 도메인 구조 예시
```
www.example.com
└── Root Domain (`.`)
    └── Top-Level Domain (`.com`)
        └── Second-Level Domain (`example.com`)
            └── Third-Level Domain (`www`)
```

#### 5.3 DNS 쿼리 과정 시각화
1. 브라우저 캐시 → OS 캐시 → ISP 캐시 → 루트 네임 서버 → TLD 서버 → SLD 서버 → 서브도메인 서버  
2. 빠른 응답을 위해 **캐싱 메커니즘 활용**  
3. 최종적으로 IP 주소를 얻고, 웹사이트 요청을 진행  

<br>

### 6. 정리
- DNS는 계층적이며, 분산된 데이터베이스 구조를 활용하여 도메인 이름을 IP 주소로 변환하는 시스템
- DNS 캐싱을 통해 성능을 최적화하며, ISP와 OS 레벨에서도 캐싱을 활용
- TCP 3-Way Handshake와 IP 라우팅 과정도 함께 수행됨
- DNS 쿼리는 루트부터 서브도메인까지 계층적으로 진행

