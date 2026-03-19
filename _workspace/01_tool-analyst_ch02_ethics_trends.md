# Ch 2. AI 윤리·저작권과 최신 트렌드 — 도구 심층 분석 자료

> 작성: tool-analyst | 작성일: 2026-03-17
> 대상 챕터: Part 1, Ch 2 "AI 윤리·저작권과 최신 트렌드"

---

## 1. 2024~2025 AI 주요 트렌드

### 1.1 멀티모달 AI의 본격화

**현황:**
- 텍스트, 이미지, 비디오, 오디오를 동시 처리하는 멀티모달 모델이 2025년 프로덕션 수준에 도달
- 소형 멀티모달 추론 모델이 특정 도메인에 맞춤 튜닝 가능한 수준으로 발전
- Gemini 3가 비디오 분석까지 포함하는 멀티모달 추론에서 업계 선도

**학생 관점 의미:**
- PDF 논문 → 이미지 속 차트/그래프까지 AI가 분석 가능
- 강의 영상을 AI에게 업로드하여 요약/노트 생성 가능
- 발표자료 이미지와 텍스트를 동시에 생성하는 워크플로우 가능

**주요 도구별 멀티모달 지원:**

| 도구 | 텍스트 | 이미지 입력 | 이미지 생성 | 비디오 분석 | 음성 |
|------|--------|-----------|-----------|-----------|------|
| ChatGPT | ✅ | ✅ | ✅ (DALL-E) | ✅ (제한적) | ✅ (음성모드) |
| Gemini | ✅ | ✅ | ✅ | ✅ (강점) | ✅ (Gemini Live) |
| Claude | ✅ | ✅ | ❌ | ❌ | ❌ |
| Perplexity | ✅ | ✅ | ✅ (DALL-E/SDXL 연동) | ❌ | ❌ |

### 1.2 에이전트 AI (Agentic AI)

**현황:**
- 2026년은 멀티 에이전트 시스템이 본격 프로덕션에 진입하는 해
- 멀티 에이전트 시스템 관련 문의량: 2024년 Q1 → 2025년 Q2 사이 **1,445% 급증**
- 특화된 에이전트들이 오케스트레이터에 의해 조율되는 구조로 설계 패러다임 전환

**주요 에이전트 도구:**
- **ChatGPT:** Codex 에이전트 (코드 자동 작성/실행), 에이전트 모드 (Deep Research 포함)
- **Claude:** Claude Code (터미널 기반 자율 코딩), Agent SDK (개발자용 에이전트 빌더), Computer Use (컴퓨터 직접 조작)
- **Gemini:** Jules (다중 에이전트 워크플로우), Gemini Code Assist, Google AI Ultra의 20배 한도
- **Perplexity:** Comet 브라우저 (AI 기반 브라우징 에이전트)

**학생 관점 의미:**
- AI가 단순 답변을 넘어 "과제를 수행"하는 시대 진입
- 여러 AI 에이전트가 역할 분담하여 팀 프로젝트 보조 가능
- 윤리적 경계 설정이 더욱 중요해짐 (어디까지가 "내 과제"인가?)

### 1.3 추론 모델 (Reasoning Models)

**현황:**
- "더 깊이 생각하기(think harder) vs 빠르게 답변하기(respond faster)"가 개발자가 선택 가능한 옵션이 됨
- OpenAI o3, Gemini 2.5 Deep Think 등 추론 특화 모델 등장
- GPT-5.x 시리즈에 범용 지능, 추론 깊이, 코딩 특화, 멀티모달이 통합

**역설적 발견 — 추론 모델의 할루시네이션 문제:**
- 추론 특화 모델(o3)이 팩트 벤치마크에서 33% 할루시네이션률 기록 (이전 모델 o1의 16% 대비 2배)
- 복잡한 문제를 잘 풀지만, 지식 공백을 그럴듯한 추측으로 메우는 경향
- 학생 주의사항: 추론 모델의 "깊이 있는 분석"도 반드시 팩트체킹 필요

### 1.4 오픈소스 AI의 약진

**현황:**
- 오픈소스와 프로프라이어터리 모델의 성능 격차: 2024년 8% → 2025년 **1.7%**로 급격히 축소
- DeepSeek-V3.2가 수학/추론에서 GPT-5에 근접 (수학 테스트 99.2%)
- Meta Llama 4 시리즈, Qwen 2.5 등 고성능 오픈소스 모델 다수 등장

