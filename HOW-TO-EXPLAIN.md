# How to Explain This Project

A plain-English guide for walking someone through this case study in an interview or a call.

## The 60-second version

> I built an ISO 27001 case study for a made-up payments company called Halcyon Ledger, which needed certification to win large customers. First I defined what the security system covers: the whole HalcyonPay product, both offices, the cloud and key suppliers. Then I ran a risk assessment and found 12 serious risks, such as fraudsters changing bank details or ransomware. For each one I chose protections and named an owner, which brought every risk down to an acceptable level. I went through all 93 controls in ISO's Annex A and recorded which apply and why. That document is the Statement of Applicability. Next I ran an internal audit, found 3 minor problems, worked out why each happened, and fixed them. Finally, leadership reviewed the results and approved going for certification.

## The 5 steps, one at a time

| Step | What it is | Why ISO asks for it | One line to say |
| --- | --- | --- | --- |
| 1. Scope | The boundary: which services, offices, people and systems are protected | You can't protect what you haven't defined, and the certificate shows the scope | "We covered everything customers rely on, not just one office." |
| 2. Risks | A list of what could go wrong, each scored as how likely × how bad (1-25) | ISO 27001 is risk-based: you choose controls because of real risks | "6 risks scored 12 or more. After the fixes, none did." |
| 3. Controls (SoA) | Going through ISO's 93 protections and saying which are needed, why, and if they're done | It proves nothing important was missed | "We use 91 of 93, each linked to a risk, law, contract or good practice." |
| 4. Internal audit | The company checking itself before the official auditors come | It finds problems early, while they're cheap to fix | "No major problems, 3 minor ones. We found the real cause of each and fixed it." |
| 5. Management review | Top leaders look at the results and make decisions | Security must be owned by leadership, not just IT | "Leaders agreed it works and funded the last two fixes." |

## Questions you might be asked

**Why did you pick a payments company?**
Payments involve money and bank details, so the risks are easy to understand, like fraud, ransomware and data leaks. Many payments companies also need ISO 27001 to sell to banks.

**How did you score risks?**
Two numbers from 1 to 5: how likely it is, and how bad it would be. Multiply them. 12 or more must be fixed; 6 or less can be accepted.

**Why are two risks still Medium after the fixes?**
For payment fraud and data leaks, the damage would still be serious if they happened. The fixes make them much less likely. The owners signed to accept what's left. Being honest about this is better than pretending risk is zero.

**Why did you leave out two controls?**
7.12 Cabling security: the offices are rented, and the building owns the cables. No servers are kept there, and all traffic is encrypted. 8.30 Outsourced development: no development is outsourced. Contractors work inside the company's own teams. Auditors always check exclusions, so each one has proof.

**What's the difference between a major and a minor nonconformity?**
Major: a requirement is missing completely, or the whole system is failing. Minor: a one-off slip where the system still works. An improvement idea (OFI) means nothing is wrong, but it could be done better.

**What did the audit find?**
Three minor problems: contractors missing training, an old document still in use, and two urgent changes never approved. For each, I found the root cause, such as contractors not being in the HR system, and fixed that so it won't happen again.

**Is the company real?**
No. Halcyon Ledger is made up, so I could show a complete ISMS without using anyone's confidential data. The methods and documents are what I would use for a real client.

## Where to point people

- **Interactive dashboard:** the easiest place to start. The Overview tab tells the story; switch on Presenter mode for the guided tour with ANU and speaking notes.
- **Full documents:** the [`01-iso27001-isms-implementation`](01-iso27001-isms-implementation/) folder has each deliverable written as a real ISMS document.
