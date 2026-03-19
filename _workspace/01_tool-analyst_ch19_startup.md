# Ch 19. AI를 활용한 창업·서비스 기획 — 도구 심층 분석 자료

> 작성: tool-analyst | 작성일: 2026-03-17
> 대상 챕터: Part 6, Ch 19 "AI를 활용한 창업·서비스 기획"

---

## 1. 창업 기획 AI 도구 비교

### 1.1 창업 기획 단계별 도구 매핑

| 창업 단계 | 핵심 도구 | 활용법 |
|----------|----------|-------|
| **시장 조사** | Perplexity, Gemini | 시장 규모, 트렌드, 경쟁사 분석 (실시간 출처 포함) |
| **문제 정의** | ChatGPT, Claude | 고객 페인포인트 분석, 페르소나 생성 |
| **비즈니스 모델** | ChatGPT, Claude | BM 캔버스 생성, 수익 모델 설계 |
| **MVP 개발** | Lovable, Replit, Bolt.new | 노코드 프로토타입 2~6주 내 구축 |
| **피치덱 제작** | Gamma, ChatGPT + Canva | AI 피치덱 자동 생성, 디자인 최적화 |
| **재무 계획** | ChatGPT Code Interpreter | 매출 예측, 손익분기점, 재무 모델링 |
| **법률/계약** | ChatGPT, Claude | 이용약관 초안, 개인정보처리방침, 계약서 검토 |

### 1.2 Perplexity 시장 조사 심층

**시장 조사에 Perplexity가 최적인 이유:**
- 실시간 웹 검색 + 학술 논문 + 뉴스 종합
- 모든 답변에 출처(Citation) 포함 → 신뢰도 높은 시장 데이터
- 후속 질문으로 심층 분석 가능

**시장 조사 프롬프트:**
```
[서비스/제품명]의 시장성을 분석해주세요:

1. TAM/SAM/SOM 시장 규모 추정 (한국 기준)
2. 시장 성장률 및 트렌드 (최근 3년)
3. 주요 경쟁사 5곳 비교표 (제품, 가격, 강점, 약점)
4. 타겟 고객 세그먼트 및 규모
5. 진입 장벽 및 기회 요인
6. PEST 분석 (정치/경제/사회/기술)

모든 데이터에 출처를 포함해주세요.
```

---

## 2. BM 캔버스 AI 생성

### 2.1 린 캔버스(Lean Canvas) 프롬프트

```
다음 사업 아이디어로 린 캔버스(Lean Canvas)를 작성해주세요:

사업 아이디어: [1~2줄 설명]
타겟 고객: [대상 사용자]
핵심 문제: [해결하려는 문제]

린 캔버스 9개 블록 모두 채워주세요:
1. 문제 (Problem) — 상위 3가지 문제
2. 고객 세그먼트 (Customer Segments) — 얼리어답터 포함
3. 고유 가치 제안 (Unique Value Proposition)
4. 솔루션 (Solution) — 문제별 핵심 기능
5. 채널 (Channels) — 고객 도달 경로
6. 수익 모델 (Revenue Streams)
7. 비용 구조 (Cost Structure)
8. 핵심 지표 (Key Metrics)
9. 경쟁 우위 (Unfair Advantage)

각 블록에 구체적 근거/수치를 포함하고,
표 형태로 한눈에 볼 수 있게 정리해주세요.
```

### 2.2 비즈니스 모델 캔버스 프롬프트

```
다음 사업 아이디어로 비즈니스 모델 캔버스(BMC)를 작성해주세요:

[사업 아이디어 상세 설명]

BMC 9개 블록:
1. 핵심 파트너 (Key Partners)
2. 핵심 활동 (Key Activities)
3. 핵심 자원 (Key Resources)
4. 가치 제안 (Value Propositions)
5. 고객 관계 (Customer Relationships)
6. 채널 (Channels)
7. 고객 세그먼트 (Customer Segments)
8. 비용 구조 (Cost Structure)
9. 수익원 (Revenue Streams)

추가:
- 각 블록의 가설(Hypothesis) 표시
- 검증이 필요한 가설 우선순위
- MVP로 검증 가능한 실험 3가지 제안
```

---

## 3. MVP 기획 + 노코드 개발

### 3.1 MVP 개발 도구 선택 가이드

| 상황 | 추천 도구 | 개발 기간 | 비용 |
|------|----------|----------|------|
| **랜딩 페이지 (검증용)** | v0 + Vercel | 1일 | 무료 |
| **웹앱 MVP (DB 포함)** | Lovable | 1~2주 | $25/월 |
| **빠른 프로토타입** | Bolt.new | 2~3일 | ~$20/월 |
| **복잡한 앱 (AI 연동)** | Replit Agent | 2~4주 | $25/월 |
| **모바일 앱 MVP** | Replit + React Native | 3~4주 | $25/월 |

### 3.2 MVP 2026 트렌드

- **AI MVP 개발 비용:** $5K~$20K (전통적 $100K+ 대비 80%↓)
- **개발 기간:** AI 활용 시 2~6주 (전통 6개월+ 대비)
- **핵심 전략:** 카테고리당 1개 도구만 마스터 (도구 과잉 방지)
- **비기술 창업자도 MVP 구축 가능:** Lovable, Replit Agent 활용

### 3.3 MVP 기능 정의 프롬프트

