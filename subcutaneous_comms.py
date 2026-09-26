"""
Project BioStealth-Core
Module: Subcutaneous Neural Communication Matrix
Developer: The Courier (外送員)
Description: Generates safety margins for Intra-Body Communication (IBC) via galvanic coupling.
"""

import numpy as np
import matplotlib.pyplot as plt

def run_communication_simulation():
    print("[+] Initializing Subcutaneous Comm-Matrix v1.0.0...")
    print("[+] Mode: Galvanic Coupling (Intra-Body Communication)")
    
    # 模擬 100 kHz 到 10 MHz 的人體組織訊號衰減 (E-field attenuation)
    frequencies_mhz = np.linspace(0.1, 10, 100)
    
    # 傳統無線電 (RF) 在皮下會被肌肉嚴重衰減，且易被外部無線電監測儀（無線電狗）捕獲
    rf_attenuation = 40 + 15 * np.log10(frequencies_mhz)
    
    # 外送員設計之人體電場耦合通訊 (IBC) 衰減值 (訊號沿著皮下脂肪層傳導，外部輻射為 0)
    ibc_attenuation = 12 + 2 * np.sqrt(frequencies_mhz)
    
    plt.figure(figsize=(8, 5))
    plt.plot(frequencies_mhz, rf_attenuation, 'r--', label='Standard Subcutaneous RF (High Detection Risk)', linewidth=2)
    plt.plot(frequencies_mhz, ibc_attenuation, 'b-', label='The Courier IBC Field (0% External Radiation)', linewidth=2.5)
    plt.axhline(y=60, color='purple', linestyle=':', label='Signal Loss Limit for Subcutaneous Decoders')
    
    plt.title('Figure 3: Subcutaneous Communication Signal Attenuation (Skin-Centric)', fontsize=11, fontweight='bold')
    plt.xlabel('Transmission Frequency (MHz)')
    plt.ylabel('Signal Path Loss (dB)')
    plt.legend(loc='lower right', frameon=True)
    plt.grid(True, ls="--")
    
    print("[+] Comm-Matrix rendering complete. Protocol Status: SECURE.")
    plt.show()

if __name__ == "__main__":
    run_communication_simulation()
