"""메뉴에 있었지만 아직 없던 페이지 11종 본문을 예시 데이터로 생성합니다.
자료실   : rules.html(정관 및 제규정), video.html(영상자료), song.html(새농민의 노래),
           sign.html(농장간판 설치 안내), forms.html(서식 자료)
농업정보 : policy.html(농업 정책 소식), farming.html(영농 기술 정보), links.html(관련 기관 바로가기)
이용안내 : privacy.html(개인정보처리방침), terms.html(이용약관), noemail.html(이메일무단수집거부)
공통 조각(sub_top, lnb, page, paging)은 make_more_pages.py의 것을 씁니다."""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from make_more_pages import lnb, page, paging, sub_top  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent.parent / "src" / "pages"

ARCHIVE_MENU = [
    ("새농민회 업무자료", "업무자료", "archive.html"),
    ("정관 및 제규정", "정관·규정", "rules.html"),
    ("영상자료", "영상자료", "video.html"),
    ("새농민의 노래", "새농민의 노래", "song.html"),
    ("농장간판 설치 안내", "농장간판", "sign.html"),
    ("서식 자료(공적비 등)", "서식 자료", "forms.html"),
]
INFO_MENU = [
    ("농업 정책 소식", "정책 소식", "policy.html"),
    ("영농 기술 정보", "영농 기술", "farming.html"),
    ("관련 기관 바로가기", "관련 기관", "links.html"),
]
GUIDE_MENU = [
    ("개인정보처리방침", "개인정보처리방침", "privacy.html"),
    ("이용약관", "이용약관", "terms.html"),
    ("이메일무단수집거부", "이메일무단수집거부", "noemail.html"),
]
HELP = """
			<div class="sn-lnb__help">
				<p class="sn-lnb__help-tit">자료 문의</p>
				<p>사무국 <a href="tel:0220805611">02-2080-5611</a></p>
				<p class="sn-lnb__help-time">평일 09시~18시</p>
			</div>"""

LOCK_NOTE = """			<div class="sn-notice-box" role="note">
				<span class="sn-notice-box__ico" aria-hidden="true">
					<svg viewBox="0 0 24 24"><rect x="5" y="10" width="14" height="10" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="currentColor" stroke-width="2"/></svg>
				</span>
				<div class="sn-notice-box__text">
					<p class="sn-notice-box__tit">{tit}</p>
					<p>{txt}</p>
				</div>
				<a href="login.html" class="krds-btn medium primary">로그인</a>
			</div>"""


def file_table(caption, rows, cate_label="분류"):
    """rows: (분류, 제목, 파일종류[], 날짜)"""
    trs = []
    for i, (cate, title, files, date) in enumerate(rows):
        badges = " ".join(f'<span class="sn-file {f.lower()[:3]}">{f}</span>' for f in files)
        trs.append(f"""						<tr>
							<td class="t-num">{len(rows) - i}</td>
							<td class="t-cate">{cate}</td>
							<td class="t-tit"><a href="archive-view.html">{title}</a></td>
							<td class="t-file">{badges}</td>
							<td class="t-date">{date}</td>
						</tr>""")
    return f"""			<div class="krds-table-wrap sn-table">
				<table class="tbl col data">
					<caption>{caption}. 번호, {cate_label}, 제목, 첨부파일, 등록일로 구성되어 있습니다.</caption>
					<colgroup><col class="c-num"><col class="c-cate"><col><col class="c-file"><col class="c-date"></colgroup>
					<thead>
						<tr><th scope="col">번호</th><th scope="col">{cate_label}</th><th scope="col">제목</th><th scope="col">첨부</th><th scope="col">등록일</th></tr>
					</thead>
					<tbody>
{chr(10).join(trs)}
					</tbody>
				</table>
			</div>"""


def write(name, html):
    (OUT / name).write_text(html, encoding="utf-8")
    print("made", name)


