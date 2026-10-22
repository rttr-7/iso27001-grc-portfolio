# 06 - Risk Register and Risk Treatment Plan (Clauses 6.1.3, 8.2, 8.3)

> **Document ID:** ISMS-RTP-001 · **Version:** 1.2 · **Owner:** ISMS Manager · **Assessment date:** January 2026 · **Residual risk accepted:** 14 July 2026 · **Classification:** Confidential

The first assessment found **12 significant risks: 2 Critical, 4 High and 6 Medium**. After treatment, **every risk scores 8 or below**, and every residual risk was formally accepted by its owner on 14 July 2026.

The full register holds 47 risks. The 35 rated Low were accepted by their owners and are monitored. Machine-readable version: [`data/risk-register.csv`](data/risk-register.csv)

## Risk register (current risk before treatment)

| ID | Risk scenario | Asset | Owner | L | I | Score | Rating |
| --- | --- | --- | --- | :---: | :---: | :---: | --- |
| R-01 | An attacker takes over a customer user account (or uses business email compromise) and changes a supplier's bank details, diverting payouts | Payee bank data, payout process | COO | 4 | 5 | 20 | 🟥 Critical |
| R-02 | Ransomware on an engineer's laptop steals AWS credentials and encrypts production and backups | Production platform, backups | CTO | 3 | 5 | 15 | 🟥 Critical |
| R-03 | A misconfigured S3 bucket or database snapshot exposes customer data publicly | Customer data in AWS | CTO | 3 | 4 | 12 | 🟧 High |
| R-04 | An access-control flaw in the API (for example IDOR) lets one customer read another's invoices | HalcyonPay application | VP Engineering | 3 | 4 | 12 | 🟧 High |
| R-06 | A leaver or contractor keeps access to SaaS tools after leaving | Corporate SaaS, source code | Head of People | 4 | 3 | 12 | 🟧 High |
| R-09 | API keys or database passwords are committed to GitHub and leaked | Secrets, production | VP Engineering | 4 | 3 | 12 | 🟧 High |
| R-08 | A privileged engineer alters payment instructions directly in the production database | Payment instructions | CTO | 2 | 5 | 10 | 🟨 Medium |
| R-07 | The OCR sub-processor is breached, exposing customer invoices | Invoice images | DPO | 3 | 3 | 9 | 🟨 Medium |
| R-11 | Personal data is kept longer than allowed, breaching GDPR storage limits | Customer and supplier personal data | DPO | 3 | 3 | 9 | 🟨 Medium |
| R-12 | Loss of a key security engineer leaves monitoring and incident response uncovered | Security operations | Head of Security | 3 | 3 | 9 | 🟨 Medium |
| R-05 | A prolonged outage of the AWS London region stops payouts beyond the SLA | Platform availability | CTO | 2 | 4 | 8 | 🟨 Medium |
| R-10 | A laptop holding customer exports is lost or stolen | Endpoints | Head of IT | 4 | 2 | 8 | 🟨 Medium |

## Risk treatment plan

