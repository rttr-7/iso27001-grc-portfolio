# 00 - Case Study Brief: Halcyon Ledger Inc.

> **Engagement:** ISO/IEC 27001:2022 ISMS implementation and internal audit · **Organization:** Halcyon Ledger Inc. (simulated) · **Period:** November 2025 to October 2026 · **Prepared by:** Amay Chivate

Halcyon Ledger had security tools but no system for managing information security. That gap was costing it enterprise revenue and leaving its biggest risks unowned. In 11 months, it implemented an ISO/IEC 27001:2022 ISMS, tested it with a full internal audit, and achieved certification.

## 1. Background

Halcyon Ledger is a 210-person US company. Its cloud platform, HalcyonPay, automates supplier invoice processing and payouts for 1,400 mid-market businesses, handling about 2.1 million payments a year. It holds supplier bank details, invoices and payment instructions for its customers, which makes it an attractive target for fraud and ransomware.

Full profile: [01 - Company profile](01-company-profile.md)

## 2. Problem statement

**Halcyon Ledger could not prove to customers, regulators or its own board that information security was being managed.** Individual controls existed, but nobody owned the risks, nothing was measured, and there was no evidence trail an auditor or customer could rely on.

| Symptom | Evidence | Business impact |
| --- | --- | --- |
| Enterprise deals stalled | 3 enterprise customers required ISO 27001 before signing | $4.2m of annual recurring revenue on hold |
| Slow customer due diligence | Security questionnaires took an average of 12 days to answer | Longer sales cycles; lost smaller deals |
| No risk ownership | No risk register, no risk owners, no acceptance criteria | Serious risks such as payment fraud were known but untreated |
| Rising threats | Payment-fraud and ransomware attacks rising across the sector | Exposure to large financial loss and loss of the payment partnership |
| Regulatory pressure | US bank customers passing third-party risk requirements down to suppliers; state privacy-law obligations | Contract and compliance risk |
| Rapid growth | Headcount up 35% in a year; onboarding and access removal inconsistent | Leavers keeping access; untrained staff |
| Thin security team | 3 security staff for 210 employees and 22 contractors | Monitoring and response depended on individuals |

**The question the board asked:** *How do we show, with evidence, that our customers' money and data are protected, and win back the stalled deals within a year?*

## 3. Why ISO/IEC 27001

| Option considered | Why it was or was not chosen |
| --- | --- |
| **ISO/IEC 27001 certification** | **Chosen.** Explicitly requested by the stalled customers; internationally recognized, including by US enterprise buyers; risk-based, so effort goes where the real risks are; certifiable by an accredited body |
| SOC 2 Type II only | Valued by many US customers, but the stalled enterprise customers asked for ISO 27001 by name |
| Self-assessment questionnaire | No independent assurance; would not satisfy enterprise procurement |
| Do nothing | Loses $4.2m in deals and leaves the main risks untreated |

The existing SOC 2 Type I report was kept, and the ISMS was designed so the same evidence can support a later SOC 2 Type II.

## 4. Objectives

| # | Objective | Target | Result |
| --- | --- | --- | --- |
| 1 | Achieve ISO/IEC 27001:2022 certification | Within 12 months | Certified 16 Oct 2026 (11 months) |
| 2 | Bring every significant risk within appetite | No risk scoring 12 or more | 6 risks above appetite reduced to 0 |
| 3 | Cut security questionnaire turnaround | Under 5 days | 4 days |
| 4 | Reduce phishing susceptibility | Click rate under 5% | 18% → 4.1% |
| 5 | Close the onboarding and leaver gaps | 100% trained in 30 days; access removed on the last day | 100% trained (from July); 98.5% same-day removal |

## 5. Scope of the engagement

The ISMS covers everything needed to design, build, run and support HalcyonPay: both offices, remote workers, the AWS cloud environment, corporate systems and key suppliers. A narrow scope would have been easier to certify, but would not have satisfied the customers who asked for it.

Full scope and exclusions: [03 - ISMS scope](03-isms-scope.md) · [04 - Context and interested parties](04-context-and-interested-parties.md)

## 6. Approach

The program followed the Plan-Do-Check-Act cycle that ISO/IEC 27001 is built on.

| Phase | What was done | Output |
| --- | --- | --- |
| Plan | Gap analysis; context and stakeholder workshops; scope; policy; risk method; risk assessment of 47 risks | [05 - Methodology](05-risk-assessment-methodology.md), [06 - Risk register and treatment plan](06-risk-register-and-treatment-plan.md), [07 - Statement of Applicability](07-statement-of-applicability.md) |
| Do | Treatments for the 12 significant risks; 14 policies; awareness training; supplier reviews | Controls in operation with evidence |
| Check | KPIs measured for 4 months; full internal audit | [08 - Internal audit report](08-internal-audit-checklist.md) |
| Act | Corrective actions with root cause; management review | [09 - Management review report](09-management-review-report.md) |

Timeline and Gantt chart: [02 - Implementation roadmap](02-implementation-roadmap.md)

## 7. Risk assessment and treatment

Each risk was scored as likelihood × impact on 5-point scales. Any risk scoring 12 or more had to be treated. Of 47 risks assessed, 12 were significant and 6 were above appetite, including:

- **Supplier bank-detail fraud (score 20):** treated with call-back verification, a 24-hour payment hold and MFA for customer administrators
- **Ransomware reaching production and backups (score 15):** treated with EDR, hardware security keys, just-in-time admin access and immutable backups

