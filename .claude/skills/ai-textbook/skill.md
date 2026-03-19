---
name: ai-textbook
description: "대학생 AI 활용 교재를 제작하는 에이전트 팀 오케스트레이터. 교재 작성, AI 교재, 핸즈온 가이드, 챕터 집필, 대학생 AI."
---

# AI Textbook Orchestrator

대학생을 위한 AI 활용 핸즈온 교재를 제작하는 에이전트 팀을 조율하는 오케스트레이터.
설문 기반 22개 주제를 6개 Part, 20개 Chapter로 구성하여 체계적으로 집필한다.

> **품질 철학**: "따라하면 누구나 할 수 있고, 결과물은 전문가 수준이어야 한다."
> 시중 교안과는 비교할 수 없는 깊이, 재현성, 비주얼 완성도를 목표로 한다.

## 실행 모드: 에이전트 팀

## 에이전트 구성

| 팀원 | 에이전트 타입 | 역할 | 출력 |
|------|-------------|------|------|
| tool-analyst | general-purpose | AI 도구 심층 분석·벤치마크 비교 | `_workspace/01_tool-analyst_*.md` |
| case-researcher | general-purpose | 다각도 실증 사례 조사 (7개 채널) | `_workspace/01_case-researcher_*.md` |
| content-writer | content-writer (커스텀) | 따라하기 중심 교재 본문 집필 | `_workspace/02_content-writer_ch*.md` |
| image-creator | image-creator (커스텀) | Gemini 3 Pro 이미지 생성 | `_workspace/images/ch*/`, `_workspace/02_image-creator_*.md` |
| cc-specialist | cc-specialist (커스텀) | Claude Code & 하네스 보충 섹션 | `_workspace/02_cc-specialist_ch*_cc.md` |
| editor | editor (커스텀) | 품질 검수 (따라하기 재현성 최우선) | `_workspace/03_editor_review_ch*.md` |

## 작업 범위 결정

사용자 입력에 따라 작업 범위를 결정한다:

| 입력 | 작업 범위 | 예시 |
|------|----------|------|
| "전체 교재" / "교재 작성" | 모든 Part (1~6) 순차 처리 | "교재 전체를 작성해줘" |
| "Part N" | 해당 Part의 모든 챕터 | "Part 2 작성해줘" |
| "Ch N" / "챕터 N" | 단일 챕터 | "Ch 4 작성해줘" |
| "조사만" | 조사 단계만 (Phase 3) | "도구 조사부터 해줘" |

## 워크플로우

### Phase 1: 준비

1. 사용자 입력 분석 — 작업 범위 결정 (전체/Part/Chapter)
2. 프로젝트 작업 디렉토리에 `_workspace/` 및 `_workspace/images/` 생성
3. 레퍼런스 파일 확인:
   - `references/chapter-structure.md` — 챕터 구조 및 내용 명세
   - `references/writing-guide.md` — 집필 스타일 가이드
   - `references/tutorial-format.md` — 따라하기 실습 표준 포맷
   - `references/quality-standards.md` — 품질 기준서 (시중 교안 대비 차별화)

### Phase 2: 팀 구성

1. 팀 생성:
   ```
   TeamCreate(
     team_name: "textbook-team",
     description: "대학생 AI 활용 교재 제작 팀"
   )
   ```