**학생 관점 의미:**
- 무료/저비용으로 고급 AI 활용 가능 (API 비용 절감)
- 개인정보 우려 시 로컬에서 실행 가능한 옵션
- 하지만 직접 설치/운영에 기술적 지식 필요

### 1.5 MCP(Model Context Protocol) 표준화

**현황:**
- 2025년 MCP가 광범위하게 채택되어, AI 에이전트가 외부 도구/데이터베이스/API에 연결하는 방식이 표준화
- 기존의 맞춤 통합 작업이 플러그앤플레이 방식으로 전환

**학생 관점 의미:**
- AI 도구들이 서로 연동되기 쉬워짐 (예: Claude Code에서 Google Docs 직접 편집)
- "도구 조합 워크플로우"가 더 실용적이고 자동화 가능해짐

---

## 2. 각 도구의 데이터 수집/학습 정책 비교

### 2.1 개인정보 및 데이터 학습 정책 비교표

| 정책 항목 | ChatGPT (OpenAI) | Gemini (Google) | Claude (Anthropic) | Perplexity |
|----------|-------------------|-----------------|---------------------|------------|
| **기본 데이터 학습** | ✅ 기본 활성화 | ✅ 기본 활성화 | ✅ 기본 활성화 (2025.9~ 정책 변경) | ✅ 기본 활성화 |
| **학습 비활성화 옵션** | ✅ 설정에서 끄기 가능 | ✅ 활동 기록 기간 조절 가능 | ✅ 설정에서 끄기 가능 | ✅ 간단한 토글로 비활성화 |
| **대화 저장 기간** | 무기한 (수동 삭제 가능) | 18개월 기본 (3/36개월 조절 가능) | 비활성화 시 즉시 삭제, 활성화 시 최대 5년 (비식별화) | 기본 저장 |
| **인간 리뷰** | 있음 (품질 개선 목적) | 있음 (대화 검토 가능) | 제한적 | 미공개 |
| **Temporary/임시 모드** | ✅ Temporary Chat (학습 미반영) | ❌ | ❌ (학습 비활성화로 대체) | ❌ |
| **기업/팀 플랜 데이터 보호** | ✅ Enterprise: 학습 미사용 보장 | ✅ Workspace: 별도 정책 | ✅ Team/Enterprise: 학습 미사용 | ✅ Enterprise: 데이터 격리 |
| **Google 생태계 통합** | ❌ | ✅ 검색기록, Gmail, YouTube 활동과 통합 | ❌ | ❌ |

### 2.2 도구별 개인정보 상세 분석

#### ChatGPT (OpenAI)
- **핵심 이슈:** 기본적으로 대화 내용을 모델 학습에 사용. Plus($20/월) 유료 사용자도 기본 설정은 학습 활성화
- **학생 주의사항:**
  - 개인 정보(학번, 연락처, 성적 등)를 입력하지 말 것
  - 민감한 과제 작업 시 Temporary Chat 모드 활용
  - 설정 → Data Controls → "Improve the model for everyone" 비활성화 권장

#### Gemini (Google)
- **핵심 이슈:** Google 계정에 연결된 모든 활동(검색, Gmail, YouTube)과 데이터가 통합될 수 있음. 인간 리뷰어가 대화 내용을 검토할 수 있음
- **학생 주의사항:**
  - 학교 Google Workspace 계정과 개인 계정을 구분하여 사용
  - 활동 기록 자동 삭제 기간을 3개월로 설정 권장
  - 민감한 개인 정보는 절대 입력하지 말 것

#### Claude (Anthropic)
- **핵심 이슈:** 2025년 9월 정책 변경으로 소비자 채팅이 학습에 사용될 수 있게 됨 (이전에는 기본 비활성화). 학습 허용 시 비식별화된 대화를 최대 5년 보관
- **학생 주의사항:**
  - 설정에서 학습 비활성화 토글 확인 필수
  - Team/Enterprise 플랜은 학습 미사용 보장
  - 가장 엄격한 보안 프로토콜을 가진 것으로 평가

#### Perplexity
- **핵심 이슈:** 유료 플랜에서도 기본적으로 데이터를 학습에 사용. 단, 설정에서 "AI Data Usage" 토글로 간단히 비활성화 가능
- **학생 주의사항:**
  - 검색 특성상 민감한 개인정보를 입력할 일이 적음
  - 그래도 설정에서 학습 비활성화 권장

