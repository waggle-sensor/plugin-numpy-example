# Numpy Plugin Example

This is a simple template for writing a plugin which computes a few stats on a fake image frame.

## Overview

* `main.py`. Main plugin code. It is primarily structured around the `process_frame` function which actually computes the stats.
* `test.py`. Minimal test file which runs `process_frame` on a test image. This is intended to help exercise core functionality without having to run the entire plugin.
* `sage.yaml`. Minimal plugin spec file. Modify this to match your example.
* `Dockerfile`. Minimal Dockerfile which uses the full ML base image. Installs all dependencies in `requirements.txt`.