| ID | Option | Treatment actions | Annex A controls | Owner | Due | Status | Residual (L × I) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| R-01 | Modify | Out-of-band call-back for any bank-detail change; Confirmation of Payee check; 24-hour hold on payouts to changed details; MFA enforced for all customer admins; anomaly alerts | 5.14, 5.17, 8.5, 8.16 | COO | 31 Mar 2026 | ✅ Complete | 2 × 4 = 8 🟨 |
| R-02 | Modify | EDR on all endpoints; phishing-resistant MFA (FIDO2 keys) for engineers; just-in-time AWS access with no standing admin; immutable backups with AWS Backup Vault Lock; quarterly restore test | 8.2, 8.5, 8.7, 8.13, 8.18 | CTO | 30 Apr 2026 | ✅ Complete | 1 × 5 = 5 🟩 |
| R-03 | Modify | S3 Block Public Access at organisation level; all infrastructure as code (Terraform) with policy checks; AWS Security Hub and Config rules alerting the SOC | 5.23, 8.9, 8.16, 8.27 | CTO | 31 Mar 2026 | ✅ Complete | 1 × 4 = 4 🟩 |
| R-04 | Modify | Static and dynamic testing in CI; tenant-isolation test suite; secure coding training; annual penetration test; public bug bounty | 8.8, 8.25, 8.26, 8.28, 8.29 | VP Engineering | 15 Dec 2026 | 🔄 In progress (bug bounty launching) | 2 × 4 = 8 🟨 |
| R-06 | Modify | HR system drives Okta joiner-mover-leaver automatically; same-day deprovisioning; quarterly access reviews by managers | 5.15, 5.18, 6.5 | Head of People | 30 Apr 2026 | ✅ Complete | 2 × 2 = 4 🟩 |
| R-09 | Modify | GitHub secret scanning with push protection; all secrets moved to AWS Secrets Manager; automatic key rotation | 5.17, 8.4, 8.24 | VP Engineering | 31 Mar 2026 | ✅ Complete | 2 × 2 = 4 🟩 |
| R-08 | Modify | No standing production database access; two-person approval for data fixes; tamper-proof audit logs sent to the SOC | 5.3, 8.2, 8.15 | CTO | 31 May 2026 | ✅ Complete | 1 × 5 = 5 🟩 |
| R-07 | Share and modify | Supplier security review; DPA with 24-hour breach notice; invoice images deleted by the vendor after 30 days | 5.19, 5.20, 5.21, 5.22 | DPO | 31 May 2026 | ✅ Complete | 2 × 3 = 6 🟩 |
| R-11 | Modify | Retention schedule agreed with Legal; automated deletion jobs; yearly retention audit | 5.33, 5.34, 8.10 | DPO | 30 Jun 2026 | ✅ Complete | 2 × 2 = 4 🟩 |
| R-12 | Share | 24x7 managed SOC contract; written runbooks; cross-training plan; one additional hire | 5.24, 6.1, 6.3 | Head of Security | 31 Jan 2027 | 🔄 In progress (hire approved) | 2 × 3 = 6 🟩 |
| R-05 | Modify | Warm standby in AWS Ireland; RTO 4 hours, RPO 15 minutes; failover tested every 6 months | 5.29, 5.30, 8.14 | CTO | 30 Jun 2026 | ✅ Complete | 2 × 2 = 4 🟩 |
| R-10 | Modify | Full-disk encryption; remote wipe through Jamf and Intune; data exports blocked to unmanaged devices | 7.9, 8.1, 8.12 | Head of IT | 28 Feb 2026 | ✅ Complete | 4 × 1 = 4 🟩 |

## Before and after

| Rating | Before treatment | After treatment |
| --- | :---: | :---: |
| 🟥 Critical (15-25) | 2 | 0 |
| 🟧 High (12-14) | 4 | 0 |
| 🟨 Medium (7-10) | 6 | 2 |
| 🟩 Low (1-6) | 0 | 10 |

The two residual Medium risks (R-01 and R-04) stay at Impact 4, because a successful fraud or a data leak would still be serious. Their likelihood has been cut, and the COO and VP Engineering accepted them with written justification, as the criteria require.

## Sign-off

| Risk owner | Risks | Residual risk accepted |
| --- | --- | --- |
| COO | R-01 | 14 Jul 2026 |
| CTO | R-02, R-03, R-05, R-08 | 14 Jul 2026 |
| VP Engineering | R-04, R-09 | 14 Jul 2026 |
| Head of People | R-06 | 14 Jul 2026 |
| DPO | R-07, R-11 | 14 Jul 2026 |
| Head of Security | R-12 | 14 Jul 2026 |
| Head of IT | R-10 | 14 Jul 2026 |

Treatment progress is reported monthly to the ISMS Steering Group.
