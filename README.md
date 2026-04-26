# eml-explore — ARCHIVED

> **🗄  This package is archived as of 2026-04-25 (E-129 consolidation).**
>
> The functionality has been folded into the main `monogate` package
> as of `monogate 2.4.0+`. New users should install:
>
> ```bash
> pip install monogate[cli]
> ```
>
> The CLI is registered as `monogate-explore` (canonical) AND
> `eml-explore` (compatibility alias) — your existing
> `eml-explore ...` shell invocations will keep working unchanged
> after the migration.
>
> The standalone `eml-explore` PyPI / GitHub package is **frozen at
> 0.1.1** and will receive no further updates.
>
> See [monogate's CHANGELOG entry for 2.4.0](https://github.com/almaguer1986/monogate/blob/master/python/CHANGELOG.md#240--2026-04-25--universality-witness--cli--jupyter-folded-in)
> for details.

---

# eml-explore (historical)

Cross-domain explorer CLI for the EML substrate. Composes
`eml-cost`, `eml-rewrite`, `eml-discover`, `eml-graph`, and
`eml-witness` through one command-line entry point.

## Install

```bash
pip install eml-explore
```

## Usage

```bash
$ eml-explore witness "1/(1+exp(-x))"
witness for 1/(1 + exp(-x))
============================================================
  predicted_depth:    2
  pfaffian_r:         1
  ...
  identified:         sigmoid (canonical) (exact) [ml]

$ eml-explore example cross-domain
Cross-domain demo — formulas across physics, GR, finance
all collapse into the same Pfaffian cost axes...

$ eml-explore corpus my_expressions.txt
corpus: my_expressions.txt
  parsed:        47 / 47 lines
  cost classes:  19
  largest class: 8
```

## Subcommands

| Command | Purpose |
|---|---|
| `eml-explore witness EXPR` | full universality witness |
| `eml-explore analyze EXPR` | Pfaffian profile only |
| `eml-explore identify EXPR` | registry matches only |
| `eml-explore class AXES`  | every registry member of an equivalence class |
| `eml-explore corpus FILE` | cluster a file of one-expression-per-line |
| `eml-explore example NAME` | built-in demo (`cross-domain`, `witness-walkthrough`) |

Every subcommand accepts `--json` for machine-readable output.

## The cross-domain demo

This is the headline finding from the substrate showcase
exercise — formulas from completely unrelated mathematical
domains (radiative physics, finance, mechanics, GR) collapse
into the same Pfaffian cost class because they share structural
shape (constant × monomial of one or two variables). The
`example cross-domain` subcommand surfaces this directly:

```bash
$ eml-explore example cross-domain
  Stefan-Boltzmann (sigma * T^4)        axes=p0-d2-w0-c0
  perpetuity (C / r)                    axes=p0-d2-w0-c0
  kinetic energy (m * v^2 / 2)          axes=p0-d2-w0-c0
  Coulomb's law (k * q1 * q2 / r)       axes=p0-d2-w0-c0
  de Broglie wavelength (h / p)         axes=p0-d2-w0-c0

distinct axes seen: 1 (collapse ratio 5.0x)
```

## Status

Beta. Patent pending.
