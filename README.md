# Face Login Enrollment Data â€” Documentation

A documentation companion to the [face recognition login and attendance system](https://github.com/faiyaadmahabub-hash/face-recognition-login-system). It explains how local enrollment data is organized while keeping staff photographs, embeddings, identifiers and attendance records out of Git.

**Status:** documentation only. This repository intentionally contains no biometric dataset and has no standalone application to run.

## Local workflow

```mermaid
flowchart LR
    A[Consented local photographs] --> B[Face-login enrollment script]
    B --> C[Local normalized embeddings]
    C --> D[Local recognition application]
```

Use your own consented photos in the face-login application's `data/person_XX/` folders. Run its enrollment script, then maintain private metadata in its ignored `metadata/people.json`. Keep retention and access arrangements appropriate to the people enrolled.

The original local collection was described as four people with 7, 4, 5 and 5 source photos. That description is historical context, not a public dataset or a recognition benchmark.

## Verification

```bash
python docs/verify_offline.py
```

On 17 October 2026, the tracked-file check found no photographs, biometric arrays or model weights; representative enrollment photos, embeddings, metadata and attendance logs matched `.gitignore`. The check does not inspect or publish private local files.

See the [verification record](docs/VERIFICATION.md) and [original documentation](docs/PROJECT_GUIDE.md). Screenshots of staff enrollment records are deliberately excluded.