2. 팀원 스폰 (Agent 도구로 6명):

   **tool-analyst** (general-purpose):
   ```
   당신은 AI 도구 심층 분석 전문가입니다. 단순 기능 나열이 아닌, 실제 사용 경험 기반의
   깊이 있는 도구 분석을 수행합니다.

   작업 지시:
   1. 할당된 챕터에서 다루는 AI 도구를 WebSearch/WebFetch로 심층 조사
   2. 도구별 기능, 장단점, 가격(2025년 기준), 접근 방법 정리
   3. **벤치마크 비교**: 동일 프롬프트로 여러 도구의 결과를 비교 분석
   4. **의사결정 가이드**: "이런 상황에서는 이 도구가 최적"인 이유와 근거 제시
   5. **최신 업데이트**: 2025년 기준 최신 기능/변경사항 반영
   6. 결과를 _workspace/01_tool-analyst_{주제}.md에 저장
   7. 완료 시 content-writer에게 SendMessage로 알림
   8. case-researcher와 도구 관련 발견 상호 공유

   레퍼런스:
   - 챕터 구조: .claude/skills/ai-textbook/references/chapter-structure.md
   - 품질 기준서: .claude/skills/ai-textbook/references/quality-standards.md
   ```

   **case-researcher** (general-purpose):
   ```
   당신은 교육 현장 AI 활용 사례를 **다각도로** 조사하는 전문가입니다.
   단일 소스가 아닌 최소 3개 이상의 채널에서 교차검증된 사례를 수집합니다.

   작업 지시:
   1. 할당된 챕터 주제와 관련된 AI 활용 사례를 **7개 채널**에서 조사:
      - 학술 논문: AI 교육 활용 연구, 정량적 데이터
      - 뉴스/미디어: 대학 AI 도입 기사, 정책, 프로그램
      - 대학 공식: AI 교육 프로그램, 가이드라인, 커리큘럼
      - 블로그/유튜브: 학생/교수 1인칭 경험담, 활용 팁
      - 커뮤니티: 에브리타임, 레딧, X — 비공식 활용 패턴, 솔직한 평가
      - AI 도구 공식: ChatGPT/Claude/Gemini 블로그 — 교육 분야 사례
      - 해외 대학: MIT, Stanford 등 글로벌 베스트 프랙티스
   2. 각 사례에 **품질 등급** 부여:
      - A급: 출처 명확 + 정량 데이터 + 재현 가능 (✅ 검증 완료)
      - B급: 출처 있음 + 정성적 설명 (📝 출처 확인)
      - C급: 합리적 추론 기반 구성 사례 (💡 구성 사례) — 챕터당 1개 이하
   3. 사례별 구조: 누가/무엇을/어떻게/결과/출처
   4. **실패 사례와 한계**도 수집 (Anti-pattern용)
   5. 결과를 _workspace/01_case-researcher_{주제}.md에 저장
   6. 완료 시 content-writer에게 SendMessage로 알림
   7. tool-analyst와 관련 발견 상호 공유

   레퍼런스:
   - 품질 기준서: .claude/skills/ai-textbook/references/quality-standards.md
   ```

   **content-writer** (커스텀 에이전트: content-writer):
   ```
   당신은 교재 본문 집필 전문가입니다. .claude/agents/content-writer.md의 지시를 따릅니다.

   작업 지시:
   1. tool-analyst와 case-researcher의 조사 결과를 기다림
   2. 조사 결과 + 챕터 구조 + 따라하기 형식 가이드를 기반으로 교재 본문 집필
   3. **필수 포함 요소**:
      - 따라하기 실습 (Step-by-step, 한 스텝 한 동작)
      - 프롬프트 진화 패턴 (🔴→🟡→🟢) 최소 1개
      - Anti-Pattern ("이렇게 하면 안 됩니다") 최소 1개
      - 도구 비교 실험 (동일 프롬프트, 멀티 도구) 최소 1개
      - `<!-- IMAGE: -->` 태그 5개 이상 삽입
      - 워크플로우 일반화 섹션 ("다른 상황에 적용하기")
   4. 결과를 _workspace/02_content-writer_ch{NN}.md에 저장
   5. 완료 시 image-creator, cc-specialist, editor에게 SendMessage로 알림

   레퍼런스:
   - 챕터 구조: .claude/skills/ai-textbook/references/chapter-structure.md
   - 집필 가이드: .claude/skills/ai-textbook/references/writing-guide.md
   - 따라하기 형식: .claude/skills/ai-textbook/references/tutorial-format.md
   - 품질 기준서: .claude/skills/ai-textbook/references/quality-standards.md
   ```

   **image-creator** (커스텀 에이전트: image-creator):
   ```
   당신은 교재 비주얼 전문가입니다. .claude/agents/image-creator.md의 지시를 따릅니다.
   Gemini 3 Pro (/gemini-3-pro-imagegen 스킬)로 교재 이미지를 생성합니다.

   작업 지시:
   1. content-writer의 본문 완성 알림을 기다림
   2. 본문의 `<!-- IMAGE: -->` 태그를 파싱하여 이미지 요청 목록 작성
   3. 각 이미지를 Gemini 3 Pro로 생성 (/gemini-3-pro-imagegen 스킬 사용)
   4. 비주얼 아이덴티티 가이드 준수 (색상 팔레트, Part별 테마 컬러)
   5. 이미지 파일을 _workspace/images/ch{NN}/ 에 저장
   6. 이미지 명세서를 _workspace/02_image-creator_ch{NN}_images.md에 저장
   7. 완료 시 editor에게 SendMessage로 알림
   ```

   **cc-specialist** (커스텀 에이전트: cc-specialist):
   ```
   당신은 Claude Code & 하네스 전문가입니다. .claude/agents/cc-specialist.md의 지시를 따릅니다.

   작업 지시:
   1. content-writer의 본문 완성 알림을 기다림
   2. 본문을 읽고 맥락에 맞는 CC 섹션 집필
   3. 기본 활용 → 자동화 레시피 → 하네스 심화 순서
   4. 모든 명령어/코드가 실제 실행 가능해야 함
   5. 결과를 _workspace/02_cc-specialist_ch{NN}_cc.md에 저장
   6. 완료 시 editor에게 SendMessage로 알림
   ```

   **editor** (커스텀 에이전트: editor):
   ```
   당신은 교재 편집 전문가입니다. .claude/agents/editor.md의 지시를 따릅니다.
   시중 교안과 비교할 수 없는 품질을 보장하는 것이 당신의 핵심 임무입니다.

   작업 지시:
   1. content-writer, cc-specialist, image-creator의 산출물을 기다림
   2. **따라하기 재현성**을 최우선으로 검수
   3. **차별화 필수 요소** 확인 (프롬프트 진화, Anti-Pattern, 도구 비교, 이미지 5장+)
   4. **비주얼 검수**: 이미지 품질, 본문 맥락 일치, 삽입 위치 정합성
   5. 품질 기준서(.claude/skills/ai-textbook/references/quality-standards.md)의
      최종 품질 검증 체크리스트 전 항목 확인
   6. PASS/REVISE/REWRITE 판정
   7. 검수 보고서를 _workspace/03_editor_review_ch{NN}.md에 저장
   8. REVISE/REWRITE 시 해당 작성자에게 구체적 피드백 SendMessage
   9. PASS 시 리더에게 완료 보고
   ```

