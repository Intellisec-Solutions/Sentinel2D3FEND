# Sentinel 2 D3FEND

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Description 
This code snippet retrieves Azure Sentinel Incidents that are mapped to MITRE ATT&CK Framework and generates the related MITRE D3FEND defenses

![](/images/Sentinel2D3FEND.png)

## CSVs
Additionally this repository provides 2 helpful CSV files: 

* Techniques.csv: The list of Techniques and their artifacts
![](/images/techniques.png)

* Defenses.csv: D3FEND defenses and the related artifacts

![](/images/Defenses.png)

## Scripts Usage 
### Sentinel to D3FEND

```
python3 Sentinel2D3FEND.py 
```
### ATT&CK Navigator Layer to D3FEND

```
python3 Layer2D3FEND.py <Layer.json>
```
![](/images/screen.png)

