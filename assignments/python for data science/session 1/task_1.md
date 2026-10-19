# Install and Launch Jupyter Notebook Without Anaconda

## Install Python

1. Download Python for Windows from the official website: <https://www.python.org/downloads/>.
2. Run the installer. Select **Add python.exe to PATH**, then click **Install Now**.
3. Open PowerShell and check that Python is installed:

   ```powershell
   py --version
   ```

## Install Jupyter Notebook

1. In PowerShell, install Jupyter Notebook with Python's package installer:

   ```powershell
   py -m pip install notebook
   ```

2. Wait for the installation to complete.

## Launch Jupyter Notebook

1. In PowerShell, move to the folder where you want to store your notebooks. For example:

   ```powershell
   cd "$HOME\Documents"
   ```

2. Start Jupyter Notebook:

   ```powershell
   py -m notebook
   ```

3. Jupyter should open its dashboard in your web browser. If it does not, copy the `http://localhost:...` URL shown in PowerShell and open it in your browser.
4. In the dashboard, select **New** and choose **Python 3 (ipykernel)** (or the available Python option) to create a notebook.
5. To stop the Jupyter server, return to PowerShell and press **Ctrl+C**.
