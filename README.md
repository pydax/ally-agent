# 🌟 AllyAgent: Low-Cognitive-Load Multi-Step Reasoning Assistant

**A Hack for Good Submission under the *Reasoning Agents* Track**

---

## 💡 Inspiration & Problem Statement
Fast-paced enterprise environments often flood employees with fragmented communication across countless long emails, dense documentation, and corporate portals. For neurodivergent individuals (such as those with ADHD or autism), this high cognitive load can trigger severe task paralysis, anxiety, and overwhelm.

**AllyAgent** serves as an intelligent cognitive filter that restructures workplace complexity into clear, executive-functioning-friendly action items.

---

## 🧠 Multi-Step Reasoning Architecture
Unlike single-turn chat wrappers, AllyAgent enforces a strict **Plan-Execute-Verify** lifecycle:
1. **Plan:** Deconstructs the user's daily intent into an analytical retrieval strategy.
2. **Execute:** Calls specialized Microsoft IQ layers via the Model Context Protocol (MCP) to extract real-time enterprise context.
3. **Verify:** Runs a localized self-correction step, validating output details against source materials to mathematically guarantee zero hallucination before presentation.

---

## 🚀 Microsoft IQ Integration via MCP
AllyAgent natively structures tool boundaries using Microsoft's Model Context Protocol (MCP) specification to bridge two critical enterprise data layers:
* **Work IQ Layer:** Intersects secure communication signals (Outlook emails, Teams chats) to extract implicit tasks and fluid deadlines.
* **Foundry IQ Layer:** Hooks directly into the centralized enterprise knowledge base to pull formal Standard Operating Procedures (SOPs) and verify exact compliance execution guidelines.

---

## 🛠️ Installation & Setup

### 1. Environment Initialization
Clone this repository and establish a local virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt