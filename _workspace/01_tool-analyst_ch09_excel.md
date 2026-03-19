# Ch 9. 엑셀·문서 작업 자동화 실습 — 도구 심층 분석 자료

> 작성: tool-analyst | 작성일: 2026-03-17
> 대상 챕터: Part 3, Ch 9 "엑셀·문서 작업 자동화 실습"

---

## 1. 엑셀 AI 도구 비교

### 1.1 주요 도구 비교표

| 도구 | 수식 생성 | VBA 매크로 | 데이터 분석 | 가격 | 적합한 상황 |
|------|----------|----------|-----------|------|-----------|
| **ChatGPT** | ★★★★★ | ★★★★★ 코드 품질 최고 | ★★★★★ Code Interpreter | Plus $20/월 | 복잡한 수식 설명, VBA 코드 생성, 데이터 분석 원스톱 |
| **Claude** | ★★★★★ | ★★★★★ | ★★★★☆ Artifacts | Pro $20/월 | 긴 데이터셋 분석(1M 토큰), 코드 로직 설명 |
| **MS Copilot** | ★★★★☆ | ★★★☆☆ | ★★★★☆ Excel 내장 | $18~21/유저/월 (Business) | Excel/Word 내에서 직접 AI 사용, Office 통합 |
| **Gemini + Sheets** | ★★★★☆ | N/A (Apps Script) | ★★★★☆ | Free / AI Pro $19.99/월 | Google Sheets 사용자, 무료 AI 분석 |
| **FormulaBot** | ★★★★★ 수식 특화 | ★★★★☆ VBA 생성기 | ★★★☆☆ | Free 기본 / 유료 | 수식·VBA만 빠르게 필요할 때 |

### 1.2 Microsoft Copilot 심층 분석

**Excel Copilot 핵심 기능:**
- 자연어로 수식 생성: "이 열의 평균을 구하고 상위 10%를 하이라이트해줘"
- 데이터 분석: "이 데이터의 트렌드를 분석해줘" → 차트/인사이트 자동 생성
- Agent Mode (2026.03~): Word, Excel, PPT에서 AI가 콘텐츠를 지능적으로 편집/포맷
- Copilot Chat: 모든 M365 앱에서 통합 AI 채팅

**가격 (2025~2026):**
| 플랜 | 가격 | AI 기능 |
|------|------|---------|
| M365 Personal/Family | 기본 요금 | Copilot Chat 무료 포함 |
| Copilot Business | $18~21/유저/월 | Excel/Word/PPT 전체 AI |
| Enterprise | $30/유저/월 | 고급 보안 + 관리 |

**2026.07 가격 인상 예정:** M365 E3 $36→$39, E5 $57→$60 (AI 기능 포함에 따른 인상)

**Agent Mode (2026.03 신기능):**
- Copilot 라이선스 없는 사용자에게도 Word/Excel/PPT Agent Mode 제공
- AI가 서식, 편집, 콘텐츠 생성을 자동으로 처리

---

## 2. AI로 엑셀 수식·함수 생성

### 2.1 수식 생성 프롬프트 예시

**기초 수식:**
```
ChatGPT/Claude에게:

엑셀에서 다음 작업을 하려고 합니다:
- A열: 학생 이름
- B열: 중간고사 점수
- C열: 기말고사 점수
- D열: 출석 점수

E열에 총점을 계산하는 수식을 만들어줘.
가중치: 중간 30%, 기말 40%, 출석 30%
F열에 학점을 자동으로 부여하는 수식도 만들어줘.
(90이상: A, 80이상: B, 70이상: C, 60이상: D, 60미만: F)
```

**고급 수식:**
```
피벗테이블 없이 다음 분석을 수식으로 구현해줘:
1. 부서별 매출 합계 (SUMIFS)
2. 조건부 순위 (RANKIFS가 없으므로 COUNTIFS 활용)
3. 동적 범위를 사용한 드롭다운 필터
4. XLOOKUP으로 여러 시트 간 데이터 연결

각 수식에 대해:
- 수식 코드
- 작동 원리 설명 (한국어)
- 입력해야 할 셀 위치 안내
```

### 2.2 도구별 수식 생성 비교

| 평가 항목 | ChatGPT | Claude | MS Copilot | FormulaBot |
|----------|---------|--------|------------|------------|
| 수식 정확도 | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★★ |
| 설명 품질 | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| 복잡한 수식 | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ |
| 즉시 실행 | ❌ (복사 필요) | ❌ (복사 필요) | ✅ (Excel 내) | ❌ (복사 필요) |
| 무료 사용 | ✅ (제한적) | ✅ (제한적) | ⚠️ (Chat만 무료) | ✅ (기본) |

---

## 3. VBA 매크로 AI 생성

### 3.1 VBA 생성 프롬프트 (S급)

