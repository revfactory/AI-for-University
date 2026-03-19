# 🔧 Claude Code & 하네스 활용 — Chapter 10 보충

> **대상 독자**: Chapter 9까지 데이터·문서 자동화를 경험한 학생
> 본문에서 **Plan-Do-Check 3축**(계획→실행→피드백)과 **간격 반복(Spaced Repetition)** 기반 학습 관리를 배웠습니다. ChatGPT Tasks로 반복 알림을, Notion AI로 일정 관리를, Anki로 복습 카드를 만드는 방법을 익혔죠. 이번 보충에서는 같은 목표를 **cron과 셸 스크립트 + Claude Code**로 구현합니다. 본문의 ChatGPT Tasks가 "클릭 한 번으로 반복 알림"이라면, cron은 **완전한 로컬 자동화** — 인터넷 없이도, AI 구독 없이도 정해진 시간에 자동으로 작업을 수행합니다. 일정 리마인더, 간격 반복 기반 복습 문제, 학습 분석까지 — "내가 잊어도 AI가 챙겨주는" 시스템을 구축합니다.

---

## 1. 자동화의 마지막 퍼즐 — 스케줄링

### 1-1. 본문 도구 vs Claude Code 자동화

본문에서는 ChatGPT Tasks, Notion AI, Anki 등 **클라우드 기반 도구**로 Plan-Do-Check 3축을 구현했습니다. Claude Code + cron은 같은 3축을 **로컬 자동화**로 구현합니다:

| Plan-Do-Check 축 | 본문 도구 | CC + cron 대응 |
|-----------------|----------|---------------|
| **Plan**(계획) | ChatGPT로 학습 계획 수립 | schedule-manager 에이전트 + CLAUDE.md 규칙 |
| **Do**(실행) | Anki 간격 반복, ChatGPT Tasks 반복 알림 | quiz-generator + cron 자동 실행 |
| **Check**(피드백) | ChatGPT로 학습 분석 | study-tracker + 주간 KPT 리뷰 자동화 |

### 1-2. 수동 실행 vs 자동 실행

| 수동 실행 | 자동 실행 |
|----------|----------|
| 사용자가 명령 입력 | 정해진 시간에 자동 실행 |
| 잊으면 안 됨 | 잊어도 실행됨 |
| 매번 같은 명령 반복 | 한 번 설정하면 반복 |
| Part 3 Ch 7~9 방식 | **이번 챕터의 방식** |

### 1-3. cron이란?

**cron**은 macOS/Linux에 기본 내장된 작업 스케줄러입니다. 정해진 시간에 명령을 자동 실행합니다:

```bash
# cron 표현식: 분 시 일 월 요일
# 매일 아침 8시에 실행
0 8 * * * /path/to/script.sh

# 매주 월요일 9시에 실행
0 9 * * 1 /path/to/script.sh

# 매일 오후 6시에 실행
0 18 * * * /path/to/script.sh
```

| 필드 | 의미 | 범위 |
|------|------|------|
| 첫 번째 | 분 | 0-59 |
| 두 번째 | 시 | 0-23 |
| 세 번째 | 일 | 1-31 |
| 네 번째 | 월 | 1-12 |
| 다섯 번째 | 요일 | 0-7 (0,7=일요일) |

### 1-4. Claude Code + cron = 자동 AI 비서

```
cron (시간 트리거) → 셸 스크립트 → Claude Code -p (비대화형) → 결과 파일/알림
```

예시 시나리오:
- **매일 아침 8시**: 오늘의 할 일 목록 생성
- **매주 일요일 저녁**: 이번 주 학습 요약 보고서
- **시험 2주 전부터**: 매일 복습 문제 자동 생성
- **매월 1일**: 동아리 회비 정리 및 알림

---

## 2. 자동 리마인더 시스템

### 2-1. 일정 리마인더 스크립트

