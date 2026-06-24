Experiment 1: YOLOv8n (baseline)

Epochs: 10
Image size: 512
Device: CPU

Results:
- Precision: 0.589
- Recall: 0.210
- mAP@0.5: 0.233
- mAP@0.5:0.95: 0.133

Observations:
- Low recall indicates missed defects
- Likely underfitting (low epochs)
- Small defects are hard to detect
``