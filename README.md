# MHA-YOLOv8 and Improved DeepSORT: Traffic Trajectory Detection and Tracking

This repository contains the data, code, and supplementary materials for the paper **"Trajectory Detection for Mixed Traffic Flow: A Deep Learning Framework with MHA-YOLOv8 Detector and Improved DeepSORT Tracker"**. The framework integrates advanced object detection and tracking algorithms to extract high-precision trajectories from UAV-captured traffic videos.

## Features
- **MHA-YOLOv8**: An enhanced YOLOv8 model with Multi-Head Attention for improved small-object detection in dense urban traffic scenarios.
- **Improved DeepSORT**: A tracking algorithm incorporating a Tunnel Tracking Module for robust object tracking under occlusion and challenging environments.
- **VRUD Dataset**: A manually annotated UAV dataset containing 20,000 traffic participant trajectories across 50,000 frames.

## Dataset
The VRUD dataset includes:
- Categories: Pedestrians, bicycles, motorcycles, cars, trucks, buses.
- Format: Oriented Bounding Boxes (OBB) and trajectories in CSV format.
- Use Cases: Mixed traffic monitoring, urban traffic safety analysis, intelligent transportation systems.

**Download Dataset**: [VRUD Dataset](#)

## Code Overview
The repository includes:
1. **Model Training Scripts**:
   - Training MHA-YOLOv8 with attention mechanisms.
   - Fine-tuning DeepSORT for trajectory tracking.
2. **Data Processing**:
   - UAV video stabilization using SIFT and GPS calibration.
   - Coordinate transformation to map trajectories to real-world coordinates.
3. **Evaluation Metrics**:
   - Object detection performance (MAP).
   - Tracking accuracy (MOTA).

## Requirements
- Python >= 3.9
- PyTorch >= 2.0.1
- OpenCV >= 4.5
- CUDA >= 11.8

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/YourUsername/MHA-YOLOv8-DeepSORT-Trajectory.git
   cd MHA-YOLOv8-DeepSORT-Trajectory
