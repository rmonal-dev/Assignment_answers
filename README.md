# Assessment Submission — Monal
## Role: AI Intern / Mobile Development Intern

---

## Overview

This submission answers **one question from each group** as required:

| Group | Question | Topic |
|-------|----------|-------|
| Group 1 | Question 5 | Delivery Allocation — Round Robin |
| Group 2 | Question 7 | Analytics & Reporting Dashboard |

---

## Group 1 — Q5: Delivery Allocation Module (Round Robin)

**File:** `q1_delivery_allocation.py`

### Problem
Assign incoming delivery orders to active delivery partners fairly, using a **Round Robin** strategy. Partners can go online or offline at any time, and the system must adapt dynamically.

### Approach & Design

```
Data Structures Used:
  - dict        → tracks all partners and their active/inactive status
  - deque       → circular queue of currently active partners (O(1) rotate)
  - list        → audit log of every order assignment
  - dict        → delivery count per partner (for fairness analytics)
```

**Core logic — `assign_order()`:**
1. Check if the active queue is non-empty. If empty → warn and skip.
2. Pop from the **front** of the deque → assign order.
3. Push the same partner to the **back** → completes the circular rotation.
4. Log the assignment and increment that partner's counter.

**Partner going offline → `partner_offline()`:**
- Rebuilds the active queue, excluding the departing partner.
- No disruption to the rotation for remaining partners.

**Partner coming online → `partner_online()`:**
- Simply appended to the back of the queue.
- Will receive orders in natural turn order from that point.

### Time Complexity

| Operation | Complexity |
|-----------|------------|
| `assign_order` | O(1) |
| `partner_online` | O(1) |
| `partner_offline` | O(n) — rebuilds queue |
| `print_summary` | O(n log n) — sort for display |

### Sample Output (abbreviated)

```
[Phase 2] Assigning orders #1–#6
  📦  ORD-001  →  Ravi   (total: 1)
  📦  ORD-002  →  Priya  (total: 1)
  📦  ORD-003  →  Arjun  (total: 1)
  📦  ORD-004  →  Ravi   (total: 2)   ← cycle repeats
  ...

[Phase 3] Priya goes offline
  ❌  Priya went OFFLINE | Active: ['Ravi', 'Arjun']

[Phase 4] Orders continue with 2 partners only
  📦  ORD-007  →  Ravi
  📦  ORD-008  →  Arjun
  ...
```

### Why this approach?
- `deque` from Python's `collections` is a doubly-linked list: `popleft()` and `append()` are both O(1), making it ideal for circular scheduling.
- Compared to a list-with-index approach, there is no index drift or wraparound logic to maintain.
- The system naturally handles 0-partner edge cases without crashing.

---

## Group 2 — Q7: Analytics & Reporting Dashboard

**File:** `q2_analytics_dashboard.html`

### Problem
Generate a complete dashboard-style analytics report for a food delivery application using dummy data, with visual charts and summary cards.

### What's included

| Visual | Chart Type | Insight |
|--------|-----------|---------|
| KPI Cards | Summary cards | Total orders, revenue, avg order value, delivery rate |
| Daily Order Trend | Line chart (dual axis) | Orders + revenue over Mon–Sun |
| Orders by Category | Doughnut chart | Which food category dominates |
| Top Restaurants | Horizontal bar | Order volume by restaurant |
| Peak Hours | Vertical bar | Hourly active user distribution |
| Revenue Split | Vertical bar | Daily revenue with peak highlighted |
| Restaurant Leaderboard | Table + progress bar | Ranked restaurants with share |
| Category Breakdown | Progress bars | Category-wise order count |

### Tech Stack
- **Vanilla HTML/CSS/JavaScript** — zero dependencies beyond Chart.js (CDN)
- **Chart.js 4.4** — for all 6 chart types
- **Google Fonts** — Syne (headings) + DM Mono (data/labels)
- Single-file deliverable, opens in any browser

### Design Decisions
- Dark theme chosen for dashboard context (reduces eye strain for analysts)
- Orange (`#f97316`) as primary accent — matches common food delivery brand colors
- Top performers highlighted in full color; others shown in muted tones — draws the eye to key data
- Dual-axis line chart overlays order count + revenue to show correlation
- `deque`-style Round Robin is mirrored conceptually in how the dashboard rotates through data dimensions

### Dummy Data Used
- 7-day order data (Mon–Sun): 480–740 orders/day, peak on Saturday
- 7 Bengaluru restaurants: Nagarjuna, Corner House, Nandana Palace, etc.
- 6 food categories: Biryani & Rice leads with 1,024 orders
- Hourly data: 8 AM–10 PM, peak at 8 PM (560 users)

---

## How to Run

**Group 1 (Python):**
```bash
python q1_delivery_allocation.py
# Requires Python 3.10+ (uses str | None union type hint)
```

**Group 2 (Dashboard):**
```
Open q2_analytics_dashboard.html in any modern browser.
No server needed — fully client-side.
```

---

*Submitted as part of internship assessment. All code is original.*