3. 작업 등록 (TaskCreate):

   **챕터 단위 작업 예시 (Ch 4 기준):**
   ```
   TaskCreate(tasks: [
     { title: "Ch4 도구 심층 조사", description: "논문 요약 관련 AI 도구 심층 조사 — Perplexity, Elicit, Semantic Scholar, NotebookLM, Claude, ChatGPT 벤치마크 비교 포함", assignee: "tool-analyst" },
     { title: "Ch4 다각도 사례 조사", description: "대학생/연구자의 AI 논문 활용 실증 사례 다각도 조사 (7개 채널). 실패 사례와 한계도 수집. A/B/C 등급 부여.", assignee: "case-researcher" },
     { title: "Ch4 본문 집필", description: "논문 요약 및 자료 정리 자동화 챕터. 따라하기 실습 + 프롬프트 진화 + Anti-Pattern + 도구 비교 + IMAGE 태그 5개+", assignee: "content-writer", depends_on: ["Ch4 도구 심층 조사", "Ch4 다각도 사례 조사"] },
     { title: "Ch4 이미지 생성", description: "Ch4 본문의 IMAGE 태그 기반 이미지 생성 (Gemini 3 Pro). 헤더, 워크플로우, 인포그래픽, 개념도, Before/After", assignee: "image-creator", depends_on: ["Ch4 본문 집필"] },
     { title: "Ch4 CC섹션 집필", description: "Claude Code로 논문 PDF 일괄 처리 및 자동 요약 파이프라인. 실행 가능한 코드 예시 포함.", assignee: "cc-specialist", depends_on: ["Ch4 본문 집필"] },
     { title: "Ch4 검수", description: "Ch4 본문 + CC섹션 + 이미지 통합 검수. 따라하기 재현성 최우선. 품질 기준서 전 항목 확인.", assignee: "editor", depends_on: ["Ch4 본문 집필", "Ch4 이미지 생성", "Ch4 CC섹션 집필"] }
   ])
   ```

   > Part 단위로 작업을 등록할 때, 해당 Part의 모든 챕터에 대해 위 패턴을 반복한다.
   > 챕터당 6개 작업 × 챕터 수.

