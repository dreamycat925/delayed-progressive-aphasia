# Delayed Progressive Aphasia (DPA) Statistical Analysis Code  

## Overview  

This repository contains the statistical analysis code used in the study investigating **Delayed Progressive Aphasia (DPA)**, a subset of neurodegenerative disorders in which language impairment emerges as a secondary symptom. The study compares DPA with **nonfluent/agrammatic primary progressive aphasia (naPPA)** using **Bayesian statistical methods** to evaluate differences in apraxia of speech (AOS) severity and other neuropsychological measures.  

## Repository Contents  

The repository includes the following scripts:  

- **`bayesian_lr.py`**: Bayesian linear regression script used to analyze differences in AOS severity, aphasic symptoms, and neuropsychological test scores between the DPA and naPPA groups.  
- **`requirements.txt`**: List of Python dependencies required for running the statistical models.  

## Reproducibility  

For full reproducibility:  
- Exact versions of dependencies are listed in `requirements.txt`.  
- Statistical methods and results are detailed in our published manuscript.  

## Citation  

If you use this code or model in your research, please cite our paper: 

```text
Delayed progressive apraxia of speech: A novel clinical entity distinct from primary progressive aphasia – A descriptive case series
Shun Akaike, Shigehisa Ura, Akihiko Ogata, Toshio Fukutake, Ichiro Yabe, Mika Otsuki
Journal of the Neurological Sciences, 2025
https://www.jns-journal.com/article/S0022-510X(25)00219-9/abstract
```

## Note

- The repository does not include raw patient data due to privacy concerns.
- The statistical models were implemented using Bayesian inference with PyMC.
- The scripts assume that data preprocessing (e.g., reading Excel files, selecting relevant cases) has been completed beforehand.
- If you use this code, please cite the corresponding paper.

## License

This code is released under the MIT License.
