#!/usr/bin/env python3
"""Part 1~6 마크다운 파일을 수정하고 PDF로 통합 생성"""

import re
import os
import markdown
from weasyprint import HTML, CSS
from pathlib import Path

BASE = Path("/Users/robin/Research/AI4University/output")

PART_FILES = [
    ("part1_AI첫걸음.md", "Part 1: AI 첫걸음"),
    ("part2_학업에_AI_날개달기.md", "Part 2: 학업에 AI 날개 달기"),
    ("part3_생산성도구마스터.md", "Part 3: 생산성 도구 마스터"),
    ("part4_데이터분석입문.md", "Part 4: 데이터 분석 입문"),
    ("part5_취업경력준비.md", "Part 5: 취업·경력 준비"),
    ("part6_프로젝트심화.md", "Part 6: 프로젝트·심화"),
]

CHAPTER_TITLES = {
    1: "생성형 AI 제대로 쓰는 법 배우기",
    2: "AI 윤리·저작권과 최신 트렌드",
    3: "AI로 과제·보고서 빠르게 작성하기",
    4: "논문 요약 및 자료 정리 자동화",
    5: "팀플·조별과제에 AI 활용하기",
    6: "전공 수업·연구에 AI 활용하기",
    7: "AI를 활용한 PPT·발표자료 제작",
    8: "생성형 AI로 이미지·홍보물 제작",
    9: "엑셀·문서 작업 자동화 실습",
    10: "AI를 활용한 일정관리·학습 관리",
    11: "설문 데이터 분석 실습",
    12: "파이썬 없이 데이터 분석 체험",
    13: "AI로 자기소개서 및 포트폴리오 작성",
    14: "AI를 활용한 면접 준비 전략",
    15: "AI 기반 인적성·필기시험 대비",
    16: "AI를 활용한 직무 분석 및 탐색",
    17: "전공과 연계한 AI 실습 프로젝트",
    18: "AI를 활용한 문제 해결 프로젝트",
    19: "AI를 활용한 창업·서비스 기획",
    20: "AI를 활용한 코딩·개발 보조",
}

PART_COLORS = {
    1: "#4A90D9",  # 블루
    2: "#7ED321",  # 그린
    3: "#F5A623",  # 오렌지
    4: "#50E3C2",  # 틸
    5: "#BD10E0",  # 퍼플
    6: "#E74C3C",  # 레드
}


def fix_workspace_refs(text):
    """_workspace 참조를 수정"""
    # CC 섹션 참조 파일 라인 삭제
    text = re.sub(r'> (?:참조 파일: )?`?_workspace/02_cc-specialist_[^`\n]*`?\s*(?:파일을 참조하세요\.)?\n?', '', text)
    # 나머지 _workspace → project 디렉토리로 변경 (하네스 교육 콘텐츠에서)
    text = text.replace('_workspace/', 'workspace/')
    return text


def fix_broken_bold(text):
    """문장 중간에 bold 처리가 안 되는 홀수 ** 삭제"""
    lines = text.split('\n')
    fixed = []
    in_code_block = False

    for line in lines:
        # 코드 블록 안에서는 수정하지 않음
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            fixed.append(line)
            continue

        if in_code_block:
            fixed.append(line)
            continue

        # **로 시작하고 닫는 **가 없는 경우 (헤더나 리스트 제외)
        # 정상적인 bold: **text** 형태
        # 비정상: **text (닫는 ** 없음)

        # 쌍이 맞는 **는 유지, 홀수 **만 제거
        count = line.count('**')
        if count % 2 != 0:
            # 홀수 ** — 마지막 홀수 **를 제거
            # 뒤에서부터 찾아 하나 제거
            idx = line.rfind('**')
            line = line[:idx] + line[idx+2:]

        fixed.append(line)

    return '\n'.join(fixed)


def fix_colon_endings(text):
    """':' 로 끝나는 문장에서 ':' 삭제 (코드블록 내부 제외)"""
    lines = text.split('\n')
    fixed = []
    in_code_block = False

    for line in lines:
        stripped_check = line.strip()
        if stripped_check.startswith('```'):
            in_code_block = not in_code_block
            fixed.append(line)
            continue

        if in_code_block:
            fixed.append(line)
            continue

        stripped = line.rstrip()

        # 테이블 행, 빈 줄, 마크다운 헤더, JSON/YAML 키:값은 건드리지 않음
        if not stripped or stripped.startswith('|') or stripped.startswith('#'):
            fixed.append(line)
            continue

        # URL 패턴 (http: https:) 은 건드리지 않음
        if stripped.endswith('http:') or stripped.endswith('https:'):
            fixed.append(line)
            continue

        # ':' 로 끝나는 줄 → ':' 삭제
        if stripped.endswith(':'):
            # 들여쓰기 보존
            indent = len(line) - len(line.lstrip())
            line = line[:indent] + stripped[:-1]

        fixed.append(line)

    return '\n'.join(fixed)


