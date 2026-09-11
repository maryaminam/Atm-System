# ATM System with Facial Recognition

An educational Python ATM application that supports PIN and facial-biometric login, and basic banking operations (withdraw, deposit, transfer, balance inquiry). The app is a desktop GUI built with CustomTkinter and uses OpenCV (LBPH) for face recognition. It is intended as a semester project / demo and uses a CSV file as a simple account store.

## Features
- Two login methods: PIN or Biometric (face recognition)
- Account types: Savings and Current (UI choice only)
- Basic transactions: Cash withdrawal, deposit, transfer, balance inquiry
- Face capture and model training utilities:
  - `face_recog.py` — capture face images to `dataset/`
  - `train_model.py` — train LBPH recognizer and produce `training.yml`
  - `recogniser.py` — run realtime face recognition (uses `training.yml`)

## Quick start (shortest path)
1. Create and activate a virtual environment:
   - macOS / Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Note: On some Linux distributions you may need to install system packages for tkinter before installing Python packages (e.g., `sudo apt install python3-tk`).

3. Prepare data and run:
   - Capture faces (optional, to add new user):
     ```bash
     python face_recog.py
     ```
     This writes images to `dataset/User.<id>.<n>.jpg`
   - Train the recognition model (after capturing):
     ```bash
     python train_model.py
     ```
     This writes `training.yml` (used by `recogniser.py`)
   - Start the ATM GUI:
     ```bash
     python project1.py
     ```

## Files and important artifacts
- `project1.py` — Main GUI application. Reads accounts from `project.csv`. Provides UI for login and transactions.
- `face_recog.py` — Utility to capture face images and save under `dataset/`.
- `train_model.py` — Builds an LBPH model from images in `dataset/` and writes `training.yml`.
- `recogniser.py` — Loads `training.yml` and `haarcascade_frontalface_default.xml` to perform realtime recognition.
- `project.csv` — Simple CSV file used as the account datastore (Acc. No,Name,Balance,Password).
- `haarcascade_frontalface_default.xml` — Pre-trained Haar Cascade included for face detection.
- `dataset/` (expected) — directory for face images created by `face_recog.py`.
- `training.yml` — Model file produced by `train_model.py` (binary file).

## Configuration
- CSV datastore: `project.csv` (used by `project1.py` via pandas). Update this file to add/remove accounts.
- `recogniser.py` contains a `names = ['None', 'Maryam', 'Tufail', 'Ammar']` list that maps numeric IDs to display names. Keep this list in sync with your user IDs in dataset images.

## Notes, caveats, and security
- This project is a demo / educational app. It is not production-ready:
  - Credentials and balances are stored in plaintext CSV (no encryption).
  - Face images and models are stored locally; handle user data and consent carefully.
  - There is no robust error handling or concurrency control for CSV edits.
- `recogniser.py` and `project1.py` use hard-coded paths and a small fixed user list — consider moving to a dynamic lookup (e.g., loading names from `project.csv`).
- The LBPH face recognizer requires `opencv-contrib-python` (the face module lives in the contrib package).

## Suggested improvements
- Add a `requirements.txt` and a setup script (added in this commit).
- Replace CSV with a small database (SQLite) to avoid race conditions and provide safer updates.
- Dynamically load user names and IDs instead of hard-coded arrays in `recogniser.py`.
- Improve UI flow and validation (handle edge cases and crashes).
- Add unit tests for business logic (operations on balances).
- Add a license file and a contributor guide if you plan to publish or share.

## Troubleshooting
- If `cv2.face` import fails: ensure `opencv-contrib-python` is installed (run `pip install opencv-contrib-python`).
- If tkinter import fails: install system package for Tk (e.g., `sudo apt install python3-tk` on Debian/Ubuntu).
- Ensure your webcam is available and not used by another application when running face capture/recogniser.

## Contributing
- Fork the repo, make changes, and raise a pull request.
- Please add unit tests for logic changes and a `requirements.txt` for reproducible setups.

## License
No license file is present in the repository. Add a LICENSE (for example, MIT) if you want to allow reuse.

## Contact
Repository owner: @maryaminam
