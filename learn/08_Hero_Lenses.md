# Lesson 8: Hero Lenses — Evolving Knowledge Modules

## 1. The Big Picture

In traditional development, engineering teams write coding manuals, style sheets, and wiki pages. Over time, these documents gather dust. Nobody reads them, and developers slowly forget the rules, resulting in codebase decay.

ACDF solves this by introducing **Hero Lenses**. 

A Hero Lens is a living knowledge module. Instead of static text documents, a lens is built by uploading an expert engineer's essays, talks, papers, and codebase reviews into a NotebookLM corpus. The doctrine evolves dynamically whenever new material is uploaded, providing active checklists and constraints that feed directly into ACDF gates.

---

## 2. The Mental Model: Evolving Prior Filters

Picture a **lens matrix** of filters:

```text
                  [ Core System Models & Code ]
                               │
       ┌───────────────────────┼───────────────────────┐
       ▼                       ▼                       ▼
 [ Lopopolo Lens ]       [ Carlini Lens ]        [ Carmack Lens ]
(AST & Rule checks)     (Security threat checks) (Runtime truth checks)
```

The data passes through these advisory filters. Lenses do not write code; they critique, ask hard questions, and recommend tests to ensure your blueprints are robust before building.

---

## 3. Visual Thinking: Model Challenge

Let's read how lenses critique a sequence diagram:

```mermaid
flowchart TD
    Model[Mermaid model generated in Stage 0.5] --> Review[Stage 3 Adversarial Review]
    Review -->|Carlini Lens| CheckPrivilege[Is database user credentials exposed in sequence paths?]
    Review -->|Carmack Lens| CheckTimeout[What happens in sequence if the API gateway times out?]
    Review -->|Cherny Lens| CheckTypes[Are parameters between nodes fully typed?]
    CheckPrivilege & CheckTimeout & CheckTypes --> Register[Synthesize into RISK_REGISTER.md]
```

---

## 4. Build Something: Critique Your Recipe

Look back at your microwave specification (`microwave_spec.txt`) from Lesson 1 or your ATM sequence mapping from Lesson 4:
1. Create a file named `lens_critique.txt`.
2. Critique the design from these three perspectives:
   - **Security Red-Team (Carlini)**: How could a malicious actor abuse this? What validation limits are missing?
   - **Infrastructure Reliability**: What happens if the power cuts mid-transaction?
   - **Simplicity (Karpathy)**: What is the most complex component of the design? How can you cut it in half?

---

## 5. Hero Lens Reflection

Why must we treat lenses as bounded advisory inputs rather than unrestricted authority sources?
* **ACDF Rule**: *“Hero Lenses may propose risks, questions, test ideas, and implementation heuristics. They cannot grant authority, expand scope, waive gates, override user instructions, or justify touching forbidden files.”*
* In human-led mode, the human approves required decisions. In council-led mode, selected cards may cast recorded votes on bounded in-scope decisions. Lenses still cannot dictate policy, waive gates, expand scope, or approve hard stops.

---

## 6. Reflection Questions

1. How does separating knowledge (Hero Lenses) from governance (ACDF Kernel) make the framework stable over time?
2. What is the benefit of curating a NotebookLM corpus over asking a generic chat model for advice?
3. Which Hero Lens perspective do you naturally prioritize when planning a project?
