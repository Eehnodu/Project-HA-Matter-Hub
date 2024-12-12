# Home Assistant – UI 설계 문서

## 기본 설정

1. HACS (Home Assistant Community Store) 설치
> [!TIP]
> 수동으로 설치할 수도 있으며, README 파일을 보면 수동으로 설치하는 방벙이 나와 있습니다.
    1. 터미널에서 명령어 실행 
        ```
       $ wget -O - https://get.hacs.xyz | bash -
       ```

    2. 재시작 후 통합구성요소에서 HACS 설치

    3. HACS를 통해 설치해야 할 항목 
       - mini-graph-card
       - button-card
       - auto-entities
       - card-mod
       - Flex-Table
       - IPCamLive
  
1. 설정
    1. 영역 및 지역 구성
        - 생산라인1, 생산라인2, 입고장, 출고장, 검수 추가
    2. 테마 추가
        - 폴더 생성 및 테마 다운로드
            - config/themes 폴더 생성 후 원하는 theme.yaml 다운로드
        - 설정 파일 수정
            - configuration.yaml: 
                ```
                frontend:
                themes: !include_dir_merge_named themes
                ```

## Dashboard 설계
1. Overview(공장 현황)
    1. 설정 
        - 제목: 공장 현황
        - URL: overview
        - 유형: Panel
        - 타입: picture-elements
    1. 센서 및 아이콘 구성 
        - **센서 아이콘**: 전구, CO2, CO, 모터 팬, 스프링쿨러(Celling, Side, Default)
        - **센서 아이콘**: 잠금 장치, IPCAM, 알림 경보 장치
    1. 상태에 따른 색상 변경 
        - card-mod 활용:
            ```
            style: |
                :host {--card-mod-icon-color: { 조건문 }}
            ```
1. Status(세부 현황)
    1. 생산라인1 뷰
        - 제목: 생산라인1
        - URL: line1
        - 유형: Section
        - Columns: 3
        - 센서 추가: 온도, 습도, 공기질, 모터 팬, 전구
        - 그래프: 공기질 센서(Co2, CO)
    1. 생산라인2 뷰
        - 제목: 생산라인2
        - URL: line2
        - 유형: Sidebar
        - 센서 추가: 진동 센서, 전구, 진동 제어 스위치
        - 추가 아이콘: 전력 상태, 원격 제어, 엔진
        - 그래프: 진동 센서1, 2, 3
    1. 입고장 뷰
        - 제목: 입고장
        - URL: in
        - 유형: Sidebar
        - 센서 추가: 구역 센서, 입고장 게이트1, 게이트2, 입고 물품 인식 센서, 재고 파악 센서
        - 테이블 구성: 
            - 입고 물품 리스트(항목, 값, 재고, 사용유무)
    1. 출고장 뷰
        - 제목: 출고장
        - URL: out
        - 유형: Sidebar
        - 센서 추가: 구역 센서, 출고장 게이트1, 게이트2, 출고 물품 인식 센서, 출고 파악 센서
        - 그래프: 
            - 출고량 그래프(일별, 주별, 월별 출고량)
    1. 검수 뷰
        - 제목: 검수
        - URL: inspect
        - 유형: Section
        - Columns: 3
        - 센서 추가: 생산라인1, 2 카메라, 생산라인1, 2 제품 인식 센서
        - 테이블 구성: 
            - 라인별 제품 항목(상태, 생산일자, 시리얼 넘버, 생산라인, 제품 버전)
1. Energy(에너지)
    1. 센서 추가: 에너지, 태양광, 가스
    1. 그래프: 
        - 에너지 사용량
        - 태양광 발전량
        - 가스 소비량
    1. 테이블 구성: 
        - 에너지, 태양광, 가스 리스트

1. Safety(안전)
    1. 설정 
        - 제목: 안전
        - URL: safety
        - 유형: Section
        - Columns: 2
    1. 센서 구성: 
        - CO2, CO, 온도
        - 사이렌 센서
        - 스프링쿨러 센서(Celling, Side, Default)
