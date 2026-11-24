"""시안 페이지 4종(수상자·활동소식·행사일정·열린마당)의 본문을 예시 데이터로 생성합니다.
결과: src/pages/awards.html, activity.html, schedule.html, open.html
실제 개발 시에는 DB 조회 결과로 대체됩니다."""
import calendar
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "src" / "pages"


def sub_top(crumbs, title, desc):
    items = ['<li class="home"><a href="index.html" class="txt">홈</a></li>']
    for i, (label, href) in enumerate(crumbs):
        cur = ' aria-current="page"' if i == len(crumbs) - 1 else ""
        items.append(f'<li><a href="{href}" class="txt"{cur}>{label}</a></li>')
    return f"""	<div class="sn-sub__top">
		<div class="inner">
			<nav class="krds-breadcrumb-wrap" aria-label="현재 경로" id="breadcrumb">
				<ol class="breadcrumb">
					{''.join(items)}
				</ol>
			</nav>
			<h2 class="sn-sub__title">{title}</h2>
			<p class="sn-sub__desc">{desc}</p>
		</div>
	</div>"""


def lnb(title, items, current, help_html=""):
    pc, mo = [], []
    for label, short, href in items:
        on = label == current
        cur = ' aria-current="page"' if on else ""
        pc.append(f'<li class="lnb-item{" active" if on else ""}"><a href="{href}" class="lnb-btn lnb-link"{cur}>{label}</a></li>')
        mo.append(f'<li><a href="{href}"{cur}>{short}</a></li>')
    nl = "\n\t\t\t\t"
    return f"""		<nav class="krds-side-navigation sn-lnb" aria-label="{title} 메뉴">
			<h2 class="lnb-tit">{title}</h2>
			<ul class="lnb-list">
				{nl.join(pc)}
			</ul>{help_html}
		</nav>

		<nav class="sn-lnb-mobile" aria-label="{title} 메뉴">
			<ul>
				{nl.join(mo)}
			</ul>
		</nav>"""


def page(top, side, content):
    return f"""<main id="container" class="sn-sub">

{top}

	<div class="inner sn-sub__body">

{side}

		<div class="sn-content">
{content}
		</div>
	</div>
</main>
"""


def paging(last):
    return f"""			<div class="krds-pagination sn-paging">
				<span class="page-navi prev disabled">이전</span>
				<div class="page-links">
					<a class="page-link active" href="#" aria-current="page"><span class="sr-only">현재페이지 </span>1</a>
					<a class="page-link" href="#">2</a>
					<a class="page-link" href="#">3</a>
					<span class="page-link link-dot"></span>
					<a class="page-link" href="#">{last}</a>
				</div>
				<a class="page-navi next" href="#">다음</a>
			</div>"""


FIND_MENU = [
    ("새농민 회원 찾기", "회원 찾기", "find.html"),
    ("이달의 새농민 수상자", "이달의 새농민", "awards.html"),
    ("새농민상 본상 수상자", "본상 수상자", "grand-award.html"),
]
NEWS_MENU = [
    ("공지사항", "공지사항", "news.html"),
    ("중앙회 활동소식", "중앙회 활동", "activity.html"),
    ("지역 활동소식", "지역 활동", "activity.html?type=region"),
    ("행사일정", "행사일정", "schedule.html"),
]

# ---------------------------------------------------------------- 1. 이달의 새농민
WINNERS = [
    ("김○○ · 이○○", "경기 이천시", "햇살들녘농장", "벼", "친환경 우렁이 농법으로 쌀 품질을 높이고, 지역 청년농 3명에게 영농 기술을 전수했습니다."),
    ("박○○ · 최○○", "충북 충주시", "감홍과수원", "사과", "고품질 ‘감홍’ 사과 브랜드화로 농가 소득을 높이고, 작목반 공동 선별을 이끌었습니다."),
    ("정○○ · 한○○", "전남 해남군", "푸른목장", "한우", "스마트 축사 도입으로 사육 환경을 개선하고, 마을 복지시설에 꾸준히 나눔을 실천했습니다."),
    ("강○○ · 오○○", "제주 서귀포시", "귤빛농원", "감귤", "타이벡 재배와 체험 농장 운영으로 6차 산업화에 앞장섰습니다."),
]
PAST = [("2026년 10월", 4), ("2026년 9월", 4), ("2026년 8월", 3), ("2026년 7월", 4), ("2026년 6월", 4), ("2026년 5월", 3)]

