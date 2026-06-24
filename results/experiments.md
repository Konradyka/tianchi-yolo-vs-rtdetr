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

Experiment 2: RT DETR (baseline)

Epochs: 10
Image size: 512
Device: CPU

Results:
- Precision: 0.670
- Recall: 0.308
- mAP@0.5: 0.357
- mAP@0.5:0.95: 0.208


Observations:
- RT-DETR achieves higher precision and recall compared to YOLOv8n baseline
- Significant improvement in recall suggests better detection of missed defects
- Higher mAP indicates improved localization and classification performance
- Model likely benefits from transformer-based global attention mechanisms
- RT-DETR appears more effective for small and subtle defects
- Training on CPU is computationally expensive and may limit performance

``