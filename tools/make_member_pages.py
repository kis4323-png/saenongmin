"""시안 페이지 5종 본문을 예시 데이터로 생성합니다.
- grand-award.html : 새농민상 본상 수상자
- board.html       : 열린마당 > 자유게시판
- login.html       : 로그인
- join.html        : 회원가입
- sitemap.html     : 사이트맵
공통 조각(sub_top, lnb, page, paging)은 make_more_pages.py의 것을 씁니다."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from make_more_pages import FIND_MENU, lnb, page, paging, sub_top  # noqa: E402  (실행 시 4개 페이지도 함께 재생성됨)

OUT = pathlib.Path(__file__).resolve().parent.parent / "src" / "pages"
OPEN_MENU = [("자주 묻는 질문", "자주 묻는 질문", "open.html"), ("자유게시판", "자유게시판", "board.html")]

# ---------------------------------------------------------------- 1. 새농민상 본상
ROUNDS = [
    (61, 2026, [("강○○ · 오○○", "제주 서귀포시", "감귤"), ("이○○ · 박○○", "경북 영천시", "포도"), ("최○○ · 김○○", "전북 김제시", "벼")]),
    (60, 2025, [("문○○ · 정○○", "충남 당진시", "한우"), ("한○○ · 윤○○", "경기 여주시", "고구마"), ("서○○ · 조○○", "강원 홍천군", "인삼")]),
    (59, 2024, [("황○○ · 문○○", "경남 함안군", "수박"), ("임○○ · 신○○", "전남 나주시", "배"), ("권○○ · 장○○", "충북 음성군", "복숭아")]),
]
blocks = []
for no, year, people in ROUNDS:
    cards = "\n".join(
        f"""						<li class="sn-member">
							<div class="sn-member__img sn-ph sn-ph--{(i + no) % 4 + 1}" role="img" aria-label="수상자 사진 자리"></div>
							<div class="sn-member__body">
								<div class="sn-member__badges"><span class="krds-badge bg-light-point">제{no}회 본상</span></div>
								<p class="sn-member__name">{name} <span>부부</span></p>
								<dl class="sn-member__info">
									<div><dt>지역</dt><dd>{region}</dd></div>
									<div><dt>주작목</dt><dd>{crop}</dd></div>
								</dl>
							</div>
						</li>"""
        for i, (name, region, crop) in enumerate(people))
    blocks.append(f"""			<section class="sn-round" aria-labelledby="round-{no}">
				<h3 id="round-{no}" class="sn-round__title"><span>제{no}회</span> {year}년 새농민상 본상</h3>
				<ul class="sn-members">
{cards}
				</ul>
			</section>""")

grand = page(
    sub_top([("새농민 찾기", "find.html"), ("새농민상 본상 수상자", "grand-award.html")],
            "새농민상 본상 수상자", "한 해 동안 우리 농업 발전에 가장 큰 공을 세운 새농민을 선정합니다."),
    lnb("새농민 찾기", FIND_MENU, "새농민상 본상 수상자"),
    f"""			<div class="sn-filter sn-filter--inline">
				<label for="g-round" class="sn-finder__label">회차 선택</label>
				<select id="g-round" class="krds-form-select large">
					<option>전체 회차</option>
					<option>제61회 (2026년)</option><option>제60회 (2025년)</option><option>제59회 (2024년)</option><option>제58회 이전</option>
				</select>
				<p class="sn-draft-wrap"><span class="sn-draft">수상자·회차 예시</span></p>
			</div>

{chr(10).join(blocks)}

