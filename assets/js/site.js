// 새농민 사이트 전용 스크립트
// KRDS ui-script.js가 메뉴·탭·글자크기 등 공통 동작을 처리하고,
// 여기에는 사이트 고유 동작만 둡니다.

document.addEventListener('DOMContentLoaded', () => {
	// 새농민 찾기: 실제 검색 페이지 연결 전까지 임시 처리
	const finder = document.querySelector('.sn-finder');
	if (finder) {
		finder.addEventListener('submit', (e) => {
			e.preventDefault();
			const keyword = finder.querySelector('#f-keyword').value.trim();
			if (!keyword) {
				finder.querySelector('#f-keyword').focus();
				return;
			}
			// TODO: 검색 결과 페이지(예: /find.html?q=)로 연결
			alert(`'${keyword}' 검색 결과 페이지는 다음 단계에서 연결됩니다.`);
		});
	}
});

// 자료실 분류 칩: 선택 상태 전환 (실제 필터링은 서버 연동 단계에서 구현)
document.addEventListener('DOMContentLoaded', () => {
	const chips = document.querySelectorAll('.sn-cate .sn-chip');
	chips.forEach((chip) => {
		chip.addEventListener('click', () => {
			chips.forEach((c) => {
				c.classList.remove('is-active');
				c.setAttribute('aria-pressed', 'false');
			});
			chip.classList.add('is-active');
			chip.setAttribute('aria-pressed', 'true');
		});
	});
});

// 상세보기: 주소 복사
document.addEventListener('DOMContentLoaded', () => {
	const btn = document.querySelector('.sn-copy-link');
	if (!btn) return;
	btn.addEventListener('click', async () => {
		try {
			await navigator.clipboard.writeText(location.href);
			btn.lastChild.textContent = ' 복사됨';
		} catch (e) {
			window.prompt('아래 주소를 복사하세요.', location.href);
		}
	});
});

// 소개 페이지: 스크롤 위치에 따라 좌측(모바일 상단) 메뉴 현재 항목 표시
document.addEventListener('DOMContentLoaded', () => {
	const sections = document.querySelectorAll('.sn-about-page .sn-block[id]');
	if (!sections.length || !('IntersectionObserver' in window)) return;
	const pcItems = document.querySelectorAll('.sn-lnb .lnb-item');
	const links = document.querySelectorAll('.sn-lnb a[href^="#"], .sn-lnb-mobile a[href^="#"]');

	const setActive = (id) => {
		links.forEach((a) => {
			const on = a.getAttribute('href') === `#${id}`;
			if (on) a.setAttribute('aria-current', 'true');
			else a.removeAttribute('aria-current');
			if (on && a.closest('.sn-lnb-mobile')) {
				a.scrollIntoView({ block: 'nearest', inline: 'center' });
			}
		});
		pcItems.forEach((li) => {
			li.classList.toggle('active', li.querySelector('a').getAttribute('href') === `#${id}`);
		});
	};

	const observer = new IntersectionObserver((entries) => {
		entries.forEach((entry) => {
			if (entry.isIntersecting) setActive(entry.target.id);
		});
	}, { rootMargin: '-20% 0px -70% 0px' });
	sections.forEach((s) => observer.observe(s));
});

// 다른 페이지에서 about.html#location 처럼 들어올 때: 로딩이 끝난 뒤 위치 다시 맞추기
window.addEventListener('load', () => {
	if (!location.hash) return;
	const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
	if (target) target.scrollIntoView({ behavior: 'instant', block: 'start' });
});

// 자주 묻는 질문: 분류 칩으로 질문 거르기
document.addEventListener('DOMContentLoaded', () => {
	const faq = document.querySelector('.sn-faq');
	if (!faq) return;
	document.querySelectorAll('.sn-cate .sn-chip').forEach((chip) => {
		chip.addEventListener('click', () => {
			const cat = chip.textContent.trim();
			faq.querySelectorAll('.accordion-item').forEach((item) => {
				const itemCat = item.querySelector('.sn-faq__cat').textContent.trim();
				item.hidden = !(cat === '전체' || cat === itemCat);
			});
		});
	});
});

// 로그인: 비밀번호 보기/숨기기
document.addEventListener('DOMContentLoaded', () => {
	document.querySelectorAll('.sn-pw__toggle').forEach((btn) => {
		btn.addEventListener('click', () => {
			const input = document.getElementById(btn.getAttribute('aria-controls'));
			const show = input.type === 'password';
			input.type = show ? 'text' : 'password';
			btn.textContent = show ? '숨기기' : '보기';
			btn.setAttribute('aria-pressed', String(show));
		});
	});
});

// 회원가입: 약관 전체 동의
document.addEventListener('DOMContentLoaded', () => {
	const all = document.getElementById('agree-all');
	if (!all) return;
	const items = document.querySelectorAll('.sn-agree__item');
	all.addEventListener('change', () => items.forEach((i) => { i.checked = all.checked; }));
	items.forEach((i) => i.addEventListener('change', () => {
		all.checked = [...items].every((x) => x.checked);
	}));
});
