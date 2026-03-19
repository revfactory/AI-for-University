# Ch18 통합 검수 리포트

## 기본 정보
- **챕터:** Ch 18. AI를 활용한 문제 해결 프로젝트
- **파트:** Part 6 — 프로젝트·심화
- **테마 컬러:** #E74C3C 레드
- **검수일:** 2026-03-17
- **판정:** ✅ PASS

---

## 1. 콘텐츠 8대 필수 기준

| # | 기준 | 판정 | 근거 |
|---|------|------|------|
| 1 | 튜토리얼 재현성 | ✅ PASS | 실습 A(⭐ 40분), B(⭐⭐ 60분), C(⭐⭐ 40분) — Step별 프롬프트+화면가이드+체크포인트 |
| 2 | 도구 정확성 | ✅ PASS | ChatGPT, Claude, Gemini, Perplexity, v0, Lovable, Bolt.new, Replit, Figma+AI — 가격/URL 현행 |
| 3 | 사례 검증 | ✅ PASS | 4사례: ScienceDirect 창의적 문제해결(A), Taylor&Francis 개념맵(A), Taylor&Francis RCT(A), AI Lean Canvas 85%(B) — 3A+1B |
| 4 | 시각 자료 | ✅ PASS | IMAGE 태그 6개 (infographic, concept, workflow, before-after, infographic, header) |
| 5 | 워크플로우 일반화 | ✅ PASS | §7 "문제 해결 파이프라인 일반화" — 5단계 디자인 씽킹 × AI 매핑 |
| 6 | 프롬프트 진화 | ✅ PASS | L282~L308 — 🔴(막연) → 🟡(구조화) → 🟢(데이터기반+실행가능) |
| 7 | Anti-Pattern | ✅ PASS | AP1: "AI는 공감하지 못한다"(L343) — 현장관찰 생략 위험. AP2: "완벽한 AI 계획서 2주차부터 지연"(L364) — 실행력 격차 |
| 8 | CC 섹션 참조 | ✅ PASS | `02_cc-specialist_ch18_cc.md` 참조 완비 |

**콘텐츠 판정: 8/8 PASS**

---

## 2. CC 섹션 검수

- **파일:** `_workspace/02_cc-specialist_ch18_cc.md` (512 lines)
- **에이전트:** problem-analyst, solution-designer, evaluator (3종)
- **CLAUDE.md:** "분석 없는 해결책 금지", 3솔루션 필수, Plan B
- **판정:** ✅ PASS (선제 검수 완료)

---

## 3. 이미지 검수

| # | 위치 | 유형 | 설명 | 스펙 매칭 |
|---|------|------|------|-----------|
| 1 | L52 | infographic | 디자인 씽킹 5단계 × AI 도구 매핑 | 대기 (Task #95) |
| 2 | L87 | concept | SPARK 프레임워크 5단계 흐름도 | 대기 |
| 3 | L276 | workflow | 문제 해결 파이프라인 5단계 | 대기 |
| 4 | L309 | before-after | 프롬프트 진화 품질 비교 | 대기 |
| 5 | L383 | infographic | Anti-Pattern 비교 | 대기 |
| 6 | L454 | header | Ch18 헤더 이미지 | 대기 |

**IMAGE 태그: 6개** (content-writer 주장 5개 → 실제 6개)
**테마 컬러:** #E74C3C 레드 통일 ✅
**헤더 IMAGE 위치:** 파일 끝 (L454) — 표준 패턴 일치 ✅

---

## 4. 포맷 일관성

| 항목 | Ch18 | 교재 표준 | 일치 |
|------|------|----------|------|
| 챕터 제목 | `# Ch 18.` | `# Ch N.` | ✅ |
| 독자 대상 | `## 🎯 이런 분이 읽으면 좋아요` | 동일 | ✅ |
| 실습 라벨 | `### 실습 A/B/C: [제목] ⭐` | 동일 | ✅ |
| Step 마커 | `**Step N:**` | 동일 | ✅ |
| 체크포인트 | `✅ **체크포인트:**` (서술형) | 동일 | ✅ |
| Anti-Pattern | `### ⚠️ Anti-Pattern N:` (서술형) | 동일 | ✅ |
| CC 참조 | `## 📎` 섹션 | 동일 | ✅ |
| SPARK 프레임워크 | 독자적 프레임워크 도입 | 챕터 특화로 적절 | ✅ |

**포맷 일관성: 완전 일치** ✅

---

## 5. 차별화 평가 (6항목)

| 항목 | 등급 | 근거 |
|------|------|------|
| 깊이 | A | SPARK 프레임워크, 5 Whys, MECE, fishbone, SCAMPER, 디자인씽킹 5단계 통합 |
| 현실감 | A | ScienceDirect/Taylor&Francis 학술논문 기반, RCT 사례 포함 |
| 재현성 | A | 캠퍼스 문제 → HMW → SCAMPER → 프로토타입 순서 실행 가능 |
| 시각 | A | 6장 IMAGE, SPARK 흐름도+파이프라인+before-after |
| 정직성 | A | "AI는 공감하지 못한다" — 한계를 정면으로 인정 |
| 확장성 | A | v0/Lovable/Bolt.new 노코드 프로토타입, MoSCoW 적용 |

**차별화: 6A**

---

## 최종 판정

### ✅ PASS — 출판 가능

Ch18은 디자인 씽킹과 AI를 결합한 문제 해결 프레임워크가 탄탄합니다. SPARK 독자 프레임워크는 교재의 차별화 요소이며, 노코드 프로토타이핑 실습이 비전공자에게도 실행 가능합니다.