# ---------------------------------------------------------------- 자료실: 정관 및 제규정
RULES = [
    ("정관", "(사)한국새농민중앙회 정관", ["HWP", "PDF"], "2026.03.02"),
    ("규정", "회원 관리 규정", ["HWP"], "2026.03.02"),
    ("규정", "이달의 새농민상 선정 및 시상 규정", ["HWP"], "2026.03.02"),
    ("규정", "새농민상 본상 심사 규정", ["HWP"], "2026.03.02"),
    ("규정", "시·도 새농민회 운영 규정", ["HWP"], "2025.02.20"),
    ("규정", "회계 및 재산 관리 규정", ["PDF"], "2025.02.20"),
    ("규정", "임원 선출 규정", ["PDF"], "2025.02.20"),
]
write("rules.html", page(
    sub_top([("자료실", "archive.html"), ("정관 및 제규정", "rules.html")],
            "정관 및 제규정", "새농민회 운영의 기준이 되는 정관과 규정을 확인할 수 있습니다."),
    lnb("자료실", ARCHIVE_MENU, "정관 및 제규정", HELP),
    f"""			<p class="sn-draft-wrap"><span class="sn-draft">규정 목록 예시 · 실제 규정명으로 교체</span></p>
{file_table("정관 및 제규정 목록", RULES)}
			<p class="sn-help-line">규정이 바뀌면 개정 이력과 함께 새 파일을 올려 드립니다. 이전 판이 필요하시면 사무국에 문의해 주세요.</p>""",
))

# ---------------------------------------------------------------- 자료실: 영상자료
VIDEOS = [
    ("창립 60주년 기념식 하이라이트", "2025.11.14", "04:12"),
    ("2026년 정기총회 스케치", "2026.02.27", "02:48"),
    ("이달의 새농민 수상자 인터뷰 – 11월", "2026.11.10", "05:30"),
    ("새농민의 노래 (합창)", "2024.06.01", "03:05"),
    ("청년농 멘토링 현장을 가다", "2026.08.22", "06:18"),
    ("새농민회 소개 영상", "2023.05.15", "03:40"),
]
cards = "\n".join(f"""				<li>
					<a href="#" class="sn-gallery__card sn-video">
						<div class="sn-gallery__img sn-ph sn-ph--{i % 4 + 1}" role="img" aria-label="{t} 영상 미리보기 자리">
							<span class="sn-video__play" aria-hidden="true"></span>
							<span class="sn-video__time"><span class="sr-only">재생 시간 </span>{d}</span>
						</div>
						<div class="sn-gallery__body">
							<p class="sn-gallery__tit">{t}</p>
							<time class="sn-gallery__date">{date}</time>
						</div>
					</a>
				</li>""" for i, (t, date, d) in enumerate(VIDEOS))
write("video.html", page(
    sub_top([("자료실", "archive.html"), ("영상자료", "video.html")],
            "영상자료", "새농민회의 행사와 수상자 이야기를 영상으로 만나보세요."),
    lnb("자료실", ARCHIVE_MENU, "영상자료", HELP),
    f"""			<p class="sn-draft-wrap"><span class="sn-draft">영상 예시 · 유튜브 영상으로 연결</span></p>
			<ul class="sn-gallery">
{cards}
			</ul>
			<p class="sn-help-line">영상은 새농민회 유튜브 채널에서 재생됩니다. 유튜브에 올린 뒤 이 목록에 주소만 추가하면 됩니다.</p>
{paging(3)}""",
))

