# 04 - Context and Interested Parties (Clauses 4.1, 4.2)

> **Document ID:** ISMS-CTX-001 · **Version:** 1.1 · **Owner:** ISMS Manager · **Review:** every 6 months · **Classification:** Internal

Halcyon's biggest security pressures are payment fraud, customers' due-diligence demands, and US financial regulation that reaches it as a supplier. These issues came out of two Steering Group workshops (PESTLE and SWOT). They feed directly into the [risk register](06-risk-register-and-treatment-plan.md).

## 4.1 Internal and external issues

| # | Type | Issue | Effect on the ISMS |
| --- | --- | --- | --- |
| E1 | External: regulatory | US state privacy laws (such as CCPA/CPRA) and the GLBA Safeguards Rule apply to customer and supplier personal data | Privacy controls 5.31, 5.34; breach notification within state-law deadlines |
| E2 | External: regulatory | US bank customers follow the Interagency Guidance on Third-Party Relationships and pass its clauses down to Halcyon | Contract clauses, exit plans, incident notice to customers within 24 hours |
| E3 | External: threat | Business email compromise and supplier bank-detail fraud are rising across the payments sector | Risk R-01; payee verification and change controls |
| E4 | External: threat | Ransomware groups target SaaS providers to reach many customers at once | Risks R-02, R-05; immutable backups, EDR, MFA everywhere |
| E5 | External: market | Enterprise buyers require ISO 27001 before signing; 3 deals stalled | Certification target set for Q3 2026 |
| E6 | External: technology | Full dependence on AWS and on a single bank partner | Supplier risk, resilience and exit planning |
| E7 | External: environmental | **Climate change** (Clause 4.1, Amendment 1:2024): heat and flood events could affect the Austin office, AWS regions and staff working from home | Assessed as relevant but low. Covered by multi-region hosting, remote working and BCP scenarios; reviewed yearly |
| I1 | Internal: people | Headcount grew 35% in 2025, and onboarding is inconsistent | Awareness program; joiner-mover-leaver process |
| I2 | Internal: culture | Fast-moving engineering culture that sees security as a blocker | Secure SDLC built into existing CI/CD instead of manual gates |
| I3 | Internal: resources | Small security team (3 people) | Managed SOC; control owners in every department |
| I4 | Internal: structure | Two states, two sets of employment law | HR controls checked against Texas and North Carolina law |

## 4.2 Interested parties and their requirements

| Interested party | Requirements and expectations | Addressed through the ISMS? | How |
| --- | --- | --- | --- |
| Customers (finance teams) | Confidential, accurate and available payments; 99.9% uptime SLA; security questionnaires answered | Yes | SoA, BCP, customer trust portal |
| Enterprise and regulated customers | ISO 27001 certificate, bank third-party contract clauses, right to audit, 24-hour incident notice | Yes | Certification, contract templates, incident procedure |
| Customers' suppliers (payees) | Bank details kept secret and unaltered | Yes | Encryption, payee-change verification |
| Bank partner | Agent obligations, AML and sanctions controls, incident reporting | Yes | Partner agreement controls, quarterly attestation |
| Regulators (state attorneys general, FTC) | Privacy-law compliance, breach reporting | Yes | Privacy program, DPO |
| Employees and contractors | Clear policies, private HR data, safe remote work | Yes | Policies, HR controls |
| Board and investors | Protect the company's value; avoid breach losses; certify on time | Yes | Management review, KPIs |
| Cyber insurer | MFA, EDR and offline backups as policy conditions | Yes | Controls 8.5, 8.7, 8.13 |
| Suppliers (AWS, OCR vendor, SOC) | Clear contracts and acceptable use | Partly | Supplier management procedure |
| Local community and media | Responsible communication about incidents | No (handled by the Communications policy) | Outside ISMS scope |

The Amendment 1:2024 note to Clause 4.2 also asks whether interested parties have climate-related requirements. None of the parties above currently has one that affects information security. This is rechecked at each review.

## Legal, regulatory and contractual register (extract)

| Requirement | Applies because | Key obligations | Owner |
| --- | --- | --- | --- |
| State privacy laws (CCPA/CPRA) | US customer and staff personal data | Notice and opt-out rights, risk assessments, breach notice within state-law deadlines | DPO |
| GLBA Safeguards Rule | Customer financial data | Written security program, risk assessment, breach notice to the FTC | DPO |
| Interagency Guidance on Third-Party Relationships (OCC/FRB/FDIC, 2023), contractual flow-down | US bank and financial-sector customers | ICT incident notice, audit rights, exit strategy, subcontracting limits | COO |
| State money-transmitter licensing (via bank partner) | Agent of a licensed bank partner | Safeguarding support, fraud reporting, record keeping | CFO |
| Computer Fraud and Abuse Act; Electronic Communications Privacy Act | US operations | Legal basis for monitoring and incident evidence | Head of Security |
| Customer master services agreement | All customers | 99.9% SLA, 24-hour incident notice, annual pen test summary | COO |