### 2.3 학생을 위한 데이터 보호 실천 가이드

```
✅ 모든 AI 도구에서 "학습/개선 참여" 옵션 비활성화하기
✅ 학번, 주민번호, 연락처 등 개인 식별 정보 절대 입력하지 않기
✅ 민감한 과제(개인 에세이, 의료/법률 관련)는 Temporary Chat 모드 사용
✅ 학교 계정과 개인 계정 분리하여 사용
✅ 정기적으로 대화 기록 삭제하기
❌ AI 채팅에 친구/동료의 개인정보 입력하지 않기
❌ 기밀 연구 데이터를 무료 플랜에 업로드하지 않기
```

---

## 3. AI 생성물 저작권 — 각 도구 이용약관 비교

### 3.1 주요 판례 및 법적 현황 (2025~2026)

**미국:**
- 2026년 3월 2일: 미국 대법원이 AI 생성 시각 예술작품의 저작권 보호 요청을 기각. "인간 창작자가 없는 저작물은 저작권 보호 대상이 아니다"는 하급심 판결 확정
- 미국 저작권청 기준: AI 생성 콘텐츠는 **"상당한 인간의 개입(significant human involvement)"**이 있어야만 저작권 보호 가능
- 2025년 한 해에만 전 세계 법원에서 AI 할루시네이션 관련 수백 건의 판결이 내려짐 (역대 전체 사례의 약 90%)

**한국:**
- AI 생성물의 저작권은 아직 명확한 판례가 확립되지 않음
- 저작권법상 "인간의 사상 또는 감정을 표현한 창작물"만 보호 대상
- AI를 도구로 활용하되, 인간의 창의적 기여가 핵심적일 경우 보호 가능성 있음

### 3.2 도구별 이용약관 비교

| 항목 | ChatGPT (OpenAI) | Gemini (Google) | Claude (Anthropic) | Perplexity |
|------|-------------------|-----------------|---------------------|------------|
| **출력물 소유권** | ✅ 사용자 소유 (ToS에 명시) | ✅ 사용자 소유 (ToS에 명시) | ✅ 사용자 소유 (ToS에 명시) | ❓ 불명확 (ToS에서 소유권 미언급) |
| **상업적 사용** | ✅ 허용 (Free 포함) | ✅ 허용 | ✅ 허용 | ✅ 허용 |
| **AI 사용 표시 의무** | ⚠️ 2026년 기준 "필수적 AI 공개(mandatory AI disclosure)" 요구 | 권장 | 권장 | 권장 |
| **IP 면책(Indemnity)** | ❌ 일반 플랜 없음 | ❌ 일반 플랜 없음 | ✅ Enterprise 플랜에서 제공 | ❌ |
| **출력물의 비독점성** | ⚠️ 다른 사용자에게 유사 출력이 생성될 수 있음 | ⚠️ 동일 | ⚠️ 동일 | ⚠️ 동일 |
| **학습 데이터 관련 소송** | 다수 진행 중 (NYT, 작가 집단 소송 등) | ✅ 프랑스 경쟁당국 €2.5억 벌금 (뉴스 기사 무단 학습) | 상대적으로 적음 | 일부 진행 중 |

### 3.3 핵심 구분: 계약상 소유 vs 법적 저작권 보호

**중요한 차이:**
- **"계약상 소유(Contractual Ownership)"**: 플랫폼 ToS에서 "출력물은 당신의 것"이라고 명시 → 플랫폼이 소유권을 주장하지 않겠다는 의미
- **"법적 저작권 보호(Statutory Copyright)"**: 실제 법적으로 저작권이 인정되어 제3자의 무단 사용을 막을 수 있는 보호 → 인간의 상당한 기여 없이는 불가능

→ 즉, AI 출력물을 "소유"할 수는 있지만, 다른 사람이 같은 내용을 사용하는 것을 법적으로 막을 수는 없을 수 있음

### 3.4 대학생을 위한 AI 저작권 실전 가이드

```
✅ AI 출력물을 "초안"으로 활용하고, 자신의 분석·비판·수정을 반드시 추가
✅ AI를 사용했음을 과제/보고서에 명시 (사용 도구, 프롬프트, 수정 과정)
✅ AI가 생성한 참고문헌은 반드시 실제 존재 여부 확인 (할루시네이션 주의)
✅ "상당한 인간의 기여"를 남길 것: 프롬프트 설계, 결과 선별, 수정, 재구성
❌ AI 출력물을 그대로 제출하지 않기 (학술 부정행위)
❌ AI 출력물에 자신의 저작권을 주장하지 않기 (법적으로 인정되지 않을 수 있음)
❌ AI가 제시한 출처를 검증 없이 인용하지 않기
```

