# Hugging Face connector handoff

The intended live dataset repo is:

```text
edithatogo/nz-legislation-corpus
```

If an authenticated Hugging Face connector/session is available, initialise the dataset repo with equivalent behaviour to:

```python
from huggingface_hub import HfApi
api = HfApi(token=HF_TOKEN)
api.create_repo("edithatogo/nz-legislation-corpus", repo_type="dataset", private=False, exist_ok=True)
```

Then upload:

- `README.md` dataset card
- `.gitattributes`
- `dataset_infos.json`
- placeholder `parquet/README.md`
- placeholder `raw_xml/README.md`
- placeholder `manifests/README.md`

Do **not** create `data/...` placeholders in the Hugging Face repo. The workflow downloads the repo into a local `data/` directory and uploads that directory's contents at repository root.

The canonical local script is:

```bash
HF_TOKEN=... HF_REPO_ID=edithatogo/nz-legislation-corpus ./scripts/create_huggingface_dataset_repo.sh
```

Connector-created repos still require the GitHub source repository to be configured with:

- `HF_TOKEN`
- `HF_REPO_ID`
- `NZ_LEGISLATION_API_KEY`
- `ZENODO_TOKEN`