```bash
#!/bin/bash
# daily_reminder.sh — 매일 아침 실행

DATE=$(date '+%Y-%m-%d %A')
SCHEDULE_FILE="$HOME/study-manager/input/schedule.md"
OUTPUT="$HOME/study-manager/output/daily_reminder_$(date '+%Y%m%d').md"

claude -p "
오늘은 ${DATE}입니다.
${SCHEDULE_FILE}에서 오늘과 이번 주의 일정을 확인해서
다음 형식으로 정리해줘:

## 오늘의 일정
- [ ] 일정1 (시간)
- [ ] 일정2 (시간)

## 이번 주 남은 일정
- 수요일: ...
- 금요일: ...

## 오늘의 한줄 조언
(동기부여 메시지)

결과를 ${OUTPUT}에 저장해줘.
" --output-file "${OUTPUT}"

# macOS 알림 보내기 (선택사항)
osascript -e "display notification \"오늘의 일정이 준비되었습니다\" with title \"Daily Reminder\""
```

### 2-2. 학습 관리 스크립트

```bash
#!/bin/bash
# weekly_review.sh — 매주 일요일 저녁 실행

WEEK=$(date '+%Y-W%V')
STUDY_LOG="$HOME/study-manager/input/study_log.md"
OUTPUT="$HOME/study-manager/output/weekly_review_${WEEK}.md"

claude -p "
${STUDY_LOG}에서 이번 주(${WEEK}) 학습 기록을 분석해서
주간 학습 리뷰를 작성해줘:

## 이번 주 학습 요약
- 총 학습 시간:
- 과목별 시간 분배:
- 완료한 과제/목표:

## 잘한 점 (Keep)
## 개선할 점 (Problem)
## 다음 주 계획 (Try)

## 과목별 복습 우선순위
(학습 시간이 적은 과목 순으로 정렬)

결과를 ${OUTPUT}에 저장해줘.
" --output-file "${OUTPUT}"
```

### 2-3. cron 등록 방법

```bash
# cron 편집기 열기
crontab -e

# 다음 줄 추가:
# 매일 아침 8시 — 일정 리마인더
0 8 * * * /bin/bash $HOME/study-manager/daily_reminder.sh

# 매주 일요일 오후 8시 — 주간 학습 리뷰
0 20 * * 0 /bin/bash $HOME/study-manager/weekly_review.sh

# 저장하고 종료 (vi: :wq, nano: Ctrl+O → Ctrl+X)
```

등록 확인:
```bash
crontab -l  # 현재 등록된 cron 작업 목록
```

---

## 3. 학습 관리 하네스 설계

### 3-1. 에이전트 팀 구성

```
~/study-manager/
├── CLAUDE.md                 ← 학습 관리 규칙
├── .claude/
│   └── agents/
│       ├── schedule-manager.md  ← 일정 관리
│       ├── study-tracker.md     ← 학습 추적·분석
│       └── quiz-generator.md    ← 복습 문제 생성
├── input/
│   ├── schedule.md           ← 학기 일정
│   ├── study_log.md          ← 학습 기록
│   └── course_notes/         ← 수업 노트
├── _workspace/
├── output/
│   ├── daily/                ← 일별 리마인더
│   └── weekly/               ← 주간 리뷰
└── scripts/
    ├── daily_reminder.sh     ← 매일 실행
    ├── weekly_review.sh      ← 매주 실행
    └── quiz_generator.sh     ← 시험 전 실행
```

**schedule-manager.md**:
```markdown
---
name: schedule-manager
description: "학기 일정을 관리하고 일별/주별 리마인더를 생성하는 에이전트"
---
# Schedule Manager — 일정 관리자

## 핵심 역할
- schedule.md에서 오늘/이번 주의 일정을 추출합니다.
- 과제 마감, 시험, 발표 등 중요 일정의 D-day를 계산합니다.
- 우선순위별로 정렬된 할 일 목록을 생성합니다.

## 작업 원칙
- 마감 임박(D-3 이내) 항목은 ⚠️로 강조합니다.
- 오늘 마감 항목은 🚨로 표시합니다.
- 완료된 항목은 자동으로 제외합니다.
- 주말에는 다음 주 미리보기를 포함합니다.

## 출력
- output/daily/reminder_YYYYMMDD.md: 일별 리마인더
```

