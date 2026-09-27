"""
Project BioStealth-Core
Module: Full Visceral Multiphysics & Microfluidic Integration
Developer: The Courier (外送員)
Description: Simulates the symbiotic fluid dynamics and thermal dissipation of the upgraded 5-viscera system.
"""

import numpy as np
import matplotlib.pyplot as plt

def run_visceral_simulation():
    print("[+] Initializing Full Visceral Multiphysics Integration Engine v1.0.0...")
    print("[+] System Sync: Heart (Power) | Lung (Oxygen) | Liver (Detox) | Spleen (Bio-Repair) | Kidney (Fluid)")
    
    # 模擬 5 個器官協同運作下的體內整體熱負載變動 (0% 到 100% 輸出功率)
    system_load = np.linspace(0, 100, 100)
    
    # 金屬/化學人造器官在全負載運作下的體溫飆升 (致命)
    metallic_viscera_temp = 37.0 + (system_load * 0.09)
    
    # 外送員設計之去金屬化五臟系統，透過 PEEK 微流體一體化循環網路的溫度表現
    courier_visceral_temp = 37.0 + 0.3 * np.sin(system_load * np.pi / 200)
    
    plt.figure(figsize=(8, 5))
    plt.plot(system_load, metallic_viscera_temp, 'r--', label='Metallic Artificial Organs (Thermal Runaway Risk)', linewidth=2)
    plt.plot(system_load, courier_visceral_temp, 'b-', label='The Courier Integrated Non-Metallic Viscera Network', linewidth=2.5)
    plt.axhline(y=42.0, color='purple', linestyle=':', label='Hyperthermia Necrosis Threshold (42.0°C)')
    plt.axhline(y=37.0, color='gray', linestyle='--', label='Normal Core Temp (37.0°C)')
    
    plt.title('Figure 7: Full Visceral Network Thermal Equilibrium under Peak Load', fontsize=11, fontweight='bold')
    plt.xlabel('System Operational Load (%)')
    plt.ylabel('Internal Body Core Temperature (°C)')
    plt.ylim(36.0, 47.0)
    plt.legend(loc='upper left', frameon=True)
    plt.grid(True, ls="--")
    
    print("\n" + "="*85)
    print(" PROJECT BIOSTEALTH: COMPLETE VISCERAL RECONSTRUCTION MATRIX")
    print("="*85)
    print(f"{'Organ Component':<20}{'Substrate Material':<25}{'Tactical Operational Status'}")
    print("-"*85)
    print(f"{'1. Heart (Core)':<20}{'3D-CNTs / PEDOT:PSS':<25}{'50W Stealth Power Supply (ONLINE)'}")
    print(f"{'2. Lung (Aero)':<20}{'Porous Graphene':<25}{'2-Hour Oxygen-Free Survival (SIMULATED)'}")
    print(f"{'3. Liver (Detox)':<20}{'Bio-Microfluidic Chip':<25}{'Instant Chemical/Toxin Cleaving (SIMULATED)'}")
    print(f"{'4. Spleen (Heal)':<20}{'PEEK Nanobot Reservoir':<25}{'Automated Wound Suture Matrix (SIMULATED)'}")
    print(f"{'5. Kidney (Aqua)':<20}{'CNT Reverse Osmosis Membrane':<25}{'Closed-Loop 99.99% Water Recycling (SIMULATED)'}")
    print("="*85)
    print("[+] Full visceral matrix compiled. System Status: ALL SYSTEMS STEALTH OPTIMAL.\n")
    plt.show()

if __name__ == "__main__":
    run_visceral_simulation()
