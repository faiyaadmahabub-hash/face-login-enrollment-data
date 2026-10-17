# Face Login Enrollment Data: Documentation Only

This repository documents the enrollment dataset used by the [face recognition login system](https://github.com/faiyaadmahabub-hash/face-recognition-login-system). Photos, face embeddings, names, staff identifiers and attendance records stay local and are excluded from this repository.

## Local dataset

The original dataset has four people, with 7, 4, 5 and 5 source photos. Accepted photos produce L2-normalized 512-dimensional InsightFace embeddings saved as NumPy arrays. This repository contains no photographs or biometric arrays.

## Local setup

1. Obtain consent before enrolling a person.
2. Add your own photos under `data/person_01/`, `data/person_02/` and so on in the face-login project.
3. Run `python face_enrollment/enroll_faces.py` there.
4. Store names and roles only in the ignored local `metadata/people.json` file.

The `.gitignore` excludes photographs, NumPy arrays, enrollment directories and private metadata. Keep the original internship dataset in its existing local folder.
