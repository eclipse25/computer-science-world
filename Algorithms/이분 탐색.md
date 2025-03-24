## 이분 탐색(Binary Search)

<br>

<img src="../_assets/binary_search.webp" width="500"/>

<br>

이진 탐색은 **정렬된 배열**에서 특정한 값의 위치를 찾아내는 탐색 알고리즘이다. 이 알고리즘의 기본 원리는 탐색 범위를 반으로 줄여가며 데이터를 찾는 것이며, 이 과정을 반복함으로써 검색 속도를 향상시킨다. 이진 탐색은 선형 탐색에 비해 훨씬 빠른 $O(\log n)$의 시간 복잡도를 가진다.

<br>

### 이진 탐색의 원리

1. **초기화:** 탐색을 시작하기 전에, `start`와 `end` 두 포인터를 배열의 가장 낮은 인덱스와 가장 높은 인덱스로 설정한다.
2. **중간점 찾기:** 현재 `start`와 `end` 사이의 중간 위치를 찾는다. 보통 `mid = (start + end) // 2`로 계산한다.
3. **조건 비교:**
   - 만약 `mid` 위치의 값이 찾고자 하는 값(`target`)과 같다면, 위치(`mid`)를 반환한다.
   - 만약 `mid` 위치의 값이 `target`보다 크다면, `target`은 `mid`의 왼쪽에 있을 것이므로, `end`를 `mid - 1`로 조정한다.
   - 만약 `mid` 위치의 값이 `target`보다 작다면, `target`은 `mid`의 오른쪽에 있을 것이므로, `start`를 `mid + 1`로 조정한다.
4. **종료 조건:** `start`가 `end`를 초과할 때까지 위 과정을 반복한다. `start`가 `end`를 초과하는 순간, 배열에 `target` 값이 없다는 것을 의미하며, 탐색을 종료한다.

이진 탐색은 다양한 알고리즘과 데이터 구조(예: 트리 검색, 데이터베이스 쿼리 최적화)에서 사용된다.

<br>

### 재귀적 구현 vs 반복적 구현

이진 탐색은 재귀적(recursive) 또는 반복적(iterative) 방법으로 구현할 수 있다.

<br>

#### 재귀를 이용한 이진 탐색

- 함수가 자기 자신을 호출하는 방식으로, 탐색 범위를 반으로 줄여가며 재귀적으로 탐색한다.
- 코드가 간결하고 이해하기 쉬운 반면, 깊은 재귀로 인한 스택 오버플로우의 위험이 있다.
- 재귀 깊이 제한에 도달하지 않는 상황에서 사용하는 것이 좋다.

```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, right)
```

<br>

#### 반복문을 이용한 이진 탐색

- while 루프를 사용하여 탐색 범위를 반으로 줄여가며 탐색한다.
- 재귀 호출의 오버헤드 없이 구현할 수 있고, 스택 오버플로우의 위험이 없다.
- 대규모 데이터를 처리하는 데 더 적합하다.

```python
def binary_search_iterative(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1
```