# ---------------------------------------------------------------- 자료실: 새농민의 노래
write("song.html", page(
    sub_top([("자료실", "archive.html"), ("새농민의 노래", "song.html")],
            "새농민의 노래", "행사 때 함께 부르는 새농민의 노래입니다. 음원과 악보를 내려받을 수 있습니다."),
    lnb("자료실", ARCHIVE_MENU, "새농민의 노래", HELP),
    """			<div class="sn-song">
				<div class="sn-song__player">
					<div class="sn-song__cover sn-ph sn-ph--1" role="img" aria-label="새농민의 노래 표지 자리"></div>
					<div class="sn-song__info">
						<p class="sn-song__tit">새농민의 노래</p>
						<dl class="sn-song__meta">
							<div><dt>작사</dt><dd>○○○</dd></div>
							<div><dt>작곡</dt><dd>○○○</dd></div>
						</dl>
						<p class="sn-draft-wrap"><span class="sn-draft">음원 파일을 받으면 재생 버튼이 생깁니다</span></p>
						<div class="sn-song__btns">
							<a href="#" class="krds-btn medium secondary">음원 내려받기 (MP3)</a>
							<a href="#" class="krds-btn medium tertiary">악보 내려받기 (PDF)</a>
						</div>
					</div>
				</div>
				<section class="sn-song__lyrics" aria-labelledby="lyrics-title">
					<h3 id="lyrics-title" class="sn-song__lyrics-tit">가사 <span class="sn-draft">가사 넣을 자리</span></h3>
					<div class="sn-song__verses">
						<p><strong>1절</strong>사무국에서 받은 1절 가사를 이곳에 넣습니다.<br>한 줄씩 줄을 바꿔 적으면<br>화면에도 그대로 보입니다.</p>
						<p><strong>2절</strong>사무국에서 받은 2절 가사를 이곳에 넣습니다.<br>후렴이 있으면 아래에 따로 적습니다.</p>
						<p><strong>후렴</strong>후렴 가사 자리</p>
					</div>
				</section>
			</div>""",
))

# ---------------------------------------------------------------- 자료실: 농장간판 설치 안내
STEPS = [
    ("신청", "이달의 새농민 또는 본상 수상자가 신청서를 시·도 새농민회에 냅니다."),
    ("확인", "시·도 새농민회가 수상 이력을 확인하고 중앙회에 올립니다."),
    ("제작", "중앙회가 정해진 규격으로 간판을 만듭니다. (약 3~4주)"),
    ("설치", "농장 입구 등 잘 보이는 곳에 설치하고 사진을 보내 주시면 끝입니다."),
]
steps = "\n".join(f"""				<li class="sn-flow__item">
					<span class="sn-flow__no">{i + 1}단계</span>
					<p class="sn-flow__tit">{t}</p>
					<p class="sn-flow__txt">{d}</p>
				</li>""" for i, (t, d) in enumerate(STEPS))
write("sign.html", page(
    sub_top([("자료실", "archive.html"), ("농장간판 설치 안내", "sign.html")],
            "농장간판 설치 안내", "새농민상 수상 농가임을 알리는 농장간판 신청 방법을 안내합니다."),
    lnb("자료실", ARCHIVE_MENU, "농장간판 설치 안내", HELP),
    f"""			<p class="sn-draft-wrap"><span class="sn-draft">절차·규격 예시 · 사무국 확인 필요</span></p>
			<div class="sn-sign">
				<div class="sn-sign__img sn-ph sn-ph--3" role="img" aria-label="농장간판 설치 예시 사진 자리"></div>
				<dl class="sn-sign__info">
					<div><dt>신청 대상</dt><dd>이달의 새농민상·새농민상 본상 수상 농가</dd></div>
					<div><dt>간판 규격</dt><dd>가로 ○○cm × 세로 ○○cm (알루미늄)</dd></div>
					<div><dt>비용</dt><dd>○○ 부담 (사무국 확인 후 기재)</dd></div>
					<div><dt>신청 방법</dt><dd>신청서를 작성해 시·도 새농민회 또는 사무국에 제출</dd></div>
				</dl>
			</div>

			<h3 class="sn-h3">신청 절차</h3>
			<ol class="sn-flow">
{steps}
			</ol>

			<div class="sn-cta">
				<p>신청서는 서식 자료실에서 내려받을 수 있습니다.</p>
				<a href="forms.html" class="krds-btn large primary">신청서 내려받기</a>
			</div>""",
))

