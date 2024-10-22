# Challenge Week Project

### Step 1: Create Conda Environment

To set up the necessary environment, first, ensure that you have Conda installed. Then, run the following commands to create the environment using the `environment.yaml` file.

```bash
conda env create -f ControlNet/environment.yaml
```

Then activate the Conda environment
```bash
conda activate control
```

### Step 2: Download the Models

After activating the environment, download the required models by running the `download_models.py` script:

```bash
python download_models.py
```
