# 08 - Internal Audit Checklist and Report (Clause 9.2)

> **Document ID:** ISMS-IAR-001 · **Audit dates:** 15-26 June 2026 · **Lead auditor:** Amay Chivate, ISO/IEC 27001 Lead Auditor · **Auditee representative:** ISMS Manager · **Classification:** Confidential

The first full internal audit covered **all clauses 4-10 and a risk-based sample of 26 Annex A controls**. It found **0 major nonconformities, 3 minor nonconformities and 5 opportunities for improvement**. The ISMS was judged ready for the Stage 1 certification audit once the corrective actions were closed.

## 1. Audit plan

| Item | Detail |
| --- | --- |
| Objective | Confirm that the ISMS conforms to ISO/IEC 27001:2022 and Halcyon's own requirements, and is effectively implemented and maintained (Clause 9.2.1) |
| Criteria | ISO/IEC 27001:2022 (incl. Amd 1:2024); ISMS Manual; Information Security Policy; SoA v1.1; legal register |
| Scope | Full ISMS scope (see [03-isms-scope.md](03-isms-scope.md)); Leeds on-site, Kraków remote |
| Method | Interviews, document review, system observation, sampling (ISO 19011:2018 guidance) |
| Independence | Auditor reports to the CEO and has no operational ISMS role (Clause 9.2.2) |
| Sampling | Annex A controls chosen by risk: every control linked to a Critical or High risk, plus a rotating sample |

| Day | Area | Auditees |
| --- | --- | --- |
| 15 Jun | Opening meeting; Clauses 4, 5, 6 | CEO, ISMS Manager |
| 16 Jun | Clauses 7, 9, 10; document control | ISMS Manager, Head of People |
| 17 Jun | Access control, HR security (5.15-5.18, 6.1-6.5) | Head of People, Head of IT |
| 18 Jun | Cloud, backup, logging (5.23, 8.9, 8.13, 8.15, 8.16) | CTO, Platform team |
| 19 Jun | Secure development, change (8.25-8.32) | VP Engineering |
| 22 Jun | Suppliers and privacy (5.19-5.22, 5.34) | DPO, Procurement |
| 23 Jun | Incident and continuity (5.24-5.30) | Head of Security, SOC provider |
| 24 Jun | Kraków (remote): endpoints, awareness, physical (6.3, 7.x, 8.1) | Kraków site lead |
| 26 Jun | Auditor review; closing meeting | Steering Group |

## 2. Clause checklist (Clauses 4-10)

**Result key:** ✅ C = conforms · 🟠 Min = minor nonconformity · 🔴 Maj = major nonconformity · 💡 OFI = opportunity for improvement

