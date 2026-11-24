"""
새농민 시안 페이지 빌드 스크립트

src/partials/header.html + src/pages/<페이지>.html + src/partials/footer.html
을 합쳐서 루트에 완성된 HTML을 만듭니다.
헤더·푸터는 한 곳(src/partials)만 고치면 모든 페이지에 반영됩니다.

사용법 (saenongmin 폴더에서):  python tools/build.py
"""
import pathlib
import re
import time

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "src"

SITE = "한국새농민중앙회"
MENUS = ["about", "news", "find", "archive", "info", "open"]

# 파일명: (제목, 설명, 주메뉴 키, 메뉴에서 현재 위치로 표시할 링크)
PAGES = {
    "index.html": (
        f"{SITE} | 21세기 한국 농업, 새농민이 함께합니다",
        "(사)한국새농민중앙회 공식 누리집. 새농민회 소식, 이달의 새농민 수상자, 새농민 회원 찾기, 업무자료를 안내합니다.",
        None,
        None,
    ),
    "about.html": (
        f"새농민회 소개 | {SITE}",
        "(사)한국새농민중앙회 인사말, 설립목적과 새농민 정신, 연혁, 조직도, 시·도 새농민회, 찾아오시는 길을 안내합니다.",
        "about",
        None,
    ),
    "news.html": (
        f"공지사항 | 소식 | {SITE}",
        "한국새농민중앙회의 주요 안내와 공지사항입니다.",
        "news",
        "news.html",
    ),
    "news-view.html": (
        f"2026년도 정기총회 개최 안내 | 공지사항 | {SITE}",
        "2026년도 (사)한국새농민중앙회 정기총회 개최 안내입니다.",
        "news",
        "news.html",
    ),
    "archive.html": (
        f"새농민회 업무자료 | 자료실 | {SITE}",
        "새농민회 현황, 회의자료, 사업계획, 수상자 명단 등 업무자료를 제공합니다.",
        "archive",
        "archive.html",
    ),
    "archive-view.html": (
        f"2026년 4분기 시·도 회장단 회의 자료 | 새농민회 업무자료 | {SITE}",
        "2026년 4분기 시·도 회장단 회의 자료입니다.",
        "archive",
        "archive.html",
    ),
    "find.html": (
        f"새농민 회원 찾기 | 새농민 찾기 | {SITE}",
        "지역, 이름, 농장 이름, 주작목으로 전국의 새농민 회원을 찾아보세요.",
        "find",
        "find.html",
    ),
    "awards.html": (
        f"이달의 새농민 수상자 | 새농민 찾기 | {SITE}",
        "매달 우리 농업을 이끄는 이달의 새농민 수상자를 소개합니다.",
        "find",
        "awards.html",
    ),
    "activity.html": (
        f"활동소식 | 소식 | {SITE}",
        "중앙회와 전국 시·도 새농민회의 활동을 사진으로 전합니다.",
        "news",
        "activity.html",
    ),
    "schedule.html": (
        f"행사일정 | 소식 | {SITE}",
        "중앙회와 시·도 새농민회의 행사 일정을 확인하세요.",
        "news",
        "schedule.html",
    ),
    "open.html": (
        f"자주 묻는 질문 | 열린마당 | {SITE}",
        "누리집 이용과 새농민회 활동에 대해 자주 묻는 질문입니다.",
        "open",
        "open.html",
    ),
    "grand-award.html": (
        f"새농민상 본상 수상자 | 새농민 찾기 | {SITE}",
        "회차별 새농민상 본상 수상자를 소개합니다.",
        "find",
        "grand-award.html",
    ),
    "board.html": (
        f"자유게시판 | 열린마당 | {SITE}",
        "새농민 회원들이 영농 정보와 소식을 나누는 자유게시판입니다.",
        "open",
        "board.html",
    ),
    "login.html": (
        f"로그인 | {SITE}",
        "한국새농민중앙회 누리집 로그인",
        None,
        "login.html",
    ),
    "join.html": (
        f"회원가입 | {SITE}",
        "한국새농민중앙회 누리집 회원가입",
        None,
        "join.html",
    ),
    "sitemap.html": (
        f"사이트맵 | {SITE}",
        "한국새농민중앙회 누리집 전체 메뉴",
        None,
        "sitemap.html",
    ),
}


def build_header(title, desc, menu, nav_href):
    h = (SRC / "partials" / "header.html").read_text(encoding="utf-8")
    h = h.replace("{{title}}", title).replace("{{description}}", desc)
    for key in MENUS:
        on = key == menu
        h = h.replace("{{cur:%s}}" % key, " sn-current" if on else "")
        h = h.replace("{{curattr:%s}}" % key, ' aria-current="true"' if on else "")
    if nav_href:
        h = re.sub(r'href="%s"' % re.escape(nav_href), f'href="{nav_href}" aria-current="page"', h)
    return h


VERSION = time.strftime("%Y%m%d%H%M")


def main():
    version = time.strftime("%Y%m%d%H%M%S")  # CSS·JS 캐시 방지용 버전
    footer = (SRC / "partials" / "footer.html").read_text(encoding="utf-8")
    for name, (title, desc, menu, nav_href) in PAGES.items():
        body = (SRC / "pages" / name).read_text(encoding="utf-8")
        html = build_header(title, desc, menu, nav_href) + "\n" + body.rstrip() + "\n\n" + footer
        html = html.replace("{{ver}}", version)
        leftover = re.findall(r"\{\{[^}]+\}\}", html)
        if leftover:
            raise SystemExit(f"{name}: 치환되지 않은 자리표시 {leftover}")
        (ROOT / name).write_text(html, encoding="utf-8")
        print("built", name)


if __name__ == "__main__":
    main()
