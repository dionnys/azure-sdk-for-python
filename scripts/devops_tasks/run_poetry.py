# this script is intended to be run either AGAINST or FROM the root of the python repo. Check --repo argument

import os
from ci_tools.functions import discover_targeted_packages
from ci_tools.parsing import ParsedSetup
from ci_tools.variables import discover_repo_root
import subprocess
import sys


CONFIGURATION_FILE = """[tool.poetry]
name = "azure-sdk-for-python"
version = "1.0.0"
description = "The azure-sdk-for-python leverages poetry to validate its dependency tree."
authors = ["scbedd"]

[tool.poetry.dependencies]
python = ">=3.7"
"""

def generate_pyproject(root: str) -> str:
   """
   Generates a pyproject.toml that contains necessary poetry configuration lines.
   """
   output = os.path.join(repo_root, 'pyproject.toml')
   all_packages = [ParsedSetup.from_path(path) for path in discover_targeted_packages("azure-*", root)]
   dependencies = []

   for pkg in all_packages:
      dependencies.append('{} = {{path = "{}"}}\n'.format(pkg.name, pkg.folder.replace("\\","/")))

   with open(output, 'w') as f:
      f.write(CONFIGURATION_FILE)
      f.writelines(dependencies)

   return output

def run_poetry(root: str) -> str:
   subprocess.run([sys.executable, "-m", "poetry", "update"], cwd=root)


if __name__ == "__main__":
   repo_root = discover_repo_root()
   generate_pyproject(repo_root)
   # run_poetry(repo_root)

   