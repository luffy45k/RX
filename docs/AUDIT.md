# Defect audit checklist

The checklist used when auditing code in this repository. Every item is a class
of bug that has to be either *fixed*, *ruled out*, or *recorded as accepted risk*
before an audit is signed off.

Status legend: `[ ]` not reviewed · `[x]` clean · `[!]` defect found (link the fix commit)

---

## 1. Crashes & error containment

- [x] Top-level `ErrorBoundary` wraps the tree so one bad component cannot white-screen the app
- [ ] Every `fetch`/network call is wrapped in `try/catch` with a user-visible failure state
- [ ] `JSON.parse` of external input is guarded (throws `SyntaxError` on malformed data)
- [ ] No unguarded array/object indexing — `arr[i]` may be `undefined` (`noUncheckedIndexedAccess`)
- [ ] Optional chaining / nullish defaults wherever an API field can be absent
- [ ] `document.getElementById` and other DOM lookups are null-checked before use
- [ ] No render path can reach `Cannot read properties of undefined`
- [ ] Errors are logged with context, never swallowed by an empty `catch {}`

## 2. React correctness

- [ ] `useEffect` dependency arrays are exhaustive and correct (no stale closures)
- [ ] Effects that subscribe return a cleanup function (listeners, timers, observers)
- [ ] `setInterval` / `setTimeout` are cleared on unmount
- [ ] No state updates after unmount (abort in-flight requests via `AbortController`)
- [ ] `key` props are stable and unique — never an array index for reorderable lists
- [ ] Component state is not mutated directly (no `state.x.push(...)`, no `sort()` in place)
- [ ] `useState` initialisers that are expensive use the lazy `useState(() => …)` form
- [ ] Derived values are computed during render rather than mirrored into state
- [ ] Controlled inputs always have `onChange` — no half-controlled components
- [ ] `StrictMode` double-invocation is safe (no side effects in render)

## 3. Async & race conditions

- [ ] Concurrent requests to the same resource cannot land out of order
- [ ] Rapid re-triggers (search/typeahead) debounce or cancel superseded requests
- [ ] Promises are awaited or explicitly handled — no floating promises
- [ ] `async` event handlers that can reject are caught
- [ ] Sequential awaits that could be parallel are not needlessly serialised
- [ ] `AbortController` is wired to component unmount for every request

## 4. Data & state management

- [ ] Reducers/state transitions are exhaustive and handle unknown actions
- [ ] Cached/stale data is invalidated when the underlying resource changes
- [ ] Pagination / infinite scroll has a termination condition (no infinite loop)
- [ ] Numeric state (counters, totals) cannot drift out of sync with the server
- [ ] `localStorage`/`sessionStorage` reads are wrapped (private mode can throw) and parsed safely
- [ ] Dates are parsed and formatted explicitly — no reliance on locale/`Date` string quirks
- [ ] Timezone handling is deliberate (UTC for storage, local for display)

## 5. Security

- [ ] No `dangerouslySetInnerHTML` with unsanitised input (XSS)
- [ ] User input is validated before it is sent or rendered
- [ ] No secrets, tokens or keys committed to the repository
- [ ] Auth tokens are not stored in `localStorage` without a documented reason
- [ ] External links use `rel="noopener noreferrer"`
- [ ] Sensitive actions are not triggered by `GET`
- [ ] Dependencies scanned (`npm audit`) — no known high/critical advisories

## 6. Performance

- [ ] Large lists are virtualised or paginated
- [ ] Expensive work is memoised only where it measurably matters
- [ ] No work in render that should be in an effect (and vice versa)
- [ ] Images/media have dimensions to avoid layout shift
- [ ] Bundle is code-split; no accidental barrel-import of the whole app

## 7. Accessibility

- [ ] Interactive elements are real buttons/links with accessible names
- [ ] Form controls have associated labels
- [ ] Errors are announced (`role="alert"` / live region)
- [ ] Focus is managed on route/dialog open and restored on close
- [ ] Colour is not the only carrier of meaning; contrast meets WCAG AA
- [ ] Keyboard navigation works end to end

## 8. Correctness of business logic

- [ ] Off-by-one checks on loops, slices and pagination boundaries
- [ ] Division/modulo guarded against zero
- [ ] Floating point money is not used for currency arithmetic
- [ ] Empty, single-item and maximum-size collections all behave
- [ ] Sorting is stable and has a defined tie-break for equal keys
- [ ] `switch` statements are exhaustive or have a `default`

## 9. Tests & tooling

- [ ] Business logic has unit tests, including edge cases
- [ ] Components have behaviour tests (not snapshot-only)
- [ ] `npm run check` (typecheck + lint + test) passes
- [ ] No skipped/disabled tests without a recorded reason
- [ ] CI runs the checks on every push

---

## Findings log

| Date | Area | Defect | Fix |
| ---- | ---- | ------ | --- |
| 2026-09-12 | Scaffolding | Repository contained no application source — no defects could exist yet | Established Vite + React + TS shell with strict typecheck, type-aware ESLint and Vitest so incoming code is audited automatically |
