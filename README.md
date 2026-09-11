# REXCOX

Web application for REXCOX (Vite + React + TypeScript).

## Getting started

```bash
npm install
npm run dev      # dev server on :5173
npm run check    # typecheck + lint + tests
```

## Scripts

| Script              | Purpose                                            |
| ------------------- | -------------------------------------------------- |
| `npm run dev`       | Vite dev server (binds `0.0.0.0`, proxy-friendly)  |
| `npm run build`     | Type-check then produce a production bundle         |
| `npm run preview`   | Serve the built bundle                              |
| `npm run typecheck` | `tsc --noEmit` with strict bug-catching flags       |
| `npm run lint`      | ESLint (type-aware rules, `--max-warnings 0`)       |
| `npm run test`      | Vitest + Testing Library (jsdom)                    |
| `npm run check`     | All three of the above — run before every commit    |

## Project layout

```
src/
  App.tsx            – application entry component
  ErrorBoundary.tsx  – top-level crash containment
  main.tsx           – React root bootstrap
  index.css          – global styles
```

## Quality gates

TypeScript runs with `strict`, `noUncheckedIndexedAccess`, `noImplicitReturns`,
`noFallthroughCasesInSwitch` and `useUnknownInCatchVariables` enabled, and ESLint
enables the type-aware ruleset plus `no-floating-promises`, `no-misused-promises`,
`require-atomic-updates` and the React Hooks rules. `npm run check` is the gate:
it must pass before code is merged.

See [docs/AUDIT.md](docs/AUDIT.md) for the defect checklist used when auditing
code in this repository.