| Clause | Audit question | Evidence expected | Evidence seen | Result |
| --- | --- | --- | --- | :---: |
| 4.1 | Have internal and external issues been determined, including whether climate change is relevant? | Context register | ISMS-CTX-001 v1.1 with climate issue E7; workshop notes from Dec 2025 | ✅ C |
| 4.2 | Are interested parties, their requirements, and which requirements the ISMS addresses identified? | Interested parties register | Register of 10 parties; mapped to contracts and legal register | ✅ C |
| 4.3 | Is the scope documented, with boundaries, interfaces and dependencies? | Scope document | ISMS-SCO-001; exclusions justified | ✅ C |
| 4.4 | Is the ISMS established, with its processes and their interactions? | ISMS Manual, process map | ISMS Manual v1.0 with process map | ✅ C |
| 5.1 | Does top management show leadership: resources, integration with business processes, communication? | Steering Group minutes, budget | 7 sets of monthly minutes; £310k budget approved | ✅ C |
| 5.2 | Is there an approved policy that includes objectives (or a framework for them) and commitments to requirements and improvement? | Signed policy | POL-01 v1.0 signed by CEO 12 Dec 2025; on intranet | ✅ C |
| 5.3 | Are roles, responsibilities and authorities assigned and communicated? | RACI, job descriptions | RACI in ISMS Manual; role descriptions sampled for 5 roles | ✅ C |
| 6.1.1 | Are risks and opportunities for the ISMS itself addressed? | ISMS risk and opportunity log | Log exists, 8 entries | ✅ C |
| 6.1.2 | Is there a defined risk assessment process with acceptance criteria that gives consistent, valid and comparable results? | Methodology, register | ISMS-RAM-001; 47 risks with owners and rationale | ✅ C |
| 6.1.3 | Is there a treatment plan, an SoA with justifications, and owner approval of residual risk? | RTP, SoA, approvals | RTP v1.1, SoA v1.1; residual approvals for 7 of 12 significant risks | 💡 OFI-1 |
| 6.2 | Are objectives measurable, monitored, communicated and planned (what, who, when, how evaluated)? | Objectives plan | 6 objectives with targets, owners and dates | ✅ C |
| 6.3 | Are changes to the ISMS planned? | Change records | Change log in GRC tool | ✅ C |
| 7.1 | Are resources determined and provided? | Budget, headcount | Budget, SOC contract, GRC tool licence | ✅ C |
| 7.2 | Is competence determined and evidenced? | Training records, CVs | Records for security team and control owners | ✅ C |
| 7.3 | Are people aware of the policy, their contribution and the effects of non-conformity? | Training completion, interviews | 31 of 40 sampled staff completed onboarding training on time | 🟠 Min NC-01 |
| 7.4 | Are internal and external communications defined? | Communication plan | Communication matrix in ISMS Manual | ✅ C |
| 7.5 | Is documented information controlled (approval, versions, access, retention)? | Document register | Superseded procedures still in use (see NC-02) | 🟠 Min NC-02 |
| 8.1 | Are processes planned and controlled, including outsourced processes? | Procedures, supplier controls | SOC and OCR vendor controls defined and monitored | ✅ C |
| 8.2 | Are risk assessments done at planned intervals and on significant change? | Assessment records | Jan 2026 assessment; new supplier triggered reassessment in May | ✅ C |
| 8.3 | Is the risk treatment plan implemented and results retained? | RTP status, evidence | 10 of 12 treatments complete with evidence | ✅ C |
| 9.1 | Is it defined what is monitored, how, when, by whom, and when results are analysed? | KPI definitions, dashboard | 14 KPIs defined; dashboard compiled by hand from 5 sources | 💡 OFI-2 |
| 9.2 | Is there an audit programme, with independent auditors and reported results? | Audit programme | 3-year programme approved; this audit | ✅ C |
| 9.3 | Does management review cover all inputs (9.3.2 a-g) and produce decisions? | Review minutes | Not yet held; scheduled for 11 Aug 2026 | ✅ C (planned) |
| 10.1 | Is continual improvement evident? | Improvement log | 23 improvements logged since Feb 2026 | ✅ C |
| 10.2 | Are nonconformities reacted to, root causes found, and corrective action effectiveness reviewed? | NC log | 4 NCs from control checks, all with root cause analysis | ✅ C |

## 3. Annex A sample checklist

| Control | Audit question | Sample and evidence | Result |
| --- | --- | --- | :---: |
| 5.9 | Is the asset inventory complete and does each asset have an owner? | 20 AWS resources and 15 laptops traced to the inventory; all found | ✅ C |
| 5.13 | Is information labelled according to the classification scheme? | 38% of SharePoint files in the Finance site carry a label | 💡 OFI-3 |
| 5.14 | Are bank-detail changes verified out of band? | 15 payee changes sampled; 15 call-backs recorded | ✅ C |
| 5.15 / 5.18 | Are access rights reviewed and removed on leaving? | Q1 access review signed off; 20 leavers sampled, 20 deprovisioned same day | ✅ C |
| 5.19 / 5.22 | Are Tier 1 suppliers assessed and reviewed? | 4 of 4 reviewed; evidence held in 3 different places | 💡 OFI-4 |
| 5.23 | Are cloud services governed? | AWS SCPs reviewed; SaaS approval records for 6 new tools | ✅ C |
| 5.24 / 5.26 | Is incident response planned and tested? | Plan v1.2; tabletop in Apr 2026; 3 real incidents handled per playbook | ✅ C |
| 5.30 | Is ICT continuity tested? | DR failover test on 12 May 2026 met RTO (3h 10m) and RPO (6 min) | ✅ C |
| 5.34 | Are PII obligations met? | Records of processing complete; 2 DPIAs reviewed | ✅ C |
| 6.1 | Is pre-employment screening done? | 15 new starters sampled; all screened before start | ✅ C |
| 6.3 | Is awareness training completed? | See NC-01 | 🟠 Min NC-01 |
| 7.7 | Are clear desk and clear screen in place? | Leeds walk-round: 2 unlocked screens out of 60 desks; MDM lock confirmed | ✅ C |
| 8.2 | Is privileged access controlled? | No standing AWS admin; 30 just-in-time sessions all had a ticket | ✅ C |
| 8.5 | Is MFA enforced? | Okta policy: FIDO2 for engineers; customer-admin MFA at 100% | ✅ C |
| 8.8 | Are vulnerabilities fixed on time? | 34 of 35 critical findings fixed within 7 days | ✅ C |
| 8.12 | Is data leakage prevented? | Purview DLP policies in audit-only mode, not blocking | 💡 OFI-5 |
| 8.13 | Are backups immutable and restore-tested? | Vault Lock confirmed; Q1 and Q2 restore tests passed | ✅ C |
| 8.15 / 8.16 | Are logs collected and monitored? | CloudTrail on all 14 accounts; SOC alerts reviewed for 1 week | ✅ C |
| 8.24 | Is cryptography used as the standard requires? | KMS key rotation on; TLS 1.2+ confirmed with external scan | ✅ C |
| 8.25 / 8.28 | Is secure development built into CI? | 10 pull requests: SAST, dependency and secret scans all ran and blocked on failure | ✅ C |
| 8.32 | Are production changes approved? | 25 emergency changes sampled; 2 had no retrospective approval | 🟠 Min NC-03 |

