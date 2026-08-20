# `.gitignore` for the Insta Analytics Project


A `.gitignore` file tells Git which files and folders should not be tracked. This is useful for excluding raw data, temporary Jupyter files, and generated machine learning artifacts that may be large, private, or reproducible.

Create a file named `.gitignore` in the root of the `insta-analytics` project with these patterns:

```gitignore
# Ignore all files in the raw data folder
/data/raw/*

# Ignore Jupyter temporary checkpoint folders anywhere in the project
**/.ipynb_checkpoints/

# Ignore saved Keras and pickle model files anywhere in the project
**/*.h5
**/*.pkl
```

The `/data/raw/*` pattern ignores every file directly inside `data/raw`. The `**/.ipynb_checkpoints/` pattern ignores checkpoint folders at any project depth. The `**/*.h5` and `**/*.pkl` patterns ignore HDF5 model files and Python pickle files wherever they occur.

After saving the file, run `git status` to confirm that matching files are not listed as untracked files.