**quiz-generator.md**:
```markdown
---
name: quiz-generator
description: "수업 노트를 바탕으로 복습 문제를 생성하는 에이전트"
---
# Quiz Generator — 복습 문제 생성기

## 핵심 역할
- course_notes/ 폴더의 수업 노트를 읽고 복습 문제를 생성합니다.
- 객관식(4지선다), 주관식(단답형), 서술형을 균형있게 포함합니다.
- 이전에 생성한 문제와 중복되지 않도록 합니다.
- **간격 반복(Spaced Repetition)** 원리를 적용합니다 — 본문에서 소개한 Anki의 원리(SAGE Journals 연구: 시험 성적 6.2~12.9% 향상)를 따릅니다.

## 작업 원칙
- Bloom의 분류 체계 기반: 기억(30%) → 이해(30%) → 적용(25%) → 분석(15%)
- 각 문제에 정답과 해설을 포함합니다.
- 문제 수: 과목당 10문제
- 난이도 표시: ⭐(기본), ⭐⭐(중급), ⭐⭐⭐(심화)
- **복습 간격 태그**: 각 문제에 [D+1], [D+3], [D+7] 복습 권장 시점을 표시합니다 (에빙하우스 망각 곡선 기반)

## 출력
- output/quiz/quiz_과목명_YYYYMMDD.md: 복습 문제
```

### 3-2. CLAUDE.md 학습 관리 규칙

```markdown
# 학습 관리 시스템 규칙

## 일정 형식
schedule.md의 일정은 다음 형식을 따릅니다:
- YYYY-MM-DD | 과목명 | 유형(과제/시험/발표) | 설명

## 학습 기록 형식
study_log.md의 기록은 다음 형식을 따릅니다:
- YYYY-MM-DD | 과목명 | 시간(분) | 내용

## 원칙
- **현실적 제약을 반드시 반영**: 통학 시간, 아르바이트, 수면 등 개인 상황을 프롬프트에 포함해야 실행 가능한 계획이 나온다 (본문 핵심 교훈)
- 동기부여 메시지는 강요하지 않고 격려 톤으로
- 학습 시간 분석 시 수면/휴식의 중요성도 언급
- 비현실적인 계획 제안 금지 (하루 최대 학습 8시간, 계획 강도는 80% 수준으로 — "작심삼일" 방지)
- "요약해줘" 대신 "테스트해줘" — 수동적 요약보다 능동적 자기 테스트를 우선
```

---

### 🔬 프롬프트 진화 실험: 학습 관리 자동화

#### 🔴 Level 1 — 초보 프롬프트

```
오늘 할 일 알려줘
```

**결과**: Claude Code에 일정 정보가 없어 일반적인 조언만 합니다. "수업에 잘 참석하세요, 과제를 미리 하세요" 같은 범용적 답변.

📋 **평가**:
- 정확성: ★☆☆☆☆
- 활용도: ★☆☆☆☆
- 문제점: 개인 일정 데이터, 실행 시점, 원하는 형식 모두 미제공

---

#### 🟡 Level 2 — 중급 프롬프트

```
input/schedule.md를 읽고 오늘(2026-03-17) 할 일을 정리해줘.
마감 임박 과제도 알려줘.
```

**결과**: 오늘 일정과 과제를 추출하지만, 매번 수동으로 실행해야 하고, 날짜를 직접 입력해야 합니다.

📋 **평가**:
- 정확성: ★★★☆☆
- 활용도: ★★★☆☆
- 개선점: 일정 파일과 날짜가 지정됨
- 아쉬운 점: 수동 실행, 알림 없음, 학습 분석 없음

---

#### 🟢 Level 3 — 전문가 프롬프트 (cron + 하네스)

```bash
# crontab에 등록 — 매일 아침 8시 자동 실행
0 8 * * * /bin/bash ~/study-manager/scripts/daily_reminder.sh
```

`daily_reminder.sh`가 매일 자동으로:
1. 오늘 날짜를 자동 감지
2. schedule.md에서 일정 추출
3. D-day 계산 및 우선순위 정렬
4. 리마인더 파일 생성
5. macOS 알림 발송

📋 **평가**:
- 정확성: ★★★★★
- 활용도: ★★★★★
- 핵심 차이: 한 번 설정하면 매일 자동 실행, 사람의 개입 없이 동작

---

#### 💡 교훈: 프롬프트의 마법

