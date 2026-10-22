# 03 - Scope of the ISMS (Clause 4.3)

> **Document ID:** ISMS-SCO-001 · **Version:** 1.1 · **Owner:** ISMS Manager · **Approved by:** CEO · **Classification:** Internal

The scope covers everything needed to build, run and support HalcyonPay, which is the service customers are actually buying. It is not limited to one office or one team. An auditor, and any enterprise customer reading the certificate, would see a narrow scope as a weak one.

## Scope statement (as it appears on the certificate)

> The information security management system supporting the design, development, operation, hosting and customer support of the HalcyonPay accounts-payable automation and payouts platform, delivered from Leeds (UK), Kraków (Poland) and remote locations, in accordance with Statement of Applicability version 1.2.

## Boundaries

| Dimension | In scope | Out of scope (with reason) |
| --- | --- | --- |
| Services | HalcyonPay web app, API, mobile approver app, supplier portal | Legacy "Halcyon Expenses" product, decommissioned on 31 March 2026 |
| Processes | Product development, DevOps, IT operations, customer support, onboarding, HR, supplier management, finance processes that touch customer data | Marketing events and public website content (no customer data; hosted by a third party) |
| Locations | Leeds head office; Kraków hub; home offices of remote workers | Co-working desks in London (no equipment kept; covered by the remote-working policy instead) |
| People | All employees and contractors with access to in-scope systems | None |
| Technology | AWS production, staging and DR accounts; corporate SaaS (M365, Okta, GitHub, Jira, Salesforce, Zendesk, Slack); company laptops and phones | Personal devices are blocked from production; allowed for M365 mail only through Intune app protection |
| Information | Customer, supplier, payment and employee data; source code; credentials and keys | None |

## Interfaces and dependencies

These sit outside Halcyon's direct control and are managed through supplier controls 5.19-5.23:

| Party | What they provide | How Halcyon manages the interface |
| --- | --- | --- |
| AWS | Infrastructure (shared responsibility model) | AWS SOC 2 and ISO 27001 reports reviewed yearly; Halcyon owns everything above the hypervisor |
| Licensed EMI partner | Payment rails, safeguarding, sanctions screening | Agent agreement; quarterly security attestation; joint incident procedure |
| Stripe | Subscription card payments | No card data enters Halcyon systems (PCI DSS SAQ A) |
| OCR sub-processor | Invoice text extraction | DPA, 30-day deletion, annual review |
| Managed SOC provider | 24x7 monitoring and first response | Contracted SLAs; monthly service review |

## Scope decisions an auditor will test

1. **Why are London co-working desks excluded?** No Halcyon equipment or paper is kept there. Staff use them like any remote location, under the Remote Working Policy (control 6.7).
2. **Why is the public website excluded?** It holds no customer data and is a separate third-party service. The login page for HalcyonPay *is* in scope because it is served by the platform.
3. **Are the Kraków contractors in scope?** Yes. Everyone with access to in-scope systems is in scope, whatever their employment type.

Scope is reviewed at every management review, and whenever a product, site or major supplier is added.

## Information security policy summary

The Information Security Policy (POL-01, Clause 5.2) is approved by the CEO and commits Halcyon to:

- protecting the confidentiality, integrity and availability of customer and payment information
- meeting legal, regulatory and contractual requirements
- setting measurable information security objectives and reviewing them at least once a year
- continual improvement of the ISMS

It is supported by 14 topic-specific policies, among them Access Control, Acceptable Use, Cryptography, Supplier Security, Secure Development, Incident Management, Business Continuity and Remote Working.