{paging(20)}""",
)
(OUT / "grand-award.html").write_text(grand, encoding="utf-8")

# ---------------------------------------------------------------- 2. 자유게시판
POSTS = [
    ("농장간판 설치 후기 공유합니다", "김○○", "2026.11.20", 42, 3, True),
    ("올해 감홍 사과 작황 어떠셨나요?", "박○○", "2026.11.18", 67, 8, False),
    ("청년농 멘토링 참여하고 싶습니다", "이○○", "2026.11.15", 88, 5, False),
    ("시·도 회장단 회의 일정 문의", "정○○", "2026.11.11", 35, 1, False),
    ("새농민의 노래 악보 구할 수 있을까요?", "최○○", "2026.11.03", 51, 2, False),
    ("겨울철 비닐하우스 관리 노하우", "강○○", "2026.10.29", 120, 11, False),
    ("60주년 행사 사진 잘 봤습니다", "윤○○", "2026.10.25", 74, 4, False),
    ("드론 방제 같이 하실 분 (경북)", "조○○", "2026.10.20", 59, 6, False),
]
rows = []
for i, (title, writer, date, hit, cmt, new) in enumerate(POSTS):
    no = 352 - i
    newb = ' <span class="sn-new" aria-label="새 글">N</span>' if new else ""
    rows.append(f"""						<tr>
							<td class="t-num">{no}</td>
							<td class="t-tit"><a href="#">{title}</a> <span class="sn-cmt" aria-label="댓글 {cmt}개">[{cmt}]</span>{newb}</td>
							<td class="t-cate">{writer}</td>
							<td class="t-date">{date}</td>
							<td class="t-hit">{hit}</td>
						</tr>""")

board = page(
    sub_top([("열린마당", "open.html"), ("자유게시판", "board.html")],
            "자유게시판", "새농민 회원들이 영농 정보와 소식을 자유롭게 나누는 공간입니다."),
    lnb("열린마당", OPEN_MENU, "자유게시판"),
    f"""			<div class="sn-notice-box sn-notice-box--soft" role="note">
				<div class="sn-notice-box__text">
					<p class="sn-notice-box__tit">누구나 읽을 수 있고, 글쓰기는 회원 로그인 후 가능합니다.</p>
					<p>광고·비방·개인정보가 담긴 글은 운영 원칙에 따라 삭제될 수 있습니다.</p>
				</div>
				<a href="login.html" class="krds-btn medium primary">글쓰기</a>
			</div>

			<form class="sn-search" action="board.html" role="search">
				<label for="b-field" class="sr-only">검색 범위</label>
				<select id="b-field" class="krds-form-select large"><option>제목</option><option>내용</option><option>작성자</option></select>
				<label for="b-keyword" class="sr-only">검색어</label>
				<input id="b-keyword" type="search" class="krds-input large" placeholder="검색어를 입력하세요">
				<button type="submit" class="krds-btn large primary"><i class="svg-icon ico-sch"></i> 검색</button>
			</form>

			<div class="sn-list-head">
				<p class="sn-total">전체 <strong>352</strong>건</p>
				<select class="krds-form-select-sort medium" aria-label="정렬"><option>최신순</option><option>조회순</option><option>댓글순</option></select>
			</div>

			<div class="krds-table-wrap sn-table sn-table--board">
				<table class="tbl col data">
					<caption>자유게시판 목록. 번호, 제목, 작성자, 등록일, 조회수로 구성되어 있습니다.</caption>
					<colgroup><col class="c-num"><col><col class="c-cate"><col class="c-date"><col class="c-hit"></colgroup>
					<thead><tr><th scope="col">번호</th><th scope="col">제목</th><th scope="col">작성자</th><th scope="col">등록일</th><th scope="col">조회</th></tr></thead>
					<tbody>
{chr(10).join(rows)}
					</tbody>
				</table>
			</div>

{paging(36)}""",
)
(OUT / "board.html").write_text(board, encoding="utf-8")

# ---------------------------------------------------------------- 3. 로그인
login = """<main id="container" class="sn-sub sn-auth">
	<div class="inner">
		<div class="sn-auth__box">
			<h2 class="sn-auth__title">로그인</h2>
			<p class="sn-auth__desc">한국새농민중앙회 누리집에 오신 것을 환영합니다.</p>

			<form class="sn-auth__form" action="#" novalidate>
				<div class="sn-finder__tabs" role="radiogroup" aria-label="회원 구분">
					<label><input type="radio" name="mtype" value="member" checked> <span>새농민 회원</span></label>
					<label><input type="radio" name="mtype" value="staff"> <span>농협 직원</span></label>
				</div>

				<div class="sn-auth__field">
					<label for="login-id" class="sn-finder__label">아이디</label>
					<input id="login-id" name="user_id" type="text" class="krds-input xlarge" autocomplete="username" placeholder="아이디를 입력하세요">
				</div>
				<div class="sn-auth__field">
					<label for="login-pw" class="sn-finder__label">비밀번호</label>
					<div class="sn-pw">
						<input id="login-pw" name="user_pw" type="password" class="krds-input xlarge" autocomplete="current-password" placeholder="비밀번호를 입력하세요">
						<button type="button" class="sn-pw__toggle" aria-pressed="false" aria-controls="login-pw">보기</button>
					</div>
				</div>
				<div class="krds-form-check sn-auth__keep">
					<input type="checkbox" id="keep-id" name="keep_id">
					<label for="keep-id">아이디 저장</label>
				</div>

				<button type="submit" class="krds-btn xlarge primary sn-auth__submit">로그인</button>

				<ul class="sn-auth__links">
					<li><a href="#">아이디 찾기</a></li>
					<li><a href="#">비밀번호 찾기</a></li>
					<li><a href="join.html"><strong>회원가입</strong></a></li>
				</ul>
			</form>

			<div class="sn-auth__help">
				<p><strong>로그인이 어려우신가요?</strong></p>
				<p>사무국으로 연락 주시면 도와드립니다. <a href="tel:0220805611">02-2080-5611</a> (평일 09시~18시)</p>
			</div>
		</div>
	</div>