# ---------------------------------------------------------------- 자료실: 서식 자료
FORMS = [
    ("간판", "농장간판 설치 신청서", ["HWP"], "2026.03.02"),
    ("공적비", "공적비 건립 신청서", ["HWP"], "2026.03.02"),
    ("공적비", "공적비 문안 작성 예시", ["HWP", "PDF"], "2026.03.02"),
    ("회원", "회원 정보 변경 신청서", ["HWP"], "2026.01.15"),
    ("회원", "신규 회원 가입 신청서", ["HWP"], "2026.01.15"),
    ("시상", "이달의 새농민상 후보자 추천서", ["HWP"], "2025.12.01"),
    ("시상", "새농민상 본상 공적 조서", ["HWP"], "2025.12.01"),
    ("기타", "경조사 지원 신청서", ["HWP"], "2025.06.10"),
]
write("forms.html", page(
    sub_top([("자료실", "archive.html"), ("서식 자료(공적비 등)", "forms.html")],
            "서식 자료", "공적비·농장간판·회원 관련 신청서 양식을 내려받을 수 있습니다."),
    lnb("자료실", ARCHIVE_MENU, "서식 자료(공적비 등)", HELP),
    f"""{LOCK_NOTE.format(tit="서식은 누구나 내려받을 수 있어요.", txt="작성한 서식은 <strong>시·도 새농민회 또는 사무국</strong>에 우편·팩스(02-2080-5612)로 보내 주세요.").replace('<a href="login.html" class="krds-btn medium primary">로그인</a>', '<a href="tel:0220805611" class="krds-btn medium secondary">전화 문의</a>')}
			<p class="sn-draft-wrap"><span class="sn-draft">서식 목록 예시</span></p>
{file_table("서식 자료 목록", FORMS)}""",
))

# ---------------------------------------------------------------- 농업정보: 정책 소식
POLICY = [
    ("농림축산식품부", "공익직불금 신청 안내", "2026.11.20"),
    ("농림축산식품부", "청년농업인 영농정착 지원사업 대상자 모집", "2026.11.14"),
    ("농촌진흥청", "겨울철 시설하우스 안전관리 요령", "2026.11.10"),
    ("농협", "농업인 안전보험 가입 안내", "2026.11.03"),
    ("농림축산식품부", "농산물 가격안정 대책 발표", "2026.10.28"),
    ("농촌진흥청", "신품종 보급 시범사업 참여 농가 모집", "2026.10.21"),
    ("국립농산물품질관리원", "농산물 원산지 표시 제도 안내", "2026.10.15"),
]
rows = "\n".join(f"""						<tr>
							<td class="t-num">{len(POLICY) - i}</td>
							<td class="t-cate">{src}</td>
							<td class="t-tit"><a href="#">{t}</a></td>
							<td class="t-date">{d}</td>
						</tr>""" for i, (src, t, d) in enumerate(POLICY))
write("policy.html", page(
    sub_top([("농업정보", "policy.html"), ("농업 정책 소식", "policy.html")],
            "농업 정책 소식", "농업인이 꼭 알아야 할 정부·기관의 정책 소식을 모았습니다."),
    lnb("농업정보", INFO_MENU, "농업 정책 소식"),
    f"""			<div class="sn-notice-box sn-notice-box--soft" role="note">
				<div class="sn-notice-box__text">
					<p class="sn-notice-box__tit">제목을 누르면 해당 기관의 원문 공고로 이동합니다.</p>
					<p>신청 기간·자격은 바뀔 수 있으니 반드시 원문을 확인해 주세요.</p>
				</div>
			</div>
			<p class="sn-draft-wrap"><span class="sn-draft">게시물 예시 · 실제 공고로 교체</span></p>
			<div class="krds-table-wrap sn-table">
				<table class="tbl col data">
					<caption>농업 정책 소식 목록. 번호, 출처, 제목, 등록일로 구성되어 있습니다.</caption>
					<colgroup><col class="c-num"><col class="c-src"><col><col class="c-date"></colgroup>
					<thead>
						<tr><th scope="col">번호</th><th scope="col">출처</th><th scope="col">제목</th><th scope="col">등록일</th></tr>
					</thead>
					<tbody>
{rows}
					</tbody>
				</table>
			</div>
{paging(12)}""",
))

