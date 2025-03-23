## OOP와 SOLID 원칙

### **객체지향 프로그래밍(Object-Oriented Programming, OOP)**

프로그램을 객체들의 집합으로 모델링하여 설계하고 구현하는 방식

**객체(Object)**
    - 데이터(속성, attribute)와 이 데이터를 처리하는 메서드(method)를 하나로 묶은 소프트웨어 단위. 
    - 클래스의 인스턴스(instance)이며, 프로그램 내에서 실제로 동작하는 개별적인 실체이다.

OOP는 프로그램의 재사용성, 유지보수성, 투명성을 향상시킨다.

<br>

#### **OOP의 주요 개념**

1. **클래스(Class)**
   - 같은 종류의 객체를 생성하기 위한 템플릿
   - 클래스는 객체의 데이터 형태와 사용할 수 있는 메서드를 정의한다.

2. **객체(Object)**
   - 클래스에 정의된 속성(데이터)과 기능(메서드)을 실제로 가지고 있는 실체
   - 클래스의 인스턴스라고도 한다.

3. **상속(Inheritance)**
   - 한 클래스가 다른 클래스의 속성과 메서드를 상속받아 사용할 수 있게 하는 것
   - 코드 재사용성을 높이고 중복을 줄이는 데 유용하다.

4. **다형성(Polymorphism)**
   - 동일한 인터페이스나 메서드가 다양한 데이터 타입이나 클래스에서 다르게 동작하는 특징을 의미한다.
   - 이를 구현하는 방식:
     - **메서드 오버로딩(Method Overloading):** 같은 이름의 메서드를 매개변수의 타입이나 개수에 따라 다르게 정의하는 것. (단, Python에서는 기본적으로 지원하지 않음)
     - **메서드 오버라이딩(Method Overriding):** 자식 클래스에서 부모 클래스의 메서드를 동일한 이름과 시그니처로 재정의하는 것.

5. **캡슐화(Encapsulation)**
   - 객체의 데이터(속성)와 메서드를 결합하여, 데이터의 접근을 제어하는 메커니즘
   - 데이터를 숨기고(정보 은닉), 외부에서 직접적인 접근을 제한한다.

<br>

### **SOLID 원칙**

객체지향 설계를 할 때 따라야 할 다섯 가지 기본 원칙
<br>
이 원칙들은 소프트웨어 설계를 더 이해하기 쉽고, 유연하며, 유지보수가 쉬운 코드로 만들어준다.

<br>

#### 1. **단일 책임 원칙(Single Responsibility Principle, SRP)**

   - 한 클래스는 하나의 책임만 가져야 한다.
   - 클래스가 변경되어야 하는 이유는 하나여야 한다.

<br>

#### 2. **개방-폐쇄 원칙(Open-Closed Principle, OCP)**

   - 소프트웨어 엔티티(클래스, 모듈, 함수 등)는 확장에는 열려 있어야 하지만, 변경에는 닫혀 있어야 한다.
   - 소프트웨어의 기능을 변경하거나 확장할 때, 기존의 코드를 변경하지 않으면서도 기능의 추가나 변경이 가능해야 한다.
   - 예를 들어, 새로운 기능을 추가하기 위해 이미 검증된 클래스를 수정하기보다 해당 클래스를 확장하여 새로운 기능을 구현한다.

<br>

#### 3. **리스코프 치환 원칙(Liskov Substitution Principle, LSP)**

   - 서브타입은 언제나 기반 타입으로 교체할 수 있어야 한다.
   - 특정 클래스를 사용하는 코드를 변경하지 않고도 해당 클래스의 서브 클래스로 교체할 수 있어야 한다.

   - 예시: 직사각형과 정사각형

        ```python
        class Rectangle:
            def __init__(self, width, height):
                self.width = width
                self.height = height
            
            def set_width(self, width):
                self.width = width
            
            def set_height(self, height):
                self.height = height
        
        class Square(Rectangle):
            def set_width(self, width):
                self.width = width
                self.height = width  # 높이도 함께 변경됨
            
            def set_height(self, height):
                self.height = height
                self.width = height  # 너비도 함께 변경됨
        ```
        - `Rectangle`을 사용하는 코드가 `Square`를 동일한 방식으로 대체하려고 하면 예상과 다르게 동작할 수 있음 → LSP 위반

<br>

#### 4. **인터페이스 분리 원칙(Interface Segregation Principle, ISP)**

   - 클라이언트는 자신이 사용하지 않는 메서드에 의존하지 않아야 하며, 인터페이스는 특정 기능별로 나누어 설계해야 한다.
   - 하나의 큰 인터페이스보다는 작은 여러 개의 인터페이스로 분리하는 것이 좋다.

   - 예시: 다기능 프린터

        ```python
        class IPrinter:
            def print(self):
                pass

        class IScanner:
            def scan(self):
                pass

        class Printer(IPrinter):
            def print(self):
                print("Printing document...")
        
        class Scanner(IScanner):
            def scan(self):
                print("Scanning document...")
        ```
        - `Printer`는 `print` 기능만, `Scanner`는 `scan` 기능만 구현
        - 불필요한 기능을 구현하지 않도록 인터페이스를 분리하여 ISP 준수

<br>

#### 5. **의존성 역전 원칙(Dependency Inversion Principle, DIP)**

   - 고수준 모듈(비즈니스 로직을 담당하는 모듈)은 저수준 모듈(세부적인 기능을 수행하는 모듈)에 직접 의존하면 안 되며, 둘 다 인터페이스나 추상 클래스와 같은 추상화된 계층에 의존해야 한다.

   - 예시: 메시지 전송 시스템

        ```python
        class IMessageSender:
            def send_message(self, message):
                pass
        
        class EmailSender(IMessageSender):
            def send_message(self, message):
                print(f"Sending Email: {message}")
        
        class SmsSender(IMessageSender):
            def send_message(self, message):
                print(f"Sending SMS: {message}")
        
        class Notification:
            def __init__(self, sender: IMessageSender):
                self.sender = sender
            
            def notify(self, message):
                self.sender.send_message(message)
        
        # 사용 예시
        email_notifier = Notification(EmailSender())
        sms_notifier = Notification(SmsSender())
        
        email_notifier.notify("Hello via Email")
        sms_notifier.notify("Hello via SMS")
        ```
        - `Notification` 클래스는 `IMessageSender` 인터페이스에 의존하여 `EmailSender`, `SmsSender`와의 직접적인 결합을 피함 → DIP 준수

<br>

### **정리**

- OOP는 유지보수성과 재사용성을 높이는 중요한 패러다임
- SOLID 원칙을 따르면 더욱 견고하고 확장 가능한 설계를 할 수 있음
- 각 원칙을 이해하고 실제 개발에 적용하는 것이 중요함