---

## 4. 학술 윤리와 AI — 한국 대학 AI 사용 가이드라인

### 4.1 교육부·대교협 가이드라인 (2025)

교육부와 한국대학교육협의회(대교협)가 '대학 AI 활용 윤리 가이드라인'을 발표. 대학가 AI 활용 부정행위 사태가 직접적 계기.

**5대 핵심원칙:**

| 원칙 | 내용 |
|------|------|
| **학문적 진실성** | 교육 목적과 원칙에 따라 AI 활용, 학습 전 과정에서 윤리적 기준 준수 |
| **인간 중심성과 책임성** | AI는 도구일 뿐, 최종 결과에 대한 책임은 인간에게 있음 |
| **투명성과 신뢰성** | AI 사용 사실과 과정을 투명하게 공개, 결과의 정확성 검증 |
| **공정성** | 모든 사용자가 AI를 공정하게 사용할 수 있어야 함, 차별 없는 접근 |
| **개인 보호 및 보안** | 개인정보 보호와 데이터 보안 준수 |

### 4.2 주요 대학 가이드라인 사례

- **연세대학교:** 2024년 5월 "생성형 AI 활용 가이드라인 v1.0" 발표. AI 활용 범위와 한계를 과목별로 교수자가 설정하도록 권장
- **고려대학교:** 2025년 8월 AI 활용 가이드라인 공개. AI 생성 결과물을 그대로 제출하는 것은 부정행위로 규정. AI 사용 시 반드시 과정을 명시
- **충북대학교:** 교육혁신본부에서 "챗 GPT 등 생성형 AI 활용 및 윤리 가이드라인" 안내

### 4.3 AI 활용 수준별 허용 범위 (일반적 기준)

| 수준 | 설명 | 예시 | 학술 윤리 판단 |
|------|------|------|--------------|
| **Level 1: 아이디어 탐색** | 주제 브레인스토밍, 개요 구상 | "이 주제로 어떤 논점이 가능할까?" | ✅ 대부분 허용 |
| **Level 2: 자료 조사 보조** | 참고문헌 검색, 개념 설명 요청 | "디지털 트랜스포메이션의 정의를 설명해줘" | ✅ 대부분 허용 (출처 검증 필수) |
| **Level 3: 초안 생성 보조** | AI 초안을 기반으로 대폭 수정/재작성 | AI 개요 → 자신의 분석으로 재구성 | ⚠️ AI 사용 명시 시 허용 (교수자 기준) |
| **Level 4: AI 출력 직접 사용** | AI 답변을 거의 수정 없이 제출 | AI가 쓴 에세이를 복붙 | ❌ 대부분 부정행위 |
| **Level 5: AI 대리 제출** | AI에게 과제 전체를 위임 | 프롬프트만 입력하고 결과 제출 | ❌ 명백한 부정행위 |

---

## 5. 할루시네이션과 편향

### 5.1 할루시네이션 현황 데이터

| 모델 | 할루시네이션률 | 벤치마크 | 비고 |
|------|-------------|---------|------|
| Gemini 2.0 Flash | **0.7%** | Vectara (2025.4) | 가장 낮은 할루시네이션률 |
| Perplexity Sonar | ~1.5% | 검색 기반 검증 | 출처 인용으로 보완 |
| Claude Opus 4 | ~2.5% | 자체 벤치마크 | "모르겠다" 인정 경향 |
| GPT-5 | ~3% | 자체 벤치마크 | 범용 성능 우수 |
| OpenAI o3 (추론 특화) | **33%** | PersonQA | 추론 모델 역설 |
| Grok-3 | **94%** | CJR 연구 (2025.3) | 매우 높은 오류율 |

**핵심 인사이트:**
- 최고 성능 모델의 할루시네이션률은 2021년 21.8%에서 2025년 0.7%로 **96% 감소**
- 그러나 AI가 할루시네이션할 때 오히려 **더 확신에 찬 어조** 사용 (MIT 연구, 2025.1)
- 2025년 수학적 증명으로 **현재 LLM 아키텍처에서 할루시네이션 완전 제거 불가능** 확인
- 2024년 AI 할루시네이션으로 인한 글로벌 재정 손실: **$674억**
- 2025년 한 해에만 전 세계 법원에서 AI 할루시네이션 관련 **수백 건의 판결** (역대 전체의 ~90%)

