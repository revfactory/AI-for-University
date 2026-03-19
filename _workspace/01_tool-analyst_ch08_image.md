# Ch 8. 생성형 AI로 이미지·홍보물 제작 — 도구 심층 분석 자료

> 작성: tool-analyst | 작성일: 2026-03-17
> 대상 챕터: Part 3, Ch 8 "생성형 AI로 이미지·홍보물 제작"

---

## 1. AI 이미지 생성 도구 비교

### 1.1 주요 도구 비교표

| 도구 | 가격 | 이미지 품질 | 텍스트 렌더링 | 사용 편의성 | 적합한 용도 |
|------|------|-----------|-------------|-----------|-----------|
| **DALL-E 3 (ChatGPT)** | ChatGPT Plus $20/월 포함 | ★★★★★ 포토리얼리스틱 | ★★★★★ 최강 | ★★★★★ 대화형 | 비즈니스 프레젠테이션, 마케팅, 텍스트 포함 이미지 |
| **Midjourney** | Basic $10/월 ~ Pro $60/월 | ★★★★★ 예술적 | ★★★☆☆ | ★★★☆☆ 웹앱/Discord | 콘셉트 아트, 소셜 미디어, 크리에이티브 |
| **Gemini Imagen** | Gemini 무료~유료 | ★★★★☆ 포토리얼리스틱 | ★★★★☆ | ★★★★★ 대화형 | 제품 사진, 그래픽, 무료 이미지 생성 |
| **Stable Diffusion** | 오픈소스 무료 (로컬) | ★★★★☆ 커스터마이즈 가능 | ★★☆☆☆ | ★★☆☆☆ 기술 필요 | 고급 커스터마이징, 대량 생성, 로컬 실행 |

### 1.2 DALL-E 3 (ChatGPT 통합) 상세

**핵심 강점:**
- ChatGPT 대화형 인터페이스로 이미지 생성 → 수정 반복이 자연스러움
- "이 이미지에서 배경을 파란색으로 바꿔줘" 같은 자연어 편집
- 텍스트 렌더링 업계 최고 (포스터, 배너에 텍스트 포함 가능)
- 포토리얼리스틱 이미지 품질 우수

**가격:** ChatGPT Plus $20/월에 포함. 무료 플랜에서도 제한적 생성 가능.

### 1.3 Midjourney 상세

**핵심 강점:**
- 가장 예술적이고 미학적으로 완성도 높은 이미지
- 후처리가 거의 불필요한 "갤러리 수준" 출력
- 스타일 일관성 유지에 강함 (--style, --sref 파라미터)

**가격:**
| 플랜 | 가격 | GPU 시간 |
|------|------|---------|
| Basic | $10/월 | 3.3시간 |
| Standard | $30/월 | 15시간 |
| Pro | $60/월 | 30시간 + Stealth 모드 |

**접근:** 웹앱(midjourney.com) 또는 Discord

### 1.4 Gemini Imagen 상세

**핵심 강점:**
- Gemini 앱에서 무료로 이미지 생성 가능
- 포토리얼리스틱 제품 사진에 강점
- 텍스트 렌더링 개선됨
- Google 생태계 통합 (Docs, Slides에서 직접 활용)

---

## 2. 디자인·홍보물 제작 도구

### 2.1 Canva AI vs 미리캔버스

| 항목 | Canva AI | 미리캔버스 |
|------|---------|----------|
| **가격** | Free / Pro $120/년 | Free / 프리미엄 유료 |
| **AI 기능** | Magic Studio 25+ AI 도구: Magic Write, AI 이미지 생성, AI 비디오(Veo-3), AI 디자인 제안 | AI 기반 디자인 추천, 한국어 특화 |
| **템플릿** | 글로벌 템플릿 풍부 | 한국 문화/교육 최적화 템플릿 |
| **한국어** | ★★★★☆ | ★★★★★ 네이티브 |
| **협업** | 팀 공동 편집 | 최대 50명 동시 편집 |
| **교육 혜택** | 교사 무료 Pro | 교사 무료 프리미엄 |
| **적합한 상황** | 글로벌 스타일 디자인, SNS, 마케팅 | 한국 학교 행사, 동아리 홍보, 한국어 포스터 |

### 2.2 학생 홍보물 제작 도구 선택 가이드

