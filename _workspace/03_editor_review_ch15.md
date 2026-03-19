# Ch 15 통합 검수 리포트

> **검수자:** editor | **검수일:** 2026-03-17 | **판정: PASS**

---

## 1. 본문 검수 (8대 필수 기준)

| # | 기준 | 판정 | 근거 |
|---|------|------|------|
| 1 | 실습 재현성 | PASS | 3개 실습 (A⭐40min, B⭐⭐30min, C⭐⭐40min). 문제 생성→오답 분석→도구 비교 단계적 재현 가능 |
| 2 | 도구 정확성 | PASS | ChatGPT, Claude, Gemini, Perplexity, 잡다 ACCA, 링커리어 CBT + 대기업 5종(GSAT, SKCT, LG Way Fit, HMAT, CJ CAT) + NCS 5영역 비교. 가격·구성 정확 |
| 3 | 사례 검증 | PASS | 4건 — SAGE 6.2~12.9%(A), 링커리어 CBT(A), Samsung GSAT 2025(A), GSAT+ChatGPT 4단계(B). 3A+1B |
| 4 | 시각 자료 | PASS | IMAGE 태그 5개 (infographic×2, concept, before-after, header). 최소 5개 충족 |
| 5 | 워크플로우 일반화 | PASS | Section 7: D-30 AI 시험 대비 파이프라인 (시험분석→기출+AI학습→속도훈련→약점보완→최종점검) |
| 6 | 프롬프트 진화 | PASS | 🔴→🟡→🟢 (L276~L298). 단순 문제요청→유형맞춤→오답기반+시간관리+난이도평가 |
| 7 | Anti-Pattern | PASS | 2건 — "AI 개념만 공부 실전 속도 미훈련"(L342), "AI 문제만 풀고 기출 안봄"(L363) |
| 8 | CC 섹션 참조 | PASS | L452~L453 → `02_cc-specialist_ch15_cc.md` |

## 2. CC 섹션 검수

| 항목 | 판정 | 비고 |
|------|------|------|
| 에이전트 구성 | PASS | problem-generator, answer-checker, weakness-trainer (3 에이전트) |
| 실행 가능성 | PASS | 오답 4분류(개념/함정/부주의/시간), cron daily practice, "기출 70% + AI 30%" 원칙 |
| 난이도 체계 | PASS | ⭐/⭐⭐/⭐⭐⭐ 실습 포함 |

## 3. 이미지 검수

| # | 파일명 | 유형 | 비율 | 삽입위치 | 매칭 |
|---|--------|------|------|----------|------|
| 1 | img_01_header_aptitude_test.png | 헤더 | 16:9 | L455 | MATCH |
| 2 | img_02_infographic_aptitude_tests.png | 인포그래픽 | 4:3 | L63 | MATCH |
| 3 | img_03_concept_test_strategy.png | 개념 | 16:9 | L100 | MATCH |
| 4 | img_04_before_after_test_prompt.png | Before/After | 16:9 | L300 | MATCH |
| 5 | img_05_infographic_anti_pattern.png | Anti-Pattern | 16:9 | L383 | MATCH |

- 테마 컬러: #BD10E0 퍼플 전체 일관 적용 확인
- 5장 모두 2K 해상도

## 4. 차별화 평가 (6대 기준)

| 기준 | 평가 |
|------|------|
| 깊이 | ★★★★★ 대기업 5종 시험 구성 비교, NCS 5영역별 AI 활용법, 잡다 ACCA 게임형 평가 해설 |
| 리얼리즘 | ★★★★★ SAGE 연구 6.2~12.9% 수치, Samsung GSAT 2025 공식 구성(수리20+추리30) |
| 재현성 | ★★★★★ 잡다 튜토리얼(무료), 링커리어 CBT(무료~유료), Anki(무료) — 무료 도구 접근성 우수 |
| 비주얼 | ★★★★☆ 5장 기준 충족, 벤 다이어그램(AI+기출+간격반복)이 전략 핵심을 시각화 |
| 정직성 | ★★★★★ "AI 문제≠기출 난이도" 명확히 경고, "기출이 기준, AI는 보조" 원칙 제시 |
| 확장성 | ★★★★★ D-30 파이프라인이 자격증, 전공필기, 공무원 시험 등 모든 객관식 시험에 적용 가능 |

## 5. 최종 판정

**PASS** — 출판 가능 상태. "AI 학습 + 기출 검증" 투트랙 전략이 교재의 핵심 메시지. 대기업 인적성 5종 비교표와 NCS 5영역별 도구 매칭이 실전적이며, "속도 훈련 없이 개념만 공부하는 실수"를 Anti-Pattern으로 경고한 점이 실용적.
