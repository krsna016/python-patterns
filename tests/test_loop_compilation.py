import pytest
import os
import ast
import glob

def test_pattern_syntax_integrity():
    # Retrieve all pattern files from the root repository
    base_dir = os.path.dirname(os.path.dirname(__file__))
    python_files = glob.glob(os.path.join(base_dir, "pattern_*.py"))
    
    # Assert that all loops and mathematical logic compile into valid ASTs without SyntaxErrors
    for py_file in python_files:
        with open(py_file, 'r', encoding='utf-8') as f:
            source = f.read()
        try:
            ast.parse(source, filename=py_file)
        except SyntaxError as e:
            pytest.fail(f"Syntax error in {os.path.basename(py_file)}: {e}")
