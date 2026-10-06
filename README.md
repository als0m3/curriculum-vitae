# Technical profile

A public technical profile generated from `resume.json`, with selected projects and contact links. It is not a job-search announcement. The previous fictional JSON Resume sample has been removed; no employment history or qualifications are invented.

## Build

Python 3.10 or newer is sufficient. No third-party packages are required.

```sh
python3 scripts/build.py
python3 -m http.server 8000 --directory docs
```

Open `http://localhost:8000`. To export a PDF, use your browser's **Print → Save as PDF**. The print stylesheet removes the dark background. Automated PDF generation from the old `resume-cli` dependency chain has been retired.

Edit `resume.json` to update the profile. The builder escapes text and accepts only HTTP/HTTPS project links. Generated `docs/` files are not committed.

## Deployment

GitHub Actions builds and deploys GitHub Pages on pushes to `main`; it also validates pull requests without deploying them. Actions are pinned to commit hashes and updated through Dependabot.

See [SECURITY.md](SECURITY.md) for private vulnerability reports.
