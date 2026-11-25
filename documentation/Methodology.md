# Methodology

## Data Collection
Packets are captured using Scapy.

## Packet Analysis
Important fields:
- Source IP
- Destination IP
- Protocol
- Size
- Timestamp

## Detection Algorithm
Rules identify:
- Port scans
- Traffic spikes
- Repeated connections
- Unknown protocols

## Alert Generation
Detected events receive severity levels.

## Storage
SQLite stores security events.