### 5.2 편향(Bias) 문제

- 학습 데이터에 내재된 성별, 인종, 문화적 편향이 AI 출력에 반영
- 한국어 학습 데이터가 영어 대비 적어, 한국 맥락에서의 편향 가능성
- 각 도구의 안전 필터(safety filter) 수준이 다름: Claude가 가장 보수적, ChatGPT가 가장 유연

---

## 6. 참고 출처

### AI 트렌드
- [The Trends That Will Shape AI in 2026 (IBM)](https://www.ibm.com/think/news/ai-tech-trends-predictions-2026)
- [7 Agentic AI Trends to Watch in 2026 (MachineLearningMastery)](https://machinelearningmastery.com/7-agentic-ai-trends-to-watch-in-2026/)
- [ICLR 2026 Trends: Agentic AI, Multimodal Models & Data Governance (Encord)](https://encord.com/iclr-2026/)
- [2025 AI Wrapped (Lambda)](https://lambda.ai/blog/2025-ai-wrapped)
- [Top LLMs and AI Trends for 2026 (Clarifai)](https://www.clarifai.com/blog/llms-and-ai-trends)

### 데이터 프라이버시
- [AI Privacy: GDPR Analysis of ChatGPT, Perplexity & Co. 2025 (CamoCopy)](https://www.camocopy.com/ai-assistants-privacy/)
- [Privacy Comparison: ChatGPT, Gemini, Claude, Perplexity (Tom's Guide)](https://www.tomsguide.com/ai/i-compared-the-privacy-of-chatgpt-gemini-claude-and-perplexity-heres-the-one-you-should-trust-most-with-your-personal-info)
- [The Great AI Privacy Divide (Medium)](https://medium.com/@michael_79773/the-great-ai-privacy-divide-one-year-later-two-worlds-apart-e74ce6187f1f)
- [OpenAI Data Privacy Compared (Protecto)](https://www.protecto.ai/blog/openai-data-privacy/)

### 저작권·이용약관
- [Who Owns AI Content? Platform Policies Compared (Terms.law)](https://www.terms.law/2025/04/09/navigating-ai-platform-policies-who-owns-ai-generated-content/)
- [Generative AI Copyright: Law, Litigation & Best Practices 2026 (AIMultiple)](https://aimultiple.com/generative-ai-copyright)
- [ChatGPT Commercial Use 2026 Legal Guide (Global GPT)](https://www.glbgpt.com/hub/chatgpt-commercial-use-2026/)

### 할루시네이션·정확도
- [AI Hallucination Report 2026 (AllAboutAI)](https://www.allaboutai.com/resources/ai-statistics/ai-hallucinations/)
- [AI Hallucination Rates Across Different Models 2026 (AboutChromebooks)](https://www.aboutchromebooks.com/ai-hallucination-rates-across-different-models/)
- [Ranked: AI Hallucination Rates by Model (Visual Capitalist)](https://www.visualcapitalist.com/sp/ter02-ranked-ai-hallucination-rates-by-model/)
- [AI Hallucination Statistics Research Report 2026 (Suprmind)](https://suprmind.ai/hub/insights/ai-hallucination-statistics-research-report-2026/)

### 한국 대학 AI 가이드라인
- [교육부 — 대학 인공지능 활용 윤리 가이드라인 시안 (교수신문)](https://www.kyosu.net/news/articleView.html?idxno=200008)
- [대학 'AI 윤리지침' 첫 발표 (한국일보)](https://weekly.hankooki.com/news/articleView.html?idxno=7153168)
- [연세대학교 — 생성형 AI 활용 가이드라인 v1.0](https://cloudcms.yonsei.ac.kr/fresh/infomation/student.do?mode=download&articleNo=190086&attachNo=161939)
- [고려대학교 — AI 활용 가이드라인](https://college.korea.ac.kr/uc/community/event.do?mode=download&articleNo=781012&attachNo=289488)
- [교육 AI 윤리와 정책 개발 (전국인력신문)](https://www.kjob.news/news/470502)
- [국내외 대학의 생성형 AI 가이드라인 비교 분석 (DBpia)](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12352562)