```
Excel VBA 매크로를 작성해주세요.

목적: 매월 반복하는 보고서 서식 자동화

기능:
1. "원본데이터" 시트에서 A~F열 데이터를 읽음
2. "보고서" 시트에 다음 서식을 자동 적용:
   - 제목행: 굵게, 배경색 파란색(#4472C4), 글자색 흰색
   - 데이터 영역: 테두리선 적용
   - 숫자열(D, E, F): 천단위 콤마, 소수점 1자리
   - 합계행: 자동 추가 + 굵게 표시
3. 완료 시 메시지 박스로 "보고서 생성 완료!" 표시

추가 요청:
- 코드에 한국어 주석 추가
- 에러 처리 (On Error) 포함
- 매크로 실행 버튼을 시트에 추가하는 방법도 안내
```

### 3.2 VBA 학습 단계별 AI 활용

| 단계 | AI 활용법 | 도구 |
|------|----------|------|
| 1. 이해 | "VBA가 뭔지 초보자 수준으로 설명해줘" | ChatGPT/Claude |
| 2. 첫 매크로 | "Hello World 매크로를 만들고 실행하는 과정을 알려줘" | ChatGPT |
| 3. 실무 적용 | 위의 S급 프롬프트로 실제 매크로 생성 | ChatGPT (코드 품질 최고) |
| 4. 디버깅 | VBA 에러 메시지를 붙여넣고 "이 에러를 해결해줘" | ChatGPT/Claude |
| 5. 고급 | "이 매크로를 리팩토링하고 성능을 개선해줘" | Claude |

---

## 4. 데이터 정리 AI 활용

### 4.1 데이터 정리 워크플로우

```
Step 1. 데이터 업로드 (ChatGPT Code Interpreter)
  → CSV/Excel 파일 업로드
  → "이 데이터의 구조와 품질을 분석해줘"

Step 2. 문제 식별
  → "빈 셀, 중복 행, 이상치를 식별해줘"
  → "데이터 타입 불일치를 찾아줘"

Step 3. 자동 정리
  → "빈 셀은 0으로 채우고, 중복 행을 제거하고,
     날짜 형식을 YYYY-MM-DD로 통일해줘"
  → Code Interpreter가 Python으로 자동 처리

Step 4. 결과 다운로드
  → 정리된 Excel/CSV 파일 다운로드
```

### 4.2 도구별 데이터 정리 비교

| 도구 | 방식 | 강점 |
|------|------|------|
| **ChatGPT (Code Interpreter)** | Python 자동 실행 → 결과 파일 다운로드 | 코딩 없이 복잡한 데이터 처리 원스톱 |
| **MS Copilot (Excel 내장)** | Excel 내에서 자연어 명령 | Office 환경에서 벗어나지 않고 작업 |
| **Claude** | 코드 생성 + Artifacts 미리보기 | 처리 로직을 명확히 설명, 교육적 |
| **Gemini (Sheets)** | Google Sheets 내장 AI | 무료, Google 생태계 통합 |

---

## 5. 보고서 서식 자동화

### 5.1 문서 작업 자동화 도구

| 작업 | 추천 도구 | 방법 |
|------|----------|------|
| Word 보고서 서식 | MS Copilot | "이 문서에 APA 양식 적용해줘" |
| 반복 서식 적용 | ChatGPT → VBA | VBA 매크로로 서식 일괄 적용 |
| 여러 문서 병합 | ChatGPT (Code Interpreter) | Python으로 여러 docx/xlsx 병합 |
| 표 자동 생성 | Claude/ChatGPT | 마크다운 표 → Word/Excel로 변환 |
| PDF 변환/추출 | ChatGPT/Claude | PDF → 텍스트/표 추출 → 정리 |

---

## 6. 참고 출처

- [MS Copilot Plans and Pricing (Microsoft)](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing-new)
- [Microsoft 365 Copilot New Agents (Thurrott)](https://www.thurrott.com/a-i/329760/ignite-2025-microsoft-365-copilot-adds-new-word-excel-and-powerpoint-agents-and-more)
- [Microsoft Copilot Pricing Guide 2026 (Copilot Experts)](https://copilot-experts.com/microsoft-copilot-pricing-guide/)
- [MS 365 Price Increase July 2026 (Directions on Microsoft)](https://www.directionsonmicrosoft.com/microsoft-to-increase-office-suite-prices-across-the-board-starting-july-2026/)
- [ChatGPT for Excel 2026 (Dupple)](https://dupple.com/learn/chatgpt-for-excel)
- [Free AI VBA Code Generator (FormulaBot)](https://www.formulabot.com/ai-vba-code-generator)
- [Best Choice for Office VBA Code with AI (Office Watch)](https://office-watch.com/2025/make-fix-office-vba-code-ai/)