def remove_image_tags(text):
    """<!-- IMAGE: ... --> 태그 제거"""
    text = re.sub(r'<!--\s*IMAGE:.*?-->', '', text)
    return text


def fix_all(text):
    """모든 수정 적용"""
    text = fix_workspace_refs(text)
    text = fix_broken_bold(text)
    text = fix_colon_endings(text)
    text = remove_image_tags(text)
    # 연속 빈 줄 정리
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text


def build_cover_html():
    """표지 HTML"""
    return """
    <div class="cover-page">
        <div class="cover-decoration"></div>
        <div class="cover-content">
            <p class="cover-subtitle">대학생을 위한</p>
            <h1 class="cover-title">AI 활용<br>핸즈온 가이드</h1>
            <div class="cover-divider"></div>
            <p class="cover-description">
                "따라하면 누구나 할 수 있고, 결과물은 전문가 수준"
            </p>
            <p class="cover-details">
                6 Parts &middot; 20 Chapters &middot; 103 Images &middot; 225 Cases
            </p>
            <p class="cover-tools">
                ChatGPT &middot; Claude &middot; Gemini &middot; Perplexity &middot; Claude Code
            </p>
        </div>
        <p class="cover-year">2026년 3월 최신판</p>
    </div>
    """


def build_toc_html():
    """목차 HTML"""
    toc = '<div class="toc-page"><h1 class="toc-title">목차</h1>\n'

    part_chapters = {
        1: [1, 2], 2: [3, 4, 5, 6], 3: [7, 8, 9, 10],
        4: [11, 12], 5: [13, 14, 15, 16], 6: [17, 18, 19, 20],
    }
    part_names = {
        1: "AI 첫걸음", 2: "학업에 AI 날개 달기", 3: "생산성 도구 마스터",
        4: "데이터 분석 입문", 5: "취업·경력 준비", 6: "프로젝트·심화",
    }

    for p in range(1, 7):
        color = PART_COLORS[p]
        toc += f'<div class="toc-part" style="border-left: 4px solid {color}; padding-left: 12px; margin: 20px 0 8px 0;">\n'
        toc += f'<h2 class="toc-part-title" style="color: {color}; margin: 0;">Part {p}. {part_names[p]}</h2>\n'
        for ch in part_chapters[p]:
            toc += f'<p class="toc-chapter">Ch {ch}. {CHAPTER_TITLES[ch]}</p>\n'
        toc += '</div>\n'

    toc += '</div>'
    return toc


def style_prompts_and_terminals(html):
    """프롬프트 블록에 테두리, 터미널 명령에 터미널 UI 스타일 적용"""
    # 코드 블록 중 프롬프트 예시 (한국어 텍스트가 많은 것) → 테두리 스타일
    # 터미널 명령 ($ 또는 claude, pip, npm 등으로 시작) → 터미널 UI

    # pre > code 블록을 파싱하여 스타일 적용
    def replace_code_block(match):
        content = match.group(1)
        stripped = content.strip()

        # 터미널 명령 감지
        is_terminal = False
        first_line = stripped.split('\n')[0] if stripped else ''
        terminal_indicators = ['$', 'claude ', 'pip ', 'npm ', 'brew ', 'mkdir ', 'cd ', 'cat ', 'ls ', 'python', 'git ']
        for indicator in terminal_indicators:
            if first_line.strip().startswith(indicator):
                is_terminal = True
                break

        if is_terminal:
            return f"""<div class="terminal-window">
                <div class="terminal-header">
                    <span class="terminal-dot red"></span>
                    <span class="terminal-dot yellow"></span>
                    <span class="terminal-dot green"></span>
                    <span class="terminal-title">Terminal</span>
                </div>
                <pre class="terminal-body"><code>{content}</code></pre>
            </div>"""

        # 프롬프트 감지 (한국어가 포함된 긴 텍스트)
        korean_chars = len(re.findall(r'[가-힣]', stripped))
        if korean_chars > 20 or '프롬프트' in stripped or '역할' in stripped:
            return f"""<div class="prompt-box">
                <div class="prompt-label">💬 프롬프트</div>
                <pre class="prompt-content"><code>{content}</code></pre>
            </div>"""

        # 일반 코드 블록
        return f'<pre><code>{content}</code></pre>'

    html = re.sub(r'<pre><code>(.*?)</code></pre>', replace_code_block, html, flags=re.DOTALL)
    return html