After treatment, no risk scored above 8, and every residual risk was formally accepted by its owner.

## 8. Why an internal audit was needed

Putting controls in place is not enough. Halcyon had to prove they **worked**, and find any gaps before the certification body did.

1. **It is a requirement.** Clause 9.2 requires internal audits at planned intervals. A certification body will not recommend certification until at least one full audit cycle and a management review are complete.
2. **Controls must operate, not just exist.** Policies written in February only count if people follow them. The audit tested real samples: 40 staff training records, 20 leavers, 25 emergency changes, 15 payee bank-detail changes.
3. **Independence.** The people who built the controls should not be the ones judging them. The audit was run by an auditor with no operational role in the ISMS.
4. **Lower cost of failure.** A major nonconformity found by the certification body at Stage 2 would delay certification by months and keep the $4.2m in deals on hold. Finding the same issue internally costs a few weeks.
5. **Input to management review.** Top management needs objective evidence to decide whether the ISMS is ready (Clause 9.3).

**Audit design**

| Element | Detail |
| --- | --- |
| Objective | Confirm the ISMS conforms to ISO/IEC 27001:2022 and is effectively implemented |
| Scope | All clauses 4 to 10, and a risk-based sample of 26 Annex A controls |
| Criteria | ISO/IEC 27001:2022, Halcyon's policies and procedures, legal and contractual requirements |
| Method | Interviews, document review, observation and sampling, following ISO 19011 |
| Dates | 15 to 26 June 2026 |

## 9. What the audit found

The audit found **no major nonconformities, 3 minor nonconformities and 5 opportunities for improvement**.

| Finding | Root cause | Correction |
| --- | --- | --- |
| 9 of 40 staff missed security training (all agency contractors) | Contractors were onboarded outside the HR system | Contractors moved into the HR system; automatic training assignment |
| An obsolete procedure without an encryption step was still in use | No step to withdraw old document versions | Single controlled repository; quarterly check |
| 2 of 25 emergency changes were never approved afterwards | Approval relied on memory | Automated reminder and escalation after 24 hours |

All three were closed and verified as effective on 5 August 2026, before the certification audit. Full details: [08 - Internal audit checklist and report](08-internal-audit-checklist.md)

## 10. Results

| Measure | Before | After |
| --- | --- | --- |
| ISO/IEC 27001 certification | None | Certified 16 Oct 2026 |
| Risks above appetite | 6 | 0 |
| Annex A controls applied | No formal selection | 91 of 93, each justified |
| Staff using phishing-resistant MFA | 12% | 100% |
| Laptops with EDR | 71% | 100% |
| Open critical and high vulnerabilities | 41 | 3 |
| Phishing simulation click rate | 18% | 4.1% |
| Questionnaire turnaround | 12 days | 4 days |
| Cyber insurance premium | Baseline | 15% lower |

## 11. Challenges and how they were handled

| Challenge | How it was handled |
| --- | --- |
| Engineers saw security as slowing them down | Controls built into the existing CI/CD pipeline, so checks run automatically instead of adding manual approval steps |
| A three-person security team | Risk and control ownership spread across department heads; a managed SOC for 24/7 monitoring |
| Two states with different employment law | Screening and HR controls checked against both Texas and North Carolina requirements |
| Contractors outside normal HR processes | Found by the internal audit and fixed at the root cause |

## 12. Lessons learned

1. **Scope for the customer, not for the audit.** A wide scope took more work but is what made the certificate valuable.
2. **Risk ownership changes behavior.** Once department heads owned named risks, treatment moved faster than any security-team request.
3. **Audit with real samples.** Every nonconformity came from testing samples, not from reading policies.
4. **Fix the root cause, not the symptom.** Training the 9 contractors fixed the finding; moving contractors into the HR system stopped it recurring.

## 13. My role

In this simulated engagement I acted as **ISMS implementation lead and internal auditor**. I:

- defined the scope, context and interested parties
- designed the risk methodology and ran the risk assessment
- produced the risk treatment plan and the Statement of Applicability for all 93 controls
- planned and conducted the internal audit, graded the findings and verified corrective actions
- prepared the management review report and objectives

## 14. Documents in this case study

| # | Document | ISO/IEC 27001 |
| --- | --- | --- |
| 01 | [Company profile](01-company-profile.md) | Organization and governance |
| 02 | [Implementation roadmap](02-implementation-roadmap.md) | Program plan |
| 03 | [ISMS scope](03-isms-scope.md) | 4.3 |
| 04 | [Context and interested parties](04-context-and-interested-parties.md) | 4.1, 4.2 |
| 05 | [Risk assessment methodology](05-risk-assessment-methodology.md) | 6.1.2 |
| 06 | [Risk register and treatment plan](06-risk-register-and-treatment-plan.md) | 6.1.3, 8.2, 8.3 |
| 07 | [Statement of Applicability](07-statement-of-applicability.md) | 6.1.3 d, Annex A |
| 08 | [Internal audit checklist and report](08-internal-audit-checklist.md) | 9.2 |
| 09 | [Management review report](09-management-review-report.md) | 9.3 |

---

*Halcyon Ledger Inc. is a fictional organization. All names, figures and findings are simulated to demonstrate how ISO/IEC 27001 is applied in practice.*