| 요소 | Level 1 | Level 2 | Level 3 |
|------|---------|---------|---------|
| 일정 데이터 | ✗ | ✓ | ✓ |
| 날짜 자동 감지 | ✗ | ✗ | ✓ |
| 자동 실행 | ✗ | ✗ | ✓ (cron) |
| 알림 | ✗ | ✗ | ✓ (macOS) |
| 학습 분석 | ✗ | ✗ | ✓ (주간 리뷰) |
| 결과 품질 | 5% | 50% | 95% |

---

### ❌ 흔한 실수: 자동화 만능주의 + cron 함정

**상황 1 — "AI 의존 학습의 역설"이 자동화에도 적용된다**

본문에서 경고한 "AI가 교사가 아니라 대필자가 되는 순간" — 이것은 cron 자동화에도 그대로 적용됩니다. quiz-generator가 매일 문제를 만들어줘도, **직접 풀지 않으면 의미 없습니다**. 자동 생성된 복습 문제를 "읽기만" 하면 본문의 간격 반복 효과(6.2~12.9% 향상)를 전혀 얻을 수 없습니다. 반드시 **직접 답을 작성한 후** 정답을 확인하세요.

**상황 2 — "작심삼일" 자동화 버전**

본문의 "작심삼일" 경고: 비현실적 계획은 3일 만에 포기합니다. cron도 마찬가지 — 매일 아침 8시 + 저녁 9시 + 일요일 리뷰를 한꺼번에 등록하면, 알림 피로로 1주일 만에 전부 무시하게 됩니다. **처음에는 일일 리마인더 1개만** 등록하고, 습관이 잡히면 점진적으로 추가하세요. 계획 강도는 본문 조언대로 "내가 가능하다고 생각하는 양의 80%"로 설정합니다.

---

**상황 3 — cron 환경 변수 함정**

cron으로 Claude Code 자동 실행을 설정할 때:

---

**잘못된 방법 — 환경 변수와 경로를 무시**:

```bash
# crontab에 이렇게 등록
0 8 * * * daily_reminder.sh
```

**결과**: cron은 사용자의 셸 환경(.zshrc 등)을 로드하지 않습니다. `claude` 명령어 경로를 찾지 못하고, 환경 변수도 없어서 스크립트가 실패합니다. 오류 로그도 확인하기 어렵습니다.

**올바른 방법**:

```bash
# 절대 경로 사용 + 환경 변수 설정 + 로그 기록
0 8 * * * /bin/bash -l $HOME/study-manager/scripts/daily_reminder.sh >> $HOME/study-manager/logs/cron.log 2>&1
```

스크립트 내부에서도:
```bash
#!/bin/bash
# 환경 변수 명시적 설정
export PATH="/usr/local/bin:/opt/homebrew/bin:$PATH"
export HOME="/Users/username"

# claude 명령어의 절대 경로 확인
CLAUDE=$(which claude)
```

**차이**: cron 환경에서는 경로와 환경 변수를 명시적으로 설정해야 합니다. `/bin/bash -l`로 로그인 셸을 사용하거나, 스크립트 내에서 직접 설정하세요. 로그 파일로 오류를 추적할 수 있게 하는 것도 중요합니다.

---

## 실습 과제

### 🎯 실습: 간단한 일일 리마인더 만들기 ⭐

**목표**: Claude Code로 오늘의 할 일 리마인더를 생성하는 스크립트를 만듭니다.
**소요 시간**: 10분
**준비물**: Claude Code
**사용 도구**: Claude Code

---

#### Step 1. 일정 파일 만들기 ⏱️ 3분

```
이번 주 대학생 일정 예시를 만들어줘.
형식: YYYY-MM-DD | 과목명 | 유형 | 설명
과제 마감 3개, 수업 5개, 시험 1개를 포함해줘.
input/schedule.md에 저장해줘.
```

✅ **체크**: `input/schedule.md`에 9개 이상의 일정이 있으면 성공

---

#### Step 2. 리마인더 생성 테스트 ⏱️ 5분

```
input/schedule.md를 읽고 오늘의 리마인더를 만들어줘.

포함 내용:
- 오늘 일정 (없으면 "오늘은 일정이 없습니다")
- 마감 임박 과제 (D-3 이내는 ⚠️, D-day는 🚨)
- 이번 주 남은 일정 미리보기

output/today_reminder.md에 저장해줘.
```

✅ **체크**: D-day가 계산된 리마인더가 생성되면 성공

