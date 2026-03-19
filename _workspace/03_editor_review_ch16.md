# Ch 16 통합 검수 리포트

> **검수자:** editor | **검수일:** 2026-03-17 | **판정: PASS**

---

## 1. 본문 검수 (8대 필수 기준)

| # | 기준 | 판정 | 근거 |
|---|------|------|------|
| 1 | 실습 재현성 | PASS | 3개 실습 (A⭐30min, B⭐⭐40min, C⭐⭐40min). 채용공고 분석→산업 비교→경력 로드맵 단계적 재현 가능 |
| 2 | 도구 정확성 | PASS | ChatGPT, Claude, Perplexity, Google Career Dreamer(2025.12 출시, 무료), CareerExplorer, Teal. 가격·출시일 정확 |
| 3 | 사례 검증 | PASS | 4건 — RAG 2,047%(A), NACE(A), USF AI Toolkit(A), NCDA 원칙(A). **4A — Part 5 최고 사례 품질** |
| 4 | 시각 자료 | PASS | IMAGE 태그 5개 (infographic×2, concept, before-after, header). 최소 5개 충족 |
| 5 | 워크플로우 일반화 | PASS | Section 7: AI 직무 탐색 5단계 파이프라인 (자기탐색→시장조사→역량매칭→경력설계→실행+검증) |
| 6 | 프롬프트 진화 | PASS | 🔴→🟡→🟢 (L269~L293). 일반 직무정보→산업맥락→역량매칭+갭분석+6개월로드맵 |
| 7 | Anti-Pattern | PASS | 2건 — "AI 추천 맹신 — 데이터 편향"(L331), "AI 커리어 테스트 확증 편향"(L352) |
| 8 | CC 섹션 참조 | PASS | L439~L440 → `02_cc-specialist_ch16_cc.md` |

## 2. CC 섹션 검수

| 항목 | 판정 | 비고 |
|------|------|------|
| 에이전트 구성 | PASS | job-analyst, skill-matcher(0~100), strategy-planner (3 에이전트) |
| 실행 가능성 | PASS | Part 5 통합(Ch13~16), 취업 대시보드, my_profile.md 공통 입력 패턴 |
| 난이도 체계 | PASS | ⭐/⭐⭐/⭐⭐⭐ 실습 포함 |

## 3. 이미지 검수

| # | 파일명 | 유형 | 비율 | 삽입위치 | 매칭 |
|---|--------|------|------|----------|------|
| 1 | img_01_header_job_analysis.png | 헤더 | 16:9 | L442 | MATCH |
| 2 | img_02_infographic_job_tools.png | 인포그래픽 | 4:3 | L63 | MATCH |
| 3 | img_03_concept_job_frameworks.png | 개념 | 16:9 | L95 | MATCH |
| 4 | img_04_before_after_job_prompt.png | Before/After | 16:9 | L295 | MATCH |
| 5 | img_05_infographic_anti_pattern.png | Anti-Pattern | 16:9 | L371 | MATCH |

- 테마 컬러: #BD10E0 퍼플 전체 일관 적용 확인
- 5장 모두 2K 해상도

## 4. 차별화 평가 (6대 기준)

| 기준 | 평가 |
|------|------|
| 깊이 | ★★★★★ 직무 분석 3프레임워크(JD/산업구조/역량갭), 2026 채용 시장 데이터(RAG 2,047%, 경력무관 42.6%) |
| 리얼리즘 | ★★★★★ 커리어온뉴스/잡코리아 실제 데이터, Google Career Dreamer 실제 도구 소개 |
| 재현성 | ★★★★★ 채용공고 복사→ChatGPT 분석이 즉시 실행 가능, Career Dreamer 무료 |
| 비주얼 | ★★★★☆ 5장 기준 충족, 삼각형 프레임워크 다이어그램이 핵심 개념 시각화 |
| 정직성 | ★★★★★ NCDA "최종 결정은 인간 가치관" 인용, AI 추천 맹신·확증 편향 이중 경고 |
| 확장성 | ★★★★★ 5단계 파이프라인이 전과, 진학, 창업, 이직 등 모든 커리어 의사결정에 적용 가능 |

## 5. 최종 판정

**PASS** — 출판 가능 상태. Part 5의 마무리 챕터로서 Ch13~15의 개별 취업 준비를 "직무 탐색→경력 설계"로 통합하는 역할을 훌륭히 수행. 사례 4건 모두 A급(Part 5 최고). "AI 추천 맹신"과 "확증 편향" 두 가지 Anti-Pattern이 커리어 AI 도구의 구조적 한계를 정확히 짚음.

---

## Part 5 전체 검수 완료 요약

| 챕터 | 본문 | CC | 이미지 | 최종 |
|------|------|-----|--------|------|
| Ch13 자기소개서·포트폴리오 | PASS (8/8) | PASS | PASS (6/6 MATCH) | **PASS** |
| Ch14 면접 준비 전략 | PASS (8/8) | PASS | PASS (5/5 MATCH) | **PASS** |
| Ch15 인적성·필기시험 대비 | PASS (8/8) | PASS | PASS (5/5 MATCH) | **PASS** |
| Ch16 직무 분석 및 탐색 | PASS (8/8) | PASS | PASS (5/5 MATCH) | **PASS** |

- **총 이미지:** 21장 (Ch13: 6, Ch14: 5, Ch15: 5, Ch16: 5)
- **테마 컬러:** #BD10E0 퍼플 — 전 챕터 일관 적용
- **Part 5 특이 사항:** 실습 포맷이 Parts 1~4와 약간 다름 (### 실습 A: / ✅ 체크포인트: / 🔧 트러블슈팅:) — Part 5 내부 일관성 유지되므로 문제 없음
- **my_profile.md 공통 입력:** CC 섹션에서 Ch13~16이 동일한 사용자 프로필을 공유하는 설계 — Part 5 통합성 우수