## 4. Audit summary

| Result | Count |
| --- | :---: |
| 🔴 Major nonconformities | 0 |
| 🟠 Minor nonconformities | 3 |
| 💡 Opportunities for improvement | 5 |
| ✅ Conforming checklist items | 37 |

**Auditor's conclusion:** the ISMS conforms to ISO/IEC 27001:2022 and is effectively implemented in most areas. The minor nonconformities are isolated failures, not a breakdown of the system. I recommend proceeding to the Stage 1 audit once NC-01 to NC-03 have corrective actions in place.

## 5. Findings and corrective actions

| ID | Grade | Requirement | Finding (statement, evidence) | Root cause | Correction and corrective action | Owner | Due | Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NC-01 | Minor | Clause 7.3; Annex A 6.3 | 9 of 40 sampled staff had not completed onboarding security training within the required 30 days. All 9 were Kraków contractors onboarded Feb-Apr 2026 | Contractors were onboarded through the agency, not the HR system, so they never received the training assignment | Correction: 9 people trained by 3 Jul. Corrective action: all contractors moved into the HR system; training assigned automatically; weekly overdue report to managers | Head of People | 31 Jul 2026 | ✅ Closed, verified 5 Aug |
| NC-02 | Minor | Clause 7.5.3 | Two superseded versions of the Customer Data Export Procedure were still on a shared drive, and Customer Success used v0.9 (no encryption step) | No rule to withdraw obsolete copies when Confluence is updated | Correction: old copies removed. Corrective action: Confluence is the single source; shared-drive policy documents redirect to it; quarterly document-register check | ISMS Manager | 17 Jul 2026 | ✅ Closed, verified 5 Aug |
| NC-03 | Minor | Annex A 8.32 | 2 of 25 emergency production changes (CHG-1184, CHG-1207) had no retrospective approval within 2 working days, as the change procedure requires | Retrospective approval relied on engineers remembering; no reminder or tracking | Correction: both changes reviewed and approved. Corrective action: an automated Jira rule flags unapproved emergency changes after 24 hours and escalates to the VP Engineering | VP Engineering | 24 Jul 2026 | ✅ Closed, verified 5 Aug |
| OFI-1 | OFI | 6.1.3 f | Residual-risk approvals were recorded by email for 5 risks | - | Record all approvals in the GRC tool | ISMS Manager | 14 Jul 2026 | ✅ Done |
| OFI-2 | OFI | 9.1 | The KPI dashboard is compiled by hand from 5 sources | - | Automate data feeds into the GRC tool | Head of Security | Q4 2026 | 🔄 Open |
| OFI-3 | OFI | A.5.13 | Low adoption of sensitivity labels | - | Default labels per SharePoint site; training | Head of IT | Q4 2026 | 🔄 Open |
| OFI-4 | OFI | A.5.22 | Supplier review evidence is held in 3 places | - | Single supplier record per vendor in the GRC tool | Procurement Lead | Q4 2026 | 🔄 Open |
| OFI-5 | OFI | A.8.12 | DLP is in audit-only mode | - | Move to blocking for Restricted data after a 30-day tuning period | Head of IT | Q4 2026 | 🔄 Open |

## 6. How the findings were graded

- **Major nonconformity:** a requirement not met at all, or a failure that raises significant doubt about the ISMS achieving its intended results.
- **Minor nonconformity:** a single or isolated failure to meet a requirement, where the system still works overall.
- **Opportunity for improvement:** the requirement is met, but there is a better or more efficient way to meet it.

Each nonconformity statement follows the three-part structure: the **requirement**, the **evidence** seen, and the **gap** between them.