> 🔧 **안 되나요?**: 날짜 계산이 틀리면 → "오늘 날짜는 2026-03-17이야. 이 기준으로 D-day를 다시 계산해줘"라고 명시하세요.

---

#### Step 3. 셸 스크립트로 감싸기 ⏱️ 2분

```
Step 2의 작업을 매일 실행할 수 있는 셸 스크립트로 만들어줘.
스크립트 이름: scripts/daily_reminder.sh
날짜는 자동으로 오늘 날짜를 감지하도록 해줘.
실행 권한도 설정해줘.
```

✅ **체크**: `scripts/daily_reminder.sh`가 생성되고, `bash scripts/daily_reminder.sh`로 실행되면 성공

---

#### 🎉 완성! — 결과물 미리보기

매일 실행하면 오늘의 할 일이 자동으로 정리되는 스크립트를 만들었습니다.

> 📊 **효과**:
> - 핵심 이해: 셸 스크립트로 Claude Code를 감싸면 반복 실행이 가능
> - 다음 실습(⭐⭐)에서 이 스크립트를 cron으로 자동화합니다

---

### 🎯 실습: cron으로 자동 리마인더 설정 ⭐⭐

**목표**: cron을 설정하여 매일 아침 자동으로 리마인더가 생성되도록 합니다.
**소요 시간**: 20분
**준비물**: 이전 실습의 리마인더 스크립트
**사용 도구**: Claude Code, cron

---

#### Step 1. 스크립트 보완 ⏱️ 5분

cron 환경에서 동작하도록 스크립트를 보완합니다:

```
scripts/daily_reminder.sh를 cron 환경에서도 동작하도록 수정해줘:
1. PATH에 claude 경로 추가
2. 절대 경로로 모든 파일 참조
3. 실행 로그를 logs/ 폴더에 기록
4. 실행 결과를 macOS 알림으로 표시 (osascript)
```

✅ **체크**: `scripts/daily_reminder.sh`에 PATH 설정, 절대 경로, 로그 기록이 포함되면 성공

---

#### Step 2. cron 등록 ⏱️ 5분

```
crontab에 daily_reminder.sh를 매일 아침 8시에 실행하도록 등록해줘.
로그는 logs/cron.log에 기록되도록 해줘.
등록 후 crontab -l로 확인해줘.
```

✅ **체크**: `crontab -l`에서 등록된 작업이 보이면 성공

> ⚠️ **주의**: macOS에서 cron을 처음 사용하면 "터미널에 디스크 접근 권한" 팝업이 나올 수 있습니다. 시스템 설정 → 개인정보 보호 및 보안 → 전체 디스크 접근 권한에서 허용하세요.

---

#### Step 3. 주간 리뷰 스크립트 추가 ⏱️ 8분

```
주간 학습 리뷰 스크립트를 만들어줘.
스크립트 이름: scripts/weekly_review.sh

기능:
1. input/study_log.md에서 이번 주 학습 기록 분석
2. 과목별 학습 시간 집계
3. KPT 형식(Keep/Problem/Try) 리뷰 작성
4. 다음 주 추천 계획

매주 일요일 오후 8시에 cron 등록도 해줘.
```

> 💡 **커스텀 포인트**: study_log.md가 없으면 Claude Code가 샘플을 생성합니다.

✅ **체크**: `scripts/weekly_review.sh`가 생성되고, cron에 등록되면 성공

> 🔧 **안 되나요?**: cron이 실행되지 않으면 → `logs/cron.log`를 확인하세요. 가장 흔한 원인은 `claude` 명령어 경로 문제입니다. `which claude`로 경로를 확인하고 스크립트에 추가하세요.

---

#### Step 4. 테스트 실행 ⏱️ 2분

```bash
# 수동으로 테스트 실행
bash ~/study-manager/scripts/daily_reminder.sh
bash ~/study-manager/scripts/weekly_review.sh

# 결과 확인
ls ~/study-manager/output/
```

✅ **체크**: `output/` 폴더에 리마인더와 리뷰 파일이 생성되면 성공

---

#### 🎉 완성! — 결과물 미리보기

매일 아침 + 매주 일요일, 자동으로 학습 관리 보고서가 생성됩니다.