# ---------------------------------------------------------------- 농업정보: 영농 기술 정보
TIPS = [
    ("과수", "월동 전 나무 관리", "수확이 끝난 과원은 낙엽을 치우고 줄기에 백색 도포제를 발라 동해를 예방합니다."),
    ("시설채소", "하우스 보온·환기", "밤에는 보온 커튼을 쓰고, 맑은 낮에는 짧게 환기해 습도를 낮춰 병 발생을 줄입니다."),
    ("축산", "축사 동파·화재 예방", "급수관 보온재를 점검하고, 난방기 주변 먼지와 전기 배선을 미리 정리합니다."),
    ("식량작물", "논 가을갈이", "볏짚을 넣고 갈아엎으면 땅심이 좋아지고 이듬해 잡초가 줄어듭니다."),
]
tips = "\n".join(f"""				<li class="sn-tip">
					<span class="krds-badge bg-light-secondary">{c}</span>
					<p class="sn-tip__tit">{t}</p>
					<p class="sn-tip__txt">{d}</p>
				</li>""" for c, t, d in TIPS)
write("farming.html", page(
    sub_top([("농업정보", "policy.html"), ("영농 기술 정보", "farming.html")],
            "영농 기술 정보", "이달에 챙겨야 할 농작업과 믿을 수 있는 영농 기술 정보를 안내합니다."),
    lnb("농업정보", INFO_MENU, "영농 기술 정보"),
    f"""			<h3 class="sn-h3">11월 농작업 한눈에 보기 <span class="sn-draft">예시 문안</span></h3>
			<ul class="sn-tips">
{tips}
			</ul>

			<div class="sn-cta">
				<p>작목별 재배 기술과 병해충 정보는 농촌진흥청 <strong>농사로</strong>에서 더 자세히 볼 수 있습니다.</p>
				<a href="https://www.nongsaro.go.kr" class="krds-btn large primary" target="_blank" rel="noopener" title="새 창 열기">농사로 바로가기</a>
			</div>""",
))

# ---------------------------------------------------------------- 농업정보: 관련 기관
GROUPS = [
    ("정부·공공기관", [
        ("농림축산식품부", "농업 정책·보도자료", "https://www.mafra.go.kr"),
        ("농촌진흥청", "농업 기술 연구·보급", "https://www.rda.go.kr"),
        ("국립농산물품질관리원", "원산지·품질 인증", "https://www.naqs.go.kr"),
        ("한국농수산식품유통공사(aT)", "농산물 유통·수출", "https://www.at.or.kr"),
    ]),
    ("농협", [
        ("농협중앙회", "농업인 지원 사업", "https://www.nonghyup.com"),
        ("농협은행", "농업인 금융", "https://banking.nonghyup.com"),
    ]),
    ("영농 정보", [
        ("농사로", "작목별 재배 기술", "https://www.nongsaro.go.kr"),
        ("농산물유통정보(KAMIS)", "오늘의 농산물 가격", "https://www.kamis.or.kr"),
        ("한국농촌경제연구원", "농업 관측·연구", "https://www.krei.re.kr"),
    ]),
]
groups = "\n".join(f"""			<section class="sn-links" aria-labelledby="lg-{gi}">
				<h3 id="lg-{gi}" class="sn-h3">{g}</h3>
				<ul class="sn-links__list">
{chr(10).join(f'''					<li><a href="{u}" class="sn-links__item" target="_blank" rel="noopener" title="새 창 열기"><span class="sn-links__name">{n}</span><span class="sn-links__desc">{d}</span></a></li>''' for n, d, u in items)}
				</ul>
			</section>""" for gi, (g, items) in enumerate(GROUPS))
write("links.html", page(
    sub_top([("농업정보", "policy.html"), ("관련 기관 바로가기", "links.html")],
            "관련 기관 바로가기", "농업인에게 도움이 되는 기관 누리집을 모았습니다. 누르면 새 창으로 열립니다."),
    lnb("농업정보", INFO_MENU, "관련 기관 바로가기"),
    groups,
))

# ---------------------------------------------------------------- 이용안내 3종
def doc_page(name, label, desc, sections, note):
    secs = "\n".join(f"""				<section class="sn-doc__sec">
					<h3>{t}</h3>
{body}
				</section>""" for t, body in sections)
    write(name, page(
        sub_top([("이용안내", name), (label, name)], label, desc),
        lnb("이용안내", GUIDE_MENU, label),
        f"""			<p class="sn-draft-wrap"><span class="sn-draft">{note}</span></p>
			<div class="sn-doc">
{secs}
			</div>""",
    ))