cards = []
for i, (name, region, farm, crop, merit) in enumerate(WINNERS):
    cards.append(f"""				<li class="sn-winner">
					<div class="sn-winner__img sn-ph sn-ph--{i % 4 + 1}" role="img" aria-label="{farm} 사진 자리"></div>
					<div class="sn-winner__body">
						<span class="krds-badge bg-light-success">{region} · {crop}</span>
						<p class="sn-winner__name">{name} <span>부부</span></p>
						<p class="sn-winner__farm">{farm}</p>
						<p class="sn-winner__merit">{merit}</p>
					</div>
				</li>""")
past = "\n".join(
    f'				<li><a href="#"><span class="sn-past__month">{m}</span><span class="sn-past__cnt">{n}가구 수상</span><i class="svg-icon ico-angle right" aria-hidden="true"></i></a></li>'
    for m, n in PAST)

awards = page(
    sub_top([("새농민 찾기", "find.html"), ("이달의 새농민 수상자", "awards.html")],
            "이달의 새농민 수상자", "매달 우리 농업을 이끄는 새농민을 선정하여 소개합니다."),
    lnb("새농민 찾기", FIND_MENU, "이달의 새농민 수상자"),
    f"""			<div class="sn-month-nav">
				<a href="#" class="krds-btn medium icon border" title="2026년 10월 보기"><span class="sr-only">이전 달</span><i class="svg-icon ico-angle left"></i></a>
				<h3 class="sn-month-nav__title">2026년 <strong>11월</strong> 이달의 새농민</h3>
				<span class="krds-btn medium icon border disabled" aria-disabled="true"><span class="sr-only">다음 달 (없음)</span><i class="svg-icon ico-angle right"></i></span>
			</div>
			<p class="sn-month-nav__desc">선정일 2026.11.05 · 총 {len(WINNERS)}가구 <span class="sn-draft">수상자·공적 예시</span></p>

			<ul class="sn-winners">
{chr(10).join(cards)}
			</ul>

			<section class="sn-past" aria-labelledby="past-title">
				<h3 id="past-title" class="sn-block__sub">지난 수상자 보기</h3>
				<ul class="sn-past__list">
{past}
				</ul>
			</section>""",
)
(OUT / "awards.html").write_text(awards, encoding="utf-8")

# ---------------------------------------------------------------- 2. 활동소식
POSTS = [
    ("중앙회", "농협 10월 정례조회 참석", "2026.10.12"),
    ("충북", "충주 중원농협 ‘감홍’ 사과 품질 평가회", "2026.10.12"),
    ("부산", "부산농협·한국새농민회 농촌 일손돕기", "2026.10.12"),
    ("전남", "해남군지부, 복지시설에 ‘사랑의 쌀’ 전달", "2026.10.12"),
    ("중앙회", "2026년 이달의 새농민상 시상식", "2026.07.06"),
    ("경북", "상주시 새농민회 곶감 작목 교육", "2026.06.18"),
    ("중앙회", "제61회 새농민상 본상 후보자 본선심사", "2026.05.24"),
    ("제주", "제주도회 고문 공적비 제막식", "2026.05.10"),
    ("강원", "평창군 새농민회 고랭지 채소 현장 견학", "2026.04.22"),
]
gal = []
for i, (cat, title, date) in enumerate(POSTS):
    badge = "bg-light-primary" if cat == "중앙회" else "bg-light-success"
    gal.append(f"""				<li>
					<a href="#" class="sn-gallery__card">
						<div class="sn-gallery__img sn-ph sn-ph--{i % 4 + 1}" role="img" aria-label="{title} 사진 자리"></div>
						<div class="sn-gallery__body">
							<span class="krds-badge {badge}">{cat}</span>
							<p class="sn-gallery__tit">{title}</p>
							<time class="sn-gallery__date">{date}</time>
						</div>
					</a>
				</li>""")

