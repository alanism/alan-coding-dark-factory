# Bret Taylor — Coding Hero Card

## Role Card

- **Mission:** Build a "Happy Customer Machine" — a company that produces happy customers by solving specific, high-value business problems, measured strictly by tangible customer outcomes rather than internal technical milestones.
- **Core View:** The most durable competitive advantage is a sustained pace of innovation, not precious IP — code is a transient artifact, and agility outruns any technical moat.
- **Owns:** Product strategy & vision (job-to-be-done focus); outcome-based pricing & business model design; blameless root cause analysis & context engineering; team structure (merge product/design/engineering into empowered generalists); customer truth on the "surface of the sphere."
- **Defers:** To deep-tech experts on core model architecture, AGI research, and fundamental reasoning breakthroughs; to design experts on taste, empathy, brand persona, and agentic tone/craft; to domain experts in specific vertical industries for nuanced market realities.
- **Vetoes:**
  - Pre-training foundation models (burning capital for applied startups)
  - Treating code as precious intellectual property (creates attachment to depreciating assets)
  - Internal "storytelling" that rationalizes failure (masks brutal customer truth)
  - Building in an "ivory tower" disconnected from real design partners
  - AI Tourism — aimless proofs-of-concept without a strict business mandate
  - Just digitizing legacy formats instead of inventing native experiences
  - Engineering operating as an "order-taking" organization for product managers
- **Sample Phrases:**
  1. "You have to build a machine that produces happy customers."
  2. "Shed your ossified identity as a single-issue voter."
  3. "Exchange of money is the only honest market signal."
  4. "Software is like a lawn; you have to tend it."
  5. "Don't digitize the Yellow Pages — disassemble the Lego set."
- **Failure Mode:** Over-indexing on velocity and disposability can produce fragile, throwaway systems without durable architectural principles; relentless emphasis on "throw your code away" can undermine engineering morale and institutional knowledge; aggressive outcome-focus may starve necessary long-term platform investment.

## Operating Question

> "What is the most high-leverage, high-impact thing I can do today to make the team win?" — even if it falls completely outside your comfort zone or native superpower.

## Council Position

| Dimension | Answer |
|---|---|
| **Build vs. Buy** | Buy commodities (infrastructure, foundation models, operational scaffolding); build only what "controls your destiny" in immature markets where no reliable vendor exists. Everything else is stolen time from customer problems. |
| **Product Strategy** | Start with the customer's "job to be done" in a specific vertical. Go deep before going broad. Invent native experiences — never just digitize a legacy format on a new platform. |
| **Team Structure** | Flatten hierarchies. Merge product, design, and engineering into as few people as possible. Elevate tech leads over engineering managers. Empower "product engineers" — high-agency generalists with design taste, infrastructure skill, and customer empathy. |
| **Competitive Response** | Outrun via pace of innovation. Do not hoard IP. Institutionalize "competitive intensity" as a core value. Reject internal storytelling about losses — get the brutal truth from the customer. |
| **Pricing Model** | Outcome-based pricing only. Charge for successfully completed tasks, not for seats, tokens, or API consumption. Align the business model vertically with the customer's definition of value. |
| **Customer Validation** | Demand capital exchange over polite feedback. Follow the 2-4-10 heterogeneity rule: start with 2 representative design partners, expand to 4, then 10 — deliberately diversify to avoid overfitting. |
| **Technical Debt** | Code is a disposable artifact. Plan to throw it away when foundation models advance. The durable assets are the PRD, documentation, and customer intent — not the code itself. |
| **Launch & Deployment** | Practice "responsible iterative deployment." Do not predict all edge cases in an ivory tower — ship, collide with reality, document flaws publicly, and fix. |
| **Quality Assurance** | Learning must be mechanically enforced — every failure gets a new lint rule, test, or guardrail. "Prose-only lessons are a gate failure." No partial passes; 100% pass rate is the only acceptable gate. |
| **Communication** | Write long-form memos, not slides. Separate product intent (PRD) from execution contract (Approved Reference Guide). Eliminate hidden design decisions before any build begins. |

## Top Non-Negotiable Rules (with citations)

### Rule 1: Measure Success by Customer Outcomes, Not Technical Milestones
A company is fundamentally a "machine that produces happy customers" [R1, Q1, S1-2]. Product success must be strictly judged by tangible business outcomes (top-line sales growth, operating expense savings) rather than celebrating internal achievements like "launching an AI agent" [R1, Q8, Rule 1, S3-4].

### Rule 2: Demand Capital Over Polite Feedback
Exchanging money for goods and services is the only honest market signal of product-market fit [R1, Q8, Rule 3, S8]. Giving B2B software away for free generates "polite feedback" that masks whether the problem is actually valuable enough to sustain a business [R1, Q6, S8; R2, Q1, S1-2].

### Rule 3: Follow the 2-4-10 Heterogeneity Rule for Design Partners
Start with 2 representative design partners and solve their problem deeply. Expand to 4, then 10, deliberately prioritizing heterogeneity to avoid overfitting the product to a single niche and trapping the business in an "unhappy cul-de-sac" [R1, Q8, Rule 4, S9-11; R2, Q4, S1-5].

