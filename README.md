# ParametricStudyAutomation
This Python script can be useful for simulation engineers who are engaged in parametric studies.

# Functionality
- Read input values from input.txt
- Update the Workbench parametrical model based on the read parameters in batch mode
- Write values to the output.txt

# How to run
- Place the Python scripts run.py and script.wbjn in the same folder as the Workbench Project and input.txt, output.txt files
- Save and archive Workbench project
- Close Workbench Project
- Delete *.wbpj and Workbench project dir *_files and remain only Workbench archive *.wbpz
- Run Windows terminal:
  - Navigate to the working directory where the source files are stored
  - At the command prompt: `python run.py`
  - Python Script is launched and parametric study starts
- New Workbench project will be created with a name test.wbpj
- Mass flow values will be written in the output.txt file


For more information see doc/doc.pdf