| 홍보물 유형 | 추천 도구 | 이유 |
|-----------|----------|------|
| 동아리 모집 포스터 (한국어) | 미리캔버스 | 한국 대학 맞춤 템플릿, 한글 폰트 풍부 |
| SNS 카드뉴스 | Canva | 인스타/페이스북 최적 템플릿, AI 리사이징 |
| 학교 행사 포스터 (영문) | Canva Pro | 글로벌 디자인, AI 이미지 생성 |
| 콘셉트 이미지/일러스트 | DALL-E 3 or Midjourney | AI 이미지 생성 |
| 배너/현수막 텍스트 포함 | DALL-E 3 | 텍스트 렌더링 최강 |

---

## 3. 이미지 프롬프트 작성법

### 3.1 이미지 프롬프트 구조

```
[주제] + [스타일] + [구도/앵글] + [조명] + [색감] + [분위기] + [해상도/비율]
```

### 3.2 프롬프트 진화 패턴

#### 🔴 Level 1
```
대학교 포스터 만들어줘
```
→ 결과: 일반적이고 활용 불가능한 이미지

#### 🟡 Level 2
```
대학교 봄 축제 포스터를 만들어줘. 벚꽃과 캠퍼스가 있는 밝은 느낌으로.
```
→ 결과: 나아졌지만 텍스트/레이아웃 부족

#### 🟢 Level 3 (S급)
```
DALL-E 3에서:

대학교 봄 축제 포스터를 디자인해줘.

내용:
- 상단: "2026 봄 축제" 텍스트 (큰 볼드체)
- 중앙: 벚꽃이 만개한 캠퍼스 일러스트 (수채화 스타일)
- 하단: "4월 15일~17일 | 중앙광장" 텍스트
- 전체 색감: 파스텔 핑크 + 화이트 + 연두색
- 스타일: 한국 대학교 동아리 포스터 느낌, 깔끔하고 현대적
- 비율: 3:4 (인스타그램 최적)
- 텍스트는 반드시 정확하게 렌더링해줘
```

### 3.3 도구별 프롬프트 팁

| 도구 | 팁 |
|------|---|
| **DALL-E 3** | 자연어로 상세 설명. "텍스트를 정확히 넣어줘" 강조. 대화형으로 수정 반복 |
| **Midjourney** | 간결한 영어 키워드 나열. 파라미터 활용: `--ar 3:4`, `--style raw`, `--v 6.1` |
| **Gemini** | "사진처럼 사실적으로" 또는 "일러스트 스타일로" 명시. 한국어 프롬프트 가능 |
| **Canva** | Magic Studio → 텍스트 입력 → 디자인 자동 생성. 템플릿 기반 수정이 더 효율적 |

---

## 4. 홍보물 제작 워크플로우

```
Step 1. 콘셉트 기획 (ChatGPT)
  → "동아리 모집 포스터의 콘셉트 5가지를 제안해줘"

Step 2. 메인 이미지 생성 (DALL-E 3 / Midjourney)
  → 콘셉트에 맞는 메인 비주얼 AI 생성

Step 3. 디자인 조합 (Canva / 미리캔버스)
  → AI 생성 이미지 + 텍스트 + 레이아웃 조합
  → 템플릿 기반으로 빠르게 완성

Step 4. 피드백 & 수정 (ChatGPT / Claude)
  → 완성본 이미지를 업로드하고 "이 포스터의 디자인 개선점을 알려줘"

Step 5. 다중 포맷 내보내기 (Canva)
  → 인스타용, 포스터용, 배너용 자동 리사이징
```

---

## 5. 참고 출처

- [Midjourney vs DALL-E vs Gemini Imagen 2026 Comparison (FreeAcademy)](https://freeacademy.ai/blog/midjourney-vs-dalle-vs-gemini-imagen-comparison-2026)
- [9 Best AI Image Generation Models 2026 (Gradually)](https://www.gradually.ai/en/ai-image-models/)
- [Nano Banana vs Midjourney vs DALL-E 2025 (Skywork)](https://skywork.ai/blog/nano-banana-vs-midjourney-vs-dalle-2025-comparison-2/)
- [Best AI Image Generators 2025 Tested & Ranked (PXZ)](https://pxz.ai/blog/best-ai-image-generators-2025-tested-ranked)
- [Canva AI Features 2026 (Labla)](https://www.labla.org/ai-tools-reviews/canva-ai-in-2026-every-feature-worth-using-and-how-to-actually-use-them/)
- [Canva Pricing 2026 (UserJot)](https://userjot.com/blog/canva-pricing-2025-free-pro-teams-costs)
- [미리캔버스 vs 해외 디자인 툴 교육 비교 (미리캔버스 블로그)](https://blog.miricanvas.com/miricanvas-design-tools-education)