def md_to_html(md_text, part_num):
    """마크다운을 HTML로 변환하며 챕터 구분자 삽입"""
    # 챕터 시작을 page break로 변환
    color = PART_COLORS[part_num]

    # Ch N. 또는 # Ch N. 패턴에 page-break 삽입
    md_text = re.sub(
        r'^(#{1,2}\s*Ch\s*\d+\.)',
        r'<div style="page-break-before: always;"></div>\n\n\1',
        md_text,
        flags=re.MULTILINE
    )

    extensions = ['tables', 'fenced_code', 'codehilite', 'toc', 'nl2br']
    html = markdown.markdown(md_text, extensions=extensions)

    # 프롬프트/터미널 스타일 적용
    html = style_prompts_and_terminals(html)

    return html


def get_css():
    """PDF용 CSS"""
    return CSS(string="""
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;700;900&display=swap');

    @page {
        size: A4;
        margin: 25mm 20mm 25mm 20mm;
        @top-center {
            content: string(chapter-title);
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 9pt;
            color: #666;
        }
        @bottom-center {
            content: counter(page);
            font-family: 'Noto Sans KR', sans-serif;
            font-size: 9pt;
            color: #999;
        }
    }

    @page :first {
        @top-center { content: none; }
        @bottom-center { content: none; }
    }

    body {
        font-family: 'Noto Sans KR', -apple-system, BlinkMacSystemFont, sans-serif;
        font-size: 10.5pt;
        line-height: 1.7;
        color: #2D3436;
    }

    /* 표지 */
    .cover-page {
        page-break-after: always;
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        position: relative;
    }
    .cover-decoration {
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 8px;
        background: linear-gradient(90deg, #4A90D9, #7ED321, #F5A623, #50E3C2, #BD10E0, #E74C3C);
    }
    .cover-subtitle {
        font-size: 16pt;
        font-weight: 300;
        color: #666;
        margin-bottom: 8px;
    }
    .cover-title {
        font-size: 36pt;
        font-weight: 900;
        color: #2D3436;
        margin: 0;
        line-height: 1.2;
    }
    .cover-divider {
        width: 80px;
        height: 3px;
        background: linear-gradient(90deg, #4A90D9, #E74C3C);
        margin: 24px auto;
    }
    .cover-description {
        font-size: 13pt;
        font-weight: 400;
        color: #555;
        font-style: italic;
        margin: 12px 0;
    }
    .cover-details {
        font-size: 10pt;
        color: #888;
        margin: 8px 0;
    }
    .cover-tools {
        font-size: 10pt;
        color: #4A90D9;
        font-weight: 500;
        margin: 4px 0;
    }
    .cover-year {
        position: absolute;
        bottom: 40px;
        font-size: 12pt;
        color: #999;
    }

    /* 목차 */
    .toc-page {
        page-break-after: always;
    }
    .toc-title {
        font-size: 24pt;
        font-weight: 700;
        margin-bottom: 24px;
        color: #2D3436;
    }
    .toc-part-title {
        font-size: 13pt;
        font-weight: 700;
    }
    .toc-chapter {
        font-size: 10.5pt;
        margin: 4px 0 4px 16px;
        color: #444;
    }

    /* 본문 */
    h1 {
        font-size: 22pt;
        font-weight: 900;
        color: #2D3436;
        margin-top: 16px;
        margin-bottom: 12px;
        string-set: chapter-title content();
        page-break-after: avoid;
    }
    h2 {
        font-size: 16pt;
        font-weight: 700;
        color: #333;
        margin-top: 20px;
        border-bottom: 2px solid #eee;
        padding-bottom: 6px;
        page-break-after: avoid;
    }
    h3 {
        font-size: 13pt;
        font-weight: 700;
        color: #444;
        margin-top: 16px;
        page-break-after: avoid;
    }
    h4 {
        font-size: 11pt;
        font-weight: 700;
        color: #555;
        margin-top: 12px;
        page-break-after: avoid;
    }

    p {
        margin: 6px 0;
        orphans: 3;
        widows: 3;
    }

    /* 코드 블록 */
    code {
        font-family: 'SF Mono', 'Menlo', 'Monaco', monospace;
        font-size: 9pt;
        background: #F5F5F5;
        padding: 1px 4px;
        border-radius: 3px;
        color: #E74C3C;
    }
    pre {
        background: #F8F9FA;
        border: 1px solid #E0E0E0;
        border-radius: 6px;
        padding: 12px 16px;
        font-size: 9pt;
        line-height: 1.5;
        overflow-wrap: break-word;
        white-space: pre-wrap;
        page-break-inside: avoid;
    }
    pre code {
        background: none;
        padding: 0;
        color: #2D3436;
    }

    /* 테이블 */
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 12px 0;
        font-size: 9.5pt;
        page-break-inside: avoid;
    }
    th {
        background: #4A90D9;
        color: white;
        font-weight: 700;
        padding: 8px 10px;
        text-align: left;
        border: 1px solid #3A7BC8;
    }
    td {
        padding: 6px 10px;
        border: 1px solid #DDD;
    }
    tr:nth-child(even) td {
        background: #F9FAFB;
    }

    /* 인용 블록 */
    blockquote {
        border-left: 4px solid #4A90D9;
        margin: 12px 0;
        padding: 8px 16px;
        background: #F0F7FF;
        color: #333;
        font-size: 10pt;
        page-break-inside: avoid;
    }

    /* 리스트 */
    ul, ol {
        margin: 6px 0;
        padding-left: 24px;
    }
    li {
        margin: 3px 0;
    }

    /* 구분선 */
    hr {
        border: none;
        border-top: 1px solid #DDD;
        margin: 24px 0;
    }

    /* 강조 */
    strong {
        font-weight: 700;
        color: #2D3436;
    }
    em {
        color: #555;
    }

    /* 체크박스 스타일 */
    .task-list-item {
        list-style: none;
    }

    /* 프롬프트 박스 — 테두리 표시 */
    .prompt-box {
        border: 2px solid #4A90D9;
        border-radius: 8px;
        margin: 14px 0;
        overflow: hidden;
        page-break-inside: avoid;
    }
    .prompt-label {
        background: #4A90D9;
        color: white;
        padding: 6px 14px;
        font-size: 9.5pt;
        font-weight: 700;
    }
    .prompt-content {
        margin: 0;
        padding: 12px 16px;
        background: #F0F7FF;
        border: none;
        border-radius: 0;
        font-size: 9.5pt;
        line-height: 1.6;
    }
    .prompt-content code {
        background: none;
        color: #2D3436;
        font-size: 9.5pt;
    }

    /* 터미널 UI */
    .terminal-window {
        border-radius: 8px;
        overflow: hidden;
        margin: 14px 0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.12);
        page-break-inside: avoid;
    }
    .terminal-header {
        background: #E0E0E0;
        padding: 8px 12px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .terminal-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        display: inline-block;
    }
    .terminal-dot.red { background: #FF5F56; }
    .terminal-dot.yellow { background: #FFBD2E; }
    .terminal-dot.green { background: #27C93F; }
    .terminal-title {
        margin-left: 8px;
        font-size: 9pt;
        color: #666;
        font-weight: 500;
    }
    .terminal-body {
        margin: 0;
        padding: 12px 16px;
        background: #1E1E1E;
        border: none;
        border-radius: 0;
        font-size: 9pt;
        line-height: 1.5;
    }
    .terminal-body code {
        background: none;
        color: #D4D4D4;
        font-size: 9pt;
    }
    """)