activity = page(
    sub_top([("소식", "news.html"), ("활동소식", "activity.html")],
            "활동소식", "중앙회와 전국 시·도 새농민회의 활동을 사진으로 전합니다."),
    lnb("소식", NEWS_MENU, "중앙회 활동소식"),
    f"""			<div class="sn-cate sn-cate--top" role="group" aria-label="소식 구분">
				<button type="button" class="sn-chip is-active" aria-pressed="true">전체</button>
				<button type="button" class="sn-chip" aria-pressed="false">중앙회</button>
				<button type="button" class="sn-chip" aria-pressed="false">지역</button>
			</div>

			<div class="sn-list-head">
				<p class="sn-total">전체 <strong>214</strong>건</p>
				<label for="a-region" class="sr-only">지역 선택</label>
				<select id="a-region" class="krds-form-select-sort medium">
					<option>전체 지역</option><option>경기</option><option>강원</option><option>충북</option><option>충남</option>
					<option>전북</option><option>전남</option><option>경북</option><option>경남</option><option>제주</option>
				</select>
			</div>

			<ul class="sn-gallery">
{chr(10).join(gal)}
			</ul>

{paging(24)}""",
)
(OUT / "activity.html").write_text(activity, encoding="utf-8")

# ---------------------------------------------------------------- 3. 행사일정
YEAR, MONTH, TODAY = 2026, 11, 23
EVENTS = {
    5: [("이달의 새농민 선정 발표", "사무국", "notice")],
    12: [("경기도회 영농기술 교육", "수원 농협교육원", "region")],
    23: [("이달의 새농민상 심사위원회", "농협중앙회 본관", "central")],
    26: [("시·도 회장단 회의", "사무국 회의실", "central")],
    28: [("전남도회 농업인 한마음 대회", "나주시 일원", "region")],
}
WEEK = ["일", "월", "화", "수", "목", "금", "토"]
cal = calendar.Calendar(firstweekday=6)
rows = []
for week in cal.monthdayscalendar(YEAR, MONTH):
    tds = []
    for wi, d in enumerate(week):
        if d == 0:
            tds.append('<td class="is-empty"></td>')
            continue
        cls = []
        if wi == 0:
            cls.append("is-sun")
        if wi == 6:
            cls.append("is-sat")
        if d == TODAY:
            cls.append("is-today")
        evs = "".join(
            f'<span class="sn-cal__ev ev-{k}">{t}</span>' for t, _, k in EVENTS.get(d, []))
        label = f"{MONTH}월 {d}일 {WEEK[wi]}요일" + (" 오늘" if d == TODAY else "") + (f", 일정 {len(EVENTS[d])}건" if d in EVENTS else "")
        tds.append(f'<td class="{" ".join(cls)}"><span class="sn-cal__day" aria-label="{label}">{d}</span>{evs}</td>')
    rows.append("<tr>" + "".join(tds) + "</tr>")
thead = "".join(f'<th scope="col"{" class=is-sun" if i == 0 else (" class=is-sat" if i == 6 else "")}>{w}</th>' for i, w in enumerate(WEEK))
evlist = []
for d in sorted(EVENTS):
    wd = WEEK[(calendar.weekday(YEAR, MONTH, d) + 1) % 7]
    for t, place, k in EVENTS[d]:
        kind = {"central": "중앙회", "region": "지역", "notice": "안내"}[k]
        evlist.append(f"""				<li class="{'is-today' if d == TODAY else ''}">
					<span class="sn-date"><b>{d}</b>{wd}</span>
					<div><span class="sn-kind ev-{k}">{kind}</span><p class="sn-schedule__tit">{t}</p><p class="sn-schedule__place">{place}</p></div>
				</li>""")

schedule = page(
    sub_top([("소식", "news.html"), ("행사일정", "schedule.html")],
            "행사일정", "중앙회와 시·도 새농민회의 행사 일정을 확인하세요."),
    lnb("소식", NEWS_MENU, "행사일정"),
    f"""			<div class="sn-month-nav">
				<a href="#" class="krds-btn medium icon border"><span class="sr-only">이전 달</span><i class="svg-icon ico-angle left"></i></a>
				<h3 class="sn-month-nav__title">{YEAR}년 <strong>{MONTH}월</strong></h3>
				<a href="#" class="krds-btn medium icon border"><span class="sr-only">다음 달</span><i class="svg-icon ico-angle right"></i></a>
			</div>
			<ul class="sn-legend" aria-label="일정 구분">
				<li class="ev-central">중앙회</li><li class="ev-region">지역</li><li class="ev-notice">안내</li>
				<li class="sn-legend__draft"><span class="sn-draft">일정 예시</span></li>
			</ul>

			<div class="sn-cal-wrap">
				<table class="sn-cal">
					<caption class="sr-only">{YEAR}년 {MONTH}월 행사 달력</caption>
					<thead><tr>{thead}</tr></thead>
					<tbody>
						{chr(10).join(rows)}
					</tbody>
				</table>
			</div>

			<section aria-labelledby="evlist-title">
				<h3 id="evlist-title" class="sn-block__sub">{MONTH}월 일정 목록</h3>
				<ol class="sn-schedule__list sn-evlist">
{chr(10).join(evlist)}
				</ol>
			</section>""",
)
(OUT / "schedule.html").write_text(schedule, encoding="utf-8")

