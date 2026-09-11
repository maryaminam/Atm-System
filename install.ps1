# Run in PowerShell (as user)
python -m venv venv
.\venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Setup complete."
Write-Host "Activate the virtualenv with: .\venv\Scripts\Activate.ps1"
Write-Host "Run the app with: python project1.py"
