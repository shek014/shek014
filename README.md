# Abhishek Ravicharan

B.Tech Computer Science & Engineering (AI & ML) · SRM Institute of Science and Technology, Chennai  
[abhishekravicharan@proton.me](mailto:abhishekravicharan@proton.me) · [LinkedIn](https://www.linkedin.com/in/abhishek-ravicharan-003043275/)

## Research

**Q-IDS: Problem-Space Adversarial Robustness of ML Intrusion Detectors**  
<sub>*Computers & Security* (Elsevier) · in preparation · [code](https://github.com/shek014/q-ids)</sub>

**Machine Learning Approaches to Passenger Survival Prediction**  
<sub>IJIREEICE · published · [paper](https://www.researchgate.net/publication/397384830_Machine_Learning_Approaches_to_Passenger_Survival_Prediction_A_Titanic_Dataset_Analysis) · [code](https://github.com/shek014/Spaceship-Titanic-Classification)</sub>

## Featured work

### Security · adversarial ML

- **[q-ids](https://github.com/shek014/q-ids)** · Studies how ML intrusion detectors hold up when the attacker modifies real network traffic rather than feature vectors. A Mininet/Scapy testbed produces labelled C2, exfiltration and benign flows; a NumPy neural network written from scratch and an 8-qubit PennyLane classifier are then targeted by an evasion search that replays each candidate attack as live packets and keeps only those a functional oracle verifies still succeed. Simple, cost-free timing changes defeat both models, the quantum classifier proves no more robust, and adversarial training on one feature axis only shifts the vulnerability to another.

### Numerical software · C++23

- **[autonne](https://github.com/shek014/autonne)** · Truncated SVD and Hermitian eigendecomposition for small dense complex matrices: the kernels [lindblad](https://github.com/verycareful/lindblad)'s MPS backend splits bonds with. Tested against LAPACK, benchmarked against Eigen, bit-identical across `-march` targets under strict floating point. Maintainer (review, CI, releases v0.2.0–v0.3.2); a joint project with [verycareful](https://github.com/verycareful) and [zParik](https://github.com/zParik).

### Systems · ML

- **[Incident Resolution Agent](https://github.com/shek014/Failure-Detection)** · Multi-agent AIOps on LangGraph: detects anomalies from Prometheus metrics, retrieves runbooks and past incidents via RAG, scores root causes and risk, and auto-resolves low-risk incidents through MCP tools, escalating to a human otherwise.
- **[Spaceship Titanic](https://github.com/shek014/Spaceship-Titanic-Classification)** · Feature engineering and gradient-boosted ensembles; 80.21% validation accuracy. Co-authored paper in IJIREEICE.
- **[Real-Time Emotion Recognition](https://github.com/shek014/Real-Time-Emotion-Recognition-System)** · YOLO-based facial emotion detection on a live webcam stream, served through Flask.

## Stack

| | |
|---|---|
| **Security & ML** | Python · NumPy · PennyLane · Scapy · Mininet · Wireshark · LangGraph · OpenCV |
| **Systems** | C++23 · CMake · GoogleTest · Docker · Linux · GitHub Actions |
| **Web** | FastAPI · Django · Next.js · TypeScript |

## Languages

<img src="./assets/languages.svg" width="100%" alt="Top languages across public repositories" />

## Activity

<img src="./assets/activity.svg" width="100%" alt="Weekly contributions over the last year" />