P = lambda *lines: "\n".join(f"\t\t\t\t\t<p>{x}</p>" for x in lines)  # noqa: E731
UL = lambda *items: "\t\t\t\t\t<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"  # noqa: E731

doc_page("privacy.html", "개인정보처리방침",
         "(사)한국새농민중앙회는 회원의 개인정보를 소중히 다룹니다.",
         [
             ("제1조 개인정보의 처리 목적", P("중앙회는 다음 목적을 위해 개인정보를 처리하며, 목적이 바뀌면 미리 동의를 받습니다.") + "\n" + UL("회원 가입·관리 및 본인 확인", "새농민상 추천·심사·시상 업무", "행사 안내 및 소식 전달")),
             ("제2조 처리하는 개인정보 항목", UL("필수: 이름, 아이디, 비밀번호, 휴대전화 번호, 소속 시·도", "선택: 이메일, 농장 이름, 주작목")),
             ("제3조 보유 및 이용 기간", P("회원 탈퇴 시 바로 파기합니다. 다만 법령에서 보관하도록 정한 정보는 그 기간 동안 보관합니다.")),
             ("제4조 제3자 제공", P("중앙회는 정보주체의 동의 또는 법률에 특별한 규정이 있는 경우를 빼고는 개인정보를 제3자에게 제공하지 않습니다.")),
             ("제5조 정보주체의 권리", P("회원은 언제든지 자신의 개인정보를 열람·정정·삭제·처리정지 요구할 수 있으며, 사무국에 서면·전화로 요청하면 지체 없이 조치합니다.")),
             ("제6조 개인정보 보호책임자", UL("개인정보 보호책임자: 이지선", "전화: 02-2080-5611 / 팩스: 02-2080-5612")),
             ("제7조 권익침해 구제 방법", UL('개인정보분쟁조정위원회: 1833-6972 (<a href="https://www.kopico.go.kr" target="_blank" rel="noopener" title="새 창 열기">www.kopico.go.kr</a>)', "개인정보침해신고센터: 국번 없이 118")),
         ],
         "표준 양식 기반 예시 · 시행 전 담당자 검토 필요")

doc_page("terms.html", "이용약관",
         "한국새농민중앙회 누리집 이용에 관한 약속입니다.",
         [
             ("제1조 목적", P("이 약관은 (사)한국새농민중앙회(이하 “중앙회”)가 운영하는 누리집의 이용 조건과 절차, 회원과 중앙회의 권리·의무를 정합니다.")),
             ("제2조 회원 가입", P("누리집 회원은 새농민상 수상자와 그 가족, 농협 임직원 등 중앙회가 정한 자격을 갖춘 분이 가입할 수 있습니다. 가입 신청 후 사무국 확인을 거쳐 승인됩니다.")),
             ("제3조 회원의 의무", UL("다른 사람의 정보를 도용하지 않습니다.", "게시판에 광고·비방·음란물 등 부적절한 글을 올리지 않습니다.", "아이디와 비밀번호를 스스로 관리합니다.")),
             ("제4조 게시물 관리", P("이 약관이나 관련 법령을 어긴 게시물은 사전 통보 없이 숨기거나 삭제할 수 있습니다.")),
             ("제5조 서비스 변경·중단", P("시스템 점검이나 운영상 필요한 경우 누리집 이용을 일시 중단할 수 있으며, 가능한 한 미리 공지합니다.")),
             ("부칙", P("이 약관은 누리집 정식 개설일부터 시행합니다.")),
         ],
         "표준 양식 기반 예시 · 시행 전 담당자 검토 필요")

doc_page("noemail.html", "이메일무단수집거부",
         "누리집에 게시된 이메일 주소의 무단 수집을 거부합니다.",
         [
             ("이메일 주소 무단 수집 거부", P("본 누리집에 게시된 이메일 주소가 전자우편 수집 프로그램이나 그 밖의 기술적 장치를 이용하여 무단으로 수집되는 것을 거부합니다.", "이를 위반하면 「정보통신망 이용촉진 및 정보보호 등에 관한 법률」에 따라 처벌받을 수 있습니다.")),
         ],
         "일반 공공기관 문안 기준")