</main>
"""
(OUT / "login.html").write_text(login, encoding="utf-8")

# ---------------------------------------------------------------- 4. 회원가입
REGIONS = "서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주".split()
ropts = "".join(f"<option>{r}</option>" for r in REGIONS)
join = f"""<main id="container" class="sn-sub sn-auth">
	<div class="inner">
		<div class="sn-auth__box sn-auth__box--wide">
			<h2 class="sn-auth__title">회원가입</h2>
			<p class="sn-auth__desc">새농민 회원으로 가입하시면 업무자료 내려받기, 회원 정보 열람 등을 이용할 수 있습니다.</p>

			<ol class="krds-step-wrap sn-steps">
				<li class="done"><span><i class="step">1단계</i><span class="step-tit">약관 동의</span></span></li>
				<li class="active"><span><em class="sr-only">현재단계</em><i class="step">2단계</i><span class="step-tit">정보 입력</span></span></li>
				<li><span><i class="step">3단계</i><span class="step-tit">가입 완료</span></span></li>
			</ol>

			<form class="sn-auth__form" action="#" novalidate>
				<fieldset class="sn-fs">
					<legend>기본 정보 <span class="sn-req-note"><b aria-hidden="true">*</b> 필수 입력</span></legend>

					<div class="sn-auth__field">
						<span class="sn-finder__label">회원 구분 <b class="sn-req" aria-label="필수">*</b></span>
						<div class="sn-finder__tabs" role="radiogroup" aria-label="회원 구분">
							<label><input type="radio" name="mtype" value="member" checked> <span>새농민 회원</span></label>
							<label><input type="radio" name="mtype" value="staff"> <span>농협 직원</span></label>
						</div>
					</div>
					<div class="sn-auth__field">
						<label for="j-name" class="sn-finder__label">이름 <b class="sn-req" aria-label="필수">*</b></label>
						<input id="j-name" type="text" class="krds-input large" autocomplete="name">
					</div>
					<div class="sn-auth__field">
						<label for="j-id" class="sn-finder__label">아이디 <b class="sn-req" aria-label="필수">*</b></label>
						<div class="sn-inline">
							<input id="j-id" type="text" class="krds-input large" autocomplete="username" aria-describedby="j-id-help">
							<button type="button" class="krds-btn large secondary">중복 확인</button>
						</div>
						<p id="j-id-help" class="sn-help">영문 소문자와 숫자 4~12자</p>
					</div>
					<div class="sn-auth__field">
						<label for="j-pw" class="sn-finder__label">비밀번호 <b class="sn-req" aria-label="필수">*</b></label>
						<input id="j-pw" type="password" class="krds-input large" autocomplete="new-password" aria-describedby="j-pw-help">
						<p id="j-pw-help" class="sn-help">영문, 숫자, 특수문자를 섞어 8자 이상</p>
					</div>
					<div class="sn-auth__field">
						<label for="j-pw2" class="sn-finder__label">비밀번호 확인 <b class="sn-req" aria-label="필수">*</b></label>
						<input id="j-pw2" type="password" class="krds-input large" autocomplete="new-password">
					</div>
					<div class="sn-auth__field">
						<label for="j-phone" class="sn-finder__label">휴대전화 <b class="sn-req" aria-label="필수">*</b></label>
						<input id="j-phone" type="tel" class="krds-input large" autocomplete="tel" placeholder="010-0000-0000">
					</div>
				</fieldset>

				<fieldset class="sn-fs">
					<legend>새농민 정보 <span class="sn-req-note">회원 찾기에 공개됩니다</span></legend>
					<div class="sn-grid2">
						<div class="sn-auth__field">
							<label for="j-region" class="sn-finder__label">지역</label>
							<select id="j-region" class="krds-form-select large"><option>선택</option>{ropts}</select>
						</div>
						<div class="sn-auth__field">
							<label for="j-crop" class="sn-finder__label">주작목</label>
							<input id="j-crop" type="text" class="krds-input large" placeholder="예) 사과">
						</div>
					</div>
					<div class="sn-auth__field">
						<label for="j-farm" class="sn-finder__label">농장 이름</label>
						<input id="j-farm" type="text" class="krds-input large" placeholder="예) 햇살농장">
					</div>
					<div class="sn-auth__field">
						<label for="j-award" class="sn-finder__label">수상 내역</label>
						<input id="j-award" type="text" class="krds-input large" placeholder="예) 2026년 11월 이달의 새농민상">
					</div>
				</fieldset>

				<fieldset class="sn-fs">
					<legend>약관 동의</legend>
					<div class="krds-check-area sn-agree">
						<div class="krds-form-check"><input type="checkbox" id="agree-all"><label for="agree-all"><strong>전체 동의</strong></label></div>
						<div class="krds-form-check"><input type="checkbox" id="agree-1" class="sn-agree__item"><label for="agree-1">[필수] 이용약관 동의</label></div>
						<div class="krds-form-check"><input type="checkbox" id="agree-2" class="sn-agree__item"><label for="agree-2">[필수] 개인정보 수집·이용 동의</label></div>
						<div class="krds-form-check"><input type="checkbox" id="agree-3" class="sn-agree__item"><label for="agree-3">[선택] 회원 찾기에 농장 정보 공개</label></div>
					</div>
				</fieldset>

				<div class="sn-auth__btns">
					<a href="login.html" class="krds-btn xlarge tertiary">취소</a>
					<button type="submit" class="krds-btn xlarge primary">가입 신청</button>
				</div>
				<p class="sn-help sn-center">새농민 회원은 사무국 확인 후 가입이 승인됩니다. (1~2일 소요)</p>
			</form>
		</div>
	</div>
