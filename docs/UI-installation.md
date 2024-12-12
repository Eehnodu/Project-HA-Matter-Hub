# HA에 타이아 UI 적용 방법

들어가기에 앞서 *홈 어시스턴트*의 사용자 인터페이스 편집 방법에 대해서 간단히 설명하겠습니다.
보통의 경우 *홈 어시스턴트*를 사용하면서 화면을 구성하기 때문에 *홈 어시스턴트*가 제공하는 화면 구성 도구를 사용해서 자신만의 UI를 만듭니다.
또 다른 방법으로 자신이 만든 화면 구성을 단번에 적용시키고 싶을때 **config** 디렉토리와 **configuration** YAML 파일을 이용하는 [방법](https://www.home-assistant.io/dashboards/dashboards/#using-yaml-for-the-overview-dashboard)도 있습니다.
여기서는 이미 만들어진 사용자 인터페이스를 적용하기 때문에 YAML 파일을 이용해서 설정하는 방법을 택합니다.

## **config** 디렉토리 찾기

`시스템 -> 해결하기 -> 시스템정보` 에서 현재 *홈 어시스턴트*가 사용하고 있는 **config** 디렉토리의 위치를 알 수 있습니다.

## 파일 복사하는 방법

*홈 어시스턴트*에 [Samba 애드온](https://github.com/home-assistant/addons/blob/master/samba/DOCS.md)을 이용하면 쉽게 파일을 복사 할 수 있습니다.

## 요약

### 단순 복사
1. 대시보드 설정 복사
    ```
    <HA-Matter-Hub-GitHub>/_config/dashboards/* ==> <Home Assistant>/config/dashboards/
    ```
1. 테마 복사
    ```
    <HA-Matter-Hub-GitHub>/_config/themes/* ==> <Home Assistant>/config/themes/
    ```
1. 리소스 복사
    ```
    <HA-Matter-Hub-GitHub>/_config/www/* ==> <Home Assistant>/config/www/
    ```
1. 파이썬 스크립트 복사
    ```
    <HA-Matter-Hub-GitHub>/_config/python_scripts/* ==> <Home Assistant>/config/python_scripts/
    ```
1. 에너지 흐름 정보 강제로 넣기
    ```
    <HA-Matter-Hub-GitHub>/_config/_storage/energy ==> <Home Assistant>/config/.storage/energy
    ```
1. 통합구성 요소 설치
    ```
    <HA-Matter-Hub-GitHub>/custom_components/* ==> <Home Assistant>/config/custom_components/
    ```
1. 최상위 설정 파일 복사
    ```
    <HA-Matter-Hub-GitHub>/_config/configuration.yaml ==> <Home Assistant>/config/configuration.yaml
    <HA-Matter-Hub-GitHub>/_config/automations.yaml ==> <Home Assistant>/config/automations.yaml
    ```

### *홈 어시스턴트* 사용자 인터페이스로 수작업

1. 대시보드
- `설정 -> 대시보드` 에서 *홈 어시스턴트* 기본 사이드바를 제거합니다.
- `프로필 -> 브라우저 설정` 에서
  - 기본 대시보드를 *공장 현황*으로 선택합니다.
  - `사이드바의 항목 순서 변경 및 숨기기`에서 타이아 사이드바 이외에 모두 숨깁니다.

1. 영역 만들어 주기
- `설정 -> 영역 및 지역` 에서 대시보드에서 사용하는 영역 추가 및 수정
- 현재 다섯 개의 영역이 설정되어 있습니다.
    - 검수
      - 영역ID : living_root
      - 이름 : 검수
      - 아이콘 : 없음
      - 층 : 없음
      - 레이블 추가 : 없음
      - 사진 추가 : 없음
      - 별칭 : 없음
    - 생산라인1
      - 영역ID : saengsanrain1
      - 이름: 생산라인1
      - 아이콘 : 없음
      - 층 : 없음
      - 레이블 추가 : 없음
      - 사진 추가 : 없음
      - 별칭 : 없음
    - 생산라인2
      - 영역ID : saengsanrain2
      - 이름: 생산라인2
      - 아이콘 : 없음
      - 층 : 없음
      - 레이블 추가 : 없음
      - 사진 추가 : 없음
      - 별칭 : 없음
    - 입고장
      - 영역ID : bedroom
      - 이름: 입고장
      - 아이콘 : 없음
      - 층 : 없음
      - 레이블 추가 : 없음
      - 사진 추가 : 있음, 원본 사진 파일 필요!
      - 별칭 : 없음
    - 출고장
      - 영역ID : kitchen
      - 이름: 출고장
      - 아이콘 : 없음
      - 층 : 없음
      - 레이블 추가 : 없음
      - 사진 추가 : 있음, 원본 사진 파일 필요!
      - 별칭 : 없음


## 필요한 파일 복사하기

>[!NOTE]
>TODO

<!--cp _config/www && wget https://github.com/kalkih/mini-graph-card/releases/download/v0.12.1/mini-graph-card-bundle.js-->


## 부족한 부분 *홈 어시스턴트* 사용자 인터페이스로 채우기

*홈 어시스턴트*의 사용자 인터페이스는 설정 파일을 조작으로 변경 불가능한 부분이 있습니다.
여기에 해당하는 사용자 인터페이스는 수작업으로 진행해야 합니다.

### 대시보드 정리

>[!NOTE]
>TODO

### 영역 추가

>[!NOTE]
>TODO