```
다음 서비스의 MVP 기능을 정의해주세요:

서비스: [서비스 설명]
타겟: [타겟 사용자]
목표: [MVP로 검증하고 싶은 가설]

MoSCoW 기법으로 기능을 분류해주세요:
- Must Have: MVP에 반드시 포함 (핵심 가치 검증)
- Should Have: 가능하면 포함
- Could Have: 시간 여유 시
- Won't Have: V2에서 개발

각 기능에:
- 기능명 + 1줄 설명
- 유저 스토리 ("~로서, ~를 원한다, ~하기 위해")
- 예상 개발 시간 (노코드 기준)
- 검증 지표 (이 기능이 성공하면 어떤 수치가 변하는지)
```

---

## 4. 피치덱 자동 생성

### 4.1 피치덱 도구 비교

| 도구 | 가격 | 핵심 기능 | 적합한 경우 |
|------|------|----------|-----------|
| **Gamma** | Free(400크레딧) / $8~15/월 | 자연어→피치덱 60초 생성, 웹 퍼블리시 | **가장 빠른 초안** |
| **ChatGPT + Canva** | Free~$20/월 + Free~$120/년 | 내용(ChatGPT) + 디자인(Canva) | 디자인 커스터마이징 |
| **Beautiful.ai** | $12/월~ | 스마트 레이아웃, 브랜드 통일 | 깔끔한 디자인 |
| **Claude + Gamma** | Free~$20/월 + Free~$15/월 | 심층 전략(Claude) + 슬라이드(Gamma) | 논리적 피치덱 |

### 4.2 피치덱 S급 프롬프트

```
다음 사업 아이디어로 투자자/심사위원용 피치덱 구조를 설계해주세요:

사업 아이디어: [상세 설명]
발표 시간: [시간]
청중: [투자자/교수/대회 심사위원]

10장 슬라이드 구성:
1. 표지 (서비스명 + 한줄 소개)
2. 문제 (고객의 핵심 페인포인트)
3. 솔루션 (우리의 해결 방법)
4. 시장 규모 (TAM/SAM/SOM)
5. 비즈니스 모델 (수익 구조)
6. 경쟁 우위 (차별화 포인트)
7. 제품 데모/목업 (핵심 화면)
8. 팀 소개 (왜 우리 팀이 해야 하는지)
9. 재무 계획 (3년 매출 예측)
10. Ask (투자 요청 금액 / 대회 목표)

각 슬라이드에:
- 핵심 메시지 1줄
- 포함할 데이터/수치
- 발표 스크립트 (30초 분량)
```

---

## 5. 창업 기획 전체 워크플로우

### 5.1 AI 활용 창업 기획 파이프라인

```
[Week 1: 발견]
  Perplexity → 시장 조사, 트렌드, 경쟁사
  ChatGPT → 고객 페르소나, 페인포인트 정의

[Week 2: 기획]
  ChatGPT/Claude → 린 캔버스, BM 캔버스
  ChatGPT Code Interpreter → 시장 규모 추정, 재무 모델

[Week 3: MVP]
  Lovable/Replit → 노코드 MVP 개발
  v0 → UI 프로토타입

[Week 4: 발표]
  Gamma → 피치덱 자동 생성
  ChatGPT → 발표 스크립트 + Q&A 대비
  Claude → 논리 검증 + 약점 보완
```

### 5.2 프롬프트 진화 패턴

**🔴 Level 1 (초보):**
```
대학생 창업 아이디어 추천해줘
```

**🟡 Level 2 (중급):**
```
대학생 대상 AI 기반 서비스 창업 아이디어 5개와 각각의 비즈니스 모델을 제안해줘
```

**🟢 Level 3 (고급):**
```
대학생 창업 경진대회(예비창업패키지) 준비:
■ 분야: EdTech (AI 학습 도우미)
■ 요청:
1. 린 캔버스 9블록 (구체적 수치 포함)
2. TAM/SAM/SOM (한국 대학생 600만명 기준)
3. 경쟁사 5곳 포지셔닝 맵 (기능×가격)
4. MVP 기능 MoSCoW 분류 (Lovable 개발 기준)
5. 3년 재무 모델 (MAU 시나리오별)
6. 피치덱 10장 구조 + 슬라이드별 스크립트
■ 대회: 발표 10분 + Q&A 5분, 심사위원 = VC + 교수
```

---

## 6. 상황별 도구 선택 가이드

| 상황 | 추천 도구 | 이유 |
|------|----------|------|
| 시장 조사 | Perplexity | 실시간 출처 포함 리서치 |
| BM 설계 | ChatGPT / Claude | 캔버스 생성 + 가설 정리 |
| 재무 모델링 | ChatGPT Code Interpreter | 엑셀 수준 계산 + 차트 |
| MVP 개발 (비개발자) | Lovable | 노코드, Supabase 통합 |
| MVP 개발 (개발자) | Cursor / Claude Code | 커스텀 개발 |
| 랜딩 페이지 | v0 + Vercel | 1일 내 배포 |
| 피치덱 | Gamma | 60초 자동 생성 |
| 발표 준비 | ChatGPT | 스크립트 + Q&A 대비 |

---

## 7. 출처

- Tericsoft: "Top 10 AI Tools Used for MVP Development by Startups in 2026"
- Altar.io: "7 AI Platforms to Supercharge Your MVP Development in 2026"
- GainHQ: "AI MVP Development Guide For Startups In 2026"
- StartupBricks: "How to Build Your MVP in 30 Days: The Complete 2026 Guide"
- Leanware: "How to Build an MVP with Generative AI: Step-by-Step Guide 2026"
- LeanPivot.ai: leanpivot.ai (AI Lean Startup Coach)
- Gamma: gamma.app
- Lovable: lovable.dev
- Bolt.new: bolt.new
- Replit: replit.com