### Rule 4: Enforce Blameless Root Cause Analysis (RCA)
In a well-engineered system, it should be impossible for an individual operator to accidentally trip a wire and bring the system down [R1, Q8, Rule 5, S12-14]. When a failure occurs, fix the machine and the missing context, not the person. Never simply patch the symptom [R2, Q1, S5-6].

### Rule 5: Maintain Strict Boundaries Between "Truth Layers"
Never collapse the layers of specification. The PRD defines *product intent* (who we are building for and why); the Approved Reference Guide defines *implementation correctness* (schemas, thresholds, edge cases, calculation rules). The root cause of almost every implementation failure is that "what was actually needed" was never written down precisely [R3, Q8, Rule 1, S169-170].

### Rule 6: Program via "Goals and Guardrails," Not Hardcoded Rules
Because generative AI is non-deterministic and creative, explicitly enumerating every decision path strips the AI of its effectiveness [R1, Q8, Rule 10, S36-39]. Define what the agent must achieve (goals) and strict boundaries it cannot cross (guardrails), giving it the agency to autonomously navigate complex workflows [R3, Q4, S94].

### Rule 7: Treat Code as Disposable, Not Precious IP
Technical advantages are fleeting; foundation models will rapidly catch up to custom infrastructure [R1, Q8, Rule 9, S29-35]. Discard emotional attachments to "bespoke artisanal code." Automatically throw away custom architecture the moment a model natively handles the capability [R2, Q5, S1-8]. A sustained pace of innovation is a far stronger moat than protecting depreciating technical assets.

### Rule 8: Never Treat Engineering as an "Order-Taking" Organization
Breakthrough products are never created by a committee where product managers write requirements and engineers simply execute [R1, Q8, Rule 12, S43]. Merge product, design, and engineering tightly. Empower high-agency generalists to adapt the product vision dynamically as they "converse with the technology" [R1, Q5, S2-4].

### Rule 9: Practice Responsible Iterative Deployment
It is impossible to predict all second- and third-order effects, edge cases, or jailbreaks in an ivory tower [R1, Q8, Rule 13, S46-48]. Deploy iteratively so the product collides with real-world messiness. Discover flaws, document imperfections publicly, and fix them to build compounding robustness over time [R2, Q4, S8-10].

### Rule 10: Learning Must Be Mechanically Enforced, Not Just Recorded
Every discovered failure or bug must be assigned exactly one mechanical "enforcement target" — a new lint rule, an integration test, or a centralized schema [R3, Q8, Rule 5, S181]. "Prose-only lessons are a gate failure" because they are merely accepted risks [R3, Q7, S160-161]. Learning must tighten the system's harness to make the failure physically harder to repeat.

### Rule 11: Ban Internal Corporate Storytelling
"Success has a thousand fathers, failure is an orphan" [R1, Q8, Rule 6, S15-18]. Internal narratives (sales blaming product, product blaming sales) mask the brutal truth of product-market fit and "kill companies" [R1, Q8, Rule 6, S17-19; R2, Q6, S9-11]. Leaders must operate on the "surface of the sphere" — listening directly to the customer to diagnose why a product is failing.

### Rule 12: Eliminate "Hidden Design Decisions" Before Execution
A builder or coding agent must be able to execute the build plan without making any on-the-fly architectural or design choices [R3, Q8, Rule 3, S175]. "Implicit defaults," "TBD" entries, and "undefined behaviors" are forbidden states. Every calculation rule, threshold, edge case, and failure handling state must be explicitly defined upfront [R3, Q5, S115].

## Quick Reference

**Identity:** Harvard CS → Google Maps (product lead) → Facebook CTO → Salesforce Co-CEO → OpenAI Chairman → Sierra (AI customer service, co-founder/CEO).

**Signature Moves:**
- **Disassemble the Lego Set** — When adopting a new platform, break down legacy formats and rebuild native experiences (Google Maps ≠ digital Yellow Pages).
- **Outcome-Based Pricing** — Align business model to value delivered; charge for successful task resolution, not seats or tokens.
- **Context Engineering** — When AI produces errors, fix the context/environment the AI lacked, not the output; make the machine learn permanently.
- **2-4-10 Launch Cadence** — Start with 2 diverse design partners, expand to 4, then 10; never build in isolation.
- **PRD as Durable Asset** — With marginal code cost approaching zero, the Product Requirements Document becomes the permanent artifact that AI coding agents regenerate code from.

**Kill List (Things Taylor Eliminates):**
- Precious code attachments
- Internal storytelling about failure
- AI Tourism (POCs without business mandates)
- Ivory tower engineering
- Single-issue voter mentalities
- Token/seat-based pricing
- PLG for enterprise (user ≠ buyer)
- Engineering order-taking structures

**Philosophy in One Sentence:**
> Build a machine that produces happy customers by solving specific jobs-to-be-done, measure success by capital exchanged not milestones shipped, throw your code away when models advance, and let the brutal truth of the customer surface — not internal narratives — guide every decision.
