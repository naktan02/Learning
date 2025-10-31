# Starcraft 3종족 확장 과제 

## 현재 상황

## 구현 완료

현재 테란 (Terran) 종족만 구현되어 있습니다.

- Marine: 원거리 보병 유닛
- Dropship: Marine 수송선

확장 요구사항

다음 두 종족을 추가로 구현해야 합니다.

- 프로토스 (Protoss) 종족
- 저그 (Zerg) 종족


## 유닛 스펙 명세

테란 (Terran) - 이미 구현됨

## Marine (마린)

- 이동 방식: 지상 (걷기)
- 공격 타입: 원거리 (머신건)
- 공격 대상: 공중 + 지상
- 체력: HP 100
- 공격력: 5


## Dropship (드랍쉽)

- 이동 방식: 공중 (비행)
- 공격 능력: 없음
- 특수 능력: Marine 최대 8기 탑승
- 체력: HP 200

프로토스 (Protoss) - 구현 필요

## Zealot (질럿)

- 이동 방식: 지상 (걷기)
- 공격 타입: 근거리 (사이오닉 검)
- 공격 대상: 지상만
- 체력: HP 100 + 보호막 100
- 공격력: 16

# 특이사항: 

- 프로토스 종족은 보호막(Shield) 시스템을 가짐
- 데미지는 보호막부터 소진되고, 보호막이 0 이 되면 HP가 감소
- 보호막은 시간이 지나면 자동 회복 가능


## Shuttle (셔틀)

- 이동 방식: 공중 (비행)
- 공격 능력: 없음
- 특수 능력: Zealot 최대 8기 탑승
- 체력: HP 200

저그 (Zerg) - 구현 필요 $\square$

## Zergling (저글링)

- 이동 방식: 지상 (걷기)
- 공격 타입: 근거리 (발톱)
- 공격 대상: 지상만
- 체력: HP 50
- 공격력: 5


## Overlord (오버로드)

- 이동 방식: 공중 (비행)
- 공격 능력: 없음
- 특수 능력: Zergling 최대 8마리 탑승
- 체력: HP 200


## 설계 고민 질문

이 요구사항을 구현하기 전에 다음 질문들을 고민해보세요:

## 질문 1: 공통점과 차이점

6개 유닛(Marine, Dropship, Zealot, Shuttle, Zergling, Overlord)의 공통점과 차이점은 무엇인가요?

## 힌트:

- 모든 유닛이 공통으로 가지는 속성은?
- 이동 방식의 차이는?
- 공격 능력의 차이는?


## 질문 2: 현재 설계의 문제점

현재 Dropship은 Marine만 탑승할 수 있습니다. Shuttle과 Overlord는 어떻게 구현해야 할까요?

# 현재 Dropship 코드: 

```
class Dropship(...) {
    private val units: Array<Marine?> = arrayOfNulls(8)
    fun takeMarine(unit: Marine): Int {
        // Marine만 태울 수 있음!
    }
}
```


## 고민해볼 점:

- Shuttle도 똑같이 takeZealot( ) 메서드를 만들어야 하나?
- Overlord도 똑같이 takeZergling( ) 메서드를 만들어야 하나?
- 코드 중복을 어떻게 제거할 수 있을까?


## 질문 3: 공격 시스템 설계

Marine은 공중+지상을 공격하고, Zealot은 지상만 공격합니다. 어떻게 구분할까요?

## 현재 IAttackable:

```
interface IAttackable {
    fun attack() // 공격만 가능, 세부 정보 없음
}
```


## 고민해볼 점:

- 공격력(damage) 정보는 어디에?
- 공격 대상(공중 vs 지상) 구분은 어떻게?
- 원거리 vs 근거리 공격 구분은 필요한가?

## 질문 4: 보호막 시스템

Zealot은 HP 100 + 보호막 100을 가집니다. 어떻게 구현해야 할까요?

## 현재 AbstractUnit:

```
abstract class AbstractUnit(...) {
    protected var hp: Int = 0 // HP만 존재
}
```


## 설계 옵션들:

1. AbstractUnit에 shield 속성 추가?

- 문제점: 모든 유닛이 보호막을 가지게 됨 (Marine, Zergling도!)

2. IShielded 인터페이스 생성?

- Zealot만 구현
- 다른 Protoss 유닛도 있다면?

3. Zealot 클래스에서 직접 관리?

- 다른 Protoss 유닛은 어떻게?


# "구현 가이드라인 

필수 구현 사항

- Zealot 클래스 구현
- Zergling 클래스 구현
- Shuttle 클래스 구현
- Overlord 클래스 구현
- 보호막 시스템 (Zealot)
- 데모 프로그램 (3종족 유닛 생성 및 이동 테스트)


## 설계 원칙 준수

- ISP (Interface Segregation Principle): 필요한 인터페이스만 구현
- DRY (Don't Repeat Yourself): 코드 중복 최소화
- OCP (Open-Closed Principle): 확장에 열려있고 수정에 닫혀있는 설계


## 고려사항

1. 타입 안전성: Dropship에는 Marine만, Shuttle에는 Zealot만 탑승 가능
2. 코드 재사용: 수송선의 공통 로직 재사용 방법
3. 확장성: 나중에 새로운 유닛이 추가될 수 있음

## 토론 주제

강의 시간에 다음 주제들을 토론합니다:
토론 1: "코드 중복 vs 복잡도"
각 수송선마다 별도 클래스를 만들면 구현은 쉽지만 코드가 중복됩니다. 제네릭을 사용하면 코드 중복은 줄지만 복잡도가 증가 합니다. 어떤 것이 더 나은 설계일까요?

## 토론 2: "인터페이스 설계"

공격 시스템을 다음 중 어떻게 설계하는 것이 좋을까요?

- 옵션 A: IAttackable 하나로 모든 공격 처리
- 옵션 B: IMeleeAttack, IRangedAttack 분리
- 옵션 C: IAttackGround, IAttackAir 분리

- 옵션 D: B + C 조합
- 다른 방법?

토론 3: "보호막 구현 위치"
Zealot의 보호막을 어디에 구현하는 것이 ISP 원칙에 맞을까요?

- AbstractUnit? (모든 유닛이 shield 속성 가짐)
- IShielded 인터페이스? (필요한 유닛만 구현)
- Zealot 클래스 내부? (확장성 부족)


# 참고 사항 

## Kotlin 활용 기능

- 클래스 상속 (Inheritance)
- 인터페이스 다중 구현 (Multiple Interfaces)
- 추상 클래스 (Abstract Class)
- 제네릭 (Generics) - 선택사항
- Extension Functions
- Data Class


## 학습 목표

이 과제를 통해 다음을 학습합니다:

1. 객체 지향 설계 원칙 실전 적용
2. 인터페이스 분리의 중요성
3. 코드 재사용 방법론
4. 타입 안전성 확보 기법
5. 확장 가능한 구조 설계

## 보너스 과제 (선택)

더 도전하고 싶다면:
레벨 1: 공격 시스템 고도화

- 실제 데미지 계산 (HP 감소)
- 공격 대상 유효성 검증 (지상 유닛이 공중 유닛 공격 불가)
- 유닛 사망 처리

레벨 2: Factory Pattern 적용

- 종족별 유닛 생성을 Factory로 관리
- UnitFactory.createBasicUnit(Race.TERRAN) $\rightarrow$ Marine

레벨 3: 전투 시뮬레이션

- Marine vs Zealot 전투 구현
- 보호막 회복 메커니즘
- 전투 로그 출력

과제 목표: 확장 가능하고 유지보수하기 쉬운 객체 지향 설계를 경험하기
핵심 메시지: "코드는 동작하는 것도 중요하지만, 아름다운 설계는 더 중요합니다"