def main():
    print("=== 1단계: 텍스트 수정 ===")

    all_html = ""
    all_html += build_cover_html()
    all_html += build_toc_html()

    for idx, (filename, part_title) in enumerate(PART_FILES):
        part_num = idx + 1
        filepath = BASE / filename
        print(f"  처리 중: {filename}")

        text = filepath.read_text(encoding='utf-8')
        original_len = len(text)

        # 수정 적용
        text = fix_all(text)

        # 수정된 파일 저장
        filepath.write_text(text, encoding='utf-8')
        print(f"    수정 완료: {original_len} → {len(text)} chars")

        # HTML 변환
        color = PART_COLORS[part_num]
        part_header = f"""
        <div style="page-break-before: always;"></div>
        <div style="background: {color}; color: white; padding: 40px 30px; margin: -25mm -20mm 20px -20mm; width: calc(100% + 40mm);">
            <p style="font-size: 12pt; font-weight: 300; margin: 0;">{part_title}</p>
        </div>
        """

        html_content = md_to_html(text, part_num)
        all_html += part_header + html_content

    print("\n=== 2단계: PDF 생성 ===")

    full_html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>대학생을 위한 AI 활용 핸즈온 가이드</title>
</head>
<body>
{all_html}
</body>
</html>"""

    # HTML 파일 저장 (디버깅용)
    html_path = BASE / "textbook_full.html"
    html_path.write_text(full_html, encoding='utf-8')
    print(f"  HTML 저장: {html_path}")

    # PDF 생성
    pdf_path = BASE / "대학생을_위한_AI활용_핸즈온가이드.pdf"
    css = get_css()

    print("  PDF 렌더링 중...")
    HTML(string=full_html, base_url=str(BASE)).write_pdf(
        str(pdf_path),
        stylesheets=[css]
    )

    file_size = pdf_path.stat().st_size / (1024 * 1024)
    print(f"\n=== 완료 ===")
    print(f"  PDF: {pdf_path}")
    print(f"  크기: {file_size:.1f} MB")


if __name__ == "__main__":
    main()