1. Security(보안)
    1. 설정 
        - 제목: 보안
        - URL: security
        - 유형: Sidebar
    1. 센서 추가: 
        - IPCAM 센서(정문1, 2, 3, 후문1, 좌측1, 2, 우측1, 2)
        - 잠금 장치, 출입 기록 센서
    1. 테이블 구성: 
        - 출입기록(이름, 소속, 출입 기록, 퇴근 기록, 출입 위치)

1. Automation(자동화)
    1. 설정 
        - 제목: 자동화
        - URL: auto
        - 유형: Section
    1. 구성: 
        - 자동화 목록 및 설정 페이지 추가

## 필요한 센서 구성
> [!NOTE]
> 현실 세계의 Matter 기기를 고려해야 합니다.
1. 환경 및 모니터링 센서
    - 전구 센서, CO2 센서, CO 센서, 온도계, 습도계, 전력량 센서, 가스 센서, 태양광 센서
2. 제어 및 작동 센서
    - 모터 팬 센서, 진동 센서, 진동 제어 센서, 스프링쿨러 센서, 잠금 장치 센서, 원격 제어 센서, 엔진 센서
3. 보안 및 경보 센서
    - IPCAM, 알림 경보 센서, 사이렌 센서
4. 출입 및 이동 관리 센서
    - 출입 기록 센서, 구역 센서, 게이트 센서, 출고 물품 인식 센서, 출고 파악 센서

## 변경 소스코드
> [!NOTE]
> 홈어시스턴트가 계속 사용하는 디렉토리이므로 수정시 주의가 필요합니다.

1. /HA-matter-hub/core/config/.storage

| 파일/디렉토리 | 설명 |
| --- | --- |
| assistant_pipeline.pipelines | Home Assistant의 음성 비서 기능을 구성할 때 필요한 파이프라인 데이터를 저장 |
| auth | Home Assistant 사용자 인증과 관련된 정보를 저장 (사용자의 로그인 정보, 인증 토큰, 사용 권한 등의 데이터 有) |
| auth_provider.homeassistant | 사용자 계정 및 비밀번호 관련 설정이 포함 |
| bluetooth.passive_update_processor | Home Assistant의 블루투스 장치 관리와 관련 有 |
| core.analytics | 통계와 분석 목적으로 사용되는 Home Assistant의 익명 분석 데이터를 관리 |
| core.area_registry | 설정 > Areas, labels & zones에 있는 데이터 |
| core.config | Home Assistant의 기본 설정 데이터(위치 정보(위도/경도), 시간대, 기본 언어 등의 전역 설정) 저장 |
| core.config_entries | Integration 관련 설정 저장 파일 (Integration을 추가하거나 변경하면 이 파일이 업데이트됨) |
| core.device_registry | 설정 > 기기 및 서비스 > 두번째 기기 탭에 등록된 Device 정보 저장 |
| <code style="color: blue">core.entity_registry</code> | Home Assistant의 Entity 데이터를 저장 |
| core.restore_state | Home Assistant의 장치나 엔티티가 재부팅 후에도 이전 상태를 복원할 수 있도록 저장된 데이터 有 |
| core.uuid | 각 UUID 저장 파일 |
| <code style="color: blue">frontend.user_data_사용자ID</code> | 특정 사용자 별로 설정한 UI 데이터를 저장 (사용자별 커스텀 설정) |
| homeassistant.exposed_entities | Google Assistant, 스마트띵스 같은 외부 통합과 공유되는 엔티티 목록을 저장 |
| http | Home Assistant의 HTTP 서버 설정을 저장 |
| http.auth | HTTP 기반 인증 데이터를 저장 |
| image | Home Assistant의 이미지 관련 데이터를 저장(사용자가 업로드한 아이콘, 배경 이미지有) |
| <code style="color: blue">lovelace_dashboards</code> | Home Assistant에서 사용하는 대시보드의 전체 목록과 구조를 관리 |
| … |  | 
| onboarding | Home Assistant의 초기 설정 마법사와 관련된 데이터를 저장(초기설정이 완료되면 더 이상 사용X) |
| person | Home Assistant에서 사용자(사람)와 관련된 정보를 관리 |
| repairs.issue_registry | Home Assistant에서 발생한 문제를 관리하는 파일 |
| trace.saved_traces | Home Assistant의 자동화 or 스크립트 실행 시 생성된 추적 데이터를 저장 |