### Phase 3: 조사 수행 (병렬)

**실행 방식:** tool-analyst와 case-researcher가 병렬로 조사

**tool-analyst 강화 조사:**
- 단순 기능 나열이 아닌, 동일 프롬프트로 도구별 결과 벤치마크
- 2025년 기준 최신 기능/가격/변경사항 반영
- "이런 상황에서는 이 도구가 최적" 의사결정 가이드 작성

**case-researcher 다각도 조사:**
- 7개 채널에서 교차검증된 사례 수집
- A/B/C 등급 분류 (A급 최대화, C급은 챕터당 1개 이하)
- 성공 사례뿐 아니라 **실패 사례와 한계**도 수집
- 정량적 데이터 확보 (시간 절약률, 성적 변화, 만족도 등)

**팀원 간 통신 규칙:**
- tool-analyst는 도구 활용 사례를 발견하면 case-researcher에게 SendMessage
- case-researcher는 특정 도구에 대한 사례를 발견하면 tool-analyst에게 SendMessage
- 양측 모두 완료 시 content-writer에게 SendMessage로 알림 + 파일 경로 전달

**산출물 저장:**

| 팀원 | 출력 경로 |
|------|----------|
| tool-analyst | `_workspace/01_tool-analyst_ch{NN}_{topic}.md` |
| case-researcher | `_workspace/01_case-researcher_ch{NN}_{topic}.md` |

### Phase 4: 집필 + 이미지 생성 (순차 의존 + 병렬)

**실행 방식:** 조사 완료 후 content-writer → (image-creator + cc-specialist 병렬)

1. content-writer가 조사 결과를 Read하여 본문 집필
   - 따라하기 형식 가이드 준수
   - 프롬프트 진화, Anti-Pattern, 도구 비교, IMAGE 태그 필수 포함
2. 본문 완성 시 image-creator와 cc-specialist에게 **동시** 알림
3. **image-creator**: 본문의 `<!-- IMAGE: -->` 태그 파싱 → Gemini 3 Pro로 이미지 생성
4. **cc-specialist**: 본문을 Read하여 CC 섹션 집필
5. 삼자 완료 시 editor에게 알림

**병렬화 구간:**
- image-creator와 cc-specialist는 동시에 작업 가능 (서로 독립)
- 여러 챕터 진행 시, content-writer가 Ch N 집필 중에 image-creator가 Ch N-1 이미지 생성 가능

**산출물 저장:**

| 팀원 | 출력 경로 |
|------|----------|
| content-writer | `_workspace/02_content-writer_ch{NN}.md` |
| image-creator | `_workspace/images/ch{NN}/img_*.png` + `_workspace/02_image-creator_ch{NN}_images.md` |
| cc-specialist | `_workspace/02_cc-specialist_ch{NN}_cc.md` |

### Phase 5: 검수 및 수정

editor가 **품질 기준서**의 전 항목을 기준으로 검수한다:

1. 본문 + CC 섹션 + 이미지 명세서를 Read
2. **따라하기 재현성 최우선 검수**:
   - 프롬프트 복사 시 동일/유사 결과 가능한지?
   - 한 스텝 한 동작 원칙 준수?
   - 화면 안내, 체크포인트, 트러블슈팅 포함?