</main>
"""
(OUT / "join.html").write_text(join, encoding="utf-8")

# ---------------------------------------------------------------- 5. 사이트맵
SITEMAP = [
    ("새농민회 소개", "about.html", [("인사말", "about.html#greeting"), ("설립목적과 새농민 정신", "about.html#purpose"), ("연혁", "about.html#history"), ("조직도", "about.html#organization"), ("시·도 새농민회", "about.html#regions"), ("찾아오시는 길", "about.html#location")]),
    ("소식", "news.html", [("공지사항", "news.html"), ("중앙회 활동소식", "activity.html"), ("지역 활동소식", "activity.html?type=region"), ("행사일정", "schedule.html")]),
    ("새농민 찾기", "find.html", [("새농민 회원 찾기", "find.html"), ("이달의 새농민 수상자", "awards.html"), ("새농민상 본상 수상자", "grand-award.html")]),
    ("자료실", "archive.html", [("새농민회 업무자료", "archive.html"), ("정관 및 제규정", "#"), ("영상자료", "#"), ("새농민의 노래", "#"), ("농장간판 설치 안내", "#"), ("서식 자료(공적비 등)", "#")]),
    ("농업정보", "#", [("농업 정책 소식", "#"), ("영농 기술 정보", "#"), ("관련 기관 바로가기", "#")]),
    ("열린마당", "open.html", [("자주 묻는 질문", "open.html"), ("자유게시판", "board.html")]),
    ("회원", "login.html", [("로그인", "login.html"), ("회원가입", "join.html"), ("이용약관", "#"), ("개인정보처리방침", "#")]),
]
cols = []
for title, href, items in SITEMAP:
    lis = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in items)
    cols.append(f"""			<section class="sn-sitemap__col">
				<h3><a href="{href}">{title}</a></h3>
				<ul>{lis}</ul>
			</section>""")
sitemap = f"""<main id="container" class="sn-sub">
{sub_top([("사이트맵", "sitemap.html")], "사이트맵", "누리집의 모든 메뉴를 한눈에 볼 수 있습니다.")}
	<div class="inner sn-sitemap">
{chr(10).join(cols)}
	</div>
</main>
"""
(OUT / "sitemap.html").write_text(sitemap, encoding="utf-8")
print("made grand-award, board, login, join, sitemap")