> 📊 **효과**:
> - 기존 방식: 매일 수동으로 일정 확인 + 주말에 수기 리뷰 — 하루 10분 × 7 = 70분/주
> - cron 자동화: 설정 한 번 → 매일 자동 — 설정 후 0분/주
> - 절약: 주당 1시간 + "잊어버릴 걱정" 제거

---

### 🎯 실습: 종합 학습 관리 하네스 구축 ⭐⭐⭐

**목표**: 일정 관리, 학습 추적, 복습 문제 생성을 통합한 학습 관리 하네스를 구축합니다.
**소요 시간**: 50분
**준비물**: Claude Code, 학기 일정, 수업 노트
**사용 도구**: Claude Code, cron

---

#### Step 1. 학습 관리 하네스 구축 ⏱️ 15분

```
~/study-manager/ 에 종합 학습 관리 하네스를 구축해줘.

폴더 구조:
~/study-manager/
├── CLAUDE.md
├── .claude/agents/ (3개)
├── input/ (schedule.md, study_log.md, course_notes/)
├── _workspace/
├── output/ (daily/, weekly/, quiz/)
├── scripts/ (3개 스크립트)
└── logs/

CLAUDE.md: 일정 형식, 학습 기록 형식, 하루 최대 학습 8시간 제한, 계획 강도 80% 원칙, "현실적 제약 반영" 규칙

에이전트:
1. schedule-manager.md — 일정 추출, D-day 계산, 리마인더
2. study-tracker.md — 학습 시간 분석, KPT 리뷰, 과목별 균형
3. quiz-generator.md — 수업 노트 기반 복습 문제 (객관식+서술형)

스크립트:
1. daily_reminder.sh — 매일 8시
2. weekly_review.sh — 매주 일요일 20시
3. quiz_generator.sh — 시험 D-7부터 매일 21시

input/ 에 이번 학기 일정 샘플과 학습 기록 샘플도 만들어줘.
```

✅ **체크**: 전체 폴더 구조 + CLAUDE.md + 에이전트 3개 + 스크립트 3개가 완성되면 성공

---

#### Step 2. 복습 문제 생성기 설정 ⏱️ 10분

```
input/course_notes/ 폴더에 "데이터베이스" 과목의
수업 노트 샘플을 2주차분 만들어줘.
그리고 quiz-generator.sh로 복습 문제 10문제를 생성해줘.

문제 형식:
- 객관식 5문제 (4지선다, 정답+해설)
- 단답형 3문제 (정답+해설)
- 서술형 2문제 (모범답안+채점기준)
- 각 문제에 난이도(⭐~⭐⭐⭐)와 관련 노트 페이지 표시
```

✅ **체크**: `output/quiz/` 폴더에 문제 파일이 생성되고, 3가지 유형이 포함되면 성공

> ⚠️ **주의**: AI 생성 문제의 정확성을 반드시 확인하세요. 특히 전공 개념과 용어가 정확한지 수업 자료와 대조하세요.

---

#### Step 3. cron 일괄 등록 ⏱️ 5분

```
3개 스크립트를 cron에 일괄 등록해줘:
1. daily_reminder.sh — 매일 08:00
2. weekly_review.sh — 매주 일요일 20:00
3. quiz_generator.sh — 매일 21:00 (시험 기간만 수동 활성화)

crontab -l로 등록 결과를 확인하고,
scripts/manage_cron.sh에 cron 등록/해제 스크립트도 만들어줘.
```

✅ **체크**: `crontab -l`에 3개 작업이 등록되고, `manage_cron.sh`가 생성되면 성공

> 🔧 **안 되나요?**: quiz_generator.sh의 시험 기간 활성화가 어려우면 → `manage_cron.sh enable-quiz` / `manage_cron.sh disable-quiz`처럼 간단한 토글 스크립트를 만들어 사용하세요.

---

#### Step 4. 전체 시스템 테스트 ⏱️ 15분

```bash
# 1. 일일 리마인더 테스트
bash ~/study-manager/scripts/daily_reminder.sh
cat ~/study-manager/output/daily/reminder_*.md

# 2. 주간 리뷰 테스트
bash ~/study-manager/scripts/weekly_review.sh
cat ~/study-manager/output/weekly/review_*.md

# 3. 복습 문제 테스트
bash ~/study-manager/scripts/quiz_generator.sh
cat ~/study-manager/output/quiz/quiz_*.md
```

