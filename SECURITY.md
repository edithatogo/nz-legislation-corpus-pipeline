# Security policy

## Secrets

Never commit API keys, Hugging Face tokens, Zenodo tokens, `.env` files, generated `data/`, or archive output. This repository should remain source-code-only.

Required production secrets live in GitHub Actions secrets:

- `NZ_LEGISLATION_API_KEY`
- `HF_TOKEN`
- `ZENODO_TOKEN`

## Publication safety

The annual Zenodo workflow defaults to draft-first behaviour. Production publication should be gated by the `zenodo-production` GitHub environment with required reviewers; sandbox/draft runs use `zenodo-sandbox`.

## Reporting issues

Open a private security advisory or contact the maintainer if you find:

- accidental secret exposure;
- incorrect destructive behavior;
- publication bypass risk;
- supply-chain issue in a dependency;
- data provenance integrity issue.
