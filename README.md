# 한국새농민중앙회 누리집 리뉴얼 (시안)

- 기반: KRDS(대한민국 정부 디자인 시스템) HTML 컴포넌트 키트 v1.1.0 (`npm install krds-uiux`)

## 폴더 구조
- `src/partials/header.html`, `footer.html` : 모든 페이지 공통 머리말·꼬리말 (여기만 고치면 전체 반영)
- `src/pages/*.html` : 페이지별 본문
- `tools/build.py` : partials + pages → 루트의 완성 HTML 생성
- `tools/make_find.py`, `find_template.html` : 회원 찾기 예시 데이터 생성
- `tools/make_more_pages.py` : 수상자·활동소식·행사일정·자주 묻는 질문 예시 본문 생성
- `tools/make_member_pages.py` : 본상·자유게시판·로그인·회원가입·사이트맵 예시 본문 생성
- `assets/krds/` : KRDS 키트 리소스 복사본 — 직접 수정하지 말 것
- `assets/css/site.css`, `assets/js/site.js` : 사이트 전용 스타일·스크립트
- 루트 `*.html` : 빌드 결과물 (직접 수정하지 말고 src를 고친 뒤 빌드)

## 페이지
| 파일 | 내용 |
|---|---|
| index.html | 메인 |
| archive.html | 자료실 > 새농민회 업무자료 (목록) |
| archive-view.html | 업무자료 상세보기 |
| find.html | 새농민 찾기 > 새농민 회원 찾기 |
| about.html | 새농민회 소개 (인사말·설립목적·연혁·조직도·시도·오시는 길) |
| news.html, news-view.html | 소식 > 공지사항 목록·상세 |
| activity.html | 소식 > 활동소식 (사진형) |
| schedule.html | 소식 > 행사일정 (달력) |
| awards.html | 새농민 찾기 > 이달의 새농민 수상자 |
| open.html | 열린마당 > 자주 묻는 질문 |
| board.html | 열린마당 > 자유게시판 |
| grand-award.html | 새농민 찾기 > 새농민상 본상 수상자 |
| login.html, join.html | 로그인, 회원가입 |
| sitemap.html | 사이트맵 |

## 빌드·미리보기
```
python tools/build.py
```
상위 폴더에서 `python -m http.server 5182 -d saenongmin` 후 http://localhost:5182

## 교체 필요한 임시 요소
- 로고(assets/img/logo.svg): 실제 CI 파일로 교체
- 사진: 메인 배경·수상자·회원 사진은 그라데이션 자리표시
- 데이터: 행사일정, 수상자·회원 이름, 자료 목록, 회원 수 등은 모두 예시
- 검색·필터·페이지 이동·내려받기: 서버(게시판) 연동 단계에서 구현
