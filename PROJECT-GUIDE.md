# Project Guide

A plain-English walkthrough of this ISO/IEC 27001 case study: what was done, why, and the reasoning behind the key decisions. No prior knowledge of ISO 27001 is needed.

▶️ **[Open the interactive dashboard](https://rttr-7.github.io/iso27001-grc-portfolio/)** · 📄 **[Read the case study brief](01-iso27001-isms-implementation/00-case-study-brief.md)**

## The project in 60 seconds

Halcyon Ledger is a simulated payments company that needed ISO 27001 certification to win large customers. First, I defined what the security management system covers: the whole HalcyonPay product, both offices, the cloud and key suppliers. Then I ran a risk assessment and found 12 significant risks, such as fraudsters changing bank details or ransomware. For each one I chose controls and named an owner, which brought every risk within the company's appetite. I reviewed all 93 controls in ISO's Annex A and recorded which apply and why in the Statement of Applicability. Next, I ran an internal audit, found 3 minor nonconformities, identified the root cause of each and corrected them. Finally, leadership reviewed the results and approved going for certification.

## The five steps

| Step | What it is | Why ISO 27001 requires it | In one line |
| --- | --- | --- | --- |
| 1. Scope | The boundary: which services, offices, people and systems are protected | You can't protect what you haven't defined, and the scope appears on the certificate | The whole service customers rely on is covered, not just one office |
| 2. Risk | A list of what could go wrong, each scored as likelihood × impact (1–25) | ISO 27001 is risk-based: controls are chosen because of real risks | 6 risks scored 12 or more; after treatment, none did |
| 3. Controls | Reviewing all 93 Annex A controls and recording which apply, why, and their status | It proves nothing important was overlooked | 91 of 93 apply, each linked to a risk, law, contract or good practice |
| 4. Internal audit | The organisation checking itself before the certification body arrives | It finds problems early, while they are cheap to fix | No major findings and 3 minor ones, each fixed at the root cause |
| 5. Management review | Top management reviews the results and makes decisions | Security must be owned by leadership, not just IT | Leadership confirmed the ISMS works and funded the remaining treatments |

## Frequently asked questions

**Why a payments company?**
Payments involve money and bank details, so the risks are concrete: fraud, ransomware and data leaks. Payments companies are also commonly asked for ISO 27001 by banks and enterprise customers.

**How were risks scored?**
Two scores from 1 to 5: how likely the risk is, and how bad its impact would be. They are multiplied together. A score of 12 or more must be treated; 6 or less can be accepted by the risk owner.

**Why are two risks still rated Medium after treatment?**
For payment fraud and tenant data leaks, the damage would still be serious if they happened. Treatment makes them much less likely, and the risk owners formally accepted what remains. Showing this honestly is better practice than claiming risk is zero.

**Why were two controls excluded?**
*7.12 Cabling security:* the offices are leased, the landlord owns the cabling, no servers are kept on-site, and all traffic is encrypted. *8.30 Outsourced development:* no development is outsourced; contractors work inside the company's own teams under the same secure development process. Each exclusion is backed by evidence an auditor can check.

**What is the difference between a major and a minor nonconformity?**
A major nonconformity means a requirement is missing completely, or the system is failing. A minor nonconformity is an isolated lapse where the system still works. An opportunity for improvement means the requirement is met but could be met better.

**What did the internal audit find?**
Three minor nonconformities: contractors who missed security training, an obsolete procedure still in use, and two emergency changes that were never approved afterwards. Each was traced to its root cause, such as contractors being onboarded outside the HR system, and fixed so it cannot recur.

**Why was an internal audit needed at all?**
ISO 27001 requires it (Clause 9.2), and a certification body will not certify without a completed audit cycle and management review. It also proves controls actually operate rather than just existing on paper. The full reasoning is in [section 8 of the case study brief](01-iso27001-isms-implementation/00-case-study-brief.md#8-why-an-internal-audit-was-needed).

**Is the company real?**
No. Halcyon Ledger is fictional, so a complete ISMS can be shown without using any organisation's confidential information. The methods and document formats are the same as those used in a real implementation.

## Where to start

- **Interactive dashboard:** the Overview tab summarises the problem, the work and the results. ANU, the guide in the corner, offers a guided tour of every section.
- **Case study brief:** [00-case-study-brief.md](01-iso27001-isms-implementation/00-case-study-brief.md) explains the problem statement, approach and outcomes.
- **Formal documents:** the [`01-iso27001-isms-implementation`](01-iso27001-isms-implementation/) folder holds each deliverable written as a real ISMS document.