✅ **체크**: 3종류의 산출물이 모두 정상 생성되면 성공

---

#### Step 5. 하네스 평가 ⏱️ 5분

```
학습 관리 하네스를 평가해줘:
1. 일정 리마인더의 정확성 (D-day, 우선순위)
2. 주간 리뷰의 인사이트 품질
3. 복습 문제의 난이도 분포와 정확성
4. cron 스케줄링의 안정성
5. 전체 시스템 개선점 3가지
결과: _workspace/system_evaluation.md
```

✅ **체크**: 5개 항목 평가가 포함된 보고서가 생성되면 성공

---

#### 🎉 완성! — 결과물 미리보기

일정 관리 + 학습 분석 + 복습 문제를 자동으로 처리하는 **개인 AI 학습 비서**를 구축했습니다.

> 📊 **효과**:
> - 기존 방식: 수동 일정 관리 + 수기 학습 기록 + 문제집 풀기 — 주당 5시간
> - 하네스 활용: cron 자동 실행 — 설정 후 주당 1시간 (검토·수정만)
> - 핵심 가치: "관리"에 쓰던 시간을 "학습" 자체에 투자

---

### 🔄 이 워크플로우를 다른 상황에 적용하기

| 이 실습의 사례 | → 이렇게 바꾸면 | 다른 활용 |
|--------------|----------------|----------|
| 학기 일정 리마인더 | 취업 준비 일정 | 채용 공고 마감·면접 리마인더 |
| 주간 학습 리뷰 | 주간 운동/건강 리뷰 | 생활 습관 관리 |
| 수업 노트 → 퀴즈 | 자격증 교재 → 문제 | 자격증 시험 대비 |
| 매일 아침 리마인더 | 매일 저녁 일기 프롬프트 | AI 활용 저널링 |
| cron + Claude Code 분석 | Notion AI + cron 연동 | .edu 무료 Notion Plus 활용 |

**핵심 패턴**: `입력 데이터 + 에이전트 + 스크립트 + cron = 자동 반복 시스템` — 정기적으로 반복되는 모든 작업에 이 패턴을 적용할 수 있습니다.

---

> 💡 **Hybrid Tip — 본문 도구 + CC 자동화 조합**
> - **빠른 시작**: 본문의 ChatGPT Tasks로 간단한 반복 알림 설정 (클릭 한 번, 설정 2분)
> - **심화 자동화**: Claude Code + cron으로 커스텀 학습 관리 시스템 구축 (설정 50분, 이후 완전 자동)
> - **최적 조합**: Notion AI(.edu 무료 Plus)로 일정 관리 + cron으로 Claude Code 분석 자동화 — Notion에 기록하고, cron이 매주 분석 보고서를 자동 생성
> - **복습 조합**: Anki/Quizlet로 모바일 플래시카드 + quiz-generator로 서술형·응용 문제 자동 생성 — 암기는 Anki, 이해도 테스트는 Claude Code

> **핵심 정리**: 본문에서 배운 Plan-Do-Check 3축과 간격 반복 원리를 Claude Code + cron으로 **완전 자동화**했습니다. 본문의 핵심 교훈 — "AI에게 현실적 제약을 알려줘라", "요약해줘보다 테스트해줘" — 은 CLAUDE.md 규칙과 에이전트 설계에 그대로 녹아 있습니다. Part 3의 여정을 돌아보면, Ch 7(슬라이드)·Ch 8(이미지)·Ch 9(데이터·문서)에서 Claude Code의 **변환 능력**을 배웠고, 이번 Ch 10에서 **스케줄링**을 더해 완전한 자동화를 달성했습니다. HEPI 2025 보고서에 따르면 AI 활용 학생의 51%가 시간 절약을 경험했는데, cron 자동화까지 갖추면 그 효과는 더욱 극대화됩니다. 이제 여러분은 단순히 "AI에게 질문하는 사람"이 아니라, **"AI가 일하는 시스템을 설계하는 사람"**이 되었습니다. 다음 파트에서는 이 모든 능력을 데이터 분석과 취업 준비에 본격적으로 활용합니다.
