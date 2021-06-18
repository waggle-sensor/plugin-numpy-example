# Numpy Plugin Example

This is a simple plugin which uses numpy to compute some stats on a test image. While not useful on its own, it serves as a starting point for plugin developers.

## Overview

Plugins contain both code and packaging information. In this example, we've organized them as follows:

1. The code consists of:
    * `main.py`. Main plugin code. It is primarily structured around the `process_frame` function which actually computes the stats.
    * `test.py`. Minimal test file which exercises `process_frame` functionality on a test image. Serves as a starting point for building automated testing.
    * `requirements.txt`. Python dependencies file. Add any required modules to this file.

2. The packaging information consists of:
    * `sage.yaml`. Sage spec file. Modify this to match your example. This is used to register your code in the [ECR](https://portal.sagecontinuum.org).
    * `Dockerfile`. Dockerfile which uses the full ML base image and installs all dependencies in `requirements.txt`. This is used to create a container image which includes any special dependencies your code may need.
