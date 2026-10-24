# ISO/IEC 27001:2022 ISMS Implementation: Halcyon Ledger Inc.

**A full, end-to-end ISMS implementation for a simulated 210-person payments SaaS company, from gap analysis to certification in 11 months.**

> Halcyon Ledger Inc. is a **fictional** company created for this case study. All names, figures and findings are simulated to show how the standard is applied in practice.

▶️ **[Open the interactive dashboard](https://rttr-7.github.io/iso27001-grc-portfolio/)**

## At a glance

| | |
| --- | --- |
| Standard | ISO/IEC 27001:2022 incl. Amendment 1:2024 (climate change) |
| Organization | B2B payments SaaS · 210 staff · US (Texas and North Carolina) · AWS hosted |
| Timeline | Nov 2025 kickoff → Oct 2026 certificate |
| Risks | 47 assessed · 12 significant (2 Critical, 4 High, 6 Medium) → 0 above appetite after treatment |
| SoA | 93 controls · 91 applicable · 2 justified exclusions · 86 implemented, 5 partial |
| Internal audit | 0 major · 3 minor NCs (all closed) · 5 OFIs |
| Outcome | Management review approved certification readiness; Stage 2 passed |

## Deliverables

| # | Artefact | ISO clause | What it shows |
| --- | --- | --- | --- |
| 00 | [Case study brief](00-case-study-brief.md) | - | Problem statement, why ISO 27001, why the audit, results and lessons learned |
| 01 | [Company profile](01-company-profile.md) | - | The simulated organization and ISMS governance |
| 02 | [Implementation roadmap](02-implementation-roadmap.md) | All | PDCA phases, Gantt chart, mandatory documents map |
| 03 | [ISMS scope](03-isms-scope.md) | 4.3 | Scope statement, boundaries, interfaces, exclusions |
| 04 | [Context and interested parties](04-context-and-interested-parties.md) | 4.1, 4.2 | Issues (incl. climate change), stakeholders, legal register |
| 05 | [Risk assessment methodology](05-risk-assessment-methodology.md) | 6.1.2 | 5x5 matrix, scales, acceptance criteria |
| 06 | [Risk register and treatment plan](06-risk-register-and-treatment-plan.md) | 6.1.3, 8.2, 8.3 | 12 significant risks, treatments, residual risk sign-off |
| 07 | [Statement of Applicability](07-statement-of-applicability.md) | 6.1.3 d | All 93 Annex A controls with justification and status |
| 08 | [Internal audit checklist and report](08-internal-audit-checklist.md) | 9.2 | Audit plan, clause and control checklists, NCs with root cause |
| 09 | [Management review report](09-management-review-report.md) | 9.3 | Inputs a-g, objectives, KPIs, decisions and actions |

Data files: [`data/risk-register.csv`](data/risk-register.csv) · [`data/statement-of-applicability.csv`](data/statement-of-applicability.csv)

## Suggested reading order

- **Hiring manager (5 minutes):** this page → [06 Risk treatment](06-risk-register-and-treatment-plan.md) → [08 Audit findings](08-internal-audit-checklist.md#5-findings-and-corrective-actions)
- **Auditor or GRC lead:** [03 Scope](03-isms-scope.md) → [05 Methodology](05-risk-assessment-methodology.md) → [07 SoA](07-statement-of-applicability.md) → [08](08-internal-audit-checklist.md) → [09](09-management-review-report.md)

## Design choices worth discussing

1. **Scope is the whole service, not one office.** A narrow scope is easier to certify but worthless to customers.
2. **Risk is scored on current controls**, so the register reflects reality rather than a theoretical worst case.
3. **Only 2 exclusions**, each backed by a verifiable scope fact. Exclusions are the first thing a certification auditor tests.
4. **Two residual Medium risks are accepted rather than hidden.** Impact stays high for payment fraud; likelihood is what treatment reduces.
5. **Nonconformities are written in requirement-evidence-gap form**, with root cause and a verified-effective date.
