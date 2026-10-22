# Information Security · GRC · ISO/IEC 27001 Portfolio

**Amay Chivate** · ISO/IEC 27001 Lead Auditor

I build and audit information security management systems. This repository shows how I work: real ISMS artefacts written for a simulated company, mapped clause by clause to ISO/IEC 27001:2022.

### ▶️ [Open the interactive ISMS dashboard](https://rttr-7.github.io/iso27001-grc-portfolio/)

Explore the risk heat map before and after treatment, all 93 Annex A controls, audit findings and management review results.

New to ISO 27001? Read the **[Project Guide](PROJECT-GUIDE.md)** for a plain-English walkthrough and FAQ.

---

## Featured case study

### [ISO/IEC 27001:2022 ISMS implementation: Halcyon Ledger Ltd](01-iso27001-isms-implementation/)

A simulated 210-person B2B payments SaaS company goes from no ISMS to certification in 11 months.

| Deliverable | Clause |
| --- | --- |
| [Case study brief: problem statement, approach and results](01-iso27001-isms-implementation/00-case-study-brief.md) | Start here |
| [ISMS scope](01-iso27001-isms-implementation/03-isms-scope.md) | 4.3 |
| [Context and interested parties](01-iso27001-isms-implementation/04-context-and-interested-parties.md) | 4.1, 4.2 |
| [Risk assessment methodology](01-iso27001-isms-implementation/05-risk-assessment-methodology.md) | 6.1.2 |
| [Risk register and treatment plan](01-iso27001-isms-implementation/06-risk-register-and-treatment-plan.md) | 6.1.3, 8.2, 8.3 |
| [Statement of Applicability (93 controls)](01-iso27001-isms-implementation/07-statement-of-applicability.md) | 6.1.3 d |
| [Internal audit checklist and report](01-iso27001-isms-implementation/08-internal-audit-checklist.md) | 9.2 |
| [Management review report](01-iso27001-isms-implementation/09-management-review-report.md) | 9.3 |

**Results:** 12 significant risks reduced to 0 above appetite · 91 of 93 controls applicable with 2 evidenced exclusions · internal audit with 0 major and 3 minor NCs, all closed with root cause analysis.

## Skills demonstrated

| Area | Evidence in this repo |
| --- | --- |
| ISMS design (ISO/IEC 27001:2022, Amd 1:2024) | Scope, context, governance, roadmap |
| Risk management (ISO/IEC 27005) | 5x5 method, acceptance criteria, register, treatment plan, residual-risk sign-off |
| Control selection (Annex A / ISO/IEC 27002) | Full SoA with risk, legal and contractual justifications |
| Auditing (ISO 19011, ISO/IEC 27007) | Audit plan, sampling, clause checklist, NC grading, requirement-evidence-gap findings |
| Regulatory mapping | UK/EU GDPR, DORA third-party flow-down, payment services obligations |
| Cloud security governance | AWS shared responsibility, IaC guardrails, immutable backups, JIT access |
| Communicating with leadership | Management review report, KPIs, objectives, decisions and budget asks |

## Repository structure

```
.
├── 01-iso27001-isms-implementation/   Case study: 10 formal ISMS documents (Markdown)
│   └── data/                          Risk register and Statement of Applicability (CSV)
├── dashboard/                         Source code for the interactive dashboard
│   ├── template.html                  Page layout, styles and behaviour
│   └── build.py                       Combines the template with the documents and data
├── docs/                              Built website, published by GitHub Pages
│   └── index.html
└── PROJECT-GUIDE.md                   Plain-English walkthrough and FAQ
```

To rebuild the website after editing a document, the CSV data or the template:

```
python3 dashboard/build.py
```

## Planned additions

- [ ] ISO 27001 to SOC 2 and DORA control mapping
- [ ] GDPR data protection impact assessment (DPIA) for a new product feature
- [ ] Supplier security assessment questionnaire and scoring model
- [ ] Incident response tabletop exercise pack
- [ ] Topic-specific policy set (access control, cryptography, secure development)

---

> **Disclaimer:** Halcyon Ledger Ltd is a fictional company. All data is simulated for demonstration. No training-provider course material is reproduced here.
