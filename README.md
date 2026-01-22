# Job Posting Understanding Pipeline (Personal)

본 프로젝트는 **개인 구직 자동화**를 목표로 합니다.  
구직 사이트의 공고를 *수집하는 것*이 목적이 아니라,  
공고 내용을 **구조화 → 이해 → 요약 → 조건에 맞게 선별**하는 파이프라인을 만드는 것이 핵심입니다.

> 수익화 목적 ❌  
> 개인 학습 및 개인 구직 활용 목적 ⭕  

---

## 프로젝트 배경

기존의 웹 스크래핑은 다음과 같은 한계가 있습니다.

- SPA(Single Page Application) 구조로 인해  
  단순 HTML 요청이나 URL 기반 파싱 시 **데이터가 비어 N=0**이 되는 문제
- 규칙 기반 파싱은 “매칭”에 그치며  
  공고의 **의미·요구사항·적합도**를 다루기 어려움

이 프로젝트는 이러한 한계를 인식하고,  
**사전학습된 언어모델(LLM)을 활용한 공고 이해 파이프라인**으로 방향을 전환합니다.

---

## 핵심 아이디어

- 공고 데이터는 **최소한으로, 안전하게 수집**
- 핵심 가치는 **이해·요약·질문응답**
- 데이터는 커밋하지 않고, 코드와 구조만 관리

---

## 전체 파이프라인 개요

```text
[브라우저 수동 저장]
        ↓
data/raw/*.html
        ↓
[HTML 파싱]
        ↓
data/snapshots/YYYY-MM-DD_wanted.jsonl
        ↓
[조건 필터링 / 요약 / 분석]
        ↓
data/outputs/latest.html (브라우저 확인용)
```

---

## 왜 “수동 HTML 저장” 방식인가?

- 구직 사이트는 자동화 접근(Headless Browser)을 차단하는 경우가 많음 (403 등)
- 공식 API는 승인 여부가 불확실함
- 개인 구직 목적에서는:
  - **약관/법적 리스크 최소화**
  - **필요할 때만 실행**
  - **재현 가능한 입력(raw HTML)**  
  이 가장 중요함

따라서 본 프로젝트는 다음 방식을 채택합니다.

> **브라우저에서 사용자가 직접 페이지를 저장 →  
> 파이프라인은 그 파일을 기준으로 동작**

---

## Project Structure

```text
Wanted_Job_Scraper/
├─ src/
│  ├─ collect/        # (보조) 수집 로직
│  ├─ parse/          # raw HTML → structured snapshot
│  ├─ query/          # 조건 기반 필터링
│  └─ nlp/            # 요약 / 질의응답 (LLM)
├─ config/
│  └─ criteria.yaml   # 개인 구직 조건
├─ data/              # ❗커밋하지 않음
│  ├─ raw/            # 수동 저장한 HTML
│  ├─ snapshots/      # 실행 시점별 JSONL
│  └─ outputs/        # HTML 리포트 / 결과물
└─ docs/
   └─ devlog/         # 시행착오 / 설계 기록
```

---

## 설치 및 환경 설정

### Python 환경
```bash
uv pip install -r requirements.txt
```

### Playwright (선택)
> 자동 수집 실험용이며, 현재 메인 파이프라인은 아닙니다.

```bash
python -m playwright install chromium
```

> 브라우저 바이너리는 OS 의존적이므로  
> `requirements.txt`가 아닌 README 설치 단계에만 명시합니다.

---

## 사용 방법 (개인 구직 기준)

### 1️⃣ 브라우저에서 공고 페이지 저장
- 원티드 등 구직 사이트에서 검색/필터 설정
- 공고 카드가 충분히 로딩되도록 스크롤
- **파일 → “웹페이지, 전체(Webpage, Complete)”로 저장**
- 저장 위치: `data/raw/`
- 예시 파일명:
  - `wanted_search_2026-01-22.html`

---

### 2️⃣ 파싱 실행 (최신 raw HTML 자동 선택)
```bash
python src/parse/parse_latest_raw.py
```

결과:
```text
data/snapshots/2026-01-22T173000_wanted.jsonl
```

---

### 3️⃣ 전체 공고 HTML 리포트 생성
```bash
python src/query/render_latest_html.py
```

결과:
```text
data/outputs/latest.html
```

→ 브라우저에서 열어 전체 공고를 한 번에 검토 가능

---

## Data Policy (중요)

- `data/**` 디렉토리는 **Git에 커밋하지 않습니다**
- 본 프로젝트는:
  - 개인 학습
  - 개인 구직 자동화
  목적에 한정됩니다
- 원본 공고 데이터의 재배포 / 서비스화는 의도하지 않습니다

---

## Roadmap

- [x] HTML 기반 파싱 실험 및 한계 확인
- [x] 수동 저장 + 재현 가능한 입력 구조 확정
- [ ] 최신 raw HTML 자동 선택 파서
- [ ] 조건 기반 필터링 (`criteria.yaml`)
- [ ] HTML 리포트 자동 생성
- [ ] 오픈소스 LLM 기반 요약 / 질의응답

---

## Notes

이 프로젝트는  
“웹 스크래핑 기술”보다  
**AI 엔지니어로서 문제를 정의하고, 안전한 구조를 선택하며,  
모델이 이해할 수 있는 형태로 데이터를 준비하는 과정**에 초점을 둡니다.
