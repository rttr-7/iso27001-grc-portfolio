# 09 - Management Review Report (Clause 9.3)

> **Document ID:** ISMS-MR-001 · **Meeting date:** 11 August 2026 · **Chair:** CEO · **Minutes:** ISMS Manager · **Classification:** Confidential

Top management concluded that **the ISMS is suitable, adequate and effective**, and approved going ahead with the Stage 1 certification audit on 25 August 2026. Five of six information security objectives were met or on track. Two investments were approved: **£85k for an additional security engineer** and **£40k for a public bug bounty**.

**Attendees:** CEO (chair), CTO, CFO, COO, Head of People, VP Engineering, Head of Information Security (ISMS Manager), DPO. **Apologies:** none. **Quorum:** met.

## 1. Status of actions from previous reviews (9.3.2 a)

This is the first formal management review. The 7 monthly Steering Group meetings since December 2025 produced 41 actions: 38 are closed and 3 are carried into this review (bug bounty, R-12 hire, DLP blocking).

## 2. Changes in issues and interested parties (9.3.2 b, c)

| Change | Effect on the ISMS | Decision |
| --- | --- | --- |
| Two new EU banking customers signed with DORA flow-down clauses | Incident notice within 4 hours of classification for major ICT incidents (stricter than the 24 hours in the standard contract) | Update the incident plan and SOC runbook by 30 Sep 2026 |
| EMI partner requested quarterly penetration-test summaries | Extra reporting duty | Accept; add to the supplier reporting calendar |
| Planned launch of HalcyonPay in Ireland (Q1 2027) | Same platform; new legal entity possible | Assess scope impact by 31 Dec 2026 |
| Climate change (Amd 1:2024) | Reassessed: still low relevance; no interested-party requirement | No change; review again in 2027 |

## 3. Information security objectives (Clause 6.2)

| ID | Objective | Target | Result (Jul 2026) | Status |
| --- | --- | --- | --- | --- |
| O-1 | No risk above appetite (score 12+) left untreated | 0 by Jul 2026 | 0 | ✅ Met |
| O-2 | New starters complete security training within 30 days | 100% | 87% (Feb-Jun); 100% in July after NC-01 fix | 🟡 Not met; now fixed |
| O-3 | Phishing simulation click rate | < 5% by Jun 2026 | 4.1% (baseline 18% in Jan) | ✅ Met |
| O-4 | Critical vulnerabilities fixed within 7 days | ≥ 95% | 97% | ✅ Met |
| O-5 | HalcyonPay availability | ≥ 99.9% | 99.96% | ✅ Met |
| O-6 | Leaver access removed on the last working day | 100% | 98.5% (2 of 134 late, both under 24 hours) | 🟡 On track |

## 4. Information security performance (9.3.2 d)

### Nonconformities and corrective actions

| Source | Raised | Closed | Open |
| --- | :---: | :---: | :---: |
| Internal audit (June 2026) | 3 minor | 3 | 0 |
| Internal control checks | 4 | 4 | 0 |
| **Total** | **7** | **7** | **0** |

All 3 audit nonconformities were closed and verified as effective on 5 August 2026 (see [08-internal-audit-checklist.md](08-internal-audit-checklist.md#5-findings-and-corrective-actions)).

### Monitoring and measurement results

| Metric | Feb 2026 | Jul 2026 | Trend |
| --- | :---: | :---: | :---: |
| Staff with phishing-resistant MFA | 12% | 100% | ⬆️ |
| Endpoints with EDR active | 71% | 100% | ⬆️ |
| AWS Security Hub score | 62% | 94% | ⬆️ |
| Open critical/high vulnerabilities | 41 | 3 | ⬆️ |
| Mean time to detect (SOC) | n/a (no SOC) | 11 minutes | - |
| Security incidents (SEV1/SEV2) | 1 | 0 | ⬆️ |

### Audit results

- Internal audit: 0 major, 3 minor NCs, 5 OFIs. Auditor recommends proceeding to certification.
- External penetration test (May 2026): 0 critical, 2 high (both fixed and retested), 6 medium.

### Fulfilment of objectives

5 of 6 met or on track; see section 3.

## 5. Feedback from interested parties (9.3.2 e)

- **Customers:** 64 security questionnaires answered in H1 2026, with average turnaround cut from 12 days to 4 days by the trust portal. The 3 stalled enterprise deals are waiting only for the certificate.
- **EMI partner:** Q2 attestation accepted with no findings.
- **Staff:** the pulse survey shows 82% "know how to report a security concern" (up from 49%).
- **Cyber insurer:** renewal premium reduced 15% after evidence of MFA, EDR and immutable backups.

## 6. Risk assessment results and treatment plan status (9.3.2 f)

- 12 significant risks treated: 10 complete, 2 in progress (R-04 bug bounty, R-12 hire).
- Residual risk: 0 Critical, 0 High, 2 Medium, 10 Low. All accepted by owners on 14 July 2026.
- One new risk added in May 2026 (new OCR sub-processor region), scored 6 (Low) and accepted.

Full detail: [06-risk-register-and-treatment-plan.md](06-risk-register-and-treatment-plan.md)

## 7. Opportunities for continual improvement (9.3.2 g)

1. Automate KPI collection into the GRC tool (OFI-2).
2. Move DLP from audit mode to blocking (OFI-5).
3. Single supplier record per vendor (OFI-4).
4. Map ISO 27001 controls to SOC 2 Type II and DORA requirements, so one set of evidence covers all three.
5. Consider ISO/IEC 27701 (privacy) extension in 2027.

## 8. Decisions and outputs (Clause 9.3.3)

| # | Decision | Type |
| --- | --- | --- |
| D-1 | The ISMS is suitable, adequate and effective; proceed to the Stage 1 audit on 25-26 Aug 2026 | Conclusion |
| D-2 | SoA v1.2 and RTP v1.2 confirmed as approved | Change to the ISMS |
| D-3 | Approve £85k for an additional security engineer (closes R-12) | Resources |
| D-4 | Approve £40k for a public bug bounty in year 1 (closes R-04) | Resources |
| D-5 | Update incident procedure for 4-hour DORA notice to EU banking customers | Change to the ISMS |
| D-6 | Objectives for 2027 to be proposed by the ISMS Manager by 30 Nov 2026, including SOC 2 Type II alignment | Improvement |
| D-7 | Assess ISMS scope impact of the Ireland launch | Change to the ISMS |

## 9. Action log

| Action | Owner | Due | Status |
| --- | --- | --- | --- |
| Recruit additional security engineer | Head of Security | 31 Jan 2027 | 🔄 In progress |
| Launch bug bounty programme | VP Engineering | 15 Dec 2026 | 🔄 In progress |
| Update incident plan and SOC runbook for DORA 4-hour notice | Head of Security | 30 Sep 2026 | ✅ Done |
| Move DLP to blocking mode for Restricted data | Head of IT | 31 Dec 2026 | 🔄 In progress |
| Automate KPI dashboard | Head of Security | 31 Dec 2026 | 🔄 In progress |
| Scope impact assessment for Ireland | ISMS Manager | 31 Dec 2026 | ⏳ Not started |
| Propose 2027 objectives | ISMS Manager | 30 Nov 2026 | ⏳ Not started |

**Next management review:** February 2027, then every 6 months.

---

*Approved by the CEO on 12 August 2026.*