# ---------------------------------------------------------------- 4. 열린마당 (자주 묻는 질문)
FAQ = [
    ("회원", "새농민회 회원은 어떻게 될 수 있나요?",
     "새농민상(이달의 새농민상·본상)을 받은 농업인은 새농민회 회원이 될 수 있습니다. 자세한 가입 절차는 거주 지역의 시·도 새농민회 또는 사무국으로 문의해 주세요."),
    ("회원", "누리집 비밀번호를 잊어버렸어요.",
     "로그인 화면의 ‘비밀번호 찾기’에서 휴대전화 인증 후 새 비밀번호를 설정할 수 있습니다. 인증이 어려우시면 사무국(02-2080-5611)으로 연락해 주세요."),
    ("새농민상", "이달의 새농민상 후보는 누가 추천하나요?",
     "지역 농협과 시·도 새농민회의 추천을 거쳐 심사위원회에서 선정합니다. 추천 일정과 서식은 공지사항에서 확인하실 수 있습니다."),
    ("자료실", "업무자료를 내려받을 수 없어요.",
     "업무자료는 새농민 회원과 농협 직원만 내려받을 수 있습니다. 로그인한 뒤에도 내려받을 수 없다면 회원 등급 확인을 위해 사무국으로 문의해 주세요."),
    ("농장간판", "농장간판은 어떻게 신청하나요?",
     "자료실 > 농장간판 설치 안내에서 신청서를 내려받아 작성한 뒤, 시·도 새농민회를 통해 제출하시면 됩니다."),
    ("기타", "제 회원 정보(농장 이름, 주작목)가 바뀌었어요.",
     "로그인 후 ‘내 정보 수정’에서 직접 바꾸시거나, 사무국으로 알려 주시면 수정해 드립니다."),
]
acc = []
for i, (cat, q, a) in enumerate(FAQ, 1):
    acc.append(f"""				<div class="accordion-item">
					<h3 class="accordion-header"><button type="button" id="faq-h{i}" class="btn-accordion" aria-controls="faq-c{i}"><span class="sn-faq__q" aria-hidden="true">Q</span><span class="sn-faq__cat">{cat}</span>{q}</button></h3>
					<div id="faq-c{i}" class="accordion-collapse collapse" aria-labelledby="faq-h{i}">
						<div class="accordion-body"><span class="sn-faq__a" aria-hidden="true">A</span><p>{a}</p></div>
					</div>
				</div>""")

open_page = page(
    sub_top([("열린마당", "open.html"), ("자주 묻는 질문", "open.html")],
            "자주 묻는 질문", "누리집 이용과 새농민회 활동에 대해 자주 묻는 질문을 모았습니다."),
    lnb("열린마당", [("자주 묻는 질문", "자주 묻는 질문", "open.html"), ("자유게시판", "자유게시판", "board.html")], "자주 묻는 질문"),
    f"""			<div class="sn-cate sn-cate--top" role="group" aria-label="질문 분류">
				<button type="button" class="sn-chip is-active" aria-pressed="true">전체</button>
				<button type="button" class="sn-chip" aria-pressed="false">회원</button>
				<button type="button" class="sn-chip" aria-pressed="false">새농민상</button>
				<button type="button" class="sn-chip" aria-pressed="false">자료실</button>
				<button type="button" class="sn-chip" aria-pressed="false">농장간판</button>
				<button type="button" class="sn-chip" aria-pressed="false">기타</button>
			</div>

			<div class="krds-accordion sn-faq">
{chr(10).join(acc)}
			</div>

			<div class="sn-ask">
				<div>
					<p class="sn-ask__tit">원하는 답을 찾지 못하셨나요?</p>
					<p>사무국에 전화로 문의하시거나 자유게시판에 남겨 주세요.</p>
				</div>
				<div class="sn-ask__btns">
					<a href="tel:0220805611" class="krds-btn large primary">02-2080-5611 전화하기</a>
					<a href="board.html" class="krds-btn large secondary">자유게시판</a>
				</div>
			</div>""",
)
(OUT / "open.html").write_text(open_page, encoding="utf-8")
print("made awards, activity, schedule, open")
