# Ch 17. 전공과 연계한 AI 실습 프로젝트 — 도구 심층 분석 자료

> 작성: tool-analyst | 작성일: 2026-03-17
> 대상 챕터: Part 6, Ch 17 "전공과 연계한 AI 실습 프로젝트"

---

## 1. 전공별 AI 도구 조합 전략

### 1.1 전공별 추천 도구 매트릭스

| 전공 계열 | 핵심 AI 도구 | 보조 도구 | 프로젝트 예시 |
|----------|------------|----------|------------|
| **인문학** | ChatGPT, Claude | NotebookLM, Perplexity | 텍스트 마이닝, 디지털 인문학 프로젝트 |
| **사회과학** | ChatGPT Code Interpreter, Jamovi | Google Forms, Claude | 설문 분석, 정책 시뮬레이션 |
| **경영학** | Perplexity, ChatGPT, Gamma | Notion AI, Claude | 시장 분석 보고서, BM 기획 |
| **자연과학** | ChatGPT, Claude, Wolfram Alpha | NotebookLM, Gemini | 실험 데이터 분석, 논문 리뷰 |
| **공학** | GitHub Copilot, Cursor, Claude Code | Replit, v0 | 프로토타입 개발, 시뮬레이션 |
| **디자인/예술** | Midjourney, DALL-E 3, Canva AI | Gamma, Claude | 포트폴리오, 컨셉 아트 |
| **교육학** | ChatGPT, NotebookLM, JASP | Canva, Gamma | 교수학습 자료 개발, 교육 평가 |
| **의학/간호** | Perplexity, Claude, Elicit | Consensus, ChatGPT | 문헌 리뷰, 임상 데이터 분석 |

### 1.2 멀티 도구 워크플로우 설계 원칙

```
원칙 1: 도구별 역할 분담
  → Perplexity = 리서치 (최신 정보 수집)
  → ChatGPT = 분석·생성 (코드 실행, 콘텐츠 생성)
  → Claude = 심층 분석 (논리 구조, 긴 텍스트)
  → Gamma/Canva = 시각화·발표 자료

원칙 2: 파이프라인 설계
  → 조사(Perplexity) → 분석(ChatGPT/Claude) → 시각화(Claude Artifacts) → 발표(Gamma)

원칙 3: 도구당 최적 용도 1가지에 집중
  → 1개 도구로 모든 것을 하려 하지 말 것
  → 각 도구의 최강 기능만 활용
```

---

## 2. 프로젝트 유형별 도구 조합

### 2.1 리서치 프로젝트 (문헌 분석형)

```
[도구 조합] Perplexity + Elicit + NotebookLM + Claude + ChatGPT

Step 1. 문헌 탐색 (Perplexity + Elicit)
  → Perplexity: 최신 연구 트렌드 조사 (출처 포함)
  → Elicit: 학술 논문 체계적 검색 (99.4% 정확도)

Step 2. 문헌 분석 (NotebookLM + Claude)
  → NotebookLM: PDF 업로드 → Audio Overview, Mind Map
  → Claude: 논문 10편 이상 한번에 분석 (1M 토큰)

Step 3. 종합 정리 (ChatGPT)
  → 문헌 리뷰 매트릭스 생성
  → 연구 갭 도출 + 연구 질문 제안

Step 4. 발표 자료 (Gamma)
  → 연구 결과를 발표용 슬라이드로 60초 변환
```

### 2.2 데이터 분석 프로젝트

```
[도구 조합] ChatGPT Code Interpreter + Claude Artifacts + Jamovi + Gemini Sheets

Step 1. 데이터 수집 (공공데이터포털 / Google Forms)
Step 2. 데이터 탐색 + 정제 (ChatGPT Code Interpreter)
Step 3. 통계 분석 (ChatGPT + Jamovi)
Step 4. 인터랙티브 시각화 (Claude Artifacts)
Step 5. 보고서 작성 (ChatGPT + Claude)
```

### 2.3 개발 프로젝트 (프로토타입형)

```
[도구 조합] Cursor/Claude Code + Replit + v0 + GitHub Copilot

Step 1. 기획 (ChatGPT) → 요구사항 정의
Step 2. UI 디자인 (v0) → 프론트엔드 코드 자동 생성
Step 3. 개발 (Cursor/Claude Code) → 풀스택 코딩
Step 4. 배포 (Replit/Vercel) → 웹 배포
Step 5. 테스트 + 수정 (Claude Code Agent)
```

### 2.4 기획/제안 프로젝트

```
[도구 조합] Perplexity + ChatGPT + Claude + Gamma + Canva

Step 1. 시장 조사 (Perplexity) → 트렌드, 경쟁사, 데이터
Step 2. 기획서 작성 (ChatGPT + Claude) → BM 캔버스, 전략
Step 3. 시각 자료 (Canva AI + Midjourney) → 목업, 인포그래픽
Step 4. 발표 자료 (Gamma) → 피치덱 자동 생성
```

---

## 3. 전공별 프로젝트 프롬프트

### 3.1 범용 프로젝트 기획 프롬프트

```
나는 [전공] [학년]이고, 전공 수업 [과목명]의 학기 프로젝트를 기획하려 합니다.

프로젝트 주제를 제안해주세요:

조건:
1. AI 도구를 적극 활용할 수 있는 주제
2. 데이터 수집 + 분석 + 시각화가 포함된 주제
3. 실제 사회적/산업적 의미가 있는 주제
4. 2~4주 내 완성 가능한 범위
5. 발표 + 보고서 형태의 산출물

각 주제에 대해:
- 주제 설명 (1~2줄)
- 활용할 AI 도구 조합
- 데이터 소스 제안
- 예상 산출물
- 난이도 (★~★★★)
```

### 3.2 프로젝트 진행 프롬프트

```
[프로젝트명]을 진행하고 있습니다.

현재 진행 상황: [현재 단계 설명]
사용 중인 도구: [도구 목록]
직면한 문제: [구체적 문제]

도움 요청:
1. 현재 문제의 해결 방안
2. 다음 단계 구체적 액션 플랜
3. 도구 활용 최적화 제안
4. 프로젝트 품질을 높이기 위한 팁
```

---

## 4. 프롬프트 진화 패턴

**🔴 Level 1 (초보):**
```
마케팅 수업 프로젝트 주제 추천해줘
```

**🟡 Level 2 (중급):**
```
경영학과 마케팅원론 수업에서 AI를 활용한 프로젝트를 하려고 해.
데이터 분석이 포함된 주제 3개와 각각의 진행 방법을 알려줘.
```

**🟢 Level 3 (고급):**
```
경영학과 4학년 마케팅전략 수업 학기 프로젝트:
■ 조건: 4주, 4인 팀, AI 필수 활용, 발표 15분 + 보고서 20페이지
■ 도구: Perplexity(시장조사) + ChatGPT(분석) + Claude(시각화) + Gamma(발표)
■ 요청:
1. 주제 3개 (MZ세대/ESG/AI 관련) + 차별화 포인트
2. 각 주제별 4주 타임라인 (주차별 마일스톤)
3. 팀원 역할 분담 제안
4. 데이터 소스 (한국 공공데이터/기업 보고서)
5. AI 활용 부분 vs 직접 작업 부분 구분
```

---

## 5. 출처

- Ch 1~16 도구 분석 자료 종합 (tool-analyst 기 작성분)
- GitHub Copilot: github.com/features/copilot
- Cursor: cursor.com
- Claude Code: code.claude.com
- Replit: replit.com
- NotebookLM: notebooklm.google
- Elicit: elicit.com
- Jamovi: jamovi.org
- Gamma: gamma.app
