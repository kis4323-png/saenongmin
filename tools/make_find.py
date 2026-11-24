"""새농민 회원 찾기 시안 페이지(src/pages/find.html)를 예시 데이터로 생성합니다.
실제 개발 시에는 DB 조회 결과로 대체됩니다."""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

MEMBERS = [
    ("김○○ · 이○○", "경기 이천시", "햇살들녘농장", "벼", "2026.11", "이달의 새농민"),
    ("박○○ · 최○○", "충북 충주시", "감홍과수원", "사과", "2026.10", "이달의 새농민"),
    ("정○○ · 한○○", "전남 해남군", "푸른목장", "한우", "2026.09", "이달의 새농민"),
    ("강○○ · 오○○", "제주 서귀포시", "귤빛농원", "감귤", "2026.05", "제61회 본상"),
    ("윤○○ · 서○○", "경북 상주시", "곶감마을농원", "감", "2025.12", "이달의 새농민"),
    ("조○○ · 임○○", "강원 평창군", "고랭지채소농장", "배추", "2025.08", "이달의 새농민"),
    ("신○○ · 권○○", "충남 논산시", "딸기향기농장", "딸기", "2025.03", "이달의 새농민"),
    ("황○○ · 문○○", "경남 함안군", "수박골농장", "수박", "2024.07", "제59회 본상"),
]
REGIONS = "서울 부산 대구 인천 광주 대전 울산 세종 경기 강원 충북 충남 전북 전남 경북 경남 제주".split()

CARD = """					<li class="sn-member">
						<div class="sn-member__img sn-ph sn-ph--{ph}" role="img" aria-label="{farm} 사진 자리"></div>
						<div class="sn-member__body">
							<div class="sn-member__badges"><span class="krds-badge {badge}">{award}</span><span class="sn-member__ym">{ym} 수상</span></div>
							<p class="sn-member__name">{name} <span>부부</span></p>
							<dl class="sn-member__info">
								<div><dt>지역</dt><dd>{region}</dd></div>
								<div><dt>농장</dt><dd>{farm}</dd></div>
								<div><dt>주작목</dt><dd>{crop}</dd></div>
							</dl>
						</div>
					</li>"""

cards = []
for i, (name, region, farm, crop, ym, award) in enumerate(MEMBERS):
    badge = "bg-light-point" if "본상" in award else "bg-light-success"
    cards.append(CARD.format(ph=i % 4 + 1, farm=farm, badge=badge, award=award, ym=ym,
                             name=name, region=region, crop=crop))
opts = "\n".join(f"\t\t\t\t\t\t\t<option>{r}</option>" for r in REGIONS)

template = (ROOT / "tools" / "find_template.html").read_text(encoding="utf-8")
page = template.replace("@@REGIONS@@", opts).replace("@@CARDS@@", "\n".join(cards))
(ROOT / "src" / "pages" / "find.html").write_text(page, encoding="utf-8")
print("made src/pages/find.html")
