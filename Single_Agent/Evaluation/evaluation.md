## ⚠️ Key Accuracy Failures & Hallucinations

When comparing the two outputs side-by-side, the LLM exhibited three major types of errors: **omissions**, **hallucinations (inventing requirements)**, and **imprecise mapping**.

### 1. Complete Omissions (Missed Requirements)

Despite having the same input, the LLM completely dropped key functional requirements:

* **League Tables & History (CSV No. 3):** The LLM completely missed the requirement to display league tables and statistics from *current and past seasons*. There is zero trace of this in the JSON.
* **Leagues (CSV No. 7):** The LLM omitted the ability to follow *leagues* (only capturing "clubs" in FR-021).
* **National Teams (CSV No. 8):** The LLM completely missed the explicit requirement to select and receive notifications for *national teams* (only capturing "favorite teams" in FR-022 and FR-023).

### 2. Hallucinations / Scope Creep (Invented Requirements)

The LLM generated several requirements that are **not** present in your validation CSV. If the CSV represents the ground-truth functional requirements, the LLM hallucinated or over-reached on the following:

* **FR-001 & FR-002 (OS Specificity):** The LLM explicitly split requirements for **Android** and **iOS** devices. The CSV makes no such platform-specific distinction.
* **FR-016 (API Technical Implementation Detail):** The LLM generated a requirement stating that live data must be retrieved *via an API from an external server*. The validation CSV only specifies that the live ticker must retrieve and display live data (CSV No. 11), without dictating this backend architectural constraint.
* **FR-017 (Modular Configuration):** The LLM invented a requirement allowing users to *individually configure the app through additional modules*. This is not in the CSV.
* **FR-026 (Offline Usability):** The LLM hallucinated an entire requirement for the app to *remain usable offline*.
* **FR-027 (Feedback Evaluation):** The LLM invented a requirement to *continuously evaluate user feedback and app reviews*.

### 3. Split & Diluted Requirements (Mapping Inaccuracy)

Instead of a clean 1:1 mapping, the LLM frequently split single cohesive requirements into multiple redundant JSON objects, which artificially inflated the requirement count while diluting the accuracy of the acceptance criteria:

* **CSV No. 4** (detailed team and player info) was split into **FR-008** (team) and **FR-009** (player).
* **CSV No. 5** (live stream links and valid rights) was split into **FR-010** (display links) and **FR-011** (verify country rights).
* **CSV No. 6** (register and log in easily) was split into **FR-019** (register) and **FR-020** (login).
* **CSV No. 10** (share news and match reports) was split into **FR-024** (share news) and **FR-025** (share game reports).

---

## 🎯 Summary of Pure Accuracy Metrics

* **Total Ground-Truth Requirements (CSV):** 15
* **Total LLM-Generated Requirements (JSON):** 27
* **Perfect 1:1 Matches:** Only **5 out of 15** (CSV 2, 9, 11, 13, 15 matched cleanly to corresponding JSON blocks).
* **Completely Missed:** **1** (CSV 3 - League Tables & Season History).
* **Partially Missed (Crucial Details Dropped):** **2** (CSV 7 dropped "leagues"; CSV 8 dropped "national teams").
* **Superfluous/Hallucinated Requirements:** **7** (FR-001, FR-002, FR-016, FR-017, FR-026, FR-027).