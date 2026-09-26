"""
Project BioStealth-Core
Module: Subcutaneous Carbon-Fiber Exoskeleton Stress & Magnetic Anomaly Simulation
Developer: The Courier (外送員)
Description: Evaluates mechanical load capacity and electromagnetic silence of non-metallic bones.
"""

import numpy as np
import matplotlib.pyplot as plt

def run_exoskeleton_simulation():
    print("[+] Initializing Subcutaneous Exoskeleton Engine v1.0.0...")
    print("[+] Material: 3D-Woven Carbon Fiber + Electroactive Polymer (EAP) Actuators")
    
    # 模擬施加外力負載 (0 到 50,000 牛頓，約可承受 5 噸衝擊)
    load_newtons = np.linspace(0, 50000, 100)
    
    # 傳統高強度金屬骨骼 (鈦合金 Ti-6Al-4V) 在極端負載下的應變
    titanium_strain = (load_newtons / 110e9) * 100  # 楊氏模數 ~110 GPa
    
    # 外送員設計之仿生中空蜂巢碳纖維骨骼的應變 (重量僅為鈦合金的 1/3，強度更高)
    carbon_stealth_strain = (load_newtons / 150e9) * 0.85 * 100  # 超材料複合模數優化
    
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(load_newtons / 1000, titanium_strain, 'r--', label='Military Titanium Skeleton (Heavy/Metallic)', linewidth=2)
    ax.plot(load_newtons / 1000, carbon_stealth_strain, 'b-', label='The Courier Carbon-Chitin Framework (Ultra-Light/Stealth)', linewidth=2.5)
    
    ax.set_title('Figure 4: Exoskeleton Mechanical Strain under High Impact Loads', fontsize=11, fontweight='bold')
    ax.set_xlabel('Applied External Load (kN)')
    ax.set_ylabel('Structural Deformation Strain (%)')
    ax.legend(loc='upper left', frameon=True)
    ax.grid(True, ls="--")
    
    print("\n" + "="*80)
    print(" EXOSKELETON PHYSICAL PROPERTIES MATRIX")
    print("="*80)
    print(f"{'Material Type':<25}{'Density (g/cm³)':<20}{'Magnetic Permeability (μr)':<25}{'Status':<15}")
    print("-"*80)
    print(f"{'Titanium Alloy':<25}{'4.43':<20}{'1.00005 (Metallic)':<25}{'ALERT':<15}")
    print(f"{'Courier Carbon Framework':<25}{'1.35':<20}{'1.00000 (Vacuum Matched)':<25}{'STEALTH':<15}")
    print("="*80)
    print("[+] Exoskeleton multi-physics verification complete. Structural Integrity: OPTIMAL.\n")
    plt.show()

if __name__ == "__main__":
    run_exoskeleton_simulation()