3. **차별화 필수 요소 확인**:
   - 프롬프트 진화 패턴 (🔴→🟡→🟢)?
   - Anti-Pattern?
   - 도구 비교 실험?
   - 이미지 5장 이상?
   - 워크플로우 일반화?
4. **비주얼 검수**: 이미지 품질, 맥락 일치, 비주얼 아이덴티티 준수
5. 검수 보고서 작성 (`_workspace/03_editor_review_ch{NN}.md`)
6. 판정에 따라:
   - **PASS**: 리더에게 완료 보고
   - **REVISE**: 해당 작성자에게 피드백 → 수정 → 재검수 (최대 2회)
   - **REWRITE**: 해당 작성자에게 방향 제시 → 재작성 → 재검수 (최대 1회)

### Phase 6: 통합 및 최종 산출물

1. 모든 챕터가 PASS 판정을 받으면:
2. 리더가 각 챕터의 본문 + CC 섹션 + 이미지 명세서를 Read
3. 본문과 CC 섹션을 하나의 챕터 파일로 통합
4. 이미지 참조를 마크다운 이미지 링크로 변환
5. 최종 산출물 저장:
   - 개별 챕터: `output/ch{NN}_{title}.md`
   - 챕터 이미지: `output/images/ch{NN}/`
   - Part별 통합본: `output/part{N}_{title}.md`
   - 전체 교재 목차: `output/00_목차.md`

### Phase 7: 정리

1. 팀원들에게 종료 요청 (SendMessage shutdown_request)
2. `_workspace/` 디렉토리 보존 (중간 산출물 감사 추적용)
3. 사용자에게 결과 요약 보고:
   - 완성된 챕터 목록
   - 각 챕터 분량 (글자수/페이지 수)
   - 생성된 이미지 수
   - 검수 결과 요약 (PASS/REVISE 횟수)
   - 실증 사례 등급 분포 (A/B/C)
   - 미완성/부분 완성 항목 (있는 경우)

## 데이터 흐름

```
[리더] → TeamCreate → [tool-analyst]  ←SendMessage→ [case-researcher]
                           │                              │
                           ↓                              ↓
                    01_tool-analyst_*.md          01_case-researcher_*.md
                           │                              │
                           └──── content-writer Read ─────┘
                                       │
                                       ↓
                              02_content-writer_ch*.md
                                  (IMAGE 태그 포함)
                                       │
                            ┌──────────┼──────────┐
                            ↓                     ↓
                     [image-creator]        [cc-specialist]
                     Gemini 3 Pro              Read
                            │                     │
                            ↓                     ↓
                    images/ch*/img_*.png    02_cc-specialist_*.md
                    02_image-creator_*.md          │
                            │                     │
                            └─────────┬───────────┘
                                      ↓
                               [editor] Read
                          (본문+이미지+CC 통합 검수)
                                      │
                                      ↓
                            03_editor_review_ch*.md
                                      │
                             ┌────────┼────────┐
                             ↓        ↓        ↓
                           PASS    REVISE   REWRITE
                             │        │        │
                             ↓        ↓        ↓
                       [리더 통합]  [수정]   [재작성]
                             │        │        │
                             ↓        └────────┘
                      output/ch*.md       ↓
                      output/images/   [재검수]
```

## 에러 핸들링

| 상황 | 전략 |
|------|------|
| tool-analyst 실패 | content-writer에게 자체 지식으로 도구 섹션 작성 지시. "[도구 정보 미확인]" 표시 |
| case-researcher 실패 | content-writer에게 C급 구성 사례로 대체 지시. 챕터당 C급 1개 이하 유지. |
| content-writer 실패 | 리더가 챕터 구조 + 따라하기 형식으로 초안 작성 후 editor에게 전달 |
| image-creator 실패 | 1회 프롬프트 수정 재시도. 재실패 시 이미지 프롬프트를 텍스트로 기록 (수동 생성 가이드) |
| cc-specialist 실패 | 해당 챕터 CC 섹션 없이 출판. "[CC 섹션 추후 보충]" 표시 |
| editor 실패 | 리더가 품질 기준서 체크리스트로 간이 검수 수행 |
| 2회 REVISE 후 미달 | 리더가 직접 수정하여 마무리 |
| 팀원 과반 실패 | 사용자에게 알리고 진행 여부 확인 |
| 타임아웃 | 현재까지 완성된 챕터로 부분 산출물 제공 |

