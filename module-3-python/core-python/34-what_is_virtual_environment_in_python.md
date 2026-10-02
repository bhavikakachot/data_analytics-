 # What Is a Virtual Environment in Python?

 A **virtual environment** is an isolated directory that contains a Python interpreter and the packages needed by one project.

 Each project can have its own virtual environment. Packages installed in one environment do not normally affect another project or the system-wide Python installation.

 ## Why Do We Create a Virtual Environment?

 ### 1. To keep project dependencies separate

 Different projects may require different packages or different versions of the same package. For example, one project may need `Django 4`, while another needs `Django 5`.

 ### 2. To avoid version conflicts

 Installing every package globally can cause one project to change or break another project. A virtual environment keeps each project's package versions independent.

 ### 3. To protect the system Python installation

 Packages installed inside a virtual environment do not clutter the global Python installation. This also reduces the risk of changing packages that Python or other applications need.

 ### 4. To make projects reproducible

 A project can record its dependencies in a file such as `requirements.txt` or `pyproject.toml`. Another developer can then create a similar environment and install the same dependencies.

 ### 5. To make deployment easier

 An application can be tested with the same package versions that will be used on a server or in production.

 ## How to Create a Virtual Environment

 Python includes the `venv` module for creating virtual environments.

 ### Windows

 ```powershell
 python -m venv .venv
 ```

 ### macOS and Linux

 ```bash
 python3 -m venv .venv
 ```

 Here, `.venv` is the folder name. It is a common convention, but you may choose another name.

 ## How to Activate the Environment

 ### Windows PowerShell

 ```powershell
 .\.venv\Scripts\Activate.ps1
 ```

 ### Windows Command Prompt

 ```cmd
 .venv\Scripts\activate.bat
 ```

 ### macOS and Linux

 ```bash
 source .venv/bin/activate
 ```

 After activation, the environment name usually appears at the beginning of the terminal prompt:

 ```text
 (.venv) C:\my-project>
 ```

 ## Install Packages in the Environment

 ```powershell
 python -m pip install requests
 ```

 The package is installed only in the active `.venv` environment.

 To see the installed packages:

 ```powershell
 python -m pip list
 ```

 ## Deactivate the Environment

 When you finish working, run:

 ```powershell
 deactivate
 ```

 ## Typical Project Workflow

 ```powershell
 # Create the environment
 python -m venv .venv

 # Activate it in Windows PowerShell
 .\.venv\Scripts\Activate.ps1

 # Install project packages
 python -m pip install requests

 # Run the program
 python main.py

 # Leave the environment
 deactivate
 ```


# How to create a virtual environment in python for windows 

1. install  virtual environment

  cmd: python -m pip install virtualenv

2. create an env projects in virtual environment 

  cmd:python -m  venv student-performance-analysis

3. activate your venv 

cmd: E:\data_analytics4pm-TTS\module-3-Python\core-python\student-performance-analysis>Scripts\activate

4. How to run projects 

  cmd : python -m app.py 

5. How to deactivate venv 

  cmd: deactivate 


# note : install each library dependency in venv  



 ## Important Notes

 - Do not commit the `.venv` folder to Git. It can be recreated and may be large.
 - Add `.venv/` to the project's `.gitignore` file.
 - Activate the environment before installing packages or running project commands.
 - A virtual environment is not a virtual machine. It isolates Python packages, but it still uses the computer's operating system and hardware.

 ## In Short

 We create a virtual environment to give each Python project its own safe, independent set of packages and versions. This prevents dependency conflicts and makes development, sharing, and deployment more reliable.