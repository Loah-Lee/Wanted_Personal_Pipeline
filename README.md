# Job Posting Understanding Pipeline (Personal)

원티드(Wanted) 등 구직 사이트의 공고를 **필요할 때 실행해서 최신 스냅샷으로 수집**하고,  
내 조건에 맞는 공고를 **필터링/정리**한 뒤 (추후) **오픈소스 LLM으로 요약/질의응답**까지 연결하는 개인 구직 자동화 프로젝트입니다.

> 목표는 “스크래핑 자체”가 아니라, 공고 내용을 모델이 이해할 수 있게 만들고  
> 사용자가 원하는 조건에 맞게 정리/요약/응답하는 파이프라인을 만드는 것입니다.

---

## What I learned (핵심 배운 점)

- SPA(싱글 페이지 앱) 환경에서는 `requests`나 단순 HTML 저장으로는 공고 DOM이 비어 `N=0`이 될 수 있음  
- 따라서 **렌더링 이후 DOM을 가져오는 수집 방식(예: Playwright)**이 필요함  
- 데이터는 커밋하지 않고(약관/저작권/개인정보 리스크 최소화), 코드/구조/로그 중심으로 관리함

---

## Project Structure

```text
Wanted_Job_Scraper/
├─ src/
│  ├─ collect/        # (예정) Playwright 등으로 공고 수집
│  ├─ parse/          # (예정) raw → structured 변환
│  ├─ query/          # (예정) 조건 기반 필터링/정렬
│  └─ nlp/            # (예정) 요약/질의응답(오픈소스 LLM)
├─ config/
│  ├─ criteria.yaml   # (예정) 내 조건/필터 규칙
│  └─ logging.yaml    # (선택) 로깅 설정
├─ data/              # ❗커밋하지 않음(.gitignore)
│  ├─ raw/            # 수집 원본(임시)
│  ├─ snapshots/      # 실행 시점별 스냅샷(JSONL)
│  └─ outputs/        # 필터 결과/리포트
└─ docs/
   └─ devlog/         # 시행착오/배운 점 기록
```

---

## Quick Start

### 1) 환경변수 설정
- `.env`는 로컬에서만 사용하고 Git에 올리지 않습니다.
- `.env.example`을 복사해서 `.env`를 만드세요.

```bash
cp .env.example .env
```

### 2) (현재) HTML snippet 파싱 테스트
> 초기 실험 단계: 렌더링된 DOM snippet을 저장해 파싱했습니다.  
> 이후 Playwright 기반 수집으로 교체 예정입니다.

```bash
python src/html/parse_wanted_list.py
```

출력 예:
```text
Saved N jobs to data/processed/jobs.jsonl
```

---

## Data Policy (중요)

- `data/**` 아래의 원본 HTML/스냅샷/결과물은 **커밋하지 않습니다.**
- 이 레포는 **개인 학습 및 개인 구직 자동화 목적**으로 운영합니다.
- 서비스 운영/재배포 목적이 아닙니다.

---

## Roadmap

- [ ] Playwright 수집(렌더링 이후 DOM 기반)으로 교체  
- [ ] 스냅샷 저장: `data/snapshots/YYYY-MM-DD_wanted.jsonl`  
- [ ] 조건 필터링(`config/criteria.yaml`) + 결과 리포트 생성  
- [ ] 오픈소스 LLM 기반 요약/질의응답(로컬/경량 우선)

---

## Notes

본 프로젝트는 웹사이트의 이용약관/robots 정책을 존중하며,  
과도한 요청이나 데이터 재배포를 지양합니다.