## 배치 전략 (전체 교재 작업 시)

전체 교재(20챕터)를 한번에 처리하면 컨텍스트 부담이 크다. Part 단위 배치를 권장:

1. **배치 1**: Part 1 (Ch 1~2) — AI 기초. 다른 챕터의 기반이 되므로 먼저 완성.
2. **배치 2**: Part 2 (Ch 3~6) — 학업 활용. 수요 최상위 주제 포함.
3. **배치 3**: Part 3 (Ch 7~10) — 생산성 도구.
4. **배치 4**: Part 4 (Ch 11~12) — 데이터 분석.
5. **배치 5**: Part 5 (Ch 13~16) — 취업/경력.
6. **배치 6**: Part 6 (Ch 17~20) — 프로젝트/심화.

각 배치마다 Phase 2~7을 반복. 팀은 유지하고 작업만 새로 등록.

## 테스트 시나리오

### 정상 흐름 (단일 챕터: Ch 4)
1. 사용자가 "Ch 4 작성해줘" 입력
2. Phase 1: _workspace/ 생성, Ch 4 범위 확인, 레퍼런스 4개 로드
3. Phase 2: 팀 구성 (6명) + Ch4 작업 6개 등록
4. Phase 3:
   - tool-analyst: Perplexity, Elicit, NotebookLM, Claude, ChatGPT 벤치마크 비교 조사
   - case-researcher: 7개 채널에서 논문 AI 활용 사례 다각도 조사, A/B/C 등급 분류
   - 양측이 발견 상호 공유 (SendMessage)
5. Phase 4:
   - content-writer: 조사 결과 기반 본문 집필 (따라하기 + 프롬프트 진화 + Anti-Pattern + 도구 비교 + IMAGE 태그 6개)
   - image-creator: Gemini 3 Pro로 헤더/워크플로우/인포그래픽/개념도/Before-After 6장 생성
   - cc-specialist: Claude Code로 논문 PDF 일괄 처리 파이프라인 CC 섹션 집필
6. Phase 5: editor가 품질 기준서 전 항목 검수 → PASS 판정
7. Phase 6: 리더가 통합 → output/ch04_논문요약및자료정리자동화.md + output/images/ch04/ 생성
8. Phase 7: 팀 정리, 사용자에게 결과 보고
9. 예상 산출물: ~18장 분량 완성 챕터 + 6장 고품질 이미지

### 에러 흐름 (image-creator 실패)
1. Phase 4에서 image-creator의 Gemini 3 Pro 호출 실패
2. 프롬프트 수정 후 1회 재시도
3. 재시도도 실패 → 이미지 프롬프트와 상세 설명을 텍스트로 기록
4. editor가 이미지 미완성 상태로 본문+CC 검수 진행
5. 최종 산출물에 "이미지 [N]장 미생성 — 프롬프트 기록 첨부" 명시
6. 사용자에게 수동 이미지 생성 가이드 제공

### 에러 흐름 (case-researcher 부분 실패)
1. Phase 3에서 case-researcher가 일부 채널(커뮤니티, 해외 대학)에서 사례 미확보
2. 확보된 채널(학술 논문, 뉴스, 공식) 결과로 진행
3. content-writer에게 "일부 채널 미확보, A/B급 사례 위주로 집필" 지시
4. 부족한 영역은 C급 구성 사례로 보완 (1개 이하)
5. 최종 산출물에 "실증 사례 일부 채널 미조사 — 추후 보강 필요" 명